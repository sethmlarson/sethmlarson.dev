# PEP 770 Software Bill-of-Materials (SBOM) data from PyPI, Fedora, and Red Hat

This year I authored [PEP 770](https://peps.python.org/pep-0770/) which proposed a new standardized location
for Software Bill-of-Materials (SBOM) data within Python wheel archives.
SBOM data can now be stored in `(package)-(version).dist-info/sboms/`.
You can see the [canonical specification](https://packaging.python.org/en/latest/specifications/binary-distribution-format/#the-dist-info-sboms-directory) on `packaging.python.org`.

<!-- more -->

While writing this document we also reserved all `.dist-info/` subdirectory names
within a registry for future use in other standards. Reviewers agreed that this
method of defining file-based metadata (such as SBOMs, but also licenses)
is a great mechanism as it doesn't require creating a new metadata field
and version.

Creating a new metadata field in particular requires large amounts
of “head-of-line blocking” to rollout completely to an ecosystem of independent
packaging installers, builders, publishers, and the Python Package Index; 
the proposed method side-steps all of this by making inclusion in the directory
the mechanism instead.

So now that this PEP is published, what has happened since? A few things:

## Unmasking the Phantom Dependency problem

In case you missed it, I published a [white paper on this project](https://alpha-omega.dev/blog/unmasking-phantom-dependencies-with-software-bill-of-materials-as-ecosystem-neutral-metadata-white-paper-by-seth-larson-python-software-foundation/) with Alpha-Omega.
If you want to learn more about the whole project from end-to-end, this is a good place to start!

## Auditwheel and cibuildwheel

Back in 2022 there was a [public issue](https://github.com/pypa/auditwheel/issues/398) opened for Auditwheel asking
to generate an SBOM during the `auditwheel repair` command. Now in
[Auditwheel v6.5.0](https://github.com/pypa/auditwheel/releases/tag/6.5.0) which was released in early November, Auditwheel
will [now automatically generate SBOM data](https://github.com/pypa/auditwheel/pull/577) and include the SBOM in
the PEP 770 specified location (`.dist-info/sboms/auditwheel.cdx.json`).

The manylinux images [adopted the new auditwheel version](https://github.com/pypa/manylinux/commit/e72d93b28c29e08d5a1fb5425b33f08b150dc591) soon after publication.
These images are used by common Python wheel building platforms like [cibuildwheel](https://github.com/pypa/cibuildwheel) and [multibuild](https://github.com/multi-build/multibuild).
Because this functionality was enabled by default we can look at Python wheel data
and determine how many packages already supply PEP 770 SBOM data:

When querying the pypi-code.org dataset including all code within Python wheels
I was able to find 332 projects on PyPI that are shipping SBOM data in their wheels:

```sql
SELECT repository, project_name, path
FROM './dataset-*.parquet'
WHERE archive_path LIKE '%.dist-info/sboms/%'
AND skip_reason == '' LIMIT 10;
```

Of these projects, these are the top-10 most downloaded with SBOM data so far:

| Project                                                                 | Downloads/Month |
|-------------------------------------------------------------------------|-----------------|
| [greenlet](https://pypi.org/project/greenlet)                           | 205M            |
| [numba](https://pypi.org/project/numba)                                 | 33M             |
| [pymssql](https://pypi.org/project/pymssql)                             | 27M             |
| [ddtrace](https://pypi.org/project/ddtrace)                             | 17M             |
| [psycopg-binary](https://pypi.org/project/psycopg-binary)               | 14M             |
| [faiss-cpu](https://pypi.org/project/faiss-cpu)                         | 13M             |
| [logbook](https://pypi.org/project/logbook)                             | 6M              |
| [simsimd](https://pypi.org/project/simsimd)                             | 2M              |
| [clang-format](https://pypi.org/project/clang-format)                   | 2M              |
| [nodejs-wheel-binaries](https://pypi.org/project/nodejs-wheel-binaries) | 1M              |

There are far more projects which will likely require SBOM data on their bundled dependencies,
so I'll continue watching the numbers grow over time!

## RedHat and Fedora adopt PEP 770

Back in July of this year, Miro Hrončok [asked if there was a mechanism for specifying the
"origin" of a package](https://discuss.python.org/t/encoding-origin-in-wheel-and-dist-info-metadata-for-downstream-security-backports/97436), as many tools incorrectly assume that any package that's
installed to an environment originated from the Python Package Index (and
therefore would use a Package URLs like `pkg:pypi/`). Their use-case was
Python packages provided by the system package manager, such as `rpm` on Fedora and RedHat Linux.
Vulnerability scanners were incorrectly assuming packages like `pip` were vulnerable
as older versions of `pip` are packaged, but with vulnerability patches backported
and applied to older versions.

*SBOMs to the rescue!* Miro [adopted PEP 770 for Fedora and RedHat Linux](https://developers.redhat.com/articles/2025/12/15/how-reduce-false-positives-security-scans)
to reduce false-positives in vulnerability scans by defining the actual correct
Package URL for the installed package in the SBOM:

```json5
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.6",
  "components": [
    {
      "type": "library",
      "name": "python3.11-setuptools",
      "version": "65.5.1-3.el9",
      // This Package URL is for the RedHat distribution,
      // of setuptools, not the PyPI distribution.
      "purl": "pkg:rpm/redhat/python3.11-setuptools@65.5.1-3.el9?arch=src"
    }
  ]
}
```

If scanners adopt this approach and other Linux distros do as well, there
will be far fewer false-positives from scanning Python environments
using those Linux distros. A win for everyone!
Miro is [asking for feedback](https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/) on this approach by consuming tools.
