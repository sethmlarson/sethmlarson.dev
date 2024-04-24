# Open Source Summit North America 2024

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

<p>Last week I attended <a href="https://events.linuxfoundation.org/soss-community-day-north-america/">SOSS Community Day</a> and <a href="https://events.linuxfoundation.org/open-source-summit-north-america/">OSS Summit</a>.
It was great to catch up with friends and to meet new people for the first time
at a cross-ecosystem open source event.</p>

<p>I gave a talk "<a href="https://sosscdna24.sched.com/event/1aNLj/embrace-the-differences-securing-open-source-ecosystems-where-they-are-seth-larson-python-software-foundation">Embrace the Differences: Securing software ecosystems where they are</a>"
which funnily enough had a complementary talk about the <a href="https://sosscdna24.sched.com/event/1aNLd/driving-security-at-scale-principles-for-package-repository-security-jack-cable-cisa-zach-steindler-github">ways software repositories can collaborate for security</a>.
</p>

<p>My talk focused on how security standards and tools typically want to operate across software ecosystems and differences in standards, tools, maintainers, and user expectations between ecosystems
can make that difficult.</p>

<p>You can <a href="https://static.sched.com/hosted_files/sosscdna24/49/soss-community-day-na-2024-embrace-the-differences.pdf">download my slides</a> and the recording will
be available <a href="https://www.youtube.com/@LinuxfoundationOrg">eventually on YouTube</a>.</p>

### OpenSSF Tabletop Session

<div class="row">
<div class="col-6 col-12-sm">
<p>I also participated in the first <a href="https://sosscdna24.sched.com/event/1aN8l/ttx-session-moderated-by-dana-wang-openssf-the-linux-foundation-panelist-contributor-details-in-description">OpenSSF Tabletop Session</a> organized and hosted by <strong>Dana Wang</strong>.
I played the role of "open source maintainer" and represented how an exploited zero-day vulnerability would
appear from the perspective of an open source project.</p><p>I emphasized the realities of vulnerability disclosure to open source projects like under-resourcing, most maintainers being volunteers, and stress caused during times of crisis.</p>
</div>
<div class="col-6 col-12-sm">
<center>
<img style="max-width: 100%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_9077.jpg"/>
<small>Cast of the tabletop session!</small>
</center>
</div>
</div>

### So many people!

I also met up with many folks doing open source security, maintenance, and funding:

* Met with many folks from the [Alpha-Omega](https://alpha-omega.dev) cohort.
  I'm looking forward to having more cross-functional discussions about new approaches to securing open source.
* Met with Michael Winser from Alpha-Omega to work on our PyCon US 2024 talk [State of Supply Chain Security for Python](https://us.pycon.org/2024/schedule/presentation/148/).
* Met with my friend [William Woodruff](https://yossarian.net/) from Trail of Bits and discussed the system TLS proposal and build provenance for Homebrew (and what could be learned for Python).
* Met with Samuel Giddins and Martin Emde from the Ruby ecosystem to discuss shared challenges for introducing security into an ecosystem.
* Met [Lauren Hanford from Tidelift](https://tidelift.com/) to discuss supporting and funding maintainers.
* Met [Mirko from Sovereign Tech Fund](https://www.linkedin.com/feed/update/urn:li:activity:7186443786615422976/) and discuss their program for hiring open source maintainers.
* Attended the [talk by Kara Sowles](https://ossna2024.sched.com/event/1aBVA) from GitHub on the state of open source funding
  and learned about "downturn-resilient" funding.
* Many folks who asked me about security initiatives happening in the Python ecosystem.

## Other items

* Participating in the [pre-PEP discussion for reviving PEP 543](https://discuss.python.org/t/pre-pep-discussion-revival-of-pep-543/51263) (system TLS).
* Created a [proposal](https://github.com/python/release-tools/issues/111) for allowing any release manager to create a CPython release.
* Created a [pull request](https://github.com/python/release-tools/pull/117) for uploading Windows SBOMs to python.org/downloads.
* Merging and backporting the [upgrade to libexpat 2.6.2](https://github.com/python/cpython/pull/117296)
* Chose which proposal(s) I would be willing to mentor for Google Summer of Code 2024 (thanks to the folks who submitted!)
* Triaged reports and fixes for the PSRT.
* I wasn't involved, but PyPI has [added Trusted Publisher support](https://blog.pypi.org/posts/2024-04-17-expanding-trusted-publisher-support/) for ActiveState, GitLab, and Google Cloud Build.

Note that I've been summoned for jury duty starting next week, so expect fewer updates over the next two weeks depending on how that goes.

That's all for this week! 👋 If you're interested in more you can read [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-33).
