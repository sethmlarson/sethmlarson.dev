# PyCon US 2024 as Security Developer-in-Residence

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

This was my first PyCon US as the Security Developer-in-Residence. I accepted the offer shortly after PyCon US 2023, where Deb Nicholson
provided an exciting cliffhanger that the PSF was [close to making a hiring decision](https://youtu.be/NZhHFDbul8g?si=NnoacwZ0orYnVGNc&t=792) for the role
during the PSF update.

The timing of my hiring to coincide with PyCon US is quite the unique opportunity, it means I get to share all the
things we've been able to accomplish together in the past year all-together in person. This also
means I get to share the road ahead and learn from many people I don't get to see
on a day-to-day, like maintainers of projects large and small, software users at organizations and companies,
and users whose work extends beyond software like scientists and industrial control systems operators.

<div class="row">
<div class="col-9">
<p>Overall I think this yearly cadence couldn't be better, I'm already looking forward
to what I'll be able to share at PyCon US 2025 back in Pittsburgh. As I've said in the past, this role wouldn't be effective
without the support of the community, so I want to thank you all for the parts you've played in me being successful.</p>
</div>
<div class="col-3">
<img src="https://storage.googleapis.com/sethmlarson-dev-static-assets/knightsnake.png" style="max-width: 100%;">
</div>
</div>

## State of Python Supply Chain Security with Alpha Omega

<p><a href="https://alpha-omega.dev/">Alpha Omega</a> is a sponsor of the Python Software Foundation, specifically for my role!
Alpha Omega's goal is to "improve global software supply chain security by partnering with open source". I presented
alongside Alpha Omega's co-founder Michael Winser. The slides for our presentation are <a href="https://storage.googleapis.com/sethmlarson-dev-static-assets/PyConUS2024-State-of-Python-Supply-Chain-Security.pdf">available online</a>.</p>


<div class="row">
<div class="col-6">
<p>Alpha Omega uses a two-pronged approach, and it's right there in the name: Alpha and Omega:</p>

<ul>
<li><strong>Alpha</strong>: Improve the security posture of the most critical projects through staffing.</li>
<li><strong>Omega</strong>: Automated security analysis, metrics, and remediation for wider range of projects.</li>
</ul>

<p>
My role is full-time staffing, so is in the "Alpha" bucket of funding.
</p>

</div>
<div class="col-6">
<center>
<p><img style="max-width: 100%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/pyconus2024-alpha-omega.jpg"/>
<br><small><i>Speaking for Alpha Omega on the state of Python supply chain security</i></small></p>
</center>
</div>
</div>

For readers of my blog, lots of the content of the presentation is review, but I went over the following accomplishments for the first year of the role:

* Python Software Foundation as a CVE Numbering Authority (and how we helped Linux, curl, and others with a guide).
* Joining Python Security Response Team and working on process
* Working with Python release managers to move the release process to GitHub Actions as an isolated build environment.
* Build reproducibility for the Python release process.
* Software Bill-of-Materials for Python release artifacts.
* Coordinated cross-ecosystem response to libwebp and xz-utils vulnerabilities.
* Tons of community work: PEP reviewer, talks, blogs, and more.

The more interesting part for existing readers is my plans for next year. My plan is to partially shift focus, continue working
with Python core developer team of course, but to start making improvements to the wider community of projects
using Python as well:

* Enabling Build Provenance and Software Bill-of-Materials for Python packages.
* Adoption of security features, hardening, and best practices for Python packages.
* Special focus on Python packaging tools and workflows.

I finished the talk by describing the unique nature of this role as being flexible
and how that's a boon for the rapidly changing space of software supply chain security.
This role has a fairly wide scoping, which means that when things come up (like xz-utils
and novel social-engineering techniques) it's in this role's scope to think about how to
respond for the Python ecosystem.

## “Vuln Together”, an open space on vulnerability management

<div class="row">
<div class="col-6">
<p><em>“Got vulns? Let's talk!”</em> -- I co-hosted this open space with GitHub Security champion and CVE board member <a href="https://github.com/taladrane">Madison Oliver</a>.
This open space focused on the soft-side of vulnerability management for open source projects: people!</p>

<p>Managing vulnerabilities for open source projects is a non-trivial and effort intensive process, because maintainers need to create and publish a security policy,
accept private vulnerability reports, and then know what reporters need, request a CVE ID, know how to estimate severity
and write an advisory text, and then how to publish an advisory alongside fixed versions. Phew!</p>

</div>
<div class="col-6">
<p>
<center>
<img style="max-width: 100%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/pyconus2024-vuln-together.jpg"/>
<br><small><i>Madison and I pictured holding the open space card for “Vuln Together”</i></small>
</p>
</center>
</div>
</div>

<div class="row">
<div class="col-6">
<p>The open space was a forum to discuss difficulties with managing vulnerabilities, answering questions, and pointing folks at resources. We shared recommendations like how maintainers can <a href="https://docs.github.com/en/code-security/security-advisories/working-with-repository-security-advisories/publishing-a-repository-security-advisory">easily request CVEs from GitHub</a>,
enable <a href="https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability">Private Vulnerability Reporting on GitHub</a> and <a href="https://docs.gitlab.com/ee/user/project/issues/confidential_issues.html">Confidential Issues on GitLab</a>
to make reporting easier, and showed resources like the <a href="https://github.com/ossf/oss-vulnerability-guide/blob/main/maintainer-guide.md">Guide for Vulnerability Disclosure Process</a>
from the OpenSSF Vulnerability Disclosures working group.</p>
</div>
<div class="col-6">
<p>
<center>
<img style="max-width: 100%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/pyconus2024-vuln-together-crowd.jpg"/>
<br><small><i>The open space was well attended!</i></small>
</center>
</p>
</div>
</div>

## Language Summit discussion on CPython security

My bingo space for "xz" was almost immediately filled at PyCon US when I attended the [Python Language Summit](https://us.pycon.org/2024/events/language-summit/) as the blogger.
Release manager and core developer Pablo Galindo Salgado spoke about the Python contribution security model in "the wake of xz-utils backdoor".

The complete language summit blog posts are [coming soon to the Python Software Foundation blog](https://pyfound.blogspot.com/) (I should know, I authored them!)
so if you're interested in this topic you can stay tuned over there. I won't spoil any of the contents of the blog post here, but it was a great discussion all around.
Lots of interesting ideas and thoughts from core developers that'll with figuring process improvements that work for CPython.

## Meeting all the people

Mike Fiedler and I were on the stage briefly after Kate Chapman's keynote for a "[Meet the Python Software Foundation Security Engineers](https://storage.googleapis.com/sethmlarson-dev-static-assets/PSF-Meet-our-Security-Engineers.pdf)"
segment where we went over our plans for the upcoming year and recommended folks to follow the [PSF](https://pyfound.blogspot.com/) and [PyPI blogs](https://blog.pypi.org/) for future updates.

Of course, I got to talk to so many people, too many to name individually. I chatted with the upcoming Release Manager for CPython, Hugo van Kemenade, on some ideas to further improve the CPython
release process, specifically around signatures. I chatted with folks from specific sub-ecosystems like Jannis Leidel from Conda and Jazzband, David Lord from Flask, and Jarek Potiuk from Airflow.

Also I handed out stickers! I went through over a hundred, it brought me a lot of joy seeing how much folks liked the derpy snake knight design.

## ... and beyond!

PyCon US 2024 is the start of conferences this year for me.
Shortly after PyCon US it was announced that [I will be keynoting](https://x.com/PyConTW/status/1793884640379335026) [PyCon Taiwan](https://tw.pycon.org/2024/en-us) in September and also speaking at [All Things Open 2024](https://2024.allthingsopen.org/) in Raleigh, North Carolina.
If you're attending either of these events get in contact with me (and I promise to bring stickers).

That's all for this post! 👋 If you're interested in more you can read [the previous report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-35).
