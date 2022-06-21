# Get paid to contribute to urllib3 (Newsletter #7)

## Announcing urllib3's bounty program

<div class="row">
<div class="col-6">
<p><strong><a href="https://urllib3.readthedocs.io/en/latest/contributing.html#getting-paid-for-your-contributions">The urllib3 team is excited to announce the start of our bounty program!</a></strong></p>

<p>We’ve recognized that one of the biggest challenges to shipping v2.0 is <strong>not having enough time to devote to contributions</strong>. Our bounty program is hoping to spur interest from the community in the urllib3 project and fairly pay contributors for their time and experience.</p>

<p>The bounty program works by marking issues with bounty amounts we’re willing to pay for anyone to complete an issue. Don't worry if you're not an existing contributor — <strong>new contributors are welcome and encouraged!</strong></p>

<p>Bounty amounts start at $100 for small issues and <strong>most issues are $300 or more</strong>. Each issue includes a series of tasks that must be completed in order to receive the bounty. Bounties are paid out through <a href="https://opencollective.com/urllib3#category-BUDGET">our public Open Collective balance</a>.</p>

<p>We’ve already seen early success from the “<a href="https://twitter.com/quentinpradet/status/1533894962185633794">soft launch</a>” of our bounty program. urllib3 maintainer <a href="https://github.com/pquentin">Quentin Pradet</a> tweeted about a single issue with a bounty and ended up generating enough interest for 3 new contributors to open 5 new pull requests! We’ve also <a href="https://opencollective.com/urllib3/expenses">already paid out for two bounties</a>.</p>

</div>
<div class="col-6">
<blockquote class="twitter-tweet"><p lang="en" dir="ltr">CPython has experimental support for OpenSSL 3.0 with &quot;known performance regressions, missing features and potential bugs&quot;. Major distributions ship Python with OpenSSL 3.0 though, which breaks urllib3 tests. 😿<br><br>Help us understand why and get paid $300! <a href="https://t.co/xoJ3c89Po3">https://t.co/xoJ3c89Po3</a></p>&mdash; Quentin Pradet 🇪🇺 (@quentinpradet) <a href="https://twitter.com/quentinpradet/status/1533894962185633794?ref_src=twsrc%5Etfw">June 6, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>
</div>

If you're interested we've [documented the process](https://urllib3.readthedocs.io/en/latest/contributing.html#getting-paid-for-your-contributions) which includes finding an issue with a bounty, completing the issue, and submitting an expense to Open Collective to be paid. If you have any questions about the process you can ask in [our community Discord](https://discord.gg/urllib3) or by emailing a maintainer.

This bounty program is an experiment so we’re looking to learn how this model can work for our project and share our findings with the rest of the open source community.

## Spotify sponsors urllib3 through their FOSS Fund

Spotify announced the [recipients of the 2022 Spotify FOSS Fund](https://engineering.atspotify.com/2022/06/say-hello-to-the-recipients-of-the-2022-spotify-foss-fund/) and urllib3 was among the 8 projects receiving funding. urllib3 was awarded **€13,000** from the total fund of **€100,000**. In the announcement post it was noted that Spotify had over 2400 dependencies and 59 nominations from staff which were narrowed down to 18 which met eligibility criteria and finally 8 projects which received funding.

## Progress on urllib3 v2.0

The [v2.0 milestone on GitHub](https://github.com/urllib3/urllib3/milestone/6) tracks our progress towards the v2.0 release of urllib3. Since the last newsletter 7 issues have been closed, leaving only [8 open issues](https://github.com/urllib3/urllib3/milestone/6) remaining for a v2.0 release. We’re hoping through our bounty program we’ll see an increase in velocity towards a v2.0 release!

Of the issues closed, here are the highlights:

- Fixing all the links and references in our documentation and making type hints in documentation more user-friendly after the migration to `BaseHTTPConnection` ([#2604](https://github.com/urllib3/urllib3/pull/2604))
- Dropping support for the unsafe SSLv2 and SSLv3 for pyOpenSSL and SecureTransport TLS implementations ([#2563](https://github.com/urllib3/urllib3/pull/2563))
- Respecting `SSLContext.hostname_checks_common_name` setting if explicitly enabled by user ([#2518](https://github.com/urllib3/urllib3/pull/2518))
- Align the logic for connecting via TLS to a proxy and the destination ([#2529](https://github.com/urllib3/urllib3/pull/2529))
- Switched to Flit for our build system and configured reproducible builds for our releases ([#2549](https://github.com/urllib3/urllib3/pull/2549))
- Switched our chunked framing logic to work consistently in all situations ([#2565](https://github.com/urllib3/urllib3/pull/2565))
- Changed the sentinel `FAILEDTELL` to use valid type hints instead of `object` ([#2519](https://github.com/urllib3/urllib3/pull/2519))

## OpenSSL 3.0

Back in September of 2021 [OpenSSL 3.0.0 was released](https://www.openssl.org/blog/blog/2021/09/07/OpenSSL3.Final/). Some time after the release of OpenSSL 3.0 various operating systems like [Ubuntu 22.04](https://discourse.ubuntu.com/t/openssl-3-0-transition-plans/24453) and [Fedora 36](https://fedoraproject.org/wiki/Changes/OpenSSL3.0) have started using OpenSSL 3.0 instead of OpenSSL 1.1.1 as their default version of OpenSSL.

This is exciting news for OpenSSL but requires more testing for urllib3 to make sure code won't break when using this new OpenSSL release. Currently support for OpenSSL 3.0 in CPython at the time of writing [is preliminary and experimental](https://mail.python.org/archives/list/python-dev@python.org/thread/ATO4DM6QYZGLSGGDZ3TRN5X3QDD5OHOE/). To ensure urllib3 users don't experience failures when using OpenSSL 3.0 [we've started testing against both OpenSSL 1.1.1 and 3.0 in our continuous integration](https://github.com/urllib3/urllib3/pull/2626). This includes testing against the [cryptography package](https://cryptography.io) which is currently compiled with OpenSSL 3.0.3 [starting in v37.0.0](https://cryptography.io/en/latest/changelog/#v37-0-0). This change was completed by [Illia Volochii](https://github.com/illia-v) and rewarded as a part of our bounty program.
