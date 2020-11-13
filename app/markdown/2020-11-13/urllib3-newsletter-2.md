# urllib3 Newsletter #2

Welcome to our second newsletter, more exciting news from our team!
If you'd like to join our community you can [find us on Discord](https://discord.gg/CHEgCZN).

## Open Collective and GitCoin Grants

Major development work on urllib3 is only possible
through financial support. We have multiple ways for
individuals and organizations to support us, either on
[Open Collective](https://opencollective.com/urllib3)
or [GitCoin Grants](https://gitcoin.co/grants/65/urllib3).

Please consider making a donation or grant if your organization
depends on urllib3.

## urllib3 1.26.0 released

Our team delivered the first release in the v1.26 release stream! 🎉🎉🎉

Big thank-you to urllib3 team members and community contributors for all
the hard work on this release:

- [Quentin Pradet](https://github.com/pquentin)
- [Hod Bin Noon](https://github.com/hodbn)
- [Jorge Lopez-Silva](https://github.com/jalopezsilva)
- [Ian Stapleton Cordasco](https://github.com/sigmavirus24)
- [Pradyun Gedam](https://github.com/pradyunsg)
- [Hasan Ramenzani](https://github.com/hramezani)
- [Rober Morales-Chaparro](https://github.com/robermorales)
- [Matthew Hughes](https://github.com/matthewhughes934)
- [Ezzeri Esa](https://github.com/savarin)
- [@PleasantMachine9](https://github.com/PleasantMachine9)

Highlights of the release include complete HTTPS proxy support,
a default `User-Agent` header, and deprecated TLS 1.0 and 1.1 handshakes
by default and some `Retry` options have been renamed, and a lot more.

[Check out the release on GitHub](https://github.com/urllib3/urllib3/releases/tag/1.26.0)
for the full list of changes, there are a lot of good ones in this release!

The v1.26 release stream comes just over a year and a half after the
[v1.25 release stream](https://github.com/urllib3/urllib3/releases/tag/1.25)
which came out on April 22nd, 2020 (ahh, simpler times!)

## Regression Fixes in v1.26

After releasing urllib3 `1.26.0` we received two regression bug reports
over two days. Both regressions were fixed and released in `1.26.1` and `1.26.2`
within hours of being reported to our issue tracker.  We're able to achieve this
because we're supported by [Tidelift](https://tidelift.com)
and [our release process allowing fast and high fidelity releases](https://blog.tidelift.com/how-tidelift-helps-urllib3-maintainer-seth-larson-support-more-python-versions-and-release-streams).

## urllib3 master branch is for v2.0 development

Starting with [this commit](https://github.com/urllib3/urllib3/commit/6611153650b697d56f14be347946f4a814d7fc72)
the `master` branch is now exclusively for v2.0 development, meaning that Python <3.6 support on the branch
will be removed very soon.

## Requests v2.25.0 supports urllib3 v1.26

Very soon after urllib3 v1.26.0 was released
[Requests also added support for urllib3 v1.26](https://github.com/psf/requests/blob/master/HISTORY.md#2250-2020-11-11).
We work very closely with Requests maintainers to ensure a smooth upgrade
process can be made by our users.

## Migrating away from Travis to GitHub Actions

Tons of work has been done by a urllib3 maintainer [Quentin Pradet](https://github.com/pquentin)
to help the project migrate from a combination of Travis and AppVeyor to GitHub Actions to support
all major operating systems. That work started before Travis announced changes
to the Open Source plan, but we're very happy that we started the migration when
we did.

Now that our [test suite is ready for Ubuntu Focal Fossa](https://github.com/urllib3/urllib3/pull/2050)
we're hopeful that migrating wholesale over to GitHub Actions can follow soon!
