# Security Developer-in-Residence Weekly Report #31

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## Windows CPython SBOMs

I've finished up work for Software Bill-of-Materials for generating Windows CPython artifacts,
these PRs are being reviewed by Windows release managers. A few things left to do:

* Run integration tests for the proposed Azure Pipelines definition.
* Add small change to upload procedure for Windows artifacts to also upload the new SBOM artifacts.

After Windows is complete the only platform left is macOS which I've asked release managers about the best way to get started for this platform.

## Conferences and Talks

I'm locked in for conference season in 2024, I'll be attending the following conferences
so if you are too then [let me know](https://sethmlarson.dev/)!

* Registered for [OSS Summit North America](https://events.linuxfoundation.org/open-source-summit-north-america/), [SOSS Community Day NA](https://events.linuxfoundation.org/soss-community-day-north-america/), and [PyCon US 2024](https://us.pycon.org/2024/).
* Speaking at SOSS Community Day NA, [which just published its schedule](https://openssf.org/blog/2024/02/26/soss-community-day-north-america-na-agenda-live/).
  My talk is titled "Embrace the Differences: Securing Open Source Ecosystems Where They Are".
* Speaking at a sponsored talk by Alpha-Omega with Alpha-Omega cofounder **Michael Wisner** at PyCon US 2024 which also [just published its schedule](https://us.pycon.org/2024/schedule/).
  The talk title is "[State of Python Supply Chain Security](https://us.pycon.org/2024/schedule/presentation/148/)".
* I'm planning on running an open space at PyCon US 2024 with **Madison Oliver** on the Open Source vulnerability ecosystem and tools specifically for open source maintainers.
  Look forward to that if you're attending PyCon US 2024.

## Other items

* [White House published a report on memory safety](https://www.whitehouse.gov/oncd/briefing-room/2024/02/26/press-release-technical-report/) this week.
  I read the report and interested folks may be interested in [my own writing on Python as a memory safe programming language](https://sethmlarson.dev/security-developer-in-residence-weekly-report-21).
  From my analytics this article is receiving more attention following the White Houses' publication.
* Linux was announced as a CVE Numbering Authority this week. The guide I authored on becoming a [CVE Numbering Authority as an Open Source
  project](https://openssf.org/blog/2023/11/27/openssf-introduces-guide-to-becoming-a-cve-numbering-authority-as-an-open-source-project/)
  was highlighted by Greg Kroah-Hartman in a [blog post](http://www.kroah.com/log/blog/2024/02/13/linux-is-a-cna/) and on the [Open Source Security podcast](https://opensourcesecurity.io/2024/02/25/episode-417-linux-kernel-security-with-greg-k-h/).
* Reviewed the Python package lock file updated proposal from **Brett Cannon**.
* Coming up with potential security-related projects for Python and Google Summer of Code.
* Working on grant renewal with Alpha-Omega for the Python Software Foundation.

I'll be taking a break from weekly updates in March because I'll be traveling in early and late March
meaning I'll only have ~5 normal work days, so if you're curious why there aren't any weekly updates
that will be why. ✈️

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-32) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-30).
