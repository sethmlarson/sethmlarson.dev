# Security Developer-in-Residence – Weekly Report #4

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## Sigstore signed Python releases

Ever since the 3.11.0 release of Python, all Python release tarballs are signed using [Sigstore](https://www.sigstore.dev).
You can [read this page](https://www.python.org/download/sigstore/) for more information about
Sigstore signatures and how to verify the signatures using the [Python Sigstore client](https://github.com/sigstore/sigstore-python).

The gist is each Release Manager for a given Python release (ie 3.7, 3.8, etc) has an identity (email address with `@python.org`)
defined in the Sigstore information page. This is the identity used to verify who signed the release. Sigstore uses OpenID Connect
which means we also need to designate an identity provider (IdP) to verify signatures.

```shell
# Currently documented example of how to verify Python signatures
$ python -m sigstore verify identity \
  --certificate Python-3.11.0.tgz.crt \
  --signature Python-3.11.0.tgz.sig \
  --cert-identity pablogsal@python.org \
  --cert-oidc-issuer https://accounts.google.com \
  Python-3.11.0.tgz
```

It was reported [that the instructions](https://github.com/sigstore/sigstore-python/issues/600) for verifying signatures weren't
consistent with the reality of how the artifacts had been signed. I put together a few simple scripts which downloaded
and attempted to verify every Python release artifact against its signatures and [published the results](https://github.com/sethmlarson/verify-python-release-signatures/).
These scripts found a few issues:

- **Ned Deily** and **Łukasz Langa** used GitHub's IdP and **Pablo Galindo Salgado** and **Thomas Wouters** used Google's IdP.
- Łukasz's identity for all signatures was `lukasz@langa.pl`, instead of the documented `lukasz@python.org`.
- Python 3.11.4 was signed with Pablo's correct identity, but with GitHub's IdP instead of Google's IdP.
- Python 3.7.14 was signed by Pablo, but Ned was the release manager for 3.7.
- Python 3.8.14 and 3.9.14 had signatures generated but weren't accessible from `python.org/download` due to permission issues.
- Python 3.10.1 and 3.10.7 onwards were signed, but 3.10.0 and 3.10.2-3.10.6 weren't signed. This is fine though as only 3.10.7
  and onwards are documented as being signed.

With these findings the release managers took the following steps to make the signature verifications consistent for consumers:

- Ned resigned the 3.7.14 release with his own identity.
- Pablo resigned 3.11.4 with the Google IdP.
- Łukasz fixed the permissions for 3.8.14 and 3.9.14 making the signatures available.
- The CDN cache had to be purged for the updates to be available.

You can see the change in state in [this commit](https://github.com/sethmlarson/verify-python-release-signatures/commit/c16b7822e5e8bdeaf4fae3ef4ad687235a05444c) to the above dataset.
From here all that's needed is fixing Łukasz's identity on signatures which may prove difficult as using GitHub
as an IdP only allows the primary email address as an identity rather than all configured email addresses.
**William Woodruff** [opened an issue](https://github.com/sigstore/fulcio/issues/1283) after discussion of this any other GitHub IdP use-cases on Sigstore's Slack channel.
I've also [opened a PR](https://github.com/python/release-tools/pull/51) in Python's release-tool to keep Sigstore
signing consistent with the documentation for future Python releases.

All of this highlights how even though Sigstore is much more ergonomic signing experience than GPG, there are still little things that can create an inconsistent experience for consumers.
I'll be updating the Sigstore documentation once we've completed this task. Thanks to all the release managers for working on this issue!

## PEP 710 (Package Provenance Info)

I stumbled on the [discuss thread](https://discuss.python.org/t/pep-710-recording-the-provenance-of-installed-packages/25428) for [PEP 710](https://peps.python.org/pep-0710/) written by [**Fridolín Pokorný**](https://fridex.github.io/) which proposes a new metadata file `provenance_url.json`
to be placed in an installed Python distribution's `.dist-info` directory if the package was
installed via an index with resolution (ie `python -m pip install urllib3`). You can read the PEP for
the exact structure of the document which includes the original download URL and a list of available hashes
for the distribution like SHA-256, etc.

<div>
<div class="row">
<div class="col-6">

<p>This PEP would allow tools to inspect an already installed Python environment and be able to recreate
exact download URLs for installed distributions along with hashes in order to ensure integrity of the distributions. This makes
the installed environment more reproducible if the download URLs are still intact.</p>

<p>Having this information available also enables tools to create a Software Bill of Materials (SBOM) from a pre-installed environment.
I created an <a href="https://github.com/sethmlarson/pip-sbom">experimental tool</a> that uses the reference implementation of PEP 710 for pip to create SPDX and CycloneDX SBOM documents.</p>

<p>From sharing this thread on Twitter I was also pointed to <a href="https://pip.pypa.io/en/stable/reference/installation-report/">pip installation reports</a>, a feature I wasn't aware of that's new in pip v22.2. (thanks <strong><a href="https://twitter.com/SBidoul">Stéphane Bidoul</a></strong>!)
This feature lets you hook into the results of pip's dependency resolution for a given CLI input to pip (ie <code>pip install -r requirements.txt</code>). I'll be experimenting with this feature in the future.</p>

</div>
<div class="col-6">
<center>
<blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/Python?src=hash&amp;ref_src=twsrc%5Etfw">#Python</a> environments to <a href="https://twitter.com/hashtag/SBOM?src=hash&amp;ref_src=twsrc%5Etfw">#SBOM</a> using draft PEP 710 👀 <a href="https://t.co/htt1QEwJLe">pic.twitter.com/htt1QEwJLe</a></p>&mdash; Seth Michael Larson (@sethmlarson) <a href="https://twitter.com/sethmlarson/status/1681672012568096771?ref_src=twsrc%5Etfw">July 19, 2023</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 
</center>
</div>
</div>
</div>

After reviewing the PEP draft I made a [few suggestions](https://discuss.python.org/t/pep-710-recording-the-provenance-of-installed-packages/25428/6)
including upgrading the "SHOULD" to a "MUST" for installing a resolved distribution from the installers' cache and clarifying if there was any
case where either `provenance_url.json` or [PEP 610](https://peps.python.org/pep-0610/)'s `direct_url.json` wouldn't be installed for a given distribution. If `provenance_url.json` can
be made required for the inverse case of PEP 610 it would mean that *all* installed distributions would
have a metadata file describing the distribution's origin.

I also suggested adding another key `index_url` which would contain the URL of the index that the distribution
was resolved from. This is useful for auditing which indices were used for which packages to arrive at the final download URL.

I am hopeful that the amount of positive interest in this PEP will result in its acceptance. If you're interested
in this PEP please participate in the [discussion thread](https://discuss.python.org/t/pep-710-recording-the-provenance-of-installed-packages/25428).

## Other projects

- aiohttp [published a vulnerability advisory](https://github.com/aio-libs/aiohttp/security/advisories/GHSA-45c4-8wx5-qw6w) that I submitted as a result of
  [inspecting non-Python artifacts shipped with wheels](https://sethmlarson.dev/security-developer-in-residence-weekly-report-2#bundled-libraries-in-python-distributions).
  In this particular case aiohttp bundled [llhttp](https://github.com/nodejs/llhttp) v6.0.6 which was vulnerable to [CVE-2023-30589](https://github.com/advisories/GHSA-cggh-pq45-6h9x) and the vulnerable behavior was accessible from
  aiohttp APIs. Upgrade to aiohttp v3.8.5 for the remediation. The PyPA advisory database was [having trouble automatically importing the advisory](https://github.com/pypa/advisory-database/issues/133),
  so I [manually submitted](https://github.com/pypa/advisory-database/pull/134) the advisory in a PR.
- [PEP 639 draft](https://peps.python.org/pep-0639/) aims to improve how packages define their licenses using SPDX License Expressions.
  These expressions would be very useful for clarity of metadata and SBOMs.
- Received [some recommendations](https://github.com/ossf/osv-schema/issues/94#issuecomment-1637409389) on how to represent Python using the [Open Source Vulnerability format](https://ossf.github.io/osv-schema/)
  (OSV). OSV is primarily focused on package ecosystems, but software which is made available outside a packaging ecosystem (like Python, curl, cmake, etc)
  there isn't a perfect way to unambiguously specific the "identity" of the project (keeping in mind that the VCS isn't your project identity).
- [Submitted an update](https://github.com/pypa/packaging.python.org/pull/1277) to the PyPA binary distribution format specification to warn about interoperability issues with build numbers.

That's all for this week! 👋 If you're interested in more you can read [next week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-3) or [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-5).
