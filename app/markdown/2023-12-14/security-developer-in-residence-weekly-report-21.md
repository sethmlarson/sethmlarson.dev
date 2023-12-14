# Python listed as memory-safe language in latest CISA recommendations

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

Memory-safety is clearly a top priority for software security, making up [70% of vulnerabilities](https://www.cisa.gov/news-events/news/urgent-need-memory-safety-software-products) in popular software like Chrome and Windows.
The US Government RFI on open source security had a focus area on memory-safety to which the [Python Software Foundation provided a response](https://www.regulations.gov/comment/ONCD-2023-0002-0107),
for which I was the primary author on this topic.

The US government organization CISA (Cybersecurity and Infrastructure Security Agency) [issued new recommendations this week](https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3608324/us-and-international-partners-issue-recommendations-to-secure-software-products/)
regarding securing software products through memory safety. You can read the [full information sheet here](https://media.defense.gov/2023/Dec/06/2003352724/-1/-1/0/THE-CASE-FOR-MEMORY-SAFE-ROADMAPS-TLP-CLEAR.PDF).

From the recommendation I have the following quote, emphasis mine:

> “Recommended memory safe programming languages mentioned in the CSI include C#, Go, Java, **Python**, Rust, and Swift.”

**This is awesome news for Python users!** 🥳

More support will be needed to migrate Python's extensive packaging ecosystem from memory-unsafe languages
to memory-safe languages. I've made recommendations on how best the US government can aid in that effort in the PSF's RFI response.
My recommendations included:

* Provide resources (financial or time) to aid in discovery, improving tooling (like [PyO3](https://github.com/PyO3)), and the actual migration of projects.
* Prioritizing projects for migration based on security-sensitivity and criticality.
* Learning from the experiences of projects which have migrated from C to Rust like [cryptography](https://www.youtube.com/watch?v=z_Eiy2W0APU).
* Hardening for projects which can't migrate to memory-safe languages for a variety of reasons.

You can see the current usage of memory-unsafe languages in Python projects [in a previous article](https://sethmlarson.dev/security-developer-in-residence-weekly-report-18).

## Other items

* PyPI Safety and Security Engineer Mike Fielder published an announcement [about 2FA enforcement of PyPI starting January 1st, 2024](https://discuss.python.org/t/announcement-2fa-requirement-for-pypi-2024-01-01/40906). **All users of PyPI will be required to use 2FA.**
* [Initial pull request](https://github.com/python/cpython/pull/112303) adding Software Bill-of-Materials for CPython dependencies has been merged.
  I've created a [list of sub-issues](https://discuss.python.org/t/create-and-distribute-software-bill-of-materials-sbom-for-python-artifacts/39293/11?u=sethmlarson) on different projects for where the work will be progressing next.
* Łukasz [will dry-run](https://github.com/python/release-tools/pull/71#issuecomment-1843852272) the automation for the CPython release process for CPython 3.13.0a3 (according to PEP 719 will be in about a week).
* Created the [CVE record](https://www.cve.org/CVERecord?id=CVE-2023-6507) and [advisory](https://mail.python.org/archives/list/security-announce@python.org/thread/AUL7QFHBLILGISS7U63B47AYSSGJJQZD/) for CVE-2023-6507. This vulnerability affects only CPython 3.12.0.
* Submitted my year-end report to OpenSSF Alpha-Omega. Subscribe to the [Alpha-Omega blog](https://alpha-omega.dev/resources/news/) to be notified when the year-end report is published.
* Submitted to the PyCon US CFP.

That's all for this week! 👋 If you're interested in more you can read [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-20).
