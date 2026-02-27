# Deprecate confusing APIs like “os.path.commonprefix()”

The [`os.path.commonprefix()` function](https://docs.python.org/3/library/os.path.html#os.path.commonprefix) has been an API in the Python
standard library for at least 35 years (since February 1991)
and in that time has been confusing users and creating security
issues, even in programs explicitly trying to mitigate vulnerabilities.
This was caused directly by the API's placement in the [`os.path` module](https://docs.python.org/3/library/os.path.html)
and further perpetuated by backwards compatibility.

<!-- more -->

Here are my top-level takeaways from investigating this issue:

* Weigh surprise and potential for misuse higher than backwards compatibility.
  Deprecate, rename, and remove security-relevant functions that aren't designed to prevent accidental misuse.
* An API's “fitness for purpose” is implied to users through an API's “labeling” (such as: module, name, parameters).
  In the case of `commonprefix`, being included in `os.path`
  module implied to users that the function was meant to be used with paths.
* Documentation isn't enough. `commonprefix` surprising behavior was documented
  since 2002 and this wasn't enough to mitigate future insecure usage two decades
  later.
* Automatic static code analysis and linting tools are likely our best bets
  at cleaning up widespread footguns like this. An [issue was opened](https://github.com/astral-sh/ruff/issues/22981) with Ruff,
  a popular code formatter for Python.

I've submitted pull requests that turn the documentation
note into an [explicit security warning](https://github.com/python/cpython/pull/144401) and [deprecate the
function](https://github.com/python/cpython/pull/144436) in Python 3.15.
I am hoping that this case can be used as evidence in the future
to more rapidly deprecate and replace functions that are confusing
or easy to use insecurely on accident.

> My work as the Security Developer-in-Residence at the [Python Software Foundation](https://www.python.org/psf-landing/) is sponsored
by [Alpha-Omega](https://alpha-omega.dev/). Thanks to Alpha-Omega for supporting
security in the Python ecosystem.

## Discovering the footgun

Earlier this month I published the advisory for [CVE-2026-1703](https://www.cve.org/CVERecord?id=CVE-2026-1703), a vulnerability in pip that allows
extremely limited path traversal when unpacking a wheel archive file.
The root-cause for this vulnerability was a function [`is_within_directory()`](https://github.com/pypa/pip/blob/b78d8085d34f67867b5c5e60282ee5d219d8903f/src/pip/_internal/utils/unpacking.py#L79)
that checked whether a `target` path was within the extraction `directory`.
Previously the function was implemented like so:

```python
import os

def is_within_directory(directory: str, target: str) -> bool:
    """
    Return true if the absolute path of target is within the directory
    """
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)

    prefix = os.path.commonprefix([abs_directory, abs_target])
    return prefix == abs_directory
```

This function was [added to pip in 2019](https://github.com/pypa/pip/pull/6313).
The function intention is to check whether `directory` is the prefix
of `target`, implying that `target` is within `directory`.

However, this is not how `os.path.commonprefix()` works in practice.
`commonprefix()` compares *character-by-character* (`/`..`a`..`/`..`b`..),
not using path segments (`/a`..`/b`..). This subtle difference means
that the function is not safe to use on paths without extra mitigations, like so:

```python
def is_within_directory(directory: str, target: str) -> bool:
    ...

    # By adding a "/" terminator, the character-by-character
    # algorithm is now safe to use for directories.
    abs_directory = os.path.abspath(directory) + "/"
    abs_target = os.path.abspath(target)

    prefix = os.path.commonprefix([abs_directory, abs_target])
    return prefix == abs_directory
```

## Investigating other usages

Seeing this insecure usage in a critical library like pip signaled to
me that this confusion was not likely to be isolated. There are almost
[40K uses of `os.path.commonprefix` on GitHub](https://github.com/search?q=os.path.commonprefix+language%3APython&type=code) alone.
The git blame
on `os.path.commonprefix` in CPython stalls out at the “initial commit” moving CPython
to git, so we're going to have to start looking at source releases
to see the full history. I also investigated the socializing around
the API to document how the function has been misused and misunderstood
over the years, and in doing so built a case to deprecate and remove
the function.

### Python 0.9.1 (1991)

The earliest version of Python source code [available on the internet](https://www.python.org/download/releases/early/) that I know of is for version 0.9.1. Wikipedia
lists this version as being published in February 1991, so ~35 years ago this month.
Looking in `lib/path.py` we see the earliest implementation of `commonprefix()`
(with tabs instead of spaces):

```python
# Return the longest prefix of all list elements.
#
def commonprefix(m):
	if not m: return ''
	prefix = m[0]
	for item in m:
		for i in range(len(prefix)):
			if prefix[:i+1] <> item[:i+1]:
				prefix = prefix[:i]
				if i = 0: return ''
				break
	return prefix
```

This implementation identical to the `commonprefix` function in current use, and still within a
path-themed module. Note that `<>` is an alias for `!=`.

### Python 2.0.1 (2000)

The earliest version of Python source code that's available on
the contemporary “[Python Source Releases](https://www.python.org/downloads/source/)” page is Python 2.0.1.
In this source release in the `Lib/posixpath.py` we still see `commonprefix()`
unchanged:

```python
# Return the longest prefix of all list elements.

def commonprefix(m):
    "Given a list of pathnames, returns the longest common leading component"
    if not m: return ''
    prefix = m[0]
    for item in m:
        for i in range(len(prefix)):
            if prefix[:i+1] <> item[:i+1]:
                prefix = prefix[:i]
                if i == 0: return ''
                break
    return prefix
```

### First report of confusing behavior (2002)

Armin Rigo [emailed the `python-dev` mailing list](https://mail.python.org/pipermail/python-dev/2002-December/030947.html) in 2002
reporting their surprise at `commonprefix()` behavior, specifically
noting the module:

> “I recently discovered that `os.path.commonprefix(list-of-strings)` returns
the longest substring that is an initial segment of all the given strings,
and that this has nothing to do with the fact that the strings might be
paths.  I wonder why this has been put in `os.path` and not in the string
module in the first place.
> This location misled me for a long time into thinking that commonprefix()
> would return the longest common \*path\*”

Michael Hudson replied that they recalled a discussion which “decided that there is no
use for such a thing, but that changing [the function] might break code for people who
found a use”. Armin’s reply notes that the location of the function is the source of
the confusion: “Can't we deprecate the thing and move it elsewhere?”.
At this point it was decided to document the unexpected behavior
with this warning:

> “Note that this may return invalid paths
because it works a character at a time.”

This thread also noted that the original intent for the function may
have been to provide the behavior you get on a terminal after partially
typing a path and then hitting `TAB` to auto-complete, but there wasn't
a definitive answer as to why the function existed in `os.path`.

### “What’s the point of os.path.commonprefix()?” (2010)

Ned Batchelder, maintainer of the popular [coverage.py project](https://github.com/coveragepy/coveragepy/), [published a blog post in 2010](https://nedbatchelder.com/blog/201003/whats_the_point_of_ospathcommonprefix)
that noted that “the function is worse than useless, it’s misleading”
and required [patching a bug out of coverage.py](https://github.com/coveragepy/coveragepy/commit/489872c0d84aeff03d164eda5201b495a73e129d) as a result.
Ned recommended that the documentation warning should explain
that the function isn't meant to be used on paths and specifically
that “the function is in the wrong place”.

### SecureDrop path traversal vulnerability (2013)

[SecureDrop](https://securedrop.org/), a system deployed by many media organizations for securely accepting whistleblower submissions,
was [vulnerable to path traversal](https://github.com/freedomofpress/securedrop/issues/194) due to using `os.path.commonprefix()`
API incorrectly. This issue was found [during a security audit](https://media.securedrop.org/media/documents/pentest-report_securedrop.pdf) by Cure53.
The confusing behavior and name mismatch wasn't reported upstream to the CPython project.
As far as I know, this is the first known security issue resulting from `commonprefix()` unexpected behavior.

### Python 3.5 (2017)

In 2017 Valentin Lorenz [reported to bugs.python.org](https://bugs.python.org/issue30267)
that `commonprefix` still doesn't actually process paths the way users expect,
using characters instead of path segments.
This report led to the addition of a new function, `os.path.commonpath()`,
which found the common path segment prefix. The function `os.path.commonprefix()` was not deprecated.

### HTTPPasswordMgr security issue (2020, 2022)

[Donát Nagy](https://bugs.python.org/issue42766) (2020) and later [Serhiy Storchaka](https://bugs.python.org/issue46756) (2022)
reported an issue in the `is_suburi()` method for the `HTTPPasswordMgr` class which used the `commonprefix()` function
insecurely. Serhiy noted that at the time, this was [just one of three
total uses](https://bugs.python.org/issue46756) of the `os.path.commonprefix()` function within the standard library
and that the use was insecure.

### Trellix campaign to fix CVE-2007-4559 (2022)

[CVE-2007-4559](https://www.cve.org/CVERecord?id=CVE-2007-4559) is a vulnerability in the Python tarfile module
which allowed path traversal during extraction of a malicious tar archive.
A security company Trellix [launched a campaign](https://www.trellix.com/blogs/research/trellix-advanced-research-center-patches-vulnerable-open-source-projects/)
to mitigate vulnerable
code on GitHub that uses `TarFile.extractall()` by first checking all tar members
for path traversal. Unfortunately, the filtering function uses `os.path.commonprefix()`
insecurely, meaning the *filtering function itself* is also vulnerable path traversal:

```python
def is_within_directory(directory, target):
    abs_directory = os.path.abspath(directory)
    abs_target = os.path.abspath(target)

    prefix = os.path.commonprefix([abs_directory, abs_target])
    return prefix == abs_directory
```

Recognize this function? This function is almost identical to the one used in pip. As far as I can tell,
the implementation was copied from pip which was merged in 2019, but not yet
discovered to be vulnerable.

According to [this GitHub comment](https://github.com/python/cpython/issues/74453#issuecomment-1500321322), over 61,000 pull requests were submited
with this insecure mitigation for CVE-2007-4559. Searching for the name `is_within_directory()` in Python files [turns
up 2.7K hits](https://github.com/search?q=is_within_directory+language%3APython&type=code&p=3). From my own testing none of the `os.path.commonprefix()` use within top projects on the Python Package Index (PyPI)
are vulnerable, but projects that use the `is_within_directory()` function provided by Trellix
on GitHub should switch to using `os.path.commonpath()`.

This long history of insecure usage was enough to [finally deprecate the function](https://github.com/python/cpython/pull/144436)
in favor of `os.path.commonpath()`. I hope this story can be
evidence that when users report accidentally using functions insecurely that it's
a signal to fix the confusing labeling by renaming or removing the
function in favor of an API designed and labeled appropriately.
