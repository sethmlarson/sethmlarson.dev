# Security Developer in Residence Weekly Report #10

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## OpenSSF Day Europe 2023

If you haven't heard, I'm presenting on my work as the Security Developer-in-Residence at
OpenSSF Day Europe 2023 along with **Cheuk Ting Ho**. You can [register to attend the conference virtually](https://events.linuxfoundation.org/openssf-day-europe/register/)
if you haven't already. I'll be in the chat answering questions throughout the conference, hope to see you there!

The past few weeks I've been finishing slides, recording my video, and collaborating with my co-presenter 🚀

## Truststore

It was a big week for Truststore!

This week I [added support for PyPy 3.10 to Truststore](https://github.com/sethmlarson/truststore/pull/113)
since PyPy implements their `SSLContext` class differently
than CPython this required an unfortunate hack after trying
and failing to find a cleaner method that allowed `isinstance(ctx, ssl.SSLContext)`
to work.

I updated the [PR to vendor Truststore into pip](https://github.com/pypa/pip/pull/12107),
the first step towards getting pip to use Truststore by default.

PDM also released [v2.9.0](https://github.com/pdm-project/pdm/releases/tag/2.9.0) recently
which uses Truststore by default on Python 3.10+. This would explain the [recent skyrocket of installs](https://www.pepy.tech/projects/truststore?versions=%2A).

Finally, Conda appears to be [evaluating using Truststore by default](https://github.com/conda/conda/pull/13075) as well! 🥳
I spoke with **Jannis Leidel** to confirm that I was happy with Conda moving forward with using Truststore as a dependency.

## Other items

* [Opened an issue](https://github.com/pypi-data/data/issues/12) on the new [py-code.org](https://py-code.org) service that gathers all data on PyPI.
  The issue is requesting dependency data from packages and other data I track in my own PyPI dataset.
* Authored the [PSF's CNA processes document](https://github.com/psf/policies/pull/1).
* [Updated pip's security policy](https://github.com/pypa/pip/pull/12254) to point to [the PSRT webpage](https://python.org/dev/security)
  * The "Supported Versions" that I initially proposed [had some additional discussion](https://github.com/pypa/pip/issues/12260).
* [Updated `get-pip.py` generation code](https://github.com/pypa/get-pip/pull/196) to verify the digests of downloaded wheels and upgraded the digest method from MD5 to SHA256.
  I don't believe that this has ever historically been an issue, since any "MITM" attack here would have had to succeed over and over again
  in CI to persist and would get committed to the set of commits before deployment, something that hasn't been observed.
* Discussed the release process of pip with pip maintainer **Pradyun Gedam**. Stay tuned for more there.
* Reviewed the [proposal for the PyPI Malware Reporting API](https://github.com/pypi/warehouse/issues/14503).

That's all for this week! 👋 If you're interested in more you can read [next week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-11) or [last week's report](http://sethmlarson.dev/security-developer-in-residence-weekly-report-9).
