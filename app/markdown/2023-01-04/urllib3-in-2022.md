# urllib3 in 2022

## Funding

In total urllib3 received **$26,615 USD in financial support**
and **distributed $18,622 USD** to maintainers and community contributors.
**We're thankful for the financial support we receive from
our sponsors.** Without funding we wouldn't be able to
compensate maintainers to continuously lead, upkeep, and secure urllib3.
Without funding we couldn't reward contributions and larger projects like urllib3 v2.0 would
either never be finished or take even longer than the year+ it's taken already to ship.

Let's dive into our sources of financial support in 2022 and how the money was spent:

### Open Collective

- $12,900 from the [Spotify 2022 FOSS Fund](https://engineering.atspotify.com/2022/06/say-hello-to-the-recipients-of-the-2022-spotify-foss-fund/)
- $1,433 from contributions via [GitHub Sponsors](https://github.com/sponsors/urllib3/)
- $160 from contributions via [Open Collective](https://opencollective.com/urllib3)

We disbursed [~$6,500 USD from our Open Collective](https://opencollective.com/urllib3/transactions?period=2022-01-01T06%3A00%3A00.000Z%E2%86%922023-01-01T05%3A59%3A59.999Z&kind=EXPENSE) to maintainers and community contributors for their work on the project.
We go into 2023 with $18,827 in our Open Collective balance. In the new year our team will continue
using Open Collective funds for "[issue bounties](http://sethmlarson.dev/get-paid-to-contribute-to-urllib3)"
to attract new contributors and reward existing ones for their hard work. We'll also hopefully have
time available for some contributors to work on larger initiatives as has been done in 2022.

### Direct payments and awards

We also had financial contributions that didn't go into our Open Collective.
These are contributions that either dispersed directly from Tidelift to maintainers
of the project or from financial awards that were given to individuals for maintaining urllib3.

- $6,152 from [Tidelift](https://tidelift.com/subscription/pkg/pypi-urllib3?utm_source=pypi-urllib3&utm_medium=referral&utm_campaign=blog), split between Seth Larson and Quentin Pradet
- $5,000 from [Tidelift](https://tidelift.com/subscription/pkg/pypi-urllib3?utm_source=pypi-urllib3&utm_medium=referral&utm_campaign=blog) to Seth Larson
- $550 from [GitHub Maintainer Month](https://github.blog/2022-06-24-thank-you-to-our-maintainers/) to Seth Larson via GitHub Sponsors
- $420 from [Indeed](https://github.com/orgs/indeedeng/sponsoring) to Seth Larson via GitHub Sponsors

## 2.0.0 alpha is now available!

The [first pre-release of urllib3 v2.0.0](https://github.com/urllib3/urllib3/releases/tag/2.0.0a1) was made available in November 2022. Massive thank-you to the many contributors who helped achieve this milestone over multiple years. The final push in November required paid full-time
work by maintainers Quentin Pradet and Seth Larson. Both of them [documented](https://quentin.pradet.me/blog/i-got-paid-to-work-on-open-source-3.html) their [experiences](https://sethmlarson.dev/working-on-urllib3-full-time-for-one-week).
The release includes the following highlighted changes:

- Added a complete set of type hints (Thanks to [Hasan Ramenzani](https://github.com/urllib3/urllib3/pulls?q=is%3Apr+author%3Ahramezani+is%3Aclosed+type+hint))
- Added a `json` parameter to `.request()` methods and `.json()` method to `HTTPResponse`
  for easier processing of JSON data both for requests and responses (Thanks to [Sai Vinay](https://github.com/urllib3/urllib3/pull/2250))
- Added a top-level `urllib3.request()` method for sending HTTP requests without configuring a `PoolManager` (Thanks to [Franek Magiera](https://github.com/urllib3/urllib3/pull/2150))
- Added ability to append multiple headers names to `HTTPHeaderDict` and not have them be merged when sent (Thanks to [Raphael Gaschignard](https://github.com/urllib3/urllib3/pull/2669))
- Added support for zstandard compression (Thanks to [Mauro Amico](https://github.com/urllib3/urllib3/pull/2624) and [Gregory Szorc](https://github.com/indygreg/python-zstandard/commit/1dc39cfea821893268176dae754355ec19609ce0))
- Removed support for verifying certificates with `commonName` by default, now only `subjectAltName` is used.
- Changed the default minimum TLS version to 1.2 (was TLS 1.0)
- Changed `multipart/form-data` header formatting to match WHATWG standard (Thanks to [David Lord](https://github.com/urllib3/urllib3/pull/2257))
- Removed support for Python 3.6 and earlier. Codebase has been optimized for Python 3.7+
- Removed the `urllib3.contrib.ntlmpool` module
- Deprecated the `urllib3.contrib.pyopenssl` and `urllib3.contrib.securetransport` modules
- Removed support for non-OpenSSL TLS libraries (ie LibreSSL, wolfSSL)
- Removed support for OpenSSL versions before 1.1.1
- Removed support for unmaintained Python implementations (Google App Engine, Jython)

The team is hopeful to publish the stable release in early 2023 after ensuring all major dependent packages are able to integrate safely. You can read the [v2.0 migration guide](https://urllib3.readthedocs.io/en/latest/v2-migration-guide.html) or [changelog](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) if you're interested more information.

## Security posture improvements

Tidelift sponsored exploratory work into improving urllib3's security posture by evaluating OpenSSF projects like [Scorecard](https://securityscorecards.dev), [Best Practices](https://bestpractices.coreinfrastructure.org), [Sigstore](https://www.sigstore.dev), and [Supply chain Levels for Software Artifacts](https://slsa.dev) (SLSA).
The results of the work resulted in urllib3 being scored [9.6/10](https://deps.dev/pypi/urllib3) on OpenSSF Scorecard which tracks a wide range of security health metrics.
This is at the time of writing the [highest score](https://github.com/sethmlarson/pypi-scorecards/blob/main/data/2022-12-31.csv) achieved by any Python package on PyPI.

Starting in v1.26.12, urllib3 is now published with [provenance attestations](https://slsa.dev/provenance) thanks to SLSA. We use the [generic GitHub SLSA generator](https://github.com/slsa-framework/slsa-github-generator) with GitHub OIDC to generate a provenance attestation and achieve [SLSA level 3](https://slsa.dev/spec/v0.1/levels). This attestation allows consumers to prove their wheels and sdists were built for a specific git tag, GitHub repository, and GitHub Action workflow.

The work of integrating Scorecard, SLSA, and Sigstore with urllib3 resulted in [at least 11 developer experience issues](https://gist.github.com/sethmlarson/b933cbc6970b81e9069d2da4c16089ce) filed and fixed in the listed projects
to help future project maintainers adopt these tools.

## 2022 in numbers

Some more statistics for urllib3 in 2022:

- **3 billion downloads in 2022 alone** with over 250 million per month. urllib3 represented **~1.63% of all downloads on PyPI for the year**. Reached [7.4 billion total downloads](https://pepy.tech/project/urllib3) by the end of 2022.
- [1 million](https://github.com/urllib3/urllib3/network/dependents) explicitly dependent public repositories on GitHub.
- [380K unique users to our documentation](https://urllib3.readthedocs.io).
- [8 releases to PyPI](https://github.com/urllib3/urllib3/releases)
- [139 commits from 14 unique contributors](https://github.com/urllib3/urllib3/graphs/contributors?from=2022-01-01&to=2022-12-31&type=c)

If you'd like to discuss this article you can join our [community Discord](https://discord.gg/urllib3).
