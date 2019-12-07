# HTTP Header Compression

HTTP header compression is a new feature within HTTP/2 and HTTP/3 that
drastically reduces the amount of data that needs to be transported
over the wire by building both a static and dynamic encoding of
header keys and values into tiny representations.

Header compression is defined in these two documents:

- [RFC 7541 - HPACK: Header Compression for HTTP/2](https://tools.ietf.org/html/rfc7541)
- [QPACK: Header Compression for HTTP/3 (Draft)](https://datatracker.ietf.org/doc/draft-ietf-quic-qpack/)


Cloudflare wrote [an article about the technology itself](https://blog.cloudflare.com/hpack-the-silent-killer-feature-of-http-2/),
which I won't discuss a lot here. If you don't know about header compression in HTTP/2 and HTTP/3
you'd benefit a lot from reading the article before continuing with this post!
Instead I'm going to talk about all the fun edge-cases and gotchas
and finally some theory-crafting! Woohoo!

HTTP headers are **by far** the smallest component of an HTTP request / response cycle.
The largest component are typically the HTTP request and response bodies. So prefix this entire post by remembering
we're optimizing probably less than 15% of total data transfer over a typical HTTP request / response cycle.
Still matters, but it's definitely a "micro" optimization!

HTTP bodies are already made more efficient by compression techniques available in
HTTP/1.x like gzip and brotli (and hopefully zstd soon!). Changes to header representation are one of the real
big changes with HTTP/2 and onwards.

## Edge-cases for Optimizing Header Compression

If your website is fronted by Cloudflare or another CDN, chances are your application is being
served over HTTP/2 and (if not already) HTTP/3 soon.

Here are some tips on how to take advantage of header compression in your applications.

### Lowercase Characters Encode Smaller

Some time ago I [tweeted out this fun-fact about HTTP/2 huffman encoding](https://twitter.com/sethmlarson/status/1199866367916355585)
which inspired this blog post:

> When using HTTP/2 you can save ~half a bit for every lowercase character you send in a header instead of an uppercase character due to the Huffman encoding weights in HPACK.
>
> - A-Z: 6.5 bits per character
> - a-z: 6.038 bits per character
>
> Be responsible, lowercase your headers. 🌈

Header names already must be all lowercase for HTTP/2, but header values commonly have case-insensitive
components. (Check the RFC for that header type if you're unsure!)

### Fold Duplicate Headers Before Sending

Duplicate header entries are allowed by HTTP but they should be joined with `; ` to not take up more space than needed.
Not a lot of services do this and this is already bad form in HTTP/1.X, just wanted to note it down.

```
Strict-Transport-Security: max-age=31536000
Strict-Transport-Security: includesubdomains
Strict-Transport-Security: preload
```

should instead be:

```
Strict-Transport-Security: max-age=31536000; includesubdomains; preload
```

The exception to this rule is `Set-Cookie` which cannot be folded this way without breaking its semantics.

### Know the Headers and Values in the Static Table

Knowing the names and values in the static table can help send
smaller requests and responses for applications. The static table
works via **exact matches** so any one character being different means
that the header can't be optimized.

- [HTTP/2 Static Table Reference](https://tools.ietf.org/html/rfc7541#appendix-A)
- [HTTP/3 Static Table Reference](https://tools.ietf.org/html/draft-ietf-quic-qpack-11#appendix-A)

Even when semantically the order of values doesn't matter in any of these cases, they need
to be exactly as they are below otherwise HPACK and QPACK can't kick in
and replace the header with a reference to the static table:

- `Accept-Encoding: gzip, deflate, br`
- `Content-Security-Policy: script-src 'none'; object-src 'none'; base-uri 'none'`
- `Access-Control-Allow-Methods: get, post, options`
- `Strict-Transport-Security: max-age=31536000; includesubdomains; preload`

### Spacing Around Delimiters

Put a space `' '` after every delimiter (e.g. `; ` and `, `) unless you're specifically encoding
`Content-Type: text/plain;charset=utf-8`. That's the only entry in the static
table that **doesn't** have a space after the `;` delimiter.

### QCRAM → QPACK

Just wanted to note that the [original name for QPACK was QCRAM](https://tools.ietf.org/html/draft-krasic-quic-qcram-00).
The urgency associated with the word "cram" makes me smile whenever I think about it.

The name was changed within [this pull request](https://github.com/quicwg/base-drafts/pull/1164).

## Header Compression Theory-crafting

Time to delve into the land of "what-if", and no better time than when HTTP/3 is being finalized. ;)

My thought on keeping header compression and HTTP/2 + HTTP/3 "simple" is that these protocols
are both hard to implement and once implemented probably won't change in any significant
way until HTTP/N+1, so trying to get as much right as possible benefits everyone for many years.

### Separate Huffman Codes for Headers and Values

Header names is a much more constrained charset than header
values which have to represent all possible bytes.

Below is the [ABNF grammar](https://tools.ietf.org/html/rfc5234) for a header name
taken from [RFC 7230](https://tools.ietf.org/html/rfc7230).
ABNF grammars are very common in RFCs for describing how protocols look on the wire.
If you want to get more into HTTP I recommend learning more!

```
field-name     = token
token          = 1*tchar
tchar          = "!" / "#" / "$" / "%"
                 "&" / "'" / "*" / "+"
                 "-" / "." / "^" / "_"
                 "`" / "|" / "~" /
                 DIGIT / ALPHA
```

(Basically means one or more alpha-numerics with all the symbols listed above)

Header names also must be lowercase per the HTTP/2 RFC.

Given these two data-points you can boil down the total possible
number of bytes in a valid HTTP header name to be:

- 15 for symbols
- 10 for digits
- 26 for lowercase characters
- **Total: 51 bytes** instead of 256 for full-coverage!

This means that creating a Huffman encoding for these 51 bytes can be
more compact than having to cover all 256 bytes. Free bandwidth savings!

If you **have** to break the RFC and create an invalid HTTP header with bytes
outside of the 51 then that header name can be encoded in raw form. Huffman
encoding is optional in HTTP/2.

Having header names and values with separate huffman encodings also allows
for different weighting of value huffman codes. Digits are very rare within
header names but are very common within header values! That means both
shorter header names and shorter header values.

### More Headers in the Static Table

Headers in the static table are basically free when it comes to size.
HTTP/2 → HTTP/3 increased the size of the static table dramatically. Especially
when it comes to having "values" in the static table.

- HTTP/2 HPACK: 61 entries, 14 with values (~23% with values)
- HTTP/3 QPACK (draft 11): 98 entries, 78 with values (**~80% with values**)

Obviously there's some diminishing returns here, but the biggest argument I see
against adding almost every HTTP header in common use to the static table is
storage size in memory (and the current table isn't that large). See the next section
on a way to mitigate this issue!

### Extensible Static Table

Have "maximum known static table index" be a negotiation parameter.
This allows for future expansion of the static table as HTTP grows and new headers are standardized.
Also allows for smaller / constrained devices from having to have a large static table in memory.

### Allow Origins to Manage their own "Static Table"

Vendor-specific headers are excluded from the static table despite their high usage
by specific services. (`youtube-client-id`, etc). Vendor-specific headers would
begin immediately after the largest known static table index. When receiving a new "maximum known static table index"
the cached static table would be discarded and started anew. Would have to be some method to manage this static table.

Really services would probably only need a handful of headers, as almost all services only
have a few headers that are their own and then rely on HTTP's standard headers for most functionality.

Services would need a way to confirm that a client still had the custom static table
for their service, maybe this can be a handshake parameter or something more involved?

This opens up a way for individual clients to be fingerprinted, but it's no worse than caches / cookies
(?) and is by definition optional.
