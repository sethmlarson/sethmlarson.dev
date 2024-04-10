# Security Developer-in-Residence Weekly Report #32

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

Returned from my vacation this week and have gotten things back in order heading into
April. This report covers what's happened since the first week of March.

## CISA Open Source Summit

I attended the [Open Source Security summit](https://www.cisa.gov/news-events/news/cisa-announces-new-efforts-help-secure-open-source-ecosystem) hosted by CISA in early March.
The event was attended by many other open source ecosystems. The summit focused on
strengthening the security of open source infrastructure like package repositories.

The [Principles for Package Repository Security](https://repos.openssf.org/principles-for-package-repository-security)
document was a top point of discussion. This document provides a roadmap for other package repositories to
prioritize security work into discrete projects and all examples have prior art that can be learned
from other package repositories (such as Trusted Publishers for PyPI).

The summit also discussed the available resources and challenges between the public sector and
open source software and a tabletop exercise between package repositories, the public sector, and open source maintainers and users.

## Google Summer of Code 2024

[Google Summer of Code](https://summerofcode.withgoogle.com/) is open now
and there are [many available ideas for Python](https://python-gsoc.org/ideas.html)
including one that I submitted with **Dustin Ingram** on adopting
the [OpenSSF Hardened Compiler Options for C/C++](https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++) for CPython. The task description is:

> * There's already a [list of compiler option candidates](https://best.openssf.org/Compiler-Hardening-Guides/Compiler-Options-Hardening-Guide-for-C-and-C++) to adopt, use that as the initial list.
> * Do some performance evaluation for how each compiler option affects performance (using CPython's existing performance suite).
>   Report back on the performance impact of enabling each option.
> * Implement a small custom tool (proposed in the [existing issue](https://github.com/python/cpython/issues/112301)) that allows ignoring existing violations of compiler options while preventing future violations.
> * At this point we've achieved a lot of value, all future CPython contributions will have these compiler options applied.
> * After the tooling is integrated, fill the rest of the project time by remediating known issues.

Applications are **due by April 2nd, 2024** so if you're interested in working on this idea act quickly
to prepare your application. I've already received some interest and have been providing some guidance to
potential applicants.

## Speaking and Tabletop Exercise participant at SOSS Community Day NA

I'm [speaking](https://sched.co/1aNLj) at the [OpenSSF SOSS Community Day](https://events.linuxfoundation.org/soss-community-day-north-america/program/schedule/) in Seattle on April 15th. I'm also a participant in
the [Tabletop Exercise](https://sched.co/1aN8l) that caps off SOSS Community Day.

## Other items

* [CPython source and documentation builds moved to GitHub Actions](https://github.com/python/release-tools/pull/71) thanks to Developer-in-Residence **Łukasz Langa**
  for reviewing and dry-running the GitHub Action during the most recent CPython release.
* Security advisories for [CVE-2023-6597](https://mail.python.org/archives/list/security-announce@python.org/thread/Q5C6ATFC67K53XFV4KE45325S7NS62LD/) and [CVE-2024-0450](https://mail.python.org/archives/list/security-announce@python.org/thread/XELNUX2L3IOHBTFU7RQHCY6OUVEWZ2FG/) were published while I was away by Ee Durbin.
* [CPython 3.13.0a5](https://www.python.org/downloads/release/python-3130a5/) is released containing some [changes to default certificate verification behavior](https://github.com/python/cpython/pull/112389). Please test the latest CPython alpha releases for 3.13!
* Reviewed **Brett Cannon**'s [lock file pre-PEP](https://discuss.python.org/t/lock-files-again-but-this-time-w-sdists/46593) to ensure package URLs and SBOMs can be constructed reliably
  and for future changes to checksum algorithms.
* I'll be blogging for the [Python Language Summit](https://us.pycon.org/2024/events/language-summit/) at PyCon US 2024.

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-33) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-31).
