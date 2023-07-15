# Security Developer-in-Residence – Weekly Report #3

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.<br>
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## PSF as a CVE Numbering Authority (CNA)

This week's primary focus has been on working towards registering the PSF as a CVE Numbering Authority (CNA)
that is managed by PSF staff. Before you can register your organization as a CNA you need a few things:

- Scope (Projects that the CNA can allocate CVE IDs for)
- Root CNA (The CNA that allocates your CVE IDs)
- Disclosure Policy (How the CNA accepts vulnerability disclosures)
- Public advisory location (Where advisories get published, both human and machine-readable formats)
- List of people to staff the CNA (as Points of Contact for your Root CNA)
- Attending trainings for onboarding as a CNA

If you're looking to learn more, there's a bunch of resources that MITRE has put together on becoming a CNA:

- [CNA Onboarding](https://www.cve.org/ResourcesSupport/Resources#cnaOnboarding)
- [CNA Rules](https://www.cve.org/ResourcesSupport/AllResources/CNARules)
- [CNA Services](https://www.cve.org/AllResources/CveServices)
- [cvelib (written in Python!)](https://github.com/RedHatProductSecurity/cvelib)

I'll be sharing insights on the PSF's journey to become a CNA along with recommendations for other open source
foundations and projects.

Since we're aiming for the PSF CNA to have Python and pip as their initial scope I've sent [proposals](https://github.com/pypa/pip/issues/12139)
to the Python Steering Committee and pip maintainers for approving CNA scoping and how the PSF CNA and the Python Security Response Team
(PSRT) will work together.

There's also been some work behind the scenes on creating a small advisory database using the [OSV](https://osv.dev) format
and importing historical vulnerability data into that database so it's available in a public machine-readable form.

## Python wheel build numbers

Python wheel distributions have a concept called "[build numbers](https://packaging.python.org/en/latest/specifications/binary-distribution-format/#file-format)" or "build tags"
which are *kind-of* part of the package version, but also not! They don't appear in the version of
the **release** on PyPI but build numbers do have an impact on resolution of packages
like when installing via pip. Higher build numbers are favored by pip over lower (or non-existent) build numbers.

```
{distribution}-{version}(-{build tag})?-{other tags}.whl
                               ^
Build number goes here! -------/
```

The primary use-case for build numbers is to be able to publish new wheels to an existing release without needing
to rebuild *all* the wheels again which would be necessary if a new release was created.

Now why are build numbers interesting from a security POV? The problem is that unlike the "partial rebuild"
mechanism for many ecosystems (like downstream repackaging) the build number **is not a part of the version**.
This means that without using hashes or direct URLs there's no way to force pip to install a wheel with a specific build number.

This also means that it's difficult to reference the newly released distributions from outside the ecosystem which
typically use versions and version ranges (like CVEs, OSV, Package URLs, etc). I've created a [discussion thread](https://discuss.python.org/t/guidance-on-wheel-build-numbers-for-external-reference-security-fixes/29621/2)
on this topic and will create some guidance for build numbers' use-case.

Relatedly: Back at PyCon US 2023 I was nerd-sniped by **William Woodruff** into writing an entire post about PEP 440 and quirks in Python versioning.
That piece is nearly complete and will hopefully be coming soon. Stay tuned!

## Trusted publishers being recommended on GitHub Actions

Last week I noted the stats on adoption of Trusted Publishers for GitHub Actions. One
of the recommendations to drive more adoption got [merged and released](https://github.com/pypa/gh-action-pypi-publish/pull/167)
to the `pypa/gh-action-pypi-publish` project. The thought is that if you're using GitHub Actions
without using Trusted Publishers then the action emits a message that's visible in the GitHub UI
recommending adopting the new feature:

> **Upgrade to Trusted Publishing**
> Trusted Publishers allows publishing packages to PyPI from automated
> environments like GitHub Actions without needing to use username/password
> combinations or API tokens to authenticate with PyPI.
> Read more: https://docs.pypi.org/trusted-publishers

Now that this has been released and we have metrics for Trusted Publisher adoption we can see if it makes
any noticeable difference in the rate of adoption.

That's all for this week! 👋