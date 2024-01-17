# Security Developer-in-Residence Weekly Report #24

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

Welcome to the first weekly report of 2024!

## Software Bill-of-Materials for CPython

Continuing from 2023 there will be a focus on Software Bill-of-Materials (SBOMs) for CPython
and incremental improvements to the CPython release process as more is automated.

I [made a suggestion to release managers](https://discuss.python.org/t/create-and-distribute-software-bill-of-materials-sbom-for-python-artifacts/39293/17) to backport SBOM tooling in the CPython repository
to all supported release streams in an effort to treat SBOMs more like an additional artifact instead of a
new feature of CPython. This would mean SBOMs would be available for previous CPython releases and we won't
have to wait until the 3.13.0 stable release in October to make them available for consumption.

## Trusted Publisher provenance on PyPI

Last week William Woodruff [published a pre-PEP discussion](https://discuss.python.org/t/pre-pep-exposing-trusted-publisher-provenance-on-pypi/42337) for using Trusted Publisher configurations
to bootstrap publish provenance on PyPI. I was involved in reviewing the initial draft, so I'm excited to see
the discussion! Some things to highlight that came from the discussion:

* Don't want to start this work concretely until there are more than one Trusted Publisher provider for PyPI.
  Currently, PyPI only supports GitHub.
* Getting the user interface right on PyPI to not overemphasize what publish provenance implies
  for consumers or make projects without publish provenance feel "insecure". Having "verified"
  URLs to the source repository seems like a good place to start?
* Publish provenance isn't build provenance, build provenance requires more than what Trusted Publishers is able to provide on its own.
* [Donald's comment](https://discuss.python.org/t/pre-pep-exposing-trusted-publisher-provenance-on-pypi/42337/38) on making things better for a common platform (in this case, GitHub and future Trusted Publisher providers) without
  requiring everyone to switch to that platform.
* Not everyone uses automated deployment workflows, we'll need to design a build integrity mechanism
  that supports these use-cases. I [commented my thoughts on such a system](https://discuss.python.org/t/pre-pep-exposing-trusted-publisher-provenance-on-pypi/42337/21) using third-party observations on build reproducibility from a claimed source.
* There are many reasons why folks aren't using Trusted Publishers, even when on GitHub.

Looking forward to helping however I can with this project once it is proposed as a PEP!

## Build reproducibility of macOS artifacts

Previously I worked on build reproducibility for CPython source artifacts which are both tarballs.
I want to provide build reproducibility to all artifacts that CPython provides
including the Windows and macOS binary installers.

Turns out that macOS's Package files (`.pkg`) use the eXtensible ARchive (XAR) format internally.
This format isn't supported by [diffoscope](https://diffoscope.org/), the tool I've been using for verifying.
I put together a quick bit of functionality in order to diff `.pkg` files which appears
to work nicely and have [submitted it upstream](https://salsa.debian.org/reproducible-builds/diffoscope/-/merge_requests/134) to the diffoscope project.

Next steps for reproducibility would be to apply diffoscope inside an automated macOS build process
to shake out any sources of non-determinism and address them.

## Software identifiers

Listened to the [Open Source Security Podcast](https://open.spotify.com/show/4YeKi2aGfxuhGj2QqazzVV?si=bc0f22fa69964c87) (which I recommend) where Josh Bressers and Kurt Seifried
discussed [software identifiers](https://open.spotify.com/episode/44ThWbJKMDGOco5spPm9VL?si=9e39d93b895c48b7) as they relate to vulnerabilities and Software Bill-of-Materials
and more specifically [CISA's RFI on software identifiers](https://www.cisa.gov/resources-tools/resources/software-identification-ecosystem-option-analysis) and [OpenSSF's response](https://openssf.org/blog/2023/12/11/openssf-responds-to-the-cisa-rfc-on-software-identification-ecosystem-analysis/).

CPE system could work if it was open for others to collaborate. Currently, mostly a closed system.
I've also found casually that CPEs tend to work much better for returning CVE matches today
compared to Package URLs even though OSV works with Package URLs natively. I suspect tooling will
improve in this area as time goes on.

[Package URLs](https://github.com/package-url/purl-spec) (PURLs) are distributed, namespaced, and intrinsic (easily discoverable).
Downside is that two completely different Package URLs may reference the same software but different methods of retrieval (which may be relevant!)
Sometimes ties software identity to its source code platform which can change (see CPython moving to GitHub).

Package URLs being namespaced also means that [they can carve out namespaces that are governed by different standards](https://fosstodon.org/@sethmlarson/111721513751102992),
for example the `pkg:pypi/...` namespace is governed by PEPs for names and versions where `pkg:npm/` is governed
by different standards. I think this ability will be critical for software identifiers to model different
ecosystems, ecosystems won't converge to one set of standards so identifying software needs to be able to
model them properly.

## Other items

* Attended the [OpenSSF Alpha-Omega monthly public meeting](https://docs.google.com/document/d/1tZjruUQvFSIXnSxK5pj-uin0G1wwHnJ4TWg0IpTWd50/edit#heading=h.s2lfxqy0p8vt). Had some great discussions about "Secure by Design".
* Spent a good chunk of time planning high-level what the first new major projects
  for 2024 would be, there will be more to share as we approach the start of those projects.
* Triaging multiple reports to the Python Security Response Team.

That's all for this year! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-25) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-23).