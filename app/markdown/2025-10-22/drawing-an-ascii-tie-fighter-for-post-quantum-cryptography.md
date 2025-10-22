# Drawing an ASCII TIE fighter for post-quantum cryptography

This is a funny short story about contributing to internet standards.
The real heroes of the story are [Filippo Valsorda](https://filippo.io/) and [all the other contributors](https://github.com/cfrg/draft-irtf-cfrg-concrete-hybrid-kems/graphs/contributors) to post-quantum cryptography standards (PQC). Without their efforts internet communications would be less secure, so thank you :)

<!-- more -->

As I understand the situation, the internet standard being discussed is “[Concrete Hybrid PQ/T Key Encapsulation Mechanisms](https://datatracker.ietf.org/doc/draft-irtf-cfrg-concrete-hybrid-kems/)” (KEMs) which combine PQ algorithms with traditional algorithms. The reasoning being that PQ algorithms are relatively new which is not *great* for cryptography which would prefer using algorithms that have survived many years of scrutiny and analysis, such as [EdDSA](https://en.wikipedia.org/wiki/EdDSA).

Therefore, it is desirable to have a “hybrid” KEM designed such that the hybrid “fails gracefully” by only losing the *quantum safety* property if the PQ algorithm is insecure, but doesn't compromise safety to traditional attack vectors that exist without sufficiently powerful quantum computers. My intuition is this will allow for more confident experimentation and deployment of PQ algorithms, as the stakes are much lower for actually rolling out the new algorithms with this construction.

There are three concrete hybrid KEM instances that are defined within the standard, they are named but the names may change in the future:

* `MLKEM768-P256`
* `MLKEM768-X25519` (aka “X-Wing”)
* `MLKEM1024-P384`

Note that the [X-Wing KEM was first published in January 2024](https://www.ietf.org/archive/id/draft-connolly-cfrg-xwing-kem-09.html), much earlier than the other KEMs in this draft.
You may have already guessed that the name of the "X-Wing" KEM is relevant to the title of the blog post :)

These hybrid KEMs are made up of 5 components:

* Traditional component that is either a “nominal group” or a traditional KEM
* A post-quantum KEM
* A pseudo-random number generator (PRG)
* A key-derivation function (KDF)
* And finally, a label which is a byte string that labels the specific combination of the above components.

For the X-Wing KEM the label is the byte string “`0x5C2E2F2F5E5C`”, which if printed out as ASCII looks like an [X-Wing from Star Wars](https://en.wikipedia.org/wiki/X-wing_fighter):

<pre style="max-width: fit-content; margin-left: auto; margin-right: auto;"><code>\./
/^\
</code></pre>

Note that the newline was added to better visualize the ASCII art of an X-Wing, the newline isn't present in the actual KEM label byte string.

This is where my concrete understanding of the context is fuzzier, and figuring it all out would require digging through IETF mailing list exchanges.
As far as I could tell from a quick read the new KEM constructions being proposed were going to have real names instead of ASCII art to match the actual name of the construction, basically what name you'd end up configuring in OpenSSL, NGINX, etc.

This naming discussions was taking time and the label being used for key derivation means that implementations of this draft standard couldn't be deployed, as that label was not finalized and could change later.

Filippo asked on the IETF mailing list whether the label and the name could be disconnected for the new set of KEM constructions and instead follow the lead of X-Wing using small ASCII art of spaceships. This would let the naming discussion continue while allowing implementers to begin deploying their experiments without fear of having the labels change at a later time.

So Filippo created a few new ASCII art pieces, one of an [imperial TIE fighter](https://en.wikipedia.org/wiki/TIE_fighter) for `MLKEM768-P256` and another of an [imperial Lambda shuttle](https://en.wikipedia.org/wiki/List_of_Star_Wars_spacecraft#Lambda-class_shuttle#:~:text=Imperial%20shuttle) for `MLKEM1024-P384`:

<pre style="max-width: fit-content; margin-left: auto; margin-right: auto;"><code>|A|   |
|V|  /-\
</code></pre>

Filippo [posted about this on Mastodon](https://abyssdomain.expert/@filippo/115384481568122932), where Frederik Braun [suggested](https://social.security.plumbing/@freddy/115390055125695964) changing the TIE fighter to `|-o-|`. Filippo wanted to keep the characters used at exactly 6 bytes, so I suggested:

<div style="margin-left: auto; margin-right: auto;width: fit-content; max-width: 100%">
<blockquote class="mastodon-embed" data-embed-url="https://mastodon.social/@sethmlarson/115390118569659776/embed" style="background: #FCF8FF; border-radius: 8px; border: 1px solid #C9C4DA; margin: 0; max-width: 540px; min-width: 270px; overflow: hidden; padding: 0;"> <a href="https://mastodon.social/@sethmlarson/115390118569659776" target="_blank" style="align-items: center; color: #1C1A25; display: flex; flex-direction: column; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Roboto, sans-serif; font-size: 14px; justify-content: center; letter-spacing: 0.25px; line-height: 20px; padding: 24px; text-decoration: none;"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32" viewBox="0 0 79 75"><path d="M63 45.3v-20c0-4.1-1-7.3-3.2-9.7-2.1-2.4-5-3.7-8.5-3.7-4.1 0-7.2 1.6-9.3 4.7l-2 3.3-2-3.3c-2-3.1-5.1-4.7-9.2-4.7-3.5 0-6.4 1.3-8.6 3.7-2.1 2.4-3.1 5.6-3.1 9.7v20h8V25.9c0-4.1 1.7-6.2 5.2-6.2 3.8 0 5.8 2.5 5.8 7.4V37.7H44V27.1c0-4.9 1.9-7.4 5.8-7.4 3.5 0 5.2 2.1 5.2 6.2V45.3h8ZM74.7 16.6c.6 6 .1 15.7.1 17.3 0 .5-.1 4.8-.1 5.3-.7 11.5-8 16-15.6 17.5-.1 0-.2 0-.3 0-4.9 1-10 1.2-14.9 1.4-1.2 0-2.4 0-3.6 0-4.8 0-9.7-.6-14.4-1.7-.1 0-.1 0-.1 0s-.1 0-.1 0 0 .1 0 .1 0 0 0 0c.1 1.6.4 3.1 1 4.5.6 1.7 2.9 5.7 11.4 5.7 5 0 9.9-.6 14.8-1.7 0 0 0 0 0 0 .1 0 .1 0 .1 0 0 .1 0 .1 0 .1.1 0 .1 0 .1.1v5.6s0 .1-.1.1c0 0 0 0 0 .1-1.6 1.1-3.7 1.7-5.6 2.3-.8.3-1.6.5-2.4.7-7.5 1.7-15.4 1.3-22.7-1.2-6.8-2.4-13.8-8.2-15.5-15.2-.9-3.8-1.6-7.6-1.9-11.5-.6-5.8-.6-11.7-.8-17.5C3.9 24.5 4 20 4.9 16 6.7 7.9 14.1 2.2 22.3 1c1.4-.2 4.1-1 16.5-1h.1C51.4 0 56.7.8 58.1 1c8.4 1.2 15.5 7.5 16.6 15.6Z" fill="currentColor"/></svg> <div style="color: #787588; margin-top: 16px;">Post by @sethmlarson@mastodon.social</div> <div style="font-weight: 500;">View on Mastodon</div> </a> </blockquote> <script data-allowed-prefixes="https://mastodon.social/" async src="https://mastodon.social/embed.js"></script>
</div>

<p></p>

Frederik and Filippo approved of my rendition, and [submitted a pull request](https://github.com/cfrg/draft-irtf-cfrg-concrete-hybrid-kems/pull/28) which was eventually merged
into the draft. I love little [easter-eggs](https://datatracker.ietf.org/doc/html/rfc2324.html#section-2.3.2) left in internet standards by authors
so it felt special to be able to contribute my own for future readers' enjoyment. *Happy implementing!* :)
