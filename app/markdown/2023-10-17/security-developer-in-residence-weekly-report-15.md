# Quarterly report for Q3 2023 on the PSF Blog

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>.
  Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

It's hard to believe, but I've been in the Security Developer-in-Residence position for 3 months now! 🥳
This is the first quarterly report for Q3 of 2023 on the many accomplishments so far and future projects
that I aim to tackle in the role. You can read the full report on the [Python Software Foundation blog](https://pyfound.blogspot.com/2023/10/security-developer-in-residence-2023-q3-report.html).

In the report I identified three flagship projects that I'm looking to work on this upcoming quarter:

* Software Bill-of-Materials for CPython
* Tracking bundled dependencies in Python packages
* CPython and pip release process improvements

You should read the full report especially the section under "Future Projects" if you're interested in any of these topics! A lot of this week has been taken up by writing this report, so there won't be much else to report here this week.

## Other items

* The CPython core developer sprint happened last week, I've been following along with all the social media posts. Very exciting stuff about the C API.
  I'll be meeting with the CPython Developer-in-Residence [Łukasz](https://lukasz.langa.pl/) to talk about everything that happened at the sprints and what's relevant to my work.
* pip v23.3 released with the following relevant changes:
  * Truststore was vendored which means you no longer need to bootstrap Truststore in order to use [pip's optional Truststore support](https://pip.pypa.io/en/stable/topics/https-certificates/#using-system-certificate-stores).
  * Upgraded the vendored certifi to not be vulnerable to [GHSA-xqr8-7jwr-rhp7](https://github.com/advisories/GHSA-xqr8-7jwr-rhp7).
  * Secure Transport support has been removed from pip due to pip no longer supporting an OpenSSL version that required it (1.0.1 and earlier).

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-16) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-14).
