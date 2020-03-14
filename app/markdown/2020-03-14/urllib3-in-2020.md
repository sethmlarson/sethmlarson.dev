# urllib3 in 2020

[2019 was a transformative year for urllib3](https://sethmlarson.dev/blog/2019-12-28/review-of-2019-for-urllib3)
and I'm hoping to keep up the pace with Python's most used HTTP client.
Here are a list of ideas, some easier achieved than others, that
would be great to ship this year!

## Acquire Funding for Larger Projects

We're excited to be working with [Tidelift](https://tidelift.com/subscription/pkg/pypi-urllib3?utm_source=pypi-urllib3&utm_medium=referral&utm_campaign=blog)
for another year as one of the original lifted Python projects.
They've enabled us to
[provide a comprehensive security disclosure workflow](https://blog.tidelift.com/why-coordinated-security-vulnerability-disclosure-policies-are-important)
and help me and another maintainer to "keep the lights on" so to speak for the project.

However for some of the larger goals mentioned in this post we'll
likely require dedicated developer-hours to achieve. In 2019 ~78% of
urllib3's $23,580 in funding came from grants. What urllib3 was able
to achieve with the grants has increased the security of the project
and benefited millions of people, your generous organization could help
us do the same in 2020!

If your organization benefits from urllib3 being secure, maintained, and
performant, and maintained please consider [contacting me to discuss
a grant opportunity](mailto:sethmichaellarson@gmail.com) or
[subscribing to Tidelift](https://tidelift.com/subscription/pkg/pypi-urllib3?utm_source=pypi-urllib3&utm_medium=referral&utm_campaign=blog)
to keep urllib3 and many more Python projects secure and maintained.

## Mentor New Contributors

Python's HTTP stack has seen a surge of activity and will need even
more helping hands to accomplish our goals and keep Python on
the bleeding edge in the HTTP space and keep our dependable existing
libraries up-to-date.

If you're looking to get started in Python Open Source and have an
interest in making high-impact contributions, learn a lot about networking,
or bolster your resume [reach out to me](mailto:sethmichaellarson@gmail.com).

## Use Operating System Trust Stores

Python's HTTP clients all rely on a trust store named [`certifi`](https://github.com/certifi/python-certifi/)
which is the [Mozilla CA Certificate Store](https://www.mozilla.org/en-US/about/governance/policies/security-group/certs/),
packaged and released on PyPI. This works well for the Internet
at large as it's the same CA certificate store that powers Firefox
and curl. However many organizations and IT machine configurations
only ensure that the operating system CA bundle is up to date
and having `certifi` be on separate means organizations can't
control the safety of their users the same way that they control
safety of browsers and other tools.

We'd also want this work to be usable by other projects in the
Python ecosystem as this is an important feature for any library
that uses TLS.

[`oscrypto.trust_list`](https://github.com/wbond/oscrypto/blob/master/oscrypto/trust_list.py)
in particular looks like a promising start.

## TLS 1.2+ by Default

Thanks to the security trail-blazing of many organizations TLS 1.2 is becoming
the new minimum security level for the Internet. CDNs and cloud services
mean almost all services deployed there use TLS 1.2+ whether their users know it
or not by taking configuration of TLS termination away from users.

Browsers are also doing their part by deprecating and eventually removing TLS 1.0
and 1.1 from future versions. Firefox, Edge, Safari, and Chrome have all committed to
removing TLS <1.2 in 2020.

This means 2020 is a great time for us to also push the
better-security-by-force envelope. :)

Setting TLS 1.2+ means that we'll be secure against TLS downgrade attacks or
if a vulnerability is found in TLS 1.0 or 1.1 our users will already be protected.
It also means that we can restrict our default cipher suites to rock-solid secure
ones instead of ones that are there only to be compatible with older TLS versions.

Even with all you'll still be able to use TLS 1.0 or 1.1 if you
specify those versions manually via `ssl_version` in the case you have to connect
to an older server.

## Drop Support for Python <2.7.9

Python 2.7.9 is the first Python version that supported `ssl.SSLContext()` objects.
Currently urllib3 supports all Python 2.7 versions but maintains a large chunk of
code that allows us to work with Python versions that don't have proper `SSLContext`
objects. This means that we're forced to do hostname verification ourselves rather
than rely on OpenSSL's own implementation of certificate verification.

We'll continue to support Python interpreters that don't have a
compiled `ssl` module, however HTTPS connections won't be possible
as is the case today.

We will also continue to in general support Python 2.7 for the forseeable
future and won't consider removing support via a breaking change until
Pip and other upstream projects also drop support.

For some data on what percentage of downloads would be effected 
[I've created a small data table](https://gist.github.com/sethmlarson/8f2272c4c1b7f6f926bec6fbce6c5689).
The number of downloads effected by the change would be ~4%.

## Add Support for Zstandard

[Zstandard](https://facebook.github.io/zstd/) defined in
[RFC 8478](https://tools.ietf.org/html/rfc8478) is looking
to be a great replacement for the long-dominant `gzip` as a content encoding.
With both great compression ratios and quick parallelizable CPU usage I'm
guessing this technology will soon take the Internet by storm, especially at
the edge / CDN layer.

When Zstandard is standardized and accepted it'd be great to already have
the feature in place to immediately start giving our users the new
performance benefits.

## Switch from Travis + AppVeyor to GitHub Actions

The number of Python versions and configurations that urllib3 supports is
quite large, testing against Linux, macOS, and Windows to ensure we're
compatible with all major OS flavors. With Travis [dropping the default
concurrency level to 3 for OSS projects](https://twitter.com/hugovk/status/1233787684587556864)
and AppVeyor continuing to support only 1 concurrent job we're feeling
cornered into long CI durations.

Fortunately we've been experiencing success with GitHub Actions as a CI
platform in other projects with the 20 concurrent jobs as well as
great flexibility and access to all platforms from one service and would
like to switch wholesale to GA from Travis and AppVeyor.

**If you have questions or there are projects you think should be prioritized
contact me on email or Twitter!**
