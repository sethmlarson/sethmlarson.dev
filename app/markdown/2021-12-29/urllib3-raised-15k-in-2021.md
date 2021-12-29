# urllib3 raised $15,000 in 2021 (Newsletter #6)

Welcome to the 6th urllib3 newsletter, end of 2021 edition! If you'd like to discuss this edition of our newsletter you can[ join our community Discord](https://discord.gg/urllib3).

## Thanks to our sponsors!

This year we received so much support from many different places, people, and organizations. We enter the new year with **$12,254.95 in OpenCollective available for distribution**.

**We're so thankful for everyone who contributed.** Your support means we can fairly pay for people's time and expertise and ensure that PyPI's most downloaded package continues to be secure, up-to-date, and working towards the future of HTTP in Python.

This large amount of funding means our team is planning on setting up a span of full-time development to focus on closing out v2.0 in addition to continuing to pay contributors both from our team and the community to work on urllib3.

### Where we received and spent our funding

All of these amounts shown below are after fees from payment processing, Coinbase, OpenCollective fiscal hosting, and cryptocurrency gas fees. In short it's the value that’s available for our team to pay out to contributors. We funnel all of our funds to [OpenCollective](https://opencollective.com/urllib3) in order to make payment processing easy for as many individuals as possible.

* $8,087.38 from [GitCoin Grants](https://gitcoin.co/grants/65/urllib3) ¹
* $5,050.00 from [Tidelift](https://tidelift.com/subscription/pkg/pypi-urllib3?utm_source=pypi-urllib3&utm_medium=referral&utm_campaign=enterprise) ²
* $1,358.97 from [GitHub Sponsors](https://github.com/sponsors/urllib3)
* $504.00 from [OpenCollective contributors](https://opencollective.com/urllib3)
* **$15,000.35** from all sources

Funds were paid out to the following individuals:

* $4,075 paid to [Seth Michael Larson](https://github.com/sethmlarson)
* $3,325 paid to [Quentin Pradet](https://github.com/pquentin)
* $1,900 paid to [Hasan Ramenzani](https://github.com/hramezani)
* $140 paid to [David Lord](https://github.com/davidism)
* **$9,440** paid in total

¹ Amount from GitCoin is only DAI and USDC that were sold for USD. Other currencies that were donated have not been converted to USD yet to avoid paying fees on small amounts.

² Tidelift is paid directly to Seth Larson and Quentin Pradet and isn't subject to OpenCollective fees.

## Releases and Contributors

There were [5 new releases of urllib3](https://github.com/urllib3/urllib3/releases) over the past year, two of which contained fixes for security issues [CVE-2021-28363](https://github.com/urllib3/urllib3/security/advisories/GHSA-5phf-pp7p-vc2r) and [CVE-2021-33503](https://github.com/urllib3/urllib3/security/advisories/GHSA-q2q7-5pp4-w6pg). Hopefully you’re using the latest 1.26.7 release! We received 197 commits from [17 unique committers](https://github.com/urllib3/urllib3/graphs/contributors?from=2021-01-1&to=2021-12-31&type=c) across the year. Thanks to everyone who contributed.

## Progress towards v2.0

The [v2.0 milestone on GitHub](https://github.com/urllib3/urllib3/milestone/6) tracks our progress towards the v2.0 release of urllib3. This year our team closed 25 issues in the v2.0 milestone, leaving only [11 open issues](https://github.com/urllib3/urllib3/milestone/6) remaining for a v2.0 release. We’re hopeful that the focus on paying for sustained development time in 2022 will mean a v2.0 release next year.

Even after v2.0 is released our team plans on continuing bug fix and security support for the v1.26.x release stream thanks to financial support from Tidelift.

## Type hints case study

[Hasan Ramenzani](https://github.com/hramezani) spent a ton of time working on type hints for the v2.0 branch. This work spanned multiple months and included so many lessons learned and interesting situations that our team [wrote a case study](https://sethmlarson.dev/blog/2021-10-18/tests-arent-enough-case-study-after-adding-types-to-urllib3) on the entire experience.

## Unreasonable effectiveness of investing in open source

Quentin Pradet was [paid to work 20 hours on urllib3](https://quentin.pradet.me/blog/i-got-paid-to-work-on-open-source-2.html) and once again proved the incredible return on investment that paid open source contributions can be. Over the course of 20 hours Quentin contributed many PRs to urllib3 which resulted in finding a bug in Python’s ssl module. Quentin [submitted a bug report](https://bugs.python.org/issue43522) to Python which inspired a [usability bug fix to OpenSSL](https://github.com/openssl/openssl/pull/14856). Not bad!

## PyCascades 2021

Seth spoke at [PyCascades 2021](https://2021.pycascades.com/) back in February about how the urllib3 team plans on shipping breaking changes in v2.0. You can watch the [recording on Youtube](https://www.youtube.com/watch?v=o9ESKvkuvXM).
