# whichprovides: an abstraction of "yum provides"

<blockquote>
  <center>
    This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>.
  </center>
</blockquote>

I'm announcing a new small project I've created as a part
of my work on Software Bill-of-Materials for Python packages.
The library is called [`whichprovides`](https://pypi.org/project/whichprovides/) and it's available
on PyPI under the same name:

```terminal
$ python -m pip install whichprovides
```

You can use the tool as a CLI, but many users will be using
this library indirectly through [tools like auditwheel](https://github.com/pypa/auditwheel/pull/577).

The primary purpose of the library is to reverse a file path
on your system back to the package ecosystem and package
that "provided" the file, similar to how `yum provides` works:

```terminal
$ python -m whichprovides /usr/bin/python3.10
/usr/bin/python3.10: pkg:deb/ubuntu/python3.10-minimal@3.10.12-1~22.04.9
```

This information allows tools to create [package URLs](https://ecma-tc54.github.io/ECMA-xxx-PURL/) (PURLs) for
the files they use for building a Python package. PURLs are useful
as a software identifier for performing vulnerability scanning.

Currently, this library supports the following package ecosystems:

* RPM (Red Hat, CentOS, Rocky Linux, AlmaLinux)
* Dpkg (Debian, Ubuntu)
* Aptitude (Ubuntu)
* Apk (Alpine)

I'm interested in adding support for other package ecosystems, too.
If you'd like to [contribute support for a new package ecosystem](https://codeberg.org/sethmlarson/whichprovides)
or just generally review the code, I'd welcome these types of contributions.
