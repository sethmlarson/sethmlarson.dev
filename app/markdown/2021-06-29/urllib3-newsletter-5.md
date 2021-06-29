# urllib3 Newsletter #5

Fifth newsletter, commence! If you'd like to discuss this edition of our newsletter
you can [join our community Discord](https://discord.gg/urllib3).

## Thanks to our Sponsors

The urllib3 team is very grateful for all of our sponsors and supporters.
If you'd like to support our team we have a [GitHub Sponsors](https://github.com/sponsors/urllib3), [GitCoin Grants](https://gitcoin.co/grants/65/urllib3), and [Open Collective](https://opencollective.com/urllib3).

Notable updates to our sponsors include:

– [GitCoin Grant Round 10](https://gitcoin.co/grants/65/urllib3) included urllib3 which has raised >$2000 so far! 🎉

– [NewRelic](https://github.com/newrelic) started sponsoring our team on GitHub Sponsors 👏

## We paid someone to work on Open Source

[David Lord](https://github.com/davidism) who is known for his work on Flask, Jinja and other Pallets
projects worked on [one of our v2.0 issues](https://github.com/urllib3/urllib3/issues/1062) related to how we encode `fields`
into the URL. We wanted to modernize how urllib3 does things, you'd think that wouldn't be too tough... However it took a ton of time to unravel what urllib3 was doing
and why that had deviated from the current standard [WHATWG HTML](https://github.com/urllib3/urllib3/issues/1062).
You can read [all of the discussion and discoveries](https://github.com/urllib3/urllib3/issues/1062#issuecomment-857981186) that went into untangling this pile of standard spaghetti and code archaeology.

The most exciting part of all this is that this is the first time we've paid
a contributor who's not a part of our team to work on Open Source, woohoo! 🥳

If you're interested in getting paid to work on urllib3 v2.0 issues you
can join our Discord or reach out to the team and we'll walk you through everything.
We're also working on making issues which we're willing to pay for work much
more visible.

## urllib3 v1.26.6 released

[We've released another patch for the urllib3 v1.26.x series](https://github.com/urllib3/urllib3/releases/tag/1.26.6).
This release included a few fixes for small bugs but also included a larger change in
deprecated the `urllib3.contrib.ntlmpool` module, more on that below.

Quentin has been [working on migrating the downstream integration tests](https://github.com/urllib3/urllib3/pull/2304)
that are run before every urllib3 release from Travis which have been defunct for
some time now to GitHub Actions. This will greatly reduce the amount of manual
work required to release urllib3 and [drastically reduce maintainer stress](https://twitter.com/sethmlarson/status/1397603959733243908),
thanks Quentin! 🙇

Quentin and I also did the release together this time around and we've created
a [complete checklist](https://github.com/urllib3/urllib3/issues/2307) to make executing releases by other collaborators easier.

## Deprecating NTLMConnectionPool in v1.26.6

The `urllib3.contrib.ntlmpool` module will now unconditionally raise a `DeprecationWarning` pointing
users to a specific issue where we justify this change and
[we'd like for users to comment](https://github.com/urllib3/urllib3/issues/2282)
if they're actually relying on the module.

The module itself was contributed a long time ago and hasn't had many issues,
pull requests, or maintenance and we actually don't have any
test cases so we're not even sure how well it works anymore...

Given that NTLM has been deprecated for 10 years we'd like to remove the
module in v2.0 but aren't sure if it should live somewhere else or if it
should be deleted completely. [Please let us know!](https://github.com/urllib3/urllib3/issues/2282)

## CVE-2021-33503

A security vulnerability was reported by [Nariyoshi Chida](https://github.com/NariyoshiChida)
in our URL parser. We coordinated with Nariyoshi and our Tidelift security contact to verify
the vulnerability and provide a suitable fix for the issue and released v1.26.5 which included the fix.

Read the full [GitHub Security Advisory](https://github.com/urllib3/urllib3/security/advisories/GHSA-q2q7-5pp4-w6pg)
for more information.

## New collaborators and contributors

We've invited a few of our contributors to become collaborators on the project
after consistent high-quality contributions. Welcome [Bastian Venthur](https://github.com/venthur)
and [Ran Benita](https://github.com/bluetech)! Thank you for everything you've done so far for urllib3 👏

We also had many first time contributors in the past month after a couple of tweets
brought in a bunch of new faces. Thanks to everyone who contributed! If you're
interested in getting started contributing to urllib3 we announce all the new
"[Contributor Friendly](https://github.com/urllib3/urllib3/issues?q=is%3Aissue+is%3Aopen+label%3A%22Contributor+Friendly+%E2%99%A5%22)"
issues in the [community Discord](https://discord.gg/urllib3).
