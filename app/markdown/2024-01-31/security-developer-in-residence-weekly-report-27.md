# Security Developer-in-Residence Weekly Report #27

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

Shorter update this week in terms of words on the page, but lots of work
is contained within them!

## CPython SBOMs

I'm getting closer to having the end-to-end flow complete for Software Bills-of-Materials documents
for specifically CPython source code artifacts. Once that's complete I'll begin branching out
to support other artifacts like the Windows and macOS binary installers.

* Landed the [final pull request](https://github.com/python/cpython/pull/114450)
  for complete traversal of the pip wheel automatically when generating the SBOM document.
* The above PR also fixed multiple issues reported by **Karolina Surma** of Fedora
  like making regenerating the SBOM documents while offline not raise an error
  and handling situations where pip is "debundled" from the ensurepip module.
* [Backported the SBOM tooling to 3.12 branch](https://github.com/python/cpython/pull/114730)
  to be included in future 3.12 releases.
  Determined that backporting beyond 3.12 would take substantially more effort
  due to setuptools' inclusion in ensurepip and its complicated vendoring situation.
* Working on the user documentation for python.org/downloads page for CPython's SBOMs
* Getting legal help regarding licensing ID questions for the CPython SBOM

## Reviewing new draft CVE Numbering Authority Rules

**Reviewed the new draft CVE Numbering Authority rules.** This document is only available for CNAs right now.
I focused on representing small open source vendor CNAs (like the Python Software Foundation, curl, etc).
Would like to add prevention of "junk" CVEs into the rules, so they can be dealt with more directly.
Will need to update the [OpenSSF CVE Numbering Authority for OSS guide](https://github.com/ossf/wg-vulnerability-disclosures/blob/main/docs/guides/becoming-a-cna-as-an-open-source-org-or-project.md)
once new rules are published.

## Other items

* Missed the announcement for last week so including here: [Diffoscope v254 includes support for the XAR/PKG
  file format](https://diffoscope.org/news/diffoscope-254-released/) which I contributed to help with reproducibility of macOS CPython artifacts.
* Published [A-O monthly report for January 2024](https://github.com/ossf/alpha-omega/blob/main/alpha/engagements/2024/psf/update-2024-01.md).
* PEP 740: Index support for digitial attestations [discussion](https://discuss.python.org/t/pep-740-index-support-for-digital-attestations/44498)
  and [draft](https://peps.python.org/pep-0740/) was created by **William Woodruff**.
* Triaged multiple reports to the Python Security Response Team.

That's all for this week! 👋 If you're interested in more you can read [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-26).
