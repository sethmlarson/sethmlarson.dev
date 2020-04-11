# Why URLs are Hard: Path Params & urlparse

Welcome to the first installment of "Why URLs are Hard": a series of stories
that I've accumulated from reading a lot about URLs.

We take URLs for granted and mostly think of them as very simple things because
of how often we interact with clean and simple URLs like `https://example.com`.
Little do you know there are decades of ancient dark magic that occurred before
we ended up with URLs we know and love today.

This story is about finding a mysterious API in Python's `urlparse` function
and discovering a now almost entirely unused URL feature. Come along with me! :)

## Comparing urlparse to RFC 3986

I was evaluating [`urlparse`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse)
from the [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html) module
and how it performed compared to other URL parser libraries.

Within the documentation it's mentioned that URLs are parsed according to [RFC 3986](https://tools.ietf.org/html/rfc3986.html)
which is a set of rules that describe how to segment a URL into different components.
Let's take a quick look at that standard to see what parts of a URL we see.

There's a cute little ASCII diagram showing off all the parts of a URL:

```
 foo://example.com:8042/over/there?name=ferret#nose
 \_/   \______________/\_________/ \_________/ \__/
  |           |            |            |        |
scheme     authority       path        query   fragment
```

... and then the `authority` section is further decomposed into:

```
authority = [ userinfo "@" ] host [ ":" port ]
```

One of the best parts of reading RFCs is thinking about how much effort people put into the adorable ASCII art :)

Okay, now that we know what to expect let's try out `urlparse` with the URL from the RFC:

```python
>>> from urllib.parse import urlparse
>>> url = (
... "foo://user:pass@example.com:8042"
... "/over/there?name=ferret#nose"
)
>>> parts = urlparse(url)
>>> parts
ParseResult(
    scheme='foo',
    netloc='user:pass@example.com:8042',
    path='/over/there',
    params='',
    query='name=ferret',
    fragment='nose'
)
>>> parts.hostname
'example.com'
>>> parts.port
8042
>>> parts.username
'user'
>>> parts.password
'pass'
```

Okay so looks like we have this as a mapping from `ParseResult` to RFC 3986:

- `parts.scheme` -> `scheme`
- `parts.netloc` -> `authority`
  - `parts.username`:`password` -> `userinfo`
  - `parts.hostname` -> `host`
  - `parts.port` -> `port`
- `parts.path` -> `path`
- `parts.params` -> ???
- `parts.query` -> `query`
- `parts.fragment` -> `fragment`

Notice the ??? in the list? I was confused too. No matter what I put into my URL I couldn't get
anything to show up in `ParseResult.params`.

The documentation for `ParseResult.params` is "Parameters for last path element"
and then isn't mentioned much anywhere else. Googling around is tough too because "`params`"
is Requests way of adding to the query string for the requested URL so most results are
about that.

When googling "Path parameters" I found [this article from 2008](https://doriantaylor.com/policy/http-url-path-parameter-syntax)
which pointed to the last paragraph of [RFC 3986 Section 3.3](https://tools.ietf.org/html/rfc3986#section-3.3)
which explains path parameters:

```
Aside from dot-segments in hierarchical paths,
a path segment is considered opaque by the
generic syntax.  URI producing applications
often use the reserved characters allowed in a
segment to delimit scheme-specific or dereference-
handler-specific subcomponents.  For example,
the semicolon (";") and equals ("=") reserved
characters are often used to delimit parameters
and parameter values applicable to that segment.
```

So `;` and `=` have special meaning within the `path`,
let's throw those into `urlparse` and see what happens:

```python
>>> urlparse("http://example.com/a;z/b;c;d=e")
ParseResult(
    scheme='http',
    netloc='example.com',
    path='/a;z=y;x/b',
    params='c;d=e',
    query='',
    fragment=''
)
```

Huh, I didn't expect it to pull the values actually outside of the `path` component.
And it looks like it only pulled the params from the last segment, `/a;z=y;x/` is untouched.
Wonder how many bugs are lurking out there because of this quirk. :)

So if you're relying on URL parsing and directly inspecting the `path` component make sure
you check your implementation and amend it to add `f";{result.params}"` if `params` is non-empty.
Either that or use a URL parser that doesn't have this quirk like [`rfc3986`](https://github.com/python-hyper/rfc3986)

I especially recommend using another library if you're making security decisions based on the URL.
[A write-up from 2011 details a security issue related to path parameters](https://www.jtmelton.com/2011/02/02/beware-the-http-path-parameter)
which an application using `ParseResult.path` alone would likely also be vulnerable to.

Hope you learned something and stay safe!
