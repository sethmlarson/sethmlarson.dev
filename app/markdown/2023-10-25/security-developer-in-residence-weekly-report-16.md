# Patching the libwebp vulnerability across the Python ecosystem

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

Vulnerabilities in extremely prolific software components like [CVE-2023-4863](https://nvd.nist.gov/vuln/detail/CVE-2023-4863) affecting libwebp have shown the far-reaching effects that vulnerabilities in bundled open source software can have.
libwebp was bundled along with an uncountable number of software installations from iOS, all browsers, all Electron apps, and more.

Python's ecosystem of packages is no different, many projects relied on libwebp for processing images and due to the simple nature
of the vulnerability it is likely that many usages of those libraries were also unsafe. In order to learn about mobilizing
an entire upstream open source software ecosystem to patch, I set out to do just that for libwebp and documented the experience.

I also wanted to learn about ways that consumers of packages can do their part without putting additional
burden on maintainers during a time of mass-patching or mitigating vulnerabilities which have active exploits.
This work started shortly after the CVE was associated with libwebp but wasn't published until now to give
projects a chance to patch their releases.

Mitigating a vulnerability on this scale requires the following steps:
 
- Determine projects which bundle a vulnerable version of libwebp
- Contact each project which hasn't already patched
- Wait for releases to be published
- Notify users about the vulnerable bundled component

Python wheels that include binary extensions tend to bundle shared libraries that they
depend on in order to work automatically when installed. There are tools that make this
process of bundling easier like [auditwheel](https://pypi.org/project/auditwheel/), [delvewheel](https://pypi.org/project/delvewheel/), and [delocate](https://pypi.org/project/delocate/).

## Finding projects with vulnerable libwebp

The initial difficulty of this problem is that bundled shared libraries in wheels aren't included
in any Python packaging metadata unlike Python package dependencies.

In order to find libwebp shared libraries inside of Python packages on PyPI via a queryable interface
I downloaded [Tom Forbes' dataset on PyPI](https://py-code.org/) locally and queried using [DuckDB](https://duckdb.org/).
Thanks to [Tom](https://tomforb.es/) for putting this together and helping me get started with the dataset.

```sql
SELECT project_name, path
FROM '*.parquet'
WHERE regexp_matches(
  path, '/(lib)?webp[^/]*\.(a|so|dylib|dll)'
)
GROUP BY project_name;
```

From examining the output of this query and combining the result with a dataset about downloads,
the following projects (among others) get highlighted:

| Project       | Downloads/month |
|---------------|-----------------|
| Pillow        | 70,053,401      |
| opencv-python | 21,714,182*     |
| pyproj        | 8,106,066       |
| Fiona         | 6,514,863       |
| rasterio      | 1,953,666       |

> \* Sum of downloads for all opencv-*-python flavors.

Looking at all the projects the total monthly downloads exceeds 100,000,000, and that's a lot of downloads!
To figure out what the relative magnitude is compared to other bundled shared libraries I ran the following
query which attempts to normalize names of shared libraries, so they can be grouped together more easily:

```sql
SELECT
  regexp_replace(
    regexp_replace(
      regexp_extract(path, '([^/]+)$'),
      '\.[0-9\.]*[0-9]', '.X'
    ),
    '-[a-f0-9]{8}\.so', '.so'
  ) AS lib,
  COUNT(DISTINCT project_name) AS projects,
  LIST(project_name)
FROM '*.parquet'
WHERE
  regexp_matches(
    path, '/[^/]*\.(a|so|dylib|dll)(\.[^/]+)?$'
  )
GROUP BY lib
ORDER BY projects DESC
LIMIT 1000;
```

With some manual labeling and data massaging I was able to end up with this table:

| Bundled Library              | Name                    | Min Projects |
|------------------------------|-------------------------|--------------|
| libgcc_s.so.X                | GCC Runtime             | 920          |
| libgomp.so.X                 | GNU OpenMP              | 747          |
| libstdc++.so.X               | GNU C++                 | 527          |
| libz.so.X                    | zlib                    | 487          |
| libgfortran.so.X             | libgfortran             | 374          |
| libquadmath.so.X             | GCC Quad Precision Math | 372          |
| libcrypto.so.X / libssl.so.X | OpenSSL (or others)     | 341          |
| liblzma.so.X                 | Xz Utils                | 235          |
| libbz2.so.X                  | Bzip2                   | 200          |
| libselinux.so.X              | SE Linux                | 189          |

Compare the above values to libwebp which was bundled by **around 50 projects**.
Note that the last column is "min projects", putting this together was a manual
task that I didn't want to spend too much time on, so the magnitude difference
is at least that much. The sums above are from all extensions
(`.so`, `.dll`, `.a`, and `.dylib`) not only `.so` files.

So I had a list of projects which were likely to be impacted. At this point
there was not much information about exactly which libwebp functions were impacted
only that the vulnerability could be triggered by loading a maliciously crafted
image. This meant I didn't have the full information available to know whether
a project's usage was *definitely* vulnerable. **This highlights the importance
of having as much information as possible in the upstream CVE to avoid churn.**

## Reaching out to each project and waiting for releases

I saw that Pillow had quickly updated their own wheels, so I didn't have to reach out to the maintainers of that project.
Other projects however I had to manually find the security contact information and then reach out. Finding
security contact information was difficult for most of the projects as [they didn't have a `SECURITY.md`
file in their repositories](https://docs.github.com/en/code-security/getting-started/adding-a-security-policy-to-your-repository)
and some had no contact information directly listed in package metadata at all.

Looking at [OpenSSF Scorecard data](https://github.com/sethmlarson/pypi-scorecards) for the top 5,000 projects on PyPI by downloads, there hasn't been a noticeable
change in the percentage of projects which have a defined security policy on GitHub (19% in July 2022, 22% today).

If maintainers plan to handle some security reports I recommend having a short security policy that references how to get
in contact, usually via [GitHub Security Advisories on the repository](https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/about-repository-security-advisories) or via email.

This was the message template that I used when initially contacting maintainers. I've included it here
because I've since learned a few things I want to change about how I reached out to folks:

> Hello,
>
> I'm Seth Larson, Security Developer-in-Residence at the PSF. I'm emailing you because there was no documented security policy for (project),
> if this isn't the correct channel to contact for these types of issues let me know.
> 
> I am contacting you because I believe (project) may be vulnerable to [CVE-2023-4863](https://nvd.nist.gov/vuln/detail/CVE-2023-4863) due to bundling a vulnerable version of libwebp in project wheels.
> v1.3.2 of libwebp fixes the vulnerability. CVE-2023-4863 is on CISA Known Exploited Vulnerabilities list meaning there are active exploits in the wild.
>
> My recommendation to fix the vulnerability:
>
> - Create a new patch release of (project) with the fixed version of libwebp.
> - In the changelog, mention that the fix upgrades the version of libwebp to not be vulnerable to CVE-2023-4863.
>
> You don't need a new CVE for this fix since the vulnerability exists in a bundled component.
> After that I can submit an advisory to the [PyPA Advisory database](https://github.com/pypa/advisory-database/) on your behalf. Let me know if you have questions.

I received replies from each project that I reached out to, many folks were appreciative of the tap on the shoulder
to upgrade their dependency:

> "The Python community is fortunate to have you on the beat."

💜

I did however want to note the following through this process:

* This report added stress to maintainers, likely due to the known exploited status of this vulnerability. In the future there may be a better way of phrasing this.
* Introducing myself as Security Developer-in-Residence might have come off as "I'm telling you what to do" and that wasn't my intention. This role isn't to boss anyone around,
  my hope is that the merits of my suggestions along with concurrent time investment into solving the problem together will make the process easier.

There were also a few reasons why a patch-and-release was difficult for some projects, among them having no access to proper build platforms and being blocked on
dependencies that were bundling libwebp such as SDL.

## Notifying users about the vulnerable bundled component

Because libwebp isn't listed in any packaging metadata it's not currently possible for vulnerability detection tooling
to alert based on insecure versions of libwebp there needs to be additional work to make vulnerability detection tooling to work.

For this task, I [added entries in the PyPA Advisory database](https://github.com/pypa/advisory-database/blob/main/vulns/pillow/PYSEC-2023-175.yaml) so tools like [pip-audit](https://pypi.org/project/pip-audit/) 
will be able to detect vulnerable bundling of libwebp until there's a standard for encoding bundled projects into Python packaging metadata.

```shell
# Use pip freeze to see we have an insecure
# version of Pillow (10.0.0) installed.
$ python -m pip freeze
...
Pillow==10.0.0

# Install pip-audit and run it against the current environment:
$ python -m pip install pip-audit
$ pip-audit

Found 3 known vulnerabilities in 1 package
Name   Version ID                  Fix Versions
------ ------- ------------------- ------------
pillow 10.0.0  PYSEC-2023-175      10.0.1
pillow 10.0.0  GHSA-j7hp-h8jx-5ppr 10.0.1
pillow 10.0.0  GHSA-56pw-mpj4-fxww 10.0.1

# Upgrade Pillow, then see that pip-audit is happy now!
$ python -m pip install --upgrade Pillow
$ pip-audit

No known vulnerabilities found
```

You could configure pip-audit to use the OSV database as a source which for Pillow that
would work as expected due to using GitHub Security Advisories (GHSA) as source as well
but not all projects I contacted created a GitHub Security Advisory. For those cases
having a `PYSEC` vulnerability ID was needed.

## Bundling, debundling, and software repositories

Thinking about bundling generally, there are a few different types of software repositories that each have their own behavior:

* **Arbitrary** (Debian, Red Hat, Conda)
* **Ecosystem-specific** (PyPI, NPM, RubyGems)
* **Applications** (Dockerhub, Quay, App Stores)

The **Arbitrary** software repositories can debundle shared libraries much easier than others because
they're capable of installing and managing arbitrary software files rather than only files from a
certain ecosystem. The libwebp vulnerability tended to affect applications and ecosystem-specific
software packages. Patching an arbitrary software repository only requires patching in one place
and ensuring dependent packages aren't restricting its use.

It's interesting to compare Conda to PyPI, as both are known for their Python packaging ecosystems
however it's much more likely for "upstream" development of Python packages to land in PyPI
and then be redistributed via Conda.

## What I learned?

Overall I learned a lot from this exercise:

* Detecting bundled shared libraries is imperfect, need a method to identify and version them
  and for that method to be automatic for broad adoption by Python packages.
* Downstream users may need to install from source if upstream isn't able to patch directly.
  Currently, there's no way to "unbundle" a wheel or to patch it again with an up-to-date
  shared library from the system.
* Contacting maintainers is a manual effort, many projects don't have a security policy.

## Other items

* The Python Software Foundation CVE Numbering Authority (CNA) [published its first CVE](https://www.cve.org/CVERecord?id=CVE-2023-5752), a medium severity vulnerability affecting pip when installing from a Mercurial repository.
* Published the [Security Developer-in-Residence Q3 Report](https://pyfound.blogspot.com/2023/10/security-developer-in-residence-2023-q3-report.html) to the PSF blog.
* Presented to the [Stockholm Python User Group](https://www.meetup.com/pysthlm/events/296576048/).

That's all for this week! 👋 If you're interested in more you can read [next week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-17) or [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-15).
