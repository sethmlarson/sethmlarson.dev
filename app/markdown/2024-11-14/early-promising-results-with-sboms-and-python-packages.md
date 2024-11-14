# Early promising results with SBOMs and Python packages

<blockquote>
  <center>
    This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>.
    Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!
  </center>
</blockquote>

I've [kicked off a project](https://discuss.python.org/t/sboms-for-python-packages-project/70261) to reduce the "phantom dependency" problem for Python. The phantom dependency problem
is where distinct software (sometimes written in Python, but often C, C++, Rust, etc) is included in
a Python package but then isn't recorded anywhere in the package metadata.

These distinct pieces of software aren't not recorded because of lack of time or awareness,
there is **no standardized method to record this information in Python package metadata**.

This means that when a software composition analysis (SCA) tool looks at the Python package
the tool will "miss" all the software that's included in the package aside from the top-level package itself.

For example, the popular Python image manipulation library "Pillow" is not only "Pillow",
the wheel files contain many more libraries to comply with the "manylinux" package platform:

```
# (the below libraries are bundled by auditwheel)
$ unzip -l pillow-11.0.0-cp312-cp312-manylinux_2_28_x86_64.whl | grep 'pillow.libs'

pillow.libs/
pillow.libs/libharfbuzz-144af51e.so.0
pillow.libs/libxcb-b8a56d01.so.1.1.0
pillow.libs/libpng16-4cc6a9fc.so.16.44.0
pillow.libs/libXau-154567c4.so.6.0.0
pillow.libs/libbrotlicommon-3ecfe81c.so.1
pillow.libs/liblzma-c9407571.so.5.6.3
pillow.libs/libfreetype-e7d5437d.so.6.20.1
pillow.libs/liblcms2-e69eef39.so.2.0.16
pillow.libs/libopenjp2-05423b53.so
pillow.libs/libtiff-0a86184d.so.6.0.2
pillow.libs/libjpeg-45e70d75.so.62.4.0
pillow.libs/libbrotlidec-ba690955.so.1
pillow.libs/libwebp-2fd3cdca.so.7.1.9
pillow.libs/libsharpyuv-898c0cb5.so.0.1.0
pillow.libs/libwebpdemux-f2642bcc.so.2.0.15
pillow.libs/libwebpmux-d524b4d5.so.3.1.0
```

