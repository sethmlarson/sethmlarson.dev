# CPython release automation, more Windows SBOMs 

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

## CPython source and docs builds are automated in GitHub Actions

While I was away on vacation, the CPython Developer-in-Residence Łukasz was able to dry-run, review, and merge
[my pull request](https://github.com/python/release-tools/pull/71)
to automate source and docs builds in GitHub Actions on
the [python/release-tools](https://github.com/python/release-tools) repository.

The automation was successfully used for the CPython [3.10.14](https://github.com/python/release-tools/actions/runs/8519755747), [3.11.9](https://github.com/python/release-tools/actions/runs/8350750234), [3.12.3](https://github.com/python/release-tools/actions/runs/8612609594), and [3.13.0a6](https://github.com/python/release-tools/actions/runs/8613852167).

This work being merged is exciting because it isolates the CPython
source and docs builds from individual release manager machines preventing those source
tarballs from being unintentionally modified. Having builds automated is a pre-requisite for
future improvements to the CPython release process, like adding automated uploads to python.org
or machine/workflow identities for Sigstore. I also expect the macOS
installer release process to be automated on GitHub Actions. Windows artifact builds are already using Azure Pipelines.

Release Managers have [requested the process be further automated](https://github.com/python/release-tools/issues/108)
which is definitely possible, especially for gathering the built release artifacts
and running the test suite locally.

### Windows Software Bill-of-Materials coming for next CPython releases

I've been collaborating with **Steve Dower** to get SBOM documents generated
for Windows Python artifacts. Challenges of developing new CI workflows aside
we now have SBOM artifacts [generating as expected](https://github.com/python/release-tools/pull/100#issuecomment-2046130399).
Next step is to automate the upload of the SBOM documents to python.org so they've
automatically available to users.

During the development of Windows SBOMs I also [noticed our CPE identifier for xz
was incorrect](https://github.com/python/cpython/pull/117656) partially due to difficulties
using the CPE Dictionary search (they only allow 3+ character queries!) This issue doesn't
impact any existing published SBOM since xz-utils is only bundled with Windows artifacts, not source artifacts.

## Thoughts on xz-utils

I've been a part of many discussions about xz-utils, both active and passive,
there are many thoughts percolating around our community right now. To capture
where I'm at with many of these discussions I wanted to write down my own thoughts:

* "Insider threats" and other attacks on trust are not unique to open source software.
  We don't get to talk about other incidents as often because the attack isn't done in the open.
* Insider threats are notoriously difficult to defend against **even with ample resources**.
  Volunteer maintainers shouldn't be expected to defend against patient and well-resourced attackers alone.
* Multiple ecosystems took action immediately, [including Python](https://discuss.python.org/t/cpython-pypi-and-many-python-packages-are-not-affected-by-the-backdoor-of-xz/49873),
  to either remove compromised versions of xz or confirm they were not using affected versions.
  This sort of immediate response should only be *expected* with full-time staffing (**thanks Alpha-Omega**!), but I know that volunteers were involved in the broader response to xz.
* Many folks, myself included, have remarked that this could have just as easily been them.
  Reviewing the "Jia Tan" commits I can't say with certainty that I would have caught them
  in code review, especially coming from a long-time co-maintainer.

How has the nature of open source affected the response to this event?

* Security experts were able to review source code, commits, conversations,
  and the accounts involved immediately. We went from the public disclosure and alerts to having a timeline
  of how the malicious account was able to gain trust within a few hours.
* We get to learn how the attack transpired in detail to hopefully improve in the future.

Things to keep in mind when working on solutions:

* Blaming open source software or maintainers is rarely the answer, and it definitely isn't the answer here.
* There isn't a single solution to this problem. We need both social and technical approaches, not exclusively one or the other.
  Instead of pointing out how certain solutions or ways of supporting OSS "*wouldn't have thwarted
  this exact attack*", let's focus on how the sum of contributions and support are
  making attacks on open source more difficult in general.
* We need better visibility into critical languishing projects. xz likely wasn't on anyone's list of critical projects before this event (when it should have been!) 
  It isn't sustainable to figure out which projects are on critical and need help
  by waiting for the next newsworthy attack or vulnerability.

I also reflected on how my own work is contributing to one of many solutions to problems like this.
I've been focusing on reproducible builds, hardening of the CPython release process, and have been
working closely with Release Managers to improve their processes.

As I mentioned above, being full-time staff means I can respond quickly to events in the community.
The ["all-clear" message](https://discuss.python.org/t/cpython-pypi-and-many-python-packages-are-not-affected-by-the-backdoor-of-xz/49873) for CPython, PyPI, and all Python packages was given a few hours after xz-utils
backdoor was disclosed to the Python Security Response Team.

I've also been working on Software Bill-of-Materials documents. These documents would not have done anything
to stop an attack similar to this, but would have helped users of CPython detect if they were using a vulnerable
component if the attack affected CPython.

## Other items

* I'm attending [SOSS Community Day](https://events.linuxfoundation.org/soss-community-day-north-america/) and [OSS Summit NA](https://events.linuxfoundation.org/open-source-summit-north-america/) in Seattle April 15th to 19th. If you're there
  and want to chat reach out to me! I spent time this week preparing to speak at SOSS Community Day.
* Added support for Python 3.13 to Truststore.
* Triaged reports to the Python Security Response Team.

That's all for this week! 👋 If you're interested in more you can read [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-32).
