# Documenting certificate distribution pain points for the Python ecosystem

I'm writing this blog post on the same day as
the [eMudhra Intermediate CA compromises news](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576) was
published so the memory of what was required from me
and unfortunately volunteer maintainers today
is still fresh and top-of-mind. Fixing the systemic
issues that many open source projects faced today
takes longer than a day of hurriedly patching everything
and publishing advisories, so I'm leaving these
as notes for future us.

I'm only writing from the perspective of the Python
ecosystem, although I know at least some of these
issues exist elsewhere. Here's some context:

* CPython uses OpenSSL for TLS on all platforms and OpenSSL
  requires CA root certificates provided as files, directories,
  or in-memory data. CPython distributes OpenSSL to Windows and macOS,
  because those platforms don't distribute OpenSSL on their own typically.
  Linux distributions do distribute OpenSSL typically.
* certifi is the Python ecosystems' packaged distribution of CA root certificates.
  certifi was designed to work well with OpenSSL, but many Linux distributions
  distribute CA root certificates as their own package, too (and do a much better job today than long ago). So in practice,
  certifi is useful today on Windows and macOS where the system certificate stores
  can't be made available as a file or directory to be compatible with OpenSSL.
* Much of the pain of this incident is because we can't revoke certificates
  actively by default on an OpenSSL-based Python installation. If we could do so,
  then any revocation mechanism could protect end-users without dependency updates.
* Some of the pain is caused by needing to update certifi as a dependency, and
  everything associated with upgrading across a dependency tree.

## Python and pip

pip bundles its dependencies because bootstrapping is a really hard problem,
including certifi. Python bundles pip because bootstrapping is a really hard
problem. So a critical issue in certifi means potentially updating both pip and Python
on short notice.

Python distributes pip through ensurepip, so the Python Security Response Team
sometimes needs to respond by upgrading pip in case of a vulnerability that
affects whether pip can be securely used to upgrade itself... like in the case
of a CA certificate compromise... So if there's an issue in certifi not only
do we need to publish a release of pip, we need to head-of-line block on that
release landing in Python (across relevant release branches, usually 3-4),
and then do releases of those branches.

pip already uses truststore (a library I maintain) by default.
For compatibility reasons, pip still adds certifi
root certificates to be considered as roots. By removing the certifi default ([which appears
to be happening](https://github.com/pypa/pip/issues/14374)) this would *slightly* improve the situation for Linux-based users,
where they could upgrade their system CA certificates and be safe, still no
revocation mechanism. The big benefit is that pip maintainers wouldn't need to do
anything in the case of a certifi CA store compromise anymore.

Many other packaging tools and infra had to take action on short notice, too,
like the manylinux build images, various bots
and cron jobs, Python build bots, Sigstore CLI for Python, and likely many more.

Once all the patching is done, the biggest problem then is alerting users as they
too have to take action to upgrade dependencies. I [published a topic on
discuss.python.org](https://discuss.python.org/t/information-for-python-users-regarding-emudhra-emsign-ca-certificate-security-incident/109576), sent an alert to security-announce@python.org, added
banners to pypi.org and discuss.python.org, and posted on social media (thanks for boosting).

## PyPI as a certificate distribution channel

An over-arching opinion that I have (and I am willing to be wrong) is that PyPI
should no longer be a certificate distribution channel. Packages like certifi were necessary
in the past to get a decent CA certificates bundle to platforms without one.
**Remember, Python is about the same age as TLS and much older than the expectation that your system has decent CA certificate bundles**.
Today I am not aware of a major platform that exists *without* a decent CA certificate bundle,
as Python isn't the only application that needs CA certificates. And I'm not sure
how much it is Python or pip's responsibility that your system provides a decent
CA certificate bundle.

Maybe it's time to evaluate leaning on system-provided certificate stores
more generally in the Python ecosystem. This would mean less work for
open source maintainers that provide applications (Python, pip), by
relying on maintainers of systems instead (distros, browsers, services like Let's Encrypt).
Systems maintainers have to do this work anyway, can we rely more on their work
so we don't have to painfully duplicate that same work across an ecosystem?

## Revocation for OpenSSL-based platforms

This is still an open question for me, what is the best way forward towards
certificate revocation for OpenSSL-based platforms like Linux distributions.
I haven't spent a lot of time thinking about this, but if we could have this
in a privacy and performance preserving way that would go a long way to reduce
the amount of short-notice demands on volunteers or open source projects.

That's all for now, time to log off and rest up.
