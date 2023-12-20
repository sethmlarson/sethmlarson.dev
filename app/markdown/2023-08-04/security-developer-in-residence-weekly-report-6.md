# Security Developer-in-Residence – Weekly Report #6

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## PSF Advisory Database

In preparation for becoming a CNA, the PSF now has a [public advisory database on GitHub](https://github.com/psf/advisory-database)
which hosts advisories in the [Open Source Vulnerability format](https://ossf.github.io/osv-schema/) (OSV). This database
will host historical advisories in addition to new advisories and CVEs for the PSF CNA for projects in scope like Python and pip.

I shared this newly published database with the OpenSSF Vulnerability Disclosures WG and received lots of feedback and tips
for managing an OSV advisory database. **Madison Oliver** of GitHub Security gave advice on being a CNA and
guidance for hosting first-party and third-party advisories as a CNA. Also received helpful feedback from **Oliver Chang** and **Andrew Pollock**. Thanks everyone!

Being a participant in the [distributed vulnerability database for OSV](https://osv.dev/) requires choosing an ID prefix for advisories.
I chose `PSF` as the prefix and the [prefix was accepted into the OSV schema specification](https://github.com/ossf/osv-schema/pull/190).
After the prefix was selected I configured automation in the database to [automatically assign IDs](https://github.com/psf/advisory-database/pull/10) for the `PSF` prefix.

I spent time importing existing advisories for Python from **Victor Stinner's** [manually curated list of vulnerability fixes](https://github.com/vstinner/python-security/blob/main/vulnerabilities.yaml).
Some of these fixes [don't include a CVE ID](https://github.com/psf/advisory-database/pull/11) so need to be disambiguated based on other information like a bugs.python.org issue ID.

## PSF CNA

The PSF CNA registration process has been making progress! 🚀

Towards publishing the materials to the OpenSSF Vulnerability Disclosures WG I've applied to join the
[CVE Outreach and Communications WG](https://www.cve.org/ProgramOrganization/WorkingGroups#OutreachandCommunicationsWorkingGroupOCWG)
to review the draft guidance materials. I'm also drafting a blog post for once the PSF is announced as a CNA.

I've been getting questions answered from the CNA Program Coordinator specifically around operating a CNA as an open source foundation or project. 
These answers will be completely written up in the guidance.

If you have a 1-2 hours of time and would like to experience the training regiment I've given PSF staff to prepare for the
CNA onboarding call you can [take a look at this Gist](https://gist.github.com/sethmlarson/44cf38a73b304b1a08bd34ba62355a81).

## Other items

* [Manually added](https://github.com/pypa/advisory-database/pull/138) the recent [certifi advisory](https://github.com/certifi/python-certifi/security/advisories/GHSA-xqr8-7jwr-rhp7) to the PyPA Advisory Database
* Created [back-filled Sigstore bundles](https://github.com/python/pythondotorg/issues/2300) from existing verification materials to be verified by CPython release managers.
* Ran into an integration issue with Sigstore Python client v2.0.0 release candidate
  not [being able to successfully verify old bundles](https://github.com/sigstore/sigstore-python/issues/724).
* Provided an OpenSSF Alpha-Omega [engagement update](https://github.com/ossf/alpha-omega/pull/197) for the month of July.

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-7) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-5).
