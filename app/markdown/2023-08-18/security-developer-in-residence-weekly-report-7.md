# Security Developer-in-Residence – Weekly Report #7

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

The past few weeks have been fairly light as I've taken time off to [get married](https://twitter.com/sethmlarson/status/1692284180183318789)! 🎉
The usual weekly cadence will resume next week.

## RFI on OSS Security by US National Cyber Director

The biggest news in the open source security space right now is the Request for Information (RFI)
titled "[Request for Information on Open Source Software Security: Areas of Long-Term Focus and Prioritization](https://www.whitehouse.gov/wp-content/uploads/2023/08/OS3I-RFI-Embargoed-Until-08102023-0500EST.pdf)".
This announcement means that the US Government is soliciting ideas from the broader community
on where to focus and what to do to improve the security of open source software.

I've been catching up this initiative since returning from time away, you can read the [fact sheet about the RFI](https://www.whitehouse.gov/oncd/briefing-room/2023/08/10/fact-sheet-office-of-the-national-cyber-director-requests-public-comment-on-open-source-software-security-and-memory-safe-programming-languages/)
and [Tidelift's summary blog post](https://blog.tidelift.com/new-rfi-shows-the-us-gov-effort-to-invest-in-open-source-is-picking-up-steam) for more information.

## Certifi and Truststore

Back in late July, certifi [published a GHSA advisory](https://github.com/advisories/GHSA-xqr8-7jwr-rhp7) about the removal of the e-Tugra root certificate.
This advisory had an associated CVE ID so should eventually make its way into the PyPA advisory database
but the automation [wasn't able to import it automatically](https://github.com/pypa/advisory-database/pull/138).
After that issue was resolved, pip was able to land a PR [upgrading certifi to the latest version](https://github.com/pypa/pip/pull/12206).

Certifi is a critical package in the Python ecosystem as it's the most common way that `SSLContext` instances
are configured due to strong ties to the OpenSSL library by Python's `ssl` module. A consequence of certifi's
use in pip in particular due to bundling causes a chain of events whenever there's a security issue with a root CA:

* Removal occurs in Mozilla Root CA Bundle
* Certifi bundles the Mozilla Root CA Bundle, requires an update, advisory, and new release of certifi.
* Pip bundles certifi, requires a new release of pip.
* New pip releases require a release of [get-pip](https://github.com/pypa/get-pip).
* Python bundles a default version of pip and it's preferable to bundle a version of pip that isn't
  vulnerable to any CVEs (but this issue is fixable by users).

This chain of updates causes a lot of churn any time there's a removed CA in certifi and doesn't account for
all the upgrades that need to happen in individual application lock files.

[Truststore](https://truststore.readthedocs.io) is a library authored by myself and David Glick which is aiming to remove the need for certifi
by using system trust stores instead of hardcoded bundle which puts the onus of keeping the trust store up-to-date on the system
itself (which for macOS and Windows can be automatically updated in the background!)

Truststore has recently received a [large amount of passive users](https://twitter.com/sethmlarson/status/1687845307558600704)
thanks to [PDM adopting the library](https://twitter.com/sethmlarson/status/1687842369440227328)
when installed via `pdm[truststore]` or `pdm[all]`. The code path is automatically used if `truststore`
is installed which means we can be sure that the library is working as intended for a wide variety of configurations.
I've been monitoring PDM's issue tracker for issues related to truststore and so far there aren't any
after being installed ~2,000 times per day.

Pip [currently supports using truststore](https://pip.pypa.io/en/stable/topics/https-certificates/#using-system-certificate-stores) if its already installed and I have an [outstanding PR](https://github.com/pypa/pip/pull/12107) for adding truststore support
to pip without the need to install the library separately.

Below is a list of projects (ordered by downloads) which directly depend on certifi that also would be
candidates to switch from certifi to truststore but don't have the same issue of bundling certifi that pip does:

- [requests](https://pypi.org/project/requests)
- [msrest](https://pypi.org/project/msrest)
- [snowflake-connector-python](https://pypi.org/project/snowflake-connector-python)
- [httpcore](https://pypi.org/project/httpcore)
- [opensearch-py](https://pypi.org/project/opensearch-py)
- [httpx](https://pypi.org/project/httpx)
- [sentry-sdk](https://pypi.org/project/sentry-sdk)
- [selenium](https://pypi.org/project/selenium)
- [pipenv](https://pypi.org/project/pipenv)
- [pyproj](https://pypi.org/project/pyproj)
- [uamqp](https://pypi.org/project/uamqp)
- [fiona](https://pypi.org/project/fiona)
- [datadog-api-client](https://pypi.org/project/datadog-api-client)
- [elastic-transport](https://pypi.org/project/elastic-transport)
- [netcdf4](https://pypi.org/project/netcdf4)
- [rasterio](https://pypi.org/project/rasterio)
- [launchdarkly-server-sdk](https://pypi.org/project/launchdarkly-server-sdk)
- [minio](https://pypi.org/project/minio)
- [yt-dlp](https://pypi.org/project/yt-dlp)

This list was generated from the following SQL query on the [pypi-data](https://github.com/sethmlarson/pypi-data) dataset.

```sql
SELECT packages.name FROM deps JOIN packages ON deps.package_name = packages.name
WHERE dep_name = 'certifi' AND extra IS NULL
ORDER BY packages.downloads DESC LIMIT 20;
```

I'm hopeful we can move away from certifi to reduce the amount of churn generated from using PyPI as a CA distribution channel.

## Other items

* Discussed with PyPI's new Safety and Security Engineer **Mike Fiedler** about Open Source Vulnerability format and its
  ability for representing malware or typo-squatted releases on PyPI. After seeing that the [OSV database now contains malware advisories](https://twitter.com/halbecaf/status/1689832761681682432),
  I checked with **Oliver Cheng** and **Caleb Brown** on the expected volume of malicious packages
  being taken down by PyPI (~1,300 per month) to verify the volume matched their expectations.
  Watch this space for more, especially regarding the [PyPI Malware Detection project](https://discuss.python.org/t/pypi-malware-detection-project/28222).
* Reviewed the [blog post for mandatory 2FA enforcement for new users of PyPI](https://blog.pypi.org/posts/2023-08-08-2fa-enforcement-for-new-users/).
* Drafted a blog post for the PSF CNA work.
* [Created a fix](https://github.com/google/osv.dev/pull/1548) in OSV tooling that was affecting pypa/advisory-database.
* [Created an issue](https://github.com/pypi/warehouse/issues/14300) for additional hardening of PyPI projects using Trusted Publishers that want to relinquish the ability to publish through other means.
* [Created a feature request](https://github.com/orgs/community/discussions/63041) for GitHub regarding default collaborators on GitHub Security Advisories.

That's all for this week! 👋 If you're interested in more you can read [next week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-8) or [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-6).
