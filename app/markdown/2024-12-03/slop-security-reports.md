# New era of slop security reports for open source

I'm on the security report triage team for CPython, pip, urllib3, Requests, and a handful of other open source projects.
I'm also in a trusted position such that I get "tagged in" to other open source projects
to help others when they need help with security.

Recently I've noticed an uptick in extremely low-quality, spammy, and LLM-hallucinated security reports to open source projects.
The issue is in the age of LLMs, these reports appear at first-glance to be potentially legitimate
and thus require time to refute. Other projects such as curl [have reported similar findings](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/).

Some reporters will run a variety of security scanning
tools and open vulnerability reports based on the results seemingly without a moment of critical thinking.
For example, urllib3 recently received a report because a tool was detecting our usage of `SSLv2` as insecure
even though our usage is to [explicitly disable SSLv2](https://github.com/urllib3/urllib3/blob/main/src/urllib3/util/ssl_.py#L309).

This issue is tough to tackle because it's distributed across thousands of open source projects
and due to the security-sensitive nature of reports open source maintainers are
discouraged from sharing their experiences or asking for help. Sharing experiences
takes time and effort, something that is in short supply amongst maintainers.

## Responding to security reports is expensive

If this is happening to a handful of projects that I have visibility for, then I suspect that this
is happening on a large scale to open source projects. This is a very concerning trend.

Security is already a topic that is not aligned with
why many maintainers contribute their time to open source software,
instead seeing security as important to help protect their users.
It's critical as reporters to respect this often volunteered time.

Security reports that waste maintainers' time
result in confusion, stress, frustration, and to top it off a sense of isolation due to the secretive nature of security reports.
All of these feelings can add to burn-out of likely highly-trusted
contributors to open source projects.

In many ways, these low-quality reports should be treated as if they are malicious. Even if this is not their intent,
the outcome is maintainers that are burnt out and more averse to legitimate security work.

## What platforms can do

If you're a platform accepting vulnerability reports on behalf of open source projects, here
are things you can do:

* Add systems to prevent automated or abusive creation of security reports.
  Require reporters to solve CAPTCHAs or heavily rate-limit security report creation
  using automation.
* Allow a security report to be made public without publishing a vulnerability record. This would
  allow maintainers to "name-and-shame" offenders and better collaborate as a community how to
  fight back against low-quality reports. Today many of these reports aren't seen due to being private by default
  or when closed.
* Remove the public attribution of reporters that abuse the system, even removing previously credited
  reports in the case of abuse.
* Take away any positive incentive to reporting security issues, for example GitHub showing
  the number of GitHub Security Advisory "credits" a user appears on.
* Prevent or hamper newly registered users from reporting security issues.

## What reporters can do

If you're starting a new campaign of scanning open source projects
and reporting potential vulnerabilities upstream:

* **DO NOT** use AI / LLM systems for "detecting" vulnerabilities. These systems today cannot understand code,
  finding security vulnerabilities requires understanding code AND understanding human-level concepts like
  intent, common usage, and context.
* **DO NOT** run experiments on open source volunteers. My alma-mater the University of Minnesota
  [rightfully had its reputation thrown in the trash in 2021](https://cse.umn.edu/cs/linux-incident)
  over their experiment to knowingly socially deceive Linux maintainers.
* **DO NOT** submit reports that haven't been reviewed **BY A HUMAN**. This reviewing time should be paid first by you, not open source volunteers.
* **DO NOT** spam projects, open a handful of reports and then **WAIT**. You could run the script and open tons of reports
  all-at-once, but likely you have faults in your process that will cause mass-frustration at scale. Learn from early mistakes and feedback.
* Have someone with experience in open source maintenance **for the size of projects you are scanning**
  review your plan before you begin. If that person is not on your team, then pay them for their time and expertise.
* Show up with patches, not just reports. By providing patches this makes the work of maintainers much easier.

Doing all of the above will likely lead to better outcomes for everyone.

## What maintainers can do

Put the same amount of effort into responding as the reporter put into submitting a sloppy report: ie, near zero.
If you receive a report that you suspect is AI or LLM generated, reply with a short response and close the report:

> "I suspect this report is (AI-generated|incorrect|spam). Please respond with more justification for this report. See: https://sethmlarson.dev/slop-security-reports"

If you hear back at all then admit your mistake and you move on
with the security report. Maybe the reporter will fix their process and you'll have helped other
open source maintainers along the way to helping yourself.

If you don't hear back: great, you saved time and can get back to
actually useful work.

Here are some questions to ask of a security report and reporter:

* If you aren't sure: ask for help! Is there someone I trust in my community that
  I can ask for another look. **You are not alone, there are many people around
  that are willing to help**. For Python open source projects you can ask for help
  from me if needed.

* Does the reporter will have a new account, no public identity,
  or multiple "credited" security reports of low quality? There are sometimes
  legitimate reasons to want anonymity, but I've seen this commonly on very
  low-stakes vulnerability reports.

* Is the vulnerability in the proof-of-concept code or the project itself?
  Oftentimes the proof-of-concept code will be using the project insecurely
  and thus the vulnerability is in the proof-of-concept code, not your code.

## Most vulnerability reporters are acting in good faith

I wanted to end this article with a note that many vulnerability reporters are
acting in good faith and are submitting high quality reports. Please keep in mind
that vulnerability reporters are humans: not perfect and trying their best
to make the world a better place.

Unfortunately, an increasing majority of reports are of low quality and are ruining the
experience for others. I hope we're able to fix this issue before it gets out of hand.
