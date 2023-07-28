# Security Developer-in-Residence – Weekly Report #2

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.<br>
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

Second weekly report for the Security Developer-in-Residence role, if you missed the first one you can give it a [read it here](https://sethmlarson.dev/security-developer-in-residence-weekly-report-1).

## Bundled libraries in Python distributions

Python is known for its ability to be a "glue" language thanks to its C API and
access to libraries written in C, C++, Go, Fortran, and Rust. This feature is likely
one of the reasons for Python's massive popularity and makes Python libraries
like numpy, pandas, and pydantic super-fast thanks to some of their code being
written in a more CPU-performant language.

This super-power of Python has implications for supply chain security, let's go through why together:

The Python Package Index (PyPI) only hosts Python distributions, usually one of two types: source distributions and wheel distributions.

Python distributions which want to leverage compiled libraries either need to have users install those compiled libraries themselves or
ship a pre-compiled library with the distribution. Having to install compiled libraries with your
system package manager and then compiling each package from source is **frustrating to users**.

A common workflow for binary wheels is to run [`cibuildwheel`](https://github.com/pypa/cibuildwheel) alongside [`auditwheel repair`](https://github.com/pypa/auditwheel) (or [`delocate`](https://github.com/matthew-brett/delocate) for macOS and [`delvewheel`](https://github.com/adang1345/delvewheel) for Windows) to build wheels
in their many different OSes and architectures (manylinux, musllinux, macOS, Windows, etc) and
then using `auditwheel repair` so that the libraries that need to get bundled are bundled into the wheel automatically.

This combination means that building binary wheels for all the different OSes and architectures has never been easier!
But that also means there's a lot of bundled libraries out there.

The kicker is that **those bundled libraries can have vulnerabilities too!**
An example of this happening is when `pdftopng` [contained vulnerable versions](https://github.com/vinayak-mehta/pdftopng/issues/12) of `libpng`
(among other libraries) bundled in their wheel. There's also this [related issue](https://github.com/pypa/advisory-database/issues/103) for the PyPI Advisory database
about vulnerabilities in shared libraries.

These bundled libraries don't show up in your `requirements.txt` or `pip freeze` so it's tougher for
you and your audit tooling to know what libraries and versions are in use.

**Software Bill of Materials (SBOM) to the rescue!** With an SBOM, you can programmatically know what
is included in the distribution you've downloaded, including the non-Python components. If auditing tools
has access to these SBOMs and a source for vulnerabilities for the relevant components you can now
check that distributions aren't vulnerable, including their sub-components!

I wanted to figure out which bundled libraries are common amongst the top 500 Python packages that provide binary wheels, so [I created a project](https://github.com/sethmlarson/vendored-libraries-in-python-dists)
to gather the dataset along with some providing some pre-computed data so you can play around yourself and not need to download 75GB to your machine. Here are the results
after normalizing the names of the `.so` files:

| Library             | Unique Packages |
|---------------------|-----------------|
| `libgcc_s.so`       | 138             |
| `libstdc++.so`      | 110             |
| `libcrypto.so`      | 56              |
| `libcom_err.so`     | 39              |
| `libkrb5.so`        | 39              |
| `libkrb5support.so` | 39              |
| `libk5crypto.so`    | 39              |
| `libgssapi_krb5.so` | 39              |
| `libgomp.so`        | 38              |
| `libkeyutils.so`    | 34              |
| `libssl.so`         | 34              |
| `libcurl.so`        | 30              |
| `liblzma.so`        | 27              |
| `libpcre.so`        | 26              |
| `libselinux.so`     | 26              |
| `libgfortran.so`    | 26              |
| `libldap.so`        | 24              |
| `liblber.so`        | 24              |
| `libpng16.so`       | 23              |
| `libhdf5.so`        | 23              |
| `libsasl2.so`       | 21              |
| `msvcp140.dll`      | 19              |
| `libquadmath.so`    | 17              |
| `libnetcdf.so`      | 17              |
| `libbz2.so`         | 16              |

There's more than only binary libraries too, packages like `pip` bundle [tons of Python libraries](https://github.com/pypa/pip/tree/main/src/pip/_vendor) with their
source code and `jupyter-notebook` bundles [TypeScript and JavaScript](https://github.com/jupyter/notebook/tree/main/packages). Adding these bundled projects to an SBOM would help tooling to
find vulnerabilities for those bundled projects, too.

But wait, it can't be that simple, can it? Let's talk about **downstream re-packagers**.

Using the same dataset, let's pick on a library that sorts near the top alphabetically: `aerospike`. This package
bundles `libssl.so.1.0.2k` with it's `manylinux2014_x86_64` wheels. For anyone who's not aware,
`libssl.so` is one of the shared libraries for OpenSSL so seeing the version `1.0.2k` might
be raising some alarm bells.

But fear not, if we examine [how that wheel was built](https://github.com/aerospike/aerospike-client-python/blob/898a7a5b42d826c9aeabbe4f52305843ed92e64c/.github/workflows/build-wheels.yml#L142)
we can see that they're using `cibuildwheel` which in turn uses the official [`manylinux2014_x86_64` container image](https://quay.io/repository/pypa/manylinux2014_x86_64)
which is based on CentOS 7. CentOS 7 uses [OpenSSL 1.0.2k](https://centos.pkgs.org/7/centos-x86_64/openssl-1.0.2k-19.el7.x86_64.rpm.html) as a base but
applies security patches to known vulnerabilities for libraries but crucially *maintains the existing library version number and API backwards-compatibility*,
so in theory the bundled library is free of vulnerabilities thanks to CentOS package maintainers. 

Why is this a problem for auditing wheels for vulnerabilities? Because if a machine sees "OpenSSL 1.0.2k" it won't
know whether that's a genuine OpenSSL 1.0.2k build (vulnerable) or one that's patched by a repackager.

[Package URLs](https://github.com/package-url/) provide a way to identify the differences between the source project and a repackaged build of the same project.
For example, here are two different package URLs for OpenSSL:

- `pkg:generic/openssl@1.0.2k`
- `pkg:rpm/centos/openssl-devel@1.0.2k-19.el7`

Using the package URL we can help disambiguate and provide more context to vulnerability detection tools.

That's not the end of the problems, there's still many tough ones to figure out:

- How to reduce the additional burden on maintainers if more vulnerabilities are showing up in their packages?
- How to reduce false-positives for vulnerability scanners?
- How to get vulnerability data from downstream re-packagers in a programmatically consumable format?
- How can wheel repair tools figure out which project is being vendored automatically?
- How to get package maintainers to manually mark which projects are being vendored when needed?

I'm just starting to work with others interested in adding SBOMs to Python distributions, so there will be more updates on this in the future.

## Trusted Publisher adoption metrics

Now that my PR for gathering metrics on trusted publishers (called OIDC publishers internally) has been deployed
I can start to share some numbers with you all. 

The metrics that have been added distinguish between projects which have only configured
Trusted Publishers and ones that have successfully published a release with a Trusted Publisher.
There's also separate metrics for projects which have been marked "critical" due to downloads.

|                   | Configured Trusted Publishers | Published with Trusted Publishers |
|-------------------|-------------------------------|-----------------------------------|
| All Projects      | ~1,570                        | ~1,020                            |
| Critical Projects | 131                           | 85                                |

From the PyPI 2FA Dashboard, there are at the time of writing 4641 critical projects
and 465,860 total projects on PyPI meaning around ~2.8% of critical projects have configured
Trusted Publishers. Trusted Publishers were [introduced](https://blog.pypi.org/posts/2023-04-20-introducing-trusted-publishers/)
back in late April, so around 78 days meaning an average of ~20 projects and ~2 new critical projects and per day
adopt Trusted Publishers.

I'll be publishing some dashboards to track these metrics over time publicly soon.

## GitHub Push Protection for PyPI API Tokens

In the [list of supported secret types](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/secret-scanning-patterns#supported-secrets),
the PyPI API tokens don't currently support "[Push Protection](https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/protecting-pushes-with-secret-scanning)".
This means that GitHub won't outright reject a commit that contains a PyPI API token, instead the commit will always go through and then the secret will be revoked shortly after.
It's a better user experience to not have to generate a new API token and zero exposure time to get rejected versus pushed so I wanted to see how difficult it'd be to get Push Protection enabled for PyPI tokens.

I emailed GitHub's Secret Scanning team and after a few hours I received this response:

> We will need to analyze the performance of your tokens to ensure they meet the threshold
> for Push Protection (they will need to have <1% false positives). We will reach out once we have done the review and let you know next steps.

I'm hopeful that given [PyPI API tokens regex pattern](https://warehouse.pypa.io/development/token-scanning.html#how-to-recognize-a-pypi-secret) of `pypi-AgEIcHlwaS5vcmc[A-Za-z0-9-_]{70,}`
that the false positive rate would be low (thanks Macaroon prefixes!) but we shall see.

If this topic interests you, [there's an open ticket](https://github.com/pypi/warehouse/issues/9280) for implementing secret scanning report
APIs for GitLab.

## Other items

- Attended my first public [Alpha-Omega monthly meeting](https://docs.google.com/document/d/1tZjruUQvFSIXnSxK5pj-uin0G1wwHnJ4TWg0IpTWd50/edit#heading=h.cvgfbwx6bfat).
- Reported my first security vulnerability to a project and requested a CVE.
- Triaged multiple reports to the Python Security Response team
- Received feedback on my high-level proposals for the Python Security Response team which was positive!
  Will be putting more detail into the proposals and eventually submit to the Steering Council for approval.

That's all for this week! 👋 If you're interested in more you can read [next week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-3) or [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-1).
