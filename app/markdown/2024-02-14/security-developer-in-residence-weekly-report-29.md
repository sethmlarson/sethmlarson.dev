# Challenges while building SBOM infrastructure for CPython

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

In case you missed it, recently I announced support for [Software Bill-of-Materials
for the CPython project](https://pyfound.blogspot.com/2024/02/software-bill-of-materials-now-available-for-cpython.html)
on the Python Software Foundation blog.

Part of the project is intended to document the challenges that the project faced to
start publishing first-party SBOM documents alongside release artifacts. Yesterday I gave
a presentation to the [OpenSSF SBOM Everywhere SIG](https://github.com/ossf/sbom-everywhere),
the [slides](https://docs.google.com/presentation/d/15BbzIpQUIQv56vpwFNAEl4y8PAALVFnR5S_YpKxxkck)
are available in Google Drive, but I'll be summarizing the discussion here:

## List of challenges so far for CPython SBOMs

**Building for sustainability**. There are no guarantees that my role will be around forever.
There's a non-zero chance that CPython core developers will need to maintain SBOM infrastructure at some point in the future. This means it needs to have buy-in,
be as low-effort to maintain as possible, fit into existing workflows, and be well documented.

This challenge sparked a bunch of conversation in the group about getting buy-in from technical leadership of open source projects.
My thoughts being the following:

* There isn't a one-size-fits-all approach for projects. Every proposal needs to be fit for that project.
* Having engagements be driven by community members.
  There's already a relationship of trust that the work will be done right by the community and that the individual won't leave as soon as the project is complete.
  I applaud Alpha-Omega's approach here of supporting communities to do security work for the ecosystems they care about.
* Being public and honest about all aspects of the work, especially the not-so-fun truths (like additional maintenance, complexity, etc).
  I created a [public discussion of the SBOM project for CPython](https://discuss.python.org/t/create-and-distribute-software-bill-of-materials-sbom-for-python-artifacts/39293)
  and enumerate its impact specifically on developers updating dependencies and how having accurate SBOMs may increase the amount of reports from users we get to patch dependencies.
* Show value for the maintainers of the project. SBOM itself may not have tons of value specifically for maintainers, but as an avenue
  for scanners to discover VEX statements and thus reduce the amount of reports we receive to pointlessly patch dependencies is a valuable capability.

**Recursive dependency bundling**: CPython bundles pip in the `ensurepip` module. pip bundles 18
dependencies. There are even more projects bundled in older CPython versions which was the primary reason
I stopped backporting beyond 3.12. This requires a customized tool to handle the job. pip and its dependencies
being a part of the Python package ecosystem helps a lot, this means we can automatically do lookups for metadata on PyPI,
drastically reducing maintainer effort to keep the SBOM updated.

**Software IDs and metadata of C projects**: Many of CPython dependencies are C projects (libexpat, mpdecimal, HACL*, etc)
and those projects aren't a part of a packaging ecosystem, they're tarballs you download and install by pasting into a directory.
This means there aren't any standards for what a version number or name should be. The unfortunate part of this
is it means the SBOM has to be updated manually when these projects are updated by core developers.

CPEs also don't exist universally for the projects, CPEs being the primary software vulnerability identifier used for C projects.
OSV and PURL don't work for projects outside of packaging ecosystems.

## Other items

* Created a presentation and presented to the OpenSSF SBOM Everywhere group on CPython SBOM project.
* More SBOM stuff:
  * [Moved pip SBOM discovery](https://github.com/python/cpython/pull/115360) from the CPython tooling to the CPython release tools.
  * [Make SBOM formatting reproducible](https://github.com/python/release-tools/pull/95)
  * [Add test suite to CPython release tooling](https://github.com/python/release-tools/pull/93)
  * [Fixed minor issue to remove whitespace from SBOM tool version](https://github.com/python/release-tools/pull/92)
* Updated and backported [libexpat to 2.6.0](https://github.com/python/cpython/issues/115399)
* [Linux announced as a CVE Numbering Authority](http://www.kroah.com/log/blog/2024/02/13/linux-is-a-cna/) and referenced my work on the [OpenSSF guide to becoming a CNA](https://openssf.org/blog/2023/11/27/openssf-introduces-guide-to-becoming-a-cve-numbering-authority-as-an-open-source-project/).
* Attended the Python Software Foundation February board meeting
* Triaged reports to the Python Security Response Team

That's all for this week! 👋 If you're interested in more you can read [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-28).
