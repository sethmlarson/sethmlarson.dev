# urllib3 Newsletter #1

Welcome to the first urllib3 newsletter! I wanted to put together
this newsletter to broadcast all the work that the urllib3
team has done the past month and to share a few very exciting
announcements!

## Open Collective and GitCoin Grants

urllib3 created an [Open Collective](https://opencollective.com/urllib3)
which we are now accepting donations and offering sponsorship to organizations and individuals.
Primarily we are looking for support to pay for core contributors to
work on urllib3 `v2.0.0`.

If cryptocurrency is more your style, we also have an
[ongoing grant through GitCoin Grants](https://gitcoin.co/grants/65/urllib3)
that allows you to support Open Source with many popular cryptocurrencies.

Thanks for considering supporting our team!

## v2.0 Roadmap and Features

The most exciting item is we released our [v2.0 Roadmap in the documentation](https://urllib3.readthedocs.io/en/latest/v2-roadmap.html)
and the [v2.0 Milestone on GitHub](https://github.com/urllib3/urllib3/milestone/6). 

You can read a whole lot more about what will be in the `v2.0.0` release
there. Here are some of the highlights:

- Drop support for Python 2.7 and 3.5
- 99% Functional API Compatibility with urllib3 `v1.x`
- Fully Type-Hinted APIs
- Use TLS 1.2+ by default with HTTPS
- Stop verifying deprecated `commonName` fields in Certificates
- Tracing information on the `HTTPResponse` object

There will be more updated on `v2.0.0` development after we ship the
release of urllib3 `v1.26.0`.

## HTTPS in HTTPS Tunnel Proxies

The major new feature coming in urllib3 `v1.26.0` is being able to
use HTTPS proxies to tunnel to HTTPS hosts.

Previously this wasn't possible, you would be forced to use HTTP to
connect to your proxy and then create an HTTPS tunnel to the origin
through your proxy. This means that the connection between you and
your proxy wasn't secure and only the connection to the origin was secure.

*Obviously not ideal!*

HTTPS proxies are becoming much more common and some proxies, such as ones
within a corporation, would be better implemented by authenticating via
a client certificate rather than a username and password.

Well thanks to the hard work of [Jorge](https://github.com/jalopezsilva),
who was recently made a collaborator on the urllib3 team, this is now possible!
The support will be released in `v1.26.0`, look forward to this!

References: [PR #2001](https://github.com/urllib3/urllib3/pull/2001),
[PR #1961](https://github.com/urllib3/urllib3/pull/1961), [PR #1923](https://github.com/urllib3/urllib3/pull/1923)

## Tidelift Blog Post on Supporting Multiple Release Streams

urllib3 was [featured in Tidelifts blog post](https://blog.tidelift.com/how-tidelift-helps-urllib3-maintainer-seth-larson-support-more-python-versions-and-release-streams)
about how Tidelift enables our team to continue supporting Python 2.7
while developing a new release stream which is Python 3.6+

## Revamped Documentation

The [urllib3 documentation](https://urllib3.readthedocs.io)
has received a major facelift thanks to the new Sphinx theme
[Furo](https://github.com/pradyunsg/furo) created by [Pradyun Gedam](https://github.com/pradyunsg). Browse
the new documentation and let us know what you think!

Reference: [PR #1950](https://github.com/urllib3/urllib3/pull/1950)

## Public Discord Channel

We now have a [Discord channel](https://discord.gg/CHEgCZN) that is open to the public. We recommend
joining if you have a question for the team or if you just want to say hello.

## Full Changelog for September 2020

Here's the full list of changes that have happened in September:

### Suppress Warnings from `multipart/*` Responses

This issue has long plagued users (first opened in 2016!) and we're really excited to have it finally fixed.
Essentially Python's `httplib` would complain about not being able to find the multipart boundary
within the body of the HTTP response. Normally this would be cause for concern, however this issue was being
emitted during the parsing of only HTTP headers, so there was no body to check yet! Suppressing these
warnings during this stage of parsing fixed the issue.

Thanks to community contributor [`@badcure`](https://github.com/badcure) for submitting this fix.

References: [PR #1665](https://github.com/urllib3/urllib3/pull/1665), [PR #800](https://github.com/urllib3/urllib3/issues/800)

### Suppress `BrokenPipeError` when writing a Request Body

When you make an HTTP request with a body and the other end closes
the pipe before you finish writing the body to the socket you can
sometimes get a `BrokenPipeError` at the send stage. But this doens't
mean that you can read the HTTP response! This change simply suppresses
`BrokenPipeError` during HTTP request write and begins the HTTP response
reading. If that stage also errors out we know we have a truly broken socket
but if not you're able to recover the HTTP response, woo!

This is another old issue, the original issue was opened on Requests in 2015.

Thanks to community contributor [`@robermorales`](https://github.com/robermorales) for submitting this fix.

Reference: [PR #1524](https://github.com/urllib3/urllib3/pull/1524)

### Improving CI Reliability

One of the most challenging things about writing a library about networking is dealing with reliability of your CI.
Networks are unpredictable and test suites need that predictability. [Quentin](https://github.com/pquentin) and [Hod](https://github.com/hodbn/) have been working
very hard to make our CI reliable so that when changes are made we don't have to guess whether
CI failures are actual failures or transient issues. This also makes the experience of new
contributors much more positive as they won't have to read arcane network errors and wonder if they broke
anything.

References: [PR #1957](https://github.com/urllib3/urllib3/pull/1957), [PR #1956](https://github.com/urllib3/urllib3/pull/1956), 
[PR #1967](https://github.com/urllib3/urllib3/pull/1967), [PR #1958](https://github.com/urllib3/urllib3/pull/1958), 
[PR #2008](https://github.com/urllib3/urllib3/pull/2008)

### Read the Docs 'Autobuild Documentation for Pull Requests'

This new-ish feature that Read the Docs is offering called
'[Autobuild Documentation for Pull Requests](https://docs.readthedocs.io/en/stable/guides/autobuild-docs-for-pull-requests.html)'

This means that instead of relying on our own docs CI builder we can
use Read the Docs and get a live preview of what the documentation would
look like once we merge. Super useful!

Reference: [PR #1954](https://github.com/urllib3/urllib3/pull/1954)

### Migrate CI to GitHub Actions

We're migrating all of our existing Travis and AppVeyor CI over to GitHub Actions.
We already had macOS builders there are we enjoyed their speed and concurrency.

In September we moved all Windows builders off AppVeyor and some of our miscellaneous
builders like linting over to GitHub Actions as well. The end goal of this effort is
to have all CI on GitHub Actions.

References: [PR #1965](https://github.com/urllib3/urllib3/pull/1965), [PR #1960](https://github.com/urllib3/urllib3/pull/1960)
