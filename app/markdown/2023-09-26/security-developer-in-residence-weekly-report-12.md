# Starting on Software Bill-of-Materials (SBOM) for CPython

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

I've started dipping my toes into creating an authoritative SBOM for the CPython project,
you can follow along in [this GitHub repository](https://github.com/sethmlarson/cpython-sbom) if you are interested.
This project is very early and this *will not* be the final product or place where this information is published,
this is only a place to experiment and get feedback on the approach and outputs before putting the final infrastructure in place.

I started with the most straightforward release artifact, the source tarball, and I am planning to tackle the binary installers
later since they'll require more research into the release processes. There is a work-in-progress SBOM file for `Python-3.11.5.tgz`
available in the [`sboms/` directory](https://github.com/sethmlarson/cpython-sbom/blob/main/sboms) on the repository.

I've also included an [SBOM for CPython 3.11.0](https://github.com/sethmlarson/cpython-sbom/blob/main/sboms/Python-3.11.0.tgz.spdx.json) which can be used to see whether vulnerability scanning tools are capable of consuming
the result SBOM and flagging subcomponents for vulnerabilities. I used [Grype](https://github.com/anchore/grype) as an example for this, and indeed it was able to consume
the SBOM and flag the known vulnerabilities:

```shell
$ grype sbom:sboms/Python-3.11.0.tgz.spdx.json

 ✔ Vulnerability DB                [updated]  
 ✔ Scanned for vulnerabilities     [9 vulnerability matches]  
   ├── by severity: 0 critical, 6 high, 3 medium, 0 low, 0 negligible
   └── by status:   0 fixed, 9 not-fixed, 0 ignored

NAME     INSTALLED  FIXED-IN  TYPE  VULNERABILITY   SEVERITY 
CPython  3.11.0                     CVE-2023-41105  High      
CPython  3.11.0                     CVE-2023-36632  High      
CPython  3.11.0                     CVE-2023-24329  High      
CPython  3.11.0                     CVE-2022-45061  High      
CPython  3.11.0                     CVE-2023-40217  Medium    
CPython  3.11.0                     CVE-2023-27043  Medium    
CPython  3.11.0                     CVE-2007-4559   Medium    
expat    2.4.7                      CVE-2022-43680  High      
expat    2.4.7                      CVE-2022-40674  High
```

The tool was able to see not only vulnerabilities in CPython *but also in the expat subcomponent*. Without an SBOM the expat subcomponent wouldn't be detected by current versions of Grype.
Running Grype on the CPython 3.11.5 SBOM results in zero known vulnerabilities. 🥳

```shell
$ grype sbom:sboms/Python-3.11.5.tgz.spdx.json 

 ✔ Vulnerability DB                [no update available]  
 ✔ Scanned for vulnerabilities     [0 vulnerability matches]  
   ├── by severity: 0 critical, 0 high, 0 medium, 0 low, 0 negligible
   └── by status:   0 fixed, 0 not-fixed, 0 ignored 

No vulnerabilities found
```

## Sigstore signatures for CPython

Now all CPython releases that have Sigstore verification materials have
"bundles" (ie `.sigstore` files) instead of the "disjoint verification materials" (ie `.crt` and `.sig` files).
These new bundles [have been back-filled from existing verification materials](https://github.com/python/pythondotorg/issues/2300) using new
[`VerificationMaterials.to_bundle()` method](https://github.com/sigstore/sigstore-python/pull/719)
in the Python Sigstore client. Thanks to **Łukasz Langa** for verifying the new bundles and publishing them to python.org.

Now that all releases have bundles available, I've also updated the [Sigstore verification instructions on python.org](https://www.python.org/download/sigstore/)
to only reference bundles:

```shell
$ python -m sigstore verify identity \
  --bundle Python-3.11.0.tgz.sigstore \
  --cert-identity pablogsal@python.org \
  --cert-oidc-issuer https://accounts.google.com \
  Python-3.11.0.tgz
```

Having bundles means one less file to download to verify a signature and that verification doesn't
need to query the transparency log, instead relying on the entry embedded within the bundle.

## Truststore support coming for Conda!

Conda has [merged the pull request](https://github.com/conda/conda/pull/13075) to add Truststore support to Conda which is slated for v23.9.0. This required creating a [top-level feedstock
for Truststore](https://github.com/AnacondaRecipes/truststore-feedstock/pull/2).

pip has merged the pull request to bundle Truststore into pip, so it's no longer required to "bootstrap" Truststore in order to have support for using system certificates.
This feature will be coming in pip v23.3.

## Python Security Response Team (PSRT) using GitHub Security Advisories

I spent some time developing a small GitHub App that would add the PSRT GitHub team to all newly
created GitHub Security Advisories and have something that works in-theory.

Unfortunately, there's currently [no way to get webhook events
for the creation of draft GitHub Security Advisories](https://github.com/orgs/community/discussions/67871), you can only get a webhook for when *security reports
are filed*. This means that anyone with access to GitHub Security Advisories (ie organization or repository admins)
wouldn't trigger the GitHub App action to add the PSRT team.

## Security Developer-in-Residence 2023 Q3 update for PSF blog

Since I've just passed 3 months in this role (time sure does fly!) I am drafting a summarized update for my work in 2023 Q3 that will be published to
the [Python Software Foundation blog](https://pyfound.blogspot.com/). Subscribe to the blog via RSS or other social media platform to get notified.

That's all for this week! 👋 If you're interested in more you can read [next week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-11) or [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-13).
