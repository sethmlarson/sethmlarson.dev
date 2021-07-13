# Everything to know about Requests v2.26.0

[Requests v2.26.0](https://github.com/psf/requests/pull/5868) is a large release which changes and removes
many features and dependencies that you should know about when upgrading.
Read on to find out all about the changes and what you should do
if you're a user of Requests.

## Summary of the release

### What changes are important?

- Changed the `requests[security]` extra into a no-op.
  Can be safely removed for v2.24.0+ for almost all users
  (OpenSSL 1.1.1+ and not relying on specific features in pyOpenSSL)
- Dropped support for Python 3.5
- Changed encoding detection library for Python 3.6+
  from `chardet` to `charset_normalizer`
- Added support for Brotli compressed response bodies

### What should you do now?

- Upgrade to Requests v2.26.0 if you're not using Python 3.5
- Stop using `requests[security]` and instead install just `requests`
- Regenerate your lock files and pinned dependencies if you're using `pip-tools`, `poetry`, or `pipenv`
- [Read the full set of changes](https://github.com/psf/requests/pull/5868) for v2.26.0

## Encoding detection with charset_normalizer

The following section has a brief discussion of licensing issues. Please remember that
I am not a lawyer and don't claim to understand anything about open source licenses.

Requests uses character detection of response bodies in order to reliably decode
`bytes` to `str` when responses don't define what encoding to use via
[`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type).
This feature only gets used when you call the `Response.text()` API.

The library that Requests uses for content encoding detection has for the past 10 years been
[`chardet`](https://github.com/chardet/chardet) which is licensed LGPL-2.1.

The LGPL-2.1 license is not a problem for almost all users, but an issue arises with statically linked Python
applications which are pretty rare but becoming more common. When Requests is bundled with a static
application users can no longer "switch out" `chardet` for a different library which causes a problem with LGPL.

Starting in v2.26.0 for Python 3 the new default library for encoding detection will be
[`charset_normalizer`](https://github.com/Ousret/charset_normalizer)
which is MIT licensed. The library itself is relatively young so a lot of work has gone into making sure users
aren't broken with this change including extensive tests against real-life websites and comparing the results
against `chardet` to ensure better performance and accuracy in every case.

Requests will continue to use `chardet` if the library is installed in your environment.
To take advantage of `charset_normalizer` you **must uninstall `chardet` from your environment**.
If you want to continue using `chardet` with Requests on Python 3 you can install
`chardet` or install Requests using `requests[use_chardet_on_py3]`:

```
$ python -m pip install requests chardet

- OR -

$ python -m pip install requests[use_chardet_on_py3]
```

## Removed the deprecated \[security\] extra

Before [Requests v2.24.0](https://github.com/psf/requests/blob/master/HISTORY.md#2240-2020-06-17) the pyOpenSSL implementation of TLS was used by default
if it was available. This pyOpenSSL code is packaged along with urllib3 as a way
to use Subject Name Identification (SNI) when Python was compiled against super-old
OpenSSL versions that didn't support it yet.

Thankfully these super-old versions of OpenSSL aren't common at all anymore! So now
that pyOpenSSL code that urllib3 provides is a lot less useful and now a maintenance
burden for our team, so we now have a long-term plan to eventually remove this code.
The biggest dependency using this code was Requests, a logical first place to start the journey.

Starting in [Requests v2.24.0](https://github.com/psf/requests/blob/master/HISTORY.md#2240-2020-06-17) pyOpenSSL wouldn't be used unless Python wasn't compiled
with TLS support (ie, no `ssl` module) or if the OpenSSL version that Python was compiled
against didn't support SNI. Basically the two rare scenarios where pyOpenSSL was actually useful!

The release of v2.24.0 came and went quietly which signaled to our team that our long-term plan
of actually removing pyOpenSSL will likely go smoothly. So in Requests v2.25.0 we officially deprecated
the `requests[security]` extra and in v2.26.0 the `[security]` extra will be a no-op. Instead
of installing `pyOpenSSL` and `cryptography` no dependencies will be installed.

What this means for you is if you've got a list of dependencies that previously used
`requests[security]` you can remove the `[security]` and only install `requests`.
If you have a lock file via a tool like `pip-tools` or `poetry` you can regenerate
the lock file and potentially see `pyOpenSSL` and `cryptography` removed from your lock file. Woo!

## Dropped support for Python 3.5

Starting in [Requests v2.25.0](https://github.com/psf/requests/blob/master/HISTORY.md#2250-2020-11-11) there
was a notice for Python 3.5's deprecation in the changelog. Now that 2.26.0 has arrived Requests will only be
supported with Python 2.7.x and 3.6+.

This is a big win for Requests maintainers as it progressively becomes more and more difficult to
maintain a codebase that supports a wide range of Python versions.

## Brotli support via urllib3

Since v1.25 urllib3 has supported automatically decoding [Brotli-compressed](https://datatracker.ietf.org/doc/html/rfc7932)
HTTP response bodies using either [Google's `brotli` library](https://github.com/google/brotli) or the
[`brotlicffi` library](https://github.com/python-hyper/brotlicffi) (previously named `brotlipy`).

Before v2.26.0 Requests would never emit an `Accept-Encoding` header with `br` signaling Brotli support
even if `urllib3` would have been able to decode the response. Now Requests will use urllib3's feature
detection for Brotli and emit `Accept-Encoding: gzip, deflate, br`. This is great news for servers that
support Brotli on pre-compressed static resources like fonts, CSS, and JavaScript. Woo!

To take advantage of Brotli decoding you need to install one of the Brotli libraries mentioned above.
You can ensure you're getting the right library for your Python implementation by installing like so:

```
$ python -m pip install urllib3[brotli]
```