I see many recognizable projects in the list of shared objects, like `libjpeg`, `libwebp`, `libpng`,
xz-utils (`liblzma`), etc. If we try to scan this installed wheel with a tool like [Syft](https://github.com/anchore/syft) we receive this report:

```
$ syft dir:venv

 ✔ Indexed file system                                                                                                                                                                                   venv
 ✔ Cataloged packages     [2 packages]  
NAME    VERSION  TYPE   
pillow  11.0.0   python  
pip     24.2     python
```

Syft isn't able to find any of the compiled libraries! So if we were to run a vulnerability scanner
we would only receive vulnerability records for Pillow and pip. My plan is to help fix this problem with Software Bill-of-Materials documents (SBOMs)
included in a standardized way inside of Python packages.

To test how well this proposal works *with today's tools*, I forked [auditwheel](https://github.com/pypa/auditwheel) and [created a rudimentary patch](https://github.com/sethmlarson/auditwheel/commit/68c3522fbd8f3377356d260e4e6d7ba4237de212) which:

* For each shared library which is being bundled into a wheel,
  record the original file path and checksum. Bundle the shared libraries into the wheel as normal.
* Using platform-specific manager query each file path back to the package that provides the file. In this specific case `rpm` was used (`rpm -qf <path>`) because `manylinux_2_28_x86_64` uses AlmaLinux 8 as the distribution.
* Gather information about that package using `rpm`, such as the name, version, etc.
* For each package, create the intrinsic "package URL" (PURL) software identifier for later use.
  This includes information about the packaging format, package name, version, but also the distro and architecture. For example, the PURL
  for the copy of libwebp used by the wheel is: `pkg:rpm/almalinux/libwebp@1.0.0-9.el8_9.1?arch=x86_64&distro=almalinux-8`
* Generate a CycloneDX SBOM file containing the above gathered information split into components and
  with relationship links between the top-level component (Pillow) and the bundled libraries.
* Embed that generated SBOM file into the wheel.

Let's run through [building Pillow from source](https://pillow.readthedocs.io/en/stable/installation/building-from-source.html) and using our forked auditwheel:

```shell
# The manylinux image may differ depending on your platform.
$ docker run --rm -it -v.:/tmp/wheelhouse \
    quay.io/pypa/manylinux_2_28_x86_64

# Install dependencies for Pillow
$ yum install --nogpgcheck libtiff-devel \
    libjpeg-devel openjpeg2-devel zlib-devel \
    freetype-devel lcms2-devel libwebp-devel \
    tcl-devel tk-devel harfbuzz-devel \
    fribidi-devel libxcb-devel

# Create a virtualenv and install auditwheel fork
$ /usr/local/bin/python3.12 -m venv venv
$ source venv/bin/activate
$ python -m pip install build
$ python -m pip install git+https://github.com/sethmlarson/auditwheel@sboms

# Download the Pillow source from PyPI
$ python -m pip download --no-binary=pillow pillow==11.0.0
$ tar -xzvf pillow-11.0.0.tar.gz

# Build a non-manylinux wheel for Pillow
$ python -m build ./pillow-11.0.0/

# Repair the wheel using auditwheel
$ auditwheel repair ./pillow-11.0.0/dist/
...
Fixed-up wheel written to /wheelhouse/pillow-11.0.0-cp312-cp312-manylinux_2_28_x86_64.whl

# Inspect the wheel for our SBOM, there it is!
$ unzip -l /wheelhouse/pillow-11.0.0-*.whl | grep '.cdx.json'
     5703  11-14-2024 19:39   pillow.libs/auditwheel.cdx.json

# Move the wheel outside our container
$ mv /wheelhouse/pillow-11.0.0-cp312-cp312-manylinux_2_28_x86_64.whl /tmp/wheelhouse/
```

So now we have a wheel file [that contains an SBOM](https://gist.github.com/sethmlarson/9b87245c99147815e8e18901f4a10444) partially describing its contents. Let's try installing that wheel and running Syft:

```
$ syft dir:venv
 ✔ Indexed file system                                                                                                                                                                       /tmp/venv-pillow
 ✔ Cataloged packages     [13 packages]  
NAME           VERSION          TYPE   
Pillow         11.0.0           python  
bzip2-libs     1.0.6-26.el8     rpm     
freetype       2.9.1-9.el8      rpm     
jbigkit-libs   2.1-14.el8       rpm     
lcms2          2.9-2.el8        rpm     
libXau         1.0.9-3.el8      rpm     
libjpeg-turbo  1.5.3-12.el8     rpm     
libpng         1.6.34-5.el8     rpm     
libtiff        4.0.9-33.el8_10  rpm     
libwebp        1.0.0-9.el8_9.1  rpm     
libxcb         1.13.1-1.el8     rpm     
openjpeg2      2.4.0-5.el8      rpm     
pip            24.2             python
```

Woo hoo! Now the proper libraries are showing up in Syft. That means we'll be able to get vulnerability information from all the contained software components.
This isn't the end, there are many many MANY ways that software ends up in a Python package. This quick validation test only shows that even with today's SBOM and SCA tools
that embedding SBOM documents into wheels can be useful for downstream tools. Onwards to even more! 🚀

If you're interested in this project, [follow the repository on GitHub](https://github.com/psf/sboms-for-python-packages) and [participate in the kick-off discussion on Python Discourse](https://discuss.python.org/t/sboms-for-python-packages-project/70261).

That's all for this post! 👋 If you're interested in more you can read [the last report](https://sethmlarson.dev/python-and-sigstore).
