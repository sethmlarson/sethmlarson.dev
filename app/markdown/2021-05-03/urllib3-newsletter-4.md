# urllib3 Newsletter #4

Welcome to our fourth newsletter! If you'd like to join our
community you can [find us on Discord](https://discord.gg/urllib3).

## Thanks to all of our Sponsors!

If you'd like to support our team we have a [GitHub Sponsors](https://github.com/sponsors/urllib3), [GitCoin Grant](https://gitcoin.co/grants/65/urllib3), and [Open Collective](https://opencollective.com/urllib3).

Big thank you to the generous individuals who are lending their financial support:

- [Andrew Janke](https://github.com/apjanke)
- [Cory Benfield](https://github.com/Lukasa)
- [Cosmin Stejerean](https://github.com/cosmin)
- [DJ](https://github.com/dujm)
- [FilePreviews](https://github.com/filepreviews)
- [Jeff Triplett](https://github.com/jefftriplett)
- [Michael McHugh](https://github.com/mmchugh)
- [MiraiSawatari](https://github.com/m1r4i)
- [Sebastián Ramírez](https://github.com/tiangolo)
- [mickeybrew](https://github.com/andripwn)
- [ume](https://github.com/bungoume)
- [Many contributors to our GitCoin Grant during Grant Round 9](https://gitcoin.co/grants/65/urllib3)!

If you or your organization uses Python: consider sponsoring our team's effort to keep urllib3 maintained
and to ship urllib3 v2.0 in 2021, we really appreciate it.

## Unreasonable effectiveness of investing in Open Source

Fellow urllib3 maintainer [Quentin Pradet](https://github.com/pquentin) recently set aside time for extended work on urllib3 v2.0, specifically
to complete a complex issue regarding urllib3 using Python's built-in `ssl.SSLContext` for certificate hostname
verification instead of using our current method of verifying certificates via our own vendored `ssl.match_hostname`.

Quentin [wrote on his blog about the work that was completed](https://quentin.pradet.me/blog/i-got-paid-to-work-on-open-source-2.html)
and about the unreasonable effectiveness of financial contributions to Open Source.

In summary about 20 hours of work was able to uncover a [security vulnerability in urllib3](https://github.com/urllib3/urllib3/security/advisories/GHSA-5phf-pp7p-vc2r),
a [bug in CPython](https://bugs.python.org/issue43522) related to `ssl.SSLContext.hostname_check_common_name`,
and a fix in OpenSSL along with completing the original task of making urllib3 use `SSLContext` for hostname verification. Wow!

## HTTP on Mars

[urllib3 is officially running on two planets!](https://github.blog/2021-04-19-open-source-goes-to-mars) 🚀

GitHub recently announced a [list of Open Source projects](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/personalizing-your-profile#list-of-qualifying-repositories-for-mars-2020-helicopter-contributor-badge) hosted on GitHub that were running
on the Mars Helicopter Ingenuity and urllib3 was among them. This announcement has been a super exciting achievement for our team
and we're all excited to see the future of Open Source being used within the realm of space exploration.

## CVE-2021-28363

[urllib3 1.26.4](https://github.com/urllib3/urllib3/releases/tag/1.26.4) included a fix for [CVE-2021-28363](https://github.com/urllib3/urllib3/security/advisories/GHSA-5phf-pp7p-vc2r) thanks to [Quentin Pradet](https://github.com/pquentin) and [Jorge Lopez-Silva](https://github.com/jalopezsilva) for their work here! Versions of urllib3 that are vulnerable to re 1.26.0 to 1.26.3. Versions prior to 1.26.0 are not affected.

## Welcoming a new collaborator!

[After multiple impactful contributions to the project](https://github.com/urllib3/urllib3/pulls?q=is%3Apr+author%3Afranekmagiera) our team welcomes [Franek Magiera](https://github.com/franekmagiera). Franek has been contributing to the effort of completely type-hinting the urllib3 API which is one of
the highlighted improvements coming to urllib3 v2.0. Thanks for all the hard work, Franek!
