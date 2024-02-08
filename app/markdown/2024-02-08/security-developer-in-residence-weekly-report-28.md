# CPython 3.12.2 is SBOM-ified!

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## SBOM for CPython source artifacts

CPython 3.12.2 is the first release that has SBOMs for source artifacts 🥳
There's an [announcement for the PSF blog](https://pyfound.blogspot.com/2024/02/software-bill-of-materials-now-available-for-cpython.html), so *go read that first!*

Work items for SBOMs that got worked on this week:

* SBOM tooling was [backported to the 3.12 branch](https://github.com/python/cpython/pull/114730)
* [Merged SBOM building to the CPython release process](https://github.com/python/release-tools/pull/82)
* Both of the above items together mean 3.12.2 could be the first release with SBOMs for source artifacts.
* Published [user documentation](https://www.python.org/download/sbom/) and a getting started guide for CPython SBOMs to [python.org/download/sbom](https://www.python.org/download/sbom/)
* Received more feedback from CPython downstream distributors and pip maintainers and have
  [opened an issue](https://github.com/python/release-tools/issues/91) for further automating pip's SBOM data discovery.
* Chilled with release managers on Discord during 3.12.2 release in case anything went wrong.
* Wrote the blog post announcement.

After consulting with legal help regarding the licensing questions that came up during
SBOM development I opted to [change](https://github.com/python/cpython/pull/115038) all `licenseConcluded` fields for dependencies in the SBOM to `NOASSERTION`
as the primary use-case for CPython's SBOMs was for supply chain and vulnerability management.

Next steps for this project include investigating SBOMs for Windows installers and continuing to learn
about Vulnerability Exchange (VEX) and how it can be applied to CPython SBOMs.

## Other items

* My work on the libwebp vulnerability was [referenced at a FOSDEM talk](https://fosdem.org/2024/schedule/event/fosdem-2024-3230-getting-lulled-into-a-false-sense-of-security-by-sbom-and-vex/) by Henrik Plate of Endor Labs.
* Got [access to CDN logs](https://github.com/python/psf-salt/pull/348) for python.org to track downloads of SBOMs and Sigstore artifacts.
* Got up to speed with the [effort](https://github.com/python/cpython/issues/91826) to switch mail protocols (SMTP, IMAP, and POP3) and FTP in the standard library to verify certificates by default.
* Had both of my PyCon US 2024 talk proposals declined, but will be attending regardless (look forward to a security-focused open space!)
* Attended the Alpha-Omega monthly community meeting.
* Triaged reports to the Python Security Response Team.

That's all for this week! 👋 If you're interested in more you can read [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-27).
