# Library dependency version specifiers aren't for fixing vulnerabilities

Let's say you are the maintainer of a Python library that depends on another 
Python library like “[urllib3](https://pypi.org/project/urllib3)”.
Because you want to make sure users receive a compatible version
of urllib3 you add a [version specifier](https://packaging.python.org/en/latest/specifications/version-specifiers/)
that restricts the version to the current “major” version so users
know that older versions aren't compatible. This is
what your `pyproject.toml` might look like:

```toml
[project]
name = "example-library"
dependencies = [
  "urllib3>=2",  
]
```

<!-- more -->

Now let's say that urllib3 publishes a vulnerability
that affects “version 2.6.2 and earlier” and is fixed in version 2.6.3.
Later you receive this pull request from a concerned user that changes
the minimum version from `2` to `2.6.3` to “disallow installing a vulnerable version or urllib3”:

```diff
  [project]
  name = "example-library"
  dependencies = [
-  "urllib3>=2",  
+  "urllib3>=2.6.3",
  ]
```

**You probably should not accept this pull request.** Version ranges
for libraries are meant to be used for *compatibility*, not for security
vulnerabilities. This is a key difference between *libraries* and *applications*:
libraries should allow the greatest version ranges within the realms of
*compatibility* and applications should only “allow” a single version of each
dependency by using a lock file (`requirements.txt` with `--hash`, `pylock.toml`, `uv.lock`).

It's not the responsibility of library maintainers to *force*
their users are using secure versions of dependencies that aren't directly
managed by the library (such as by bundling). **That is the responsibility of users**.

You can imagine scenarios where a security vulnerability might affect
compatibility, such as if a feature is removed or changed in a backwards-incompatible
way. In this case then a version range update may be warranted.

Another scenario is where your library version specifiers disallows upgrading to
a version with a security fix, such as when a security fix is only available
for urllib3 2.x but your library is only compatible with urllib3 1.x. In this
case you as a library maintainer may want to consider this request to allow
your users to upgrade to secure versions more easily. However, even in this
scenario it is *not a vulnerability in your library* if your version specifiers
don't allow an easy upgrade from a vulnerable version to a fixed version
of a dependency.
