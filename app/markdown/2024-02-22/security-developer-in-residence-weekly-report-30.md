# Windows SBOM work and Alpha-Omega 2023 annual report

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## Starting on SBOMs for Python Windows artifacts

Windows artifacts for CPython get built [using Azure Pipelines](https://github.com/python/release-tools/tree/master/windows-release)
so the generation of the final SBOM for Windows artifacts should also be added to these workflows.

Part of the workflows is to [download source code](https://github.com/python/cpython-source-deps) for dependencies like OpenSSL, libffi, and more.
These dependencies and their versions are tracked in a [file named `get_externals.bat`](https://github.com/python/cpython/blob/main/PCbuild/get_externals.bat) in a unintentionally parseable format
that the CPython SBOM tooling can [extract and generate an SBOM file for](https://github.com/python/cpython/pull/115789). This works in a similar way
to the "checked-in" source dependencies where any changes require the partial SBOM to be regenerated
and acknowledged by core developers during PR review.

The plan is to find this SBOM during the Windows release build and then depending on
which libraries have been pulled locally by `get_externals.bat` an SBOM will be generated
for the Windows artifact.

After chatting with **Steve Dower** it seems that the Windows build happens once
and then is repackaged into all the different distribution methods (python.org, Windows store, Nuget, etc)
so we'll only need to generate the Windows-specific SBOM once and then reuse it for each distribution method.

I also [removed `regen-sbom` makefile target from `regen-all`](https://github.com/python/cpython/pull/115790) to avoid breaking downstream distributors.

## Alpha-Omega published 2023 Annual Report

Alpha-Omega [published its 2023 annual report](https://openssf.org/blog/alpha-omega/2024/02/16/alpha-omega-2023-annual-report/) this week
and there's a ton of goodness inside, including lots of mentions of the Python Software Foundation and my own work.
I contributed content to this report last year, so I'm excited to see it published.

One quote regarding my current role:

> Alpha-Omega has helped fund security champion roles at the **Python
Software Foundation**, the Eclipse Foundation, and the Rust Foundation. In all
cases, we are seeing significant impact as these individuals are incubating a
security culture in their respective communities.

Both Deb Nicholson, the executive director of the PSF and I were quoted in the report,
take a look if you're interested in what Alpha-Omega has next in 2024.

## Other items

* Working on grant renewal with Alpha-Omega for the Python Software Foundation.
* [CPython 3.13.0a4 was released](https://www.python.org/downloads/release/python-3130a4/) which also included SBOM documents.
* Draft and submit talk for Alpha-Omega at PyCon US 2024.
* Reviewed the [OpenSSF announcement blog post for Linux becoming a CNA](https://openssf.org/blog/2024/02/14/linux-kernel-achieves-cve-numbering-authority-status/)
* [Reviewed the lock file with sdists proposal](https://discuss.python.org/t/lock-files-again-but-this-time-w-sdists/46593/17) from **Brett Cannon**

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-31) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-29).
