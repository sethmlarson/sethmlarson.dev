# Sponsored Work on urllib3

urllib3 is a popular HTTP client library in Python for which I've been a maintainer for the past 2 years. Some months ago the urllib3 maintainers were approached by [GitCoin](https://gitcoin.co) with a [grant opportunity](https://gitcoin.co/grants/65/urllib3) for funded work on urllib3. In this post I'll be documenting the work that I've completed as a result of this grant.

[Quentin Pradet](https://github.com/pquentin/) also wrote about his experience working on the same grant. [Check out his blog post here](https://quentin.pradet.me/blog/ive-been-paid-to-work-on-open-source.html). 🎉

I focused my development efforts on urllib3's URL parser which was recently upgraded to be RFC 3986 compliant with the [`rfc3986`](https://github.com/python-hyper/rfc3986/) package.

It turns out that the package is a little too heavy for platforms with fewer CPU and memory resources like Raspberry Pi and the import time suffered due to the amount of regular expression parsing occurring within `rfc3986`. The effects caused `urllib3` to take [800ms to import instead of 250ms](https://github.com/urllib3/urllib3/issues/1590).

I read the RFC and with the figured out what components of the package we needed and re-implemented them simpler and with less complicated regular expressions in order to avoid the expensive compilation while still maintaining the level of correctness we needed to provide a secure URL parser. 

It turns out that we don't need to strictly parse the `username`, `password`, `path`, `query` or `fragment` components, instead we split on the component delimiters and then percent-encode all invalid characters within the component because all of the above components accept percent-encoded values.

Basically the only components that we strictly parse are the scheme, host and port. All other components we accept the characters that are passed to urllib3 and percent-encode them in order to avoid CRLF-injection and unicode-based attacks that originally spurred the development of an RFC 3986 compliant URL parser for urllib3.

This allows us to continue to support "technically" incorrect URLs in a safe way that results in better usability while still secure. Unfortunately the `host` component is the most complex and still needs some work for me to be completely happy with it.

The second minor discovery I made was that our `ConnectionPool.request()` method didn't apply the same URL parsing logic as the top-level `PoolManager.request()` and so would be inconsistent. I added the logic to `ConnectionPool.request()` for relative URLs.

List of Pull Requests made as a result of the Grant:

- [Pull #1647](https://github.com/urllib3/urllib3/pull/1647)
- [Pull #1673](https://github.com/urllib3/urllib3/pull/1673)
- [Pull #1692](https://github.com/urllib3/urllib3/pull/1692)
- [Pull #1732](https://github.com/urllib3/urllib3/pull/1732)

The work I've done as a result of this grant has inspired me to begin working on a URL parser called [`irl`](https://github.com/urllib3/urllib3/issues/1590) specifically targeting simplicity, correctness, usability, and an interface that lends itself to being used by HTTP clients.

I'd like to thank everyone who donated funds to GitCoin to support my work on this Grant. 💖