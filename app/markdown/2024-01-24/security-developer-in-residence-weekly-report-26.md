# Releases on the Python Package Index are never “done”

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## PEP 740 and open-ended PyPI releases

PEP 740 is a proposal to add support for digital attestations to PyPI artifacts,
for example publish provenance attestations, which can be verified and used by tooling.

**William Woodruff** has been working on [PEP 740](https://github.com/python/peps/pull/3618) which is in draft on GitHub, William addressed my feedback this week.
During this work the [open-endedness of PyPI releases came up during our discussion](https://github.com/python/peps/pull/3618#discussion_r1453694294), specifically how it
is a common gotcha for folks designing tools and policy for multiple software ecosystems difficult.

> What does it mean for PyPI releases to be *open-ended?* It means that you can always upload new files
> to an existing release on PyPI even if the release has been created for years. This is because a PyPI
> “release” is only a thin layer aggregating a bunch of files on PyPI that happen to share the same version.

This discussion between us was opened up as a [wider discussion on discuss.python.org](https://discuss.python.org/t/restricting-open-ended-releases-on-pypi/43566) about this property. Summarizing this discussion:

* New Python releases mean new wheels need to be built for non-ABI3 compatible projects. IMO this is the most compelling reason to keep this property.
* Draft releases seem semi-related, being able to put artifacts into a "queue" before making them public.
* Ordering of which wheel gets evaluated as an installation candidate isn't defined well.
  Up to installers, tends to be more specific -> less specific.
* PyPI doesn't allow single files to be yanked even though PEP 592 allows
  for yanking at the file level instead of only the release level.
* The "attack" vector is fairly small, this property would mostly only provide additional secrecy for attackers by blending into existing releases.

## CPython Software Bill-of-Materials update

[CPython 3.13.0a3 was released](https://www.get-python.org/downloads/release/python-3130a3/), this is the very first CPython release that contains any SBOM metadata
at all, and thus we can create an initial draft SBOM document.

Much of the work on CPython's SBOMs was done to fix issues related to pip's vendored dependencies
and issues found by downstream distributors of CPython builds like Red Hat. The issues were as follows:

* [Don't require internet access to run the SBOM script](https://github.com/python/cpython/issues/114240).
  We use internet access to automatically generate metadata for pip, but if the internet isn't available
  we should continue using the metadata that we already have (assuming the file hasn't changed) and then rely
  on CI which should always have internet access (the script fails in CI) to verify the values.
* [If pip wheel is removed, don't raise an unskippable error](https://github.com/python/cpython/issues/114244).
  Redistributors will typically remove the wheel in favor of their own distribution of pip for ensurepip.
* [Enumerate pip's vendored dependencies in the SBOM](https://github.com/python/cpython/issues/114250).
  This requires parsing the `vendor.txt` script inside of pip's vendor directory.

All of these issues are mostly related and touch the same place in the codebase, so resulted in a [medium-sized pull
request](https://github.com/python/cpython/pull/114450) to fix all the issues together.

On the release side, I've [addressed feedback](https://github.com/python/release-tools/pull/82) from the first round of reviews for generating SBOMs for source code artifacts
and uploading them during the release. Once those SBOMs start being generated they'll [automatically begin being added](https://github.com/python/release-tools/pull/84) to python.org/downloads.

## Other items

* [Two new Developer-in-Residence roles have been filled at the Python Software Foundation](https://pyfound.blogspot.com/2024/01/announcing-deputy-developer-in.html).
  Welcome, Petr Viktorin as the Deputy Developer-in-Residence and Serhiy Storchaka as the Supporting Developer-in-Residence.
  We've already gotten a chance to collaborate and I look forward to even more.
* scikit-learn is [considering build reproducibility](https://github.com/scikit-learn/scikit-learn/issues/28151).
* Wrote my piece for the Python Software Foundation Annual Impact report.
* Submitted to the OpenSSF SOSS Community Day Call for Proposals (see you in Washington!)
* [Reviewed a fix by](https://github.com/python/cpython/pull/114179) **Erlend Aasland** for the SBOM generation script.
* I [published a blog post](https://sethmlarson.dev/removing-maintainers-from-open-source-projects) which provides guidance
  on how to remove a maintainer from an open source project to reduce the attack surface of an open source project.

That's all for this week! 👋 If you're interested in more you can read [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-25).
