# Security Developer-in-Residence Weekly Report #22

<blockquote>
  <center>This critical role would not be possible without funding from the OpenSSF <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

This week was all about working on Software Bill-of-Materials tooling and documentation for CPython.
I [published a new resource](https://devguide.python.org/developer-workflow/sbom/) to the [CPython core developer guide](https://devguide.python.org/).
This documents Software Bill-of-Materials and all of the tooling and processes for adding, updating, and removing
dependencies. I'll continue to add to this document as more is developed in this project.

During an upgrade to CPython's `ensurepip` module, the bundled `pip` wheel was [upgraded to version 23.3.2](https://github.com/python/cpython/pull/113249)
however during the upgrade there was some confusion about what to do with an SBOM CI failure due to the
Developer Guide documentation not yet being live. This resulted in the SBOM becoming out-of-date.

I [fixed the SBOM](https://github.com/python/cpython/pull/113262) ahead of the 3.13.0a3 release and
[automated the pip SBOM metadata discovery](https://github.com/python/cpython/pull/113295) since pip is a part of a packaging ecosystem which isn't the case for most
of CPython dependencies in the source tree.

Next steps for the SBOM infrastructure for CPython include adding [Windows dependencies into the SBOMs](https://github.com/python/cpython/issues/112844) released for the Windows installers
and doing discovery work on macOS installers.

## Other items

* The OpenSSF [published its annual report for 2023](https://openssf.org/blog/2023/12/18/2023-year-in-review-openssf-publishes-annual-report/)
  which contained a bunch of highlights from the Python ecosystem and Alpha-Omega's engagement with the Python Software Foundation (*including all the work I've done this year!*)
  Give it a read if you're interested in a one-stop-shop for big things happening in the open source ecosystem.
* Switched to using [`make regen-configure`](https://github.com/python/release-tools/pull/79) for the CPython release process
  now that the Makefile target is available for [all currently supported CPython release streams](https://github.com/python/cpython/issues/112160).
* [Reviewed](https://github.com/pypi/warehouse/issues/14961#issuecomment-1856913333) the secret scanning payload [proposed by GitGuardian](https://github.com/pypi/warehouse/issues/14961).
  This payload would allow PyPI to alert users when secrets are uploaded with donated secret scanning expertise from GitGuardian.

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-23) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-21).