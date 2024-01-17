# Defending against the PyTorch supply chain attack PoC

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

Last week there which a [publication](https://johnstawinski.com/2024/01/11/playing-with-fire-how-we-executed-a-critical-supply-chain-attack-on-pytorch/)
into a proof-of-concept supply chain attack against PyTorch using persistence in self-hosted GitHub runners, capturing tokens from triggerable jobs as a
third-party contributor, and modifying workflows. This report was [#1 on Hacker News](https://news.ycombinator.com/item?id=38969533) for most of Sunday. In the
comments of this publication there was a lot of discussion and folks questioning "how do you defend from this type of attack"?

Luckily for open source users, there are already techniques that can be used today to mitigate the downstream impact of a compromised dependency:

* Using a lock file with pinned hashes like pip with `--require-hashes`, `poetry.lock`, or `Pipfile.lock`.
* Reviewing diffs between currently pinned and new candidate releases. The diff must be of the **[installed
  artifacts](https://pypi.org/project/torch/#files)**, not using git tags or source repository information.
  Tools like [diffoscope](https://pypi.org/project/diffoscope/) are useful for diffing wheel files which are actually zip files in disguise.
* For larger organizations the cost of manual review can be amortized by mirroring PyPI and
  only updating dependencies that have been manually reviewed.
* Binary or compiled dependencies can be compiled from source to ensure malicious code isn't hidden from human inspection.

These are tried-and-true methods to protect yourself and ensure dependencies aren't compromised regardless of what happens upstream.
Obviously the suggestions above take time and effort to implement. Generally there's desire from me and others to make the above steps easier for consumers
like exposing build provenance for easier reviewing of source code or by improving the overall safety of PyPI content using malware scanning and reporting.

Part of my plans for 2024 is to create guidance for Python open source consumers and maintainers for
how to safely use packaging tools both from the perspective of supply chain integrity but also for vulnerabilities, builds, etc.
So stay tuned for that!

## CPython Software Bill-of-Materials update

Last week I published a [draft for CPython's SBOM document](https://gist.github.com/sethmlarson/103891c6cac4d41b11daab89e6c84868) specifically for the source tarballs
in order to solicit feedback from consumers of SBOMs and developers of SBOM tooling. I received great feedback from **Adolfo Garcia Veytia**
and **Ritesh Noronha** including the following points:

* Strip version information from the `fileName` attribute
* The top-level CPython component had no relationships to non-file components, should have `DEPENDS_ON` relationships to all its dependent packages.
* Fix the formatting of the "Tool: " name and version. Correct format is `{name}-{version}`.
* Use the `fileName` attribute on the CPython package instead of using a separate file component for the tarball containing CPython source code.
* Include an email address for all "Person" identities.
* Guidance on alternatives to the `documentNamespace` field.

After applying this feedback we now have an SBOM which meets [NTIA's Minimum Elements of an SBOM](https://www.ntia.doc.gov/files/ntia/publications/sbom_minimum_elements_report.pdf)
and scores 9.6 out of 10 for the [SBOM Quality Score](https://sbombenchmark.dev/).

Next I'm working on the infrastructure for actually generating and making the SBOM available for consumers:

* [Created a PR](https://github.com/python/release-tools/pull/82) for generating the draft SBOM. Next need to hook into the actual release process and opportunistically generate an SBOM.
* [Applied changes](https://github.com/python/release-tools/pull/82/commits/9b1fdfa9605a9e71ff32333cb2e71ad3304ceed6) according to feedback from SBOM reviewers.
* [Created a PR](https://github.com/python/pythondotorg/pull/2359) for enabling hosting an SBOM artifact on [https://python.org/downloads](https://python.org/downloads)

## Other items

* Reviewed [PEP 740 proposal](https://github.com/python/peps/pull/3618) for arbitrary attestation mechanism for PyPI artifacts.
* Triaged multiple reports to the Python Security Response Team.

That's all for this week! 👋 If you're interested in more you can read [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-24).
