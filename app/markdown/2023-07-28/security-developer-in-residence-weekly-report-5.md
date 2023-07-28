# Security Developer-in-Residence – Weekly Report #5

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## CVE Numbering Authority (CNA) registration

I've continued working on having the Python Software Foundation registered as a CNA. We have at this
point submitted our registration containing a list of contacts, a disclosure policy, location of
advisories and an advisory database. We've received an onboarding meeting date (August 21st) where
we'll meet with the CNA partner team to ask questions about the process and fill out some example CVE records.

The Python Steering Council have **approved having Python scoped under the PSF CNA**! 🥳

Part of being a CNA is creating and updating CVE records which can be tough to do by hand to large JSON documents.
To make managing CVE records a more guided experience there are tools like [Vulnogram](https://github.com/Vulnogram/Vulnogram)
which provide a UI to editing a CVE record. Vulnogram lets you create template files that you can load into
the program, so it's possible to pre-fill Python's security release schedule into the "Affected versions"
fields for CVE records along with other fields like vendor, CPEs, product name, etc:

```json
{
  "vendor": "Python Software Foundation",
  "product": "Python",
  "repo": "https://github.com/python/cpython",
  "versions": [
    {
      "status": "affected",
      "version": "0.0.0",
      "lessThanEqual": "3.8.17",
      "versionType": "python"
    },
    {
      "status": "affected",
      "version": "3.9.0",
      "lessThanEqual": "3.9.17",
      "versionType": "python"
    },
    {
      "status": "affected",
      "version": "3.10.0",
      "lessThanEqual": "3.10.12",
      "versionType": "python"
    },
    {
      "status": "affected",
      "version": "3.11.0",
      "lessThanEqual": "3.11.4",
      "versionType": "python"
    }
  ],
  "defaultStatus": "unaffected"
}
```

Vulnogram also has the ability to render human-readable advisories from the input information which should make the manual
aspects of CVE disclosure easier. There's a [YouTube video all about Vulnogram](https://www.youtube.com/watch?v=o3V-fmQpC0o)
and how to use it with [CVE Services](https://www.cve.org/AllResources/CveServices).

I attended the [**OpenSSF Vulnerability Disclosures** working group](https://github.com/ossf/wg-vulnerability-disclosures)
call and discussed the PSF CNA motivations and my desire to create materials for other open source projects looking to become CNAs for their own project.
The folks on the call agreed that the documentation for a "minimum viable CNA" geared towards maintainers of open source projects would be
a valuable resource. Look forward to updates here as the PSF progresses through the CNA onboarding process.

## Sigstore signed Python releases

Last week I reported that Sigstore signatures for Python releases were being worked on in order to have a consistent
and well-documented experience as a downstream consumer of release artifact signatures. This week I can report that
all Python releases with signatures are now consistent with the [documented signing methods](https://www.python.org/download/sigstore).

My announcement [spawned a conversation](https://fosstodon.org/@sethmlarson/110781155153378648) about downstream distributions consumption of Sigstore signatures
compared to GPG signatures, mostly that there is no way to have a previously configured trust configuration (for Sigstore that is a identity and provider pair,
for GPG that would be a key) continue to work and be extended to a new trust configuration (ie adding a new identity/provider for Sigstore or GPG key).
For Sigstore a consumer would need to check the documented release manager in order to know which identity to verify for a given Python release stream.

## Sigstore bundles

When Sigstore signing was first applied to Python releases there were two files created, a certificate (`.crt`) and a signature (`.sig`)
for each release artifact. Some time later the concept of a Sigstore "bundle" emerged as a way to have a single file with all materials
required to verify an artifact (the certificate, signature, and the Rekor transparency log entry). By default, the Sigstore Python client
creates both sets of verification materials when signing an artifact.

This meant that the downloads page would need to document [both ways of verifying Python release artifacts](https://github.com/python/pythondotorg/issues/2285)
which is already confusing, but then there would need to be an additional decision for consumers as well! Old releases may only contain a crt/sig combination
and not a bundle. I raised this issue in the [Sigstore Slack](https://www.sigstore.dev/community) and was recommended by **William Woodruff** that this
functionality [may be useful for others](https://github.com/sigstore/sigstore-python/issues/718#issuecomment-1654048226) looking to migrate to the newer improved Sigstore bundles.

Together we [created an issue](https://github.com/sigstore/sigstore-python/issues/718) describing the problem and I [authored a pull request](https://github.com/sigstore/sigstore-python/pull/719) that adds the internal APIs
required in order to transform `crt`/`sig` files into a bundle. This will allow back-filling bundles to previous Python release artifacts without needing to resign them.

## Other items

* [Manually submitted CVE-2023-37276](https://github.com/pypa/advisory-database/pull/134) which [promptly broke the automation](https://github.com/pypa/advisory-database/pull/135) due to bad formatting, [submitted a PR](https://github.com/pypa/advisory-database/pull/137) to ensure formatting is consistent for manually submitted advisories.
* Participated in a [Discuss thread](https://discuss.python.org/t/ssl-changing-the-default-sslcontext-verify-flags/30230) on adding more secure default values for `SSLContext.verify_flags`

That's all for this week! 👋 If you're interested in more you can read [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-4).
