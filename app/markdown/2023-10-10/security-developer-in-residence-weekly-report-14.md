# Reproducible builds for CPython source tarballs

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

It was a short week for me with a day of PTO and the Python Software Foundation observing Indigenous Peoples' Day in the USA.

More focused time on CPython's release process! Using [diffoscope](https://diffoscope.org/) which is a tool that does a deep diff of files or directories
and then gives a summary of the differences, we can see what the differences are between the official CPython 3.12.0
release tarballs and the ones I built using GitHub Actions:

```
│ ├── file list
│ │ @@ -1,4764 +1,4764 @@
│ │ -drwxr-xr-x   0                             0 2023-10-02 11:48:14.000000 Python-3.12.0/
...
│ │ +drwx------   0 thomas (1000) thomas (1000) 0 2023-10-02 12:03:24.000000 Python-3.12.0/
```

The biggest difference was in the archive metadata. You can see Thomas Wouters from the official python.org tarball for Python 3.12.0 there!

Tar files save metadata about the user and group, just like a filesystem would,
and the default behavior is to save the calling users' information. I consulted the [guide on reproducible-builds.org
for archives](https://reproducible-builds.org/docs/archives/) and the documentation for GNU tar which has a [section on reproducibility](https://www.gnu.org/software/tar/manual/html_node/Reproducibility.html#Reproducibility).
From reading these documents I found the following individual options:

* Use the commit time (`git log v3.12.0 -1 --pretty=%ct`) as the maximum `mtime` metadata value for `tar`.
  Those options manifest as `--mtime` and `--clamp-mtime`.
* Sort the entries within the tar file by name so that the discovery process from the filesystem doesn't matter.
  The order isn't guaranteed on some platforms, so sorting after the fact is required. Use `--sort=name` for this behavior.
* Set an explicit known user and group ID, in this case `0` for both user and group instead of inheriting from the current user
  of `tar`. Uses options `--owner=0`, `--group=0`, and `--numeric-owner`.
* Omit a bunch of optional metadata like process ID, file access time, status change time, and some file permissions:
  `--pax-option=exthdr.name=%d/PaxHeaders/%f,delete=atime,delete=ctime` and `--mode=go+u,go-w`.
* Added the `--no-name` option to the gzip compression subroutine to avoid embedding the name into the gzip stream.

You can see the [complete pull request to python/release-tools](https://github.com/python/release-tools/pull/62) which has all the options together.

After adding these options I was able to reproduce a source build on GitHub Actions byte-for-byte with
the same build locally and by using [reprotest](https://salsa.debian.org/reproducible-builds/reprotest) was able to verify that this process worked for many different
filesystem and user scenarios.

Another [improvement I added to the Windows installer builds](https://github.com/python/release-tools/pull/61) to ensure that the git tag
wasn't erroneously or maliciously rewritten upstream at the beginning of the Windows installers build. This change
adds another input to the Windows build process which is the upstream git commit SHA and then checks that known good
value against the resolved git tag after the CPython source code is downloaded. This means that the correct git commit
is being used and that malicious code can't be injected into the Windows installers unknowingly.

## Other items

* Finishing up the Q3 report for the Security Developer-in-Residence position. Hope to publish this report to the PSF blog this month.
* I'll be chatting remotely with attendees at the [Stockholm Python meetup](https://www.meetup.com/pysthlm/events/296576048/) on the 18th of October.
* Working with the OpenSSF SBOM Everywhere WG on finalizing the "[Best Practices for Naming and Directory conventions for SBOMs](https://docs.google.com/document/d/1-jFoh_R7FV4NhHuUkt4Atz3h4K9b4bnmolntSbytspE)" document.
* OpenSSF Day Europe recordings have been uploaded to YouTube. Here are two notable talks for Python:
  * [We make Python safer than ever](https://www.youtube.com/watch?v=jhzv5RU56V4) by Cheuk Ting Ho (OpenSSF) and Seth Larson (PSF)
  * [Trusted Publishing: Lessons from PyPI](https://www.youtube.com/watch?v=Cc7hl_tyKWE) by William Woodruff

That's all for this week! 👋 If you're interested in more you can read [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-13).
