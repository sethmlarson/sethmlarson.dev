# Python Security Response Team handling of CVE-2023-40217

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

Welcome to the 8th weekly update for the Security Developer-in-Residence position.

## Python vulnerability disclosure end-to-end

The [advisory for CVE-2023-40217](https://mail.python.org/archives/list/security-announce@python.org/thread/PEPLII27KYHLF4AK3ZQGKYNCRERG4YXY/) was published this week which affects Python versions
before 3.11.5, 3.10.13, 3.9.18, and 3.8.18. This was my first end-to-end vulnerability disclosure for Python which
included handling of embargoed info (ie non-public), a coordinated release of fixed Python versions, and publishing of the advisory
to the [security-announce@python.org mailing list](https://mail.python.org/mailman3/lists/security-announce.python.org/)
and to the [PSF Advisory Database](https://github.com/psf/advisory-database).

Now that I've experienced the flow from end-to-end and I can start to think about where there is potential for improvement
and what items need to be on our "checklist" to reduce stress and guesswork from remediation developers,
release managers, and coordinators. This process is pretty opaque (for obvious reasons) so I also wanted to share
the experience with everyone to know what's happening in the background to keep Python users safe.

### Initial report and requesting a CVE ID

We received a report from **Aapo Oksman** on August 8th. The advisory and fixed Python versions were made available on August 24th,
so roughly 2 weeks between initial report and having the vulnerability resolved by the Python Security Response Team (PSRT)
while concurrently triaging other reports.

I assumed the role of Coordinator for this vulnerability report which meant making sure everything was completed before moving on to the next stage in the process and ensuring
the reporter and release managers were kept up-to-date on what was happening and when they'd need to take action in the future.

The PSF is not yet a CNA, so I offered to request a CVE ID from MITRE on behalf of Aapo Oksman. I asked Aapo if he'd like to be
credited for the vulnerability before sending my request to [MITRE's CVE form](https://cveform.mitre.org/).

### Determining severity, impact, and exploitability

The initial report appeared to be a 10/10 CVSS:3.1 ([CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N](https://cvss.js.org/#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N)), but due to the conditions required to cause the vulnerability and
the applicability of the vulnerable behavior to protocols used with TLS (ie HTTPS, FTP, SMTP, etc) we narrowed down the
actual vulnerable usages to be primarily servers using TLS with client certificate authentication (eg: mTLS). Most other usages don't have a practical
impact unless using a custom application-level protocol that doesn't behave like HTTPS or other protocols.

We also reduced the CVSS Confidentiality impact to NONE, because there is no chance of data leakage after the vulnerable behavior is used due to
the socket needing to be closed, so even if authentication is bypassed using the vulnerability the server won't have an open socket
to transmit the response over the wire. However, modifications/deletions of resources (ie `DELETE /resource`) that are only gated based on client certificate authentication would still
be impacted as a server response isn't necessary to be sent for operations to take place, hence the scoring of "HIGH" for Integrity on CVSS.

After this discussion within the PSRT and with the reporter we reassessed the vulnerability to be still 8.6/10 CVSS:3.1 ([CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:N](https://cvss.js.org/#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:N))
which is still severity HIGH.

At this time I started drafting an advisory with all the exploit-ability descriptions and affected versions and shared the draft with the reporter prior to publishing.

### Developing and landing patches

The patch for the vulnerability was developed and reviewed on a private GitHub repository. The PSRT doesn't currently use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories/repository-security-advisories/collaborating-in-a-temporary-private-fork-to-resolve-a-repository-security-vulnerability) in
order to work privately on a pull request together, this is a potential area of improvement if I'm able to ensure a good developer experience.

After we were happy with the patch we shared it with the reporter who confirmed that the patch fixed the vulnerability.
At this point we were ready to start working a bit more in public and get the patch landed in Python and back-ported to supported branches.

We tried creating a pull request with the patch, but [blurb](https://pypi.org/project/blurb/) (tool for managing CPython news entries) requires an existing GitHub issue ID,
so we needed to create an issue first. We created [this issue](https://github.com/python/cpython/issues/108310) which started off blank as a placeholder but then was later populated with information to not give away
more about the vulnerability before the fix was released.

After we [created and merged the first PR](https://github.com/python/cpython/pull/108315) we started to run into problems due to test stability that hadn't shown themselves when developing the initial patch and test cases due
to buildbots. Python's buildbots are designed to only accept public URLs so couldn't be used on our private GitHub repository to test the patches, we had to rely on only
the GitHub Actions test suite which hadn't shown the flakiness issue.

After a few days of debugging the issue by Łukasz, Greg, and Victor there were [two](https://github.com/python/cpython/pull/108344) [additional](https://github.com/python/cpython/pull/108370) PRs made in order to have stable buildbots and ensure that the fix hadn't subtly broken
anything else in the Python test suite. The last thing we wanted to do was to unnecessarily break people's code with our patch, likely then requiring  another round of bugfixes and releases. I included these patches in the advisory as optional in order to preserve test suite reliability.

I noted down that due to the restriction of buildbots not being able to test private patches that we'd want to be less outwardly visible that a given patch was to remediate a vulnerability due to the potential for dwell time between
landing a patch and getting a confirmation that the patch was stable enough to release.

### Releasing Python and publishing advisories

At this point the buildbots were green and we were ready to make some Python releases. I had been in contact with the release managers for 3.11 through 3.8 throughout this process
with an understanding that 3.12 would be receiving a pre-release fix on schedule and didn't need to be pulled forward in time due to pre-release Python versions not being recommended for production.

At this point the draft advisory was ready to be published to `security-announce@python.org` once all the versions were available. After getting the +1 that all Python releases were published
I sent the advisory via email and [published to the PSF advisory database](https://github.com/psf/advisory-database/pull/16). I also reached out to MITRE via the CVE form to notify them of the published advisory for CVE-2023-40217 and to make the [CVE record
public](https://nvd.nist.gov/vuln/detail/CVE-2023-40217).

Thanks **Aapo Oksman**, **Łukasz Langa**, **Gregory P. Smith**, **Thomas Wouters**, **Victor Stinner**, **Steve Dower**, and **Ned Deily** for their work on this vulnerability fix and for answering all my questions along the way.
It really takes a village to keep Python secure! 😊

## Open Source Vulnerability Database

There's a distributed [vulnerability database](https://osv.dev/) using the Open Source Vulnerability (OSV) format
that's hosted by Google which provides a human and machine-friendly frontend. This is super useful for
browsing around vulnerabilities and linking downstream fixes in Linux distributions with upstream CVE IDs.

I'd like the PSF Advisory Database which uses OSV to be a part of this database so downstream fixes can start being
linked automatically. [This issue](https://github.com/google/osv.dev/issues/1552) is open to track the ingestion from the new PSF advisory database.
A few issues got raised for our compliance with OSV, mostly to do with Python not being a "package" per-say and so can't take advantage
of the `ECOSYSTEM` version range specifier.

You can see an example of what the recent advisory for CVE-2023-40217 (in the [PSF database as PSF-2023-8](https://github.com/psf/advisory-database/blob/main/advisories/python/PSF-2023-8.json))
would look like in the OSV UI:

<div><center><img style="border-radius: 1em; max-width: 100%;" src="https://user-images.githubusercontent.com/18519037/263330616-f5207098-18e0-4f20-b829-52a954cfbea4.png"/></center></div>

### "Shadow" CVE IDs

[Imported 3 CVE IDs](https://github.com/psf/advisory-database/pull/14) into the advisory database that
were filed against Python that weren't submitted to the PSRT directly. Instead, it appears folks
reported issues to MITRE directly and a CVE ID was issued without our knowledge. All of these CVE IDs
affect Python versions older than 3.9.1 and are fixed for newer Python versions.

One of the CVE IDs (CVE-2023-38898) appears to be of very low quality and contains incorrect information, I've
filed a rejection request with MITRE to have this CVE withdrawn.

Thanks to **Samuel Enrique** for reporting these incidents to us so we could handle them appropriately.
If you find any CVE IDs that aren't a part of the PSF advisory database you can [open an issue here](https://github.com/psf/advisory-database/issues/new/choose).

## Other items

* Attended the CNA onboarding meeting on behalf of the PSF along with other PSF staff.
  * Was a great experience, the CNA program folks were friendly and answered all of our questions.
  * Part of becoming a CNA is an exercise determining the number of CVE IDs to issue and the contents of their
    corresponding CVE records with all minimum required fields and additional metadata if applicable.
  * All the prospective CNA operators and I collaborated on these example CVE records and submitted
    them to the CNA program for approval.
* [PDM](https://github.com/pdm-project/pdm) is already using truststore by default when installed via `pdm[truststore]` or `pdm[all]`.
  * I [opened an issue](https://github.com/pdm-project/pdm/issues/2195) suggesting use truststore for all installations on Python 3.10+
  * It appears PDM is [moving to adopt truststore by default](https://github.com/pdm-project/pdm/pull/2200) as I suggested 🚀
* Did some work to make truststore able to be adopted by pip like ensuring that `python -m compileall` will work from Python 3.7 even if truststore only supports Python 3.10+ due to pip vendoring its dependencies.
  * https://github.com/pypa/pip/pull/12107
  * https://github.com/sethmlarson/truststore/pull/108
* Quality updates to PSF advisory database records:
  * Imported references from CVE records and python-security ([psf/advisory-database#13](https://github.com/psf/advisory-database/pull/13) and [psf/advisory-database#18](https://github.com/psf/advisory-database/pull/18))
  * Fixed the formatting of newlines in the description of PSF-2023-9 ([psf/advisory-database#17](https://github.com/psf/advisory-database/pull/17))
  * Improvements to the CVE record import tool.

That's all for this week! 👋 If you're interested in more you can read [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-7).
