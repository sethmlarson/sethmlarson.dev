# OSS Security RFI, Guide to become a CNA, and PEP 639

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

The past week has been almost exclusively writing for me! Here's a rundown on what I've been writing about:

## Request for Information (RFI) on Open Source Software Security

As many folks in the Open Source security space are aware of, the deadline for the [US Government RFI submissions](https://www.federalregister.gov/documents/2023/08/10/2023-17239/request-for-information-on-open-source-software-security-areas-of-long-term-focus-and-prioritization) (November 9th, 2023) is fast-approaching!
I've been working with my colleagues at the Python Software Foundation to draft a response to the RFI over the past months now. The past few
weeks have had a lot of time spent on collaborating and refining our response to the point where I am quite proud of it now.

If this is your first time hearing of the RFI, the [Linux Foundation](https://www.linuxfoundation.org/blog/what-you-need-to-know-about-the-us-federal-governments-rfi-on-open-source-software-security) and [Tidelift](https://blog.tidelift.com/new-rfi-shows-the-us-gov-effort-to-invest-in-open-source-is-picking-up-steam) have both covered the RFI, what it is and why it's an exciting development for open source.

The Python Software Foundation's response to the RFI is about capturing what we believe is important regarding the US governments approach to
securing open source software. Whatever gets done by the US government is likely to have huge implications for everyone maintaining and consuming
open source software, so it's critical that policy and decisions are made with sustainability in mind.

I'm honored to be a part of this and to represent so many Pythonistas in my work both for this RFI and every day as Security Developer-in-Residence. 💜

## Becoming a CVE Numbering Authority as an Open Source project

Throughout the process of joining the CVE Numbering Authority program for the Python Software Foundation
I noted down all the steps and requirements to become a CNA. I [transformed these notes into a digestible document](https://github.com/ossf/wg-vulnerability-disclosures/pull/139)
that's specifically written for Open Source projects and organizations. This document has had extensive review from
both the OpenSSF Vulnerability Disclosures Working Group and multiple CVE Working Groups.

This guide has recently been [published under the OpenSSF Vulnerability Disclosures WG GitHub repository](https://github.com/ossf/wg-vulnerability-disclosures/blob/main/docs/guides/becoming-a-cna-as-an-open-source-org-or-project.md). I'm
now in the process of drafting an announcement blog post for the [OpenSSF blog](https://openssf.org/blog).

## PEP 639 - Licensing clarity in packaging metadata

I've [raised my hand](https://discuss.python.org/t/pep-639-round-2-improving-license-clarity-with-better-package-metadata/12622/95) to help [PEP 639](https://peps.python.org/pep-0639/)
make its way to acceptance as this PEP was one that I noted as being important for Software Bill-of-Materials being adoptable
for the Python packaging ecosystem. I wanted to also thank **Karolina Surma** who works on Python packaging at Red Hat for joining as a coauthor of PEP 639
as well and is already making use of the PEP. Thanks so much!

The gist of this PEP is to move package tooling and maintainers to adopt [SPDX License IDs and expressions](https://spdx.org/licenses/)
in order to more accurately represent the licenses of Python packages. Previous standards would use an open-ended string `License` field along with [`License :: *` trove classifiers](https://pypi.org/classifiers/).
This approach isn't able to capture all licensing situations (such as `'MIT OR GPL-2.0-only'`) and especially struggles with license revisions.

Due to the inability to capture these more complication situations, it often meant that tooling consuming Python packages would need to look at `LICENSE`, `NOTICE`, or `COPYING`
files and do their own text detection in order to have an accurate view of the licensing situation. Choosing a license is one of the more important decisions
before releasing software into the wild, so ensuring that that choice is unambiguous is very important!

## Other Items

* [Discussed "affectedness" based on modules and functions for the PyPA Advisory database](https://github.com/pypa/advisory-database/issues/149). Having this information would allow
  vulnerability scanning tools like [pip-audit](https://github.com/pypa/pip-audit) to only associate a vulnerability with a project if the affected module or function
  is used by the project. In theory this information will reduce the amount of false-positives when a vulnerability only affects
  a single feature rather than the entire project.
* [OSV announced broad support for C/C++ projects and vulnerabilities](https://osv.dev/blog/posts/introducing-broad-c-c++-support/). Will need to test this out against the Python ecosystem
  to provide feedback on their detection tooling and how it applies to Python.
* Published the [engagement report for October 2023](https://github.com/ossf/alpha-omega/pull/265) to Alpha-Omega.

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-18) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-16).
