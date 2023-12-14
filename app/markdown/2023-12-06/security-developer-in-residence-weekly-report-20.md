# Review of the Security Developer-in-Residence role in 2023

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

This report is short on new work due to me being "mostly away" since Thanksgiving. This week I've been working on November and end-of-year reports for this roles' sponsor the Alpha-Omega project and the PSF.

### November 2023 update

I've [published the Alpha-Omega update for November 2023](https://github.com/ossf/alpha-omega/blob/main/alpha/engagements/2023/psf/update-2023-11.md)
which highlights the [Python Software Foundation's response to the US Government RFI](https://github.com/ossf/alpha-omega/blob/main/alpha/engagements/2023/psf/update-2023-11.md#highlight-python-software-foundation-response-to-us-government-rfi) on open source security,
the [publication of the guide](https://openssf.org/blog/2023/11/27/openssf-introduces-guide-to-becoming-a-cve-numbering-authority-as-an-open-source-project/) for becoming a CVE Numbering Authority as an open source project to the OpenSSF blog,
and the [proposal for adding Software Bill of Materials](https://discuss.python.org/t/create-and-distribute-software-bill-of-materials-sbom-for-python-artifacts/39293/10) to the CPython release process.

### 2023 end-of-year report

Creating these end-of-year reports had me looking back through what I've done,
and I'm proud of what I've been able to accomplish since June. The list of highlights includes:

* Joined the Python Security Response Team as a coordinator for disclosures, remediations, and releases.
* Authorized the Python Software Foundation as a CVE Numbering Authority covering Python and pip.
* Authored and published the guide to becoming a CVE Numbering Authority as an open source organization.
* Created a database for vulnerabilities in the CPython runtime using the Open Source Vulnerability (OSV) format.
  Populated this database with historical and new vulnerabilities. This database has been integrated into the global
  OSV database for use by software vulnerability scanners.
* Documented the CPython release process and identified sources of supply chain risk in the current process.
* Audited current Sigstore signatures for CPython releases and worked with core developers to fix discrepancies. Updated tools
  so that signatures would always be consistent.
* Back-filled the new Sigstore bundle format to old releases so tooling can make use of offline verification and only one format of verification materials.
* Build reproducibility for CPython's source artifacts.
* Proposed implementation for moving CPython's source and documentation releases to GitHub Actions as a hardened and SLSA-compliant build platform.
* Proposed implementation for Software Bill-of-Materials generation and publication as a part of the CPython release process.
* Helped author the Python Software Foundations first response to a government Request For Information about investing in open source security.
* Spoke at OpenSSF Day Europe 2023 with Cheuk Ting-Ho, appeared on Talk Python, received news coverage from The Register and The New Stack.
* Authored [20 weekly report posts on my blog](https://sethmlarson.dev/blog), 6 monthly reports, and 2 end-of-year reports.

None of the above would have been possible without the trust and support of the Python community.
The year isn't quite over yet, but I'm already excited for what we can all accomplish next year together. Thanks a million, everyone! 💜

That's all for this week! 👋 If you're interested in more you can read [next week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-21) or [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-19).
