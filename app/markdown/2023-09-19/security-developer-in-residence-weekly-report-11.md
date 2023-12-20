# CPython vulnerabilities are now published to the Open Source Vulnerability Database

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

[Security advisories for Python](https://osv.dev/vulnerability/PSF-2023-8) are now published to the [OSV Vulnerability Database](https://osv.dev)! 🎉🥳 This means you can use
[the OSV API](https://google.github.io/osv.dev/api/) to access machine-parseable information about security vulnerabilities affecting Python.

The vulnerability information is ingested from the Python Software Foundation's [Advisory Database on GitHub](https://github.com/psf/advisory-database)
which was primarily sourced from **Victor Stinner's** [python-security project](https://python-security.readthedocs.io/). This database
is open to contributions, so if you see anything missing or incorrect we welcome pull requests. This is a huge step forward in automaticity and discoverability
of vulnerability information for Python itself which previously would have required custom tooling.

Thanks to **Oliver Chang** and **Andrew Pollock** for [setting up the ingestion into the database and helping resolve issues](https://github.com/google/osv.dev/issues/1552).

To get complete information about a single vulnerability by its ID you can query the API directly:

```json
$ curl "https://api.osv.dev/v1/vulns/PSF-2023-8" | jq

{
  "id": "PSF-2023-8",
  "summary": "Bypass TLS handshake on closed sockets",
  "details": "Instances of `ssl.SSLSocket` are vulnerable to a bypass ...",
  "aliases": [
    "CVE-2023-40217"
  ],
  "modified": "2023-09-18T01:59:58.377178Z",
  "published": "2023-08-24T00:00:00Z",
  "references": [
    ...
  ],
  "affected": [
    {
      "ranges": [
        {
          "type": "GIT",
          "repo": "https://github.com/python/cpython",
          "events": [
            {
              "introduced": "0"
            },
            {
              "fixed": "b4bcc06a9cfe13d96d5270809d963f8ba278f89b"
            },
...
```

If you have a git commit hash for CPython you can query the database to see all vulnerabilities that affect that git commit.
I'm hopeful that the database can be improved to add support for git tags in order to support querying by Python version.

```shell
$ curl -s -d '{"commit": "7f777ed95a19224294949e1b4ce56bbffcb1fe9f"}' \
  https://api.osv.dev/v1/query | jq ".vulns[].id" | sort

"PSF-2007-1"
"PSF-2007-2"
"PSF-2008-1"
"PSF-2008-10"
"PSF-2008-2"
...
```

Currently the OSV database only allows you to query by *package version* which isn't available for projects like "upstream" Python since they
are distributed outside of a packaging ecosystem (ie via [https://python.org/downloads](https://python.org/downloads)).
Re-distributions of Python in packaging ecosystems like Debian have their own set of advisories which are also available on OSV.
You can look at [DLA-3477-1](https://osv.dev/vulnerability/DLA-3477-1) for an example of what such an advisory looks like for a redistribution of Python.

If you're interested in OSV you can check out **Andrew Pollock's** excellent [talk](https://events.linuxfoundation.org/openssf-day-europe/program/schedule/)
and [slides](https://static.sched.com/hosted_files/openssfdayeu2023/fa/OSV%20and%20the%20Life%20of%20an%20Open%20Source%20Vulnerability.pdf) about OSV at OpenSSF Day Europe 2023.

## OpenSSF Day Europe 2023

Woke up early in the morning to catch the livestream of OpenSSF Day Europe 2023. The [slides for my presentation](https://static.sched.com/hosted_files/openssfdayeu2023/a3/Final%20-%20OpenSSF%20Day%20Europe%202023.pdf)
have been uploaded to the [event page](https://events.linuxfoundation.org/openssf-day-europe/program/schedule/)
and I expect the recordings will be made available on the [OpenSSF YouTube Channel](https://www.youtube.com/@OpenSSF/videos) at a later date.
**Massive thank-you to my co-presenter [Cheuk-Ting Ho](https://cheuk.dev/)** for presenting live and in-person
about why the investments into Python security are important and what individual users can do to do their part.

I also got to listen to [William Woodruff's talk](https://events.linuxfoundation.org/openssf-day-europe/program/schedule/) on [Trusted Publishing on PyPI](https://docs.pypi.org/trusted-publishers/)
and things to be aware of for other ecosystems looking to implement a similar scheme.

## GitHub Security Advisories for the PSRT

Moving forward with more improvements to the Python Security Response Team (PSRT) process, I began to
create a simple GitHub app that allows configuring a default GitHub team to be added to
every new draft GitHub Security Advisory (GHSA) that's submitted to a GitHub repository.

I've made a feature request for this functionality to be native to GHSA, [please upvote this
request](https://github.com/orgs/community/discussions/63041) if it seems useful to other projects.

The reason this GitHub App is needed is that by default, GitHub Security Advisories only populate
*admins* of the GitHub repository as collaborators. The PSRT is made up of many individuals, a team
that is much larger than what we'd want for GitHub administrators, and so being able to add a separate
team as collaborators adds less risk.

Unfortunately I have been unable to get a [`repository_advisory:reported` event](https://docs.github.com/en/webhooks/webhook-events-and-payloads?actionType=reported#repository_advisory)
to be sent to the GitHub app, despite many attempts to configure
the permissions and settings. The APIs are so new and the amount of configurations I tried was so exhaustive that
I [filed a potential bug about this issue](https://github.com/orgs/community/discussions/67518).

## Other items

* Reviewed the [Inbound Malware Report post](https://blog.pypi.org/posts/2023-09-18-inbound-malware-reporting/) on PyPI's blog.
* Sigstore v2 and bundles work for `python/release-tools`
  * [python/release-tools#55](https://github.com/python/release-tools/issues/55)
  * [sigstore/sigstore-python#771](https://github.com/sigstore/sigstore-python/issues/771)
  * [python/pythondotorg#2285](https://github.com/python/pythondotorg/issues/2285)

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-12) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-10).
