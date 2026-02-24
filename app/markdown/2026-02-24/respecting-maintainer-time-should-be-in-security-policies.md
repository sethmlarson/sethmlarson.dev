# Respecting maintainer time should be in security policies

Generative AI tools becoming more common means that vulnerability reports
these days are *loooong*. If you're an open source maintainer, you
unfortunately know what I'm talking about. Markdown-formatted, more than five headings,
similar in length to a blog post, and characterized as a
vulnerability worthy of its own domain name.

This makes triaging vulnerabilities by often under-resourced
maintainer more difficult, time-consuming, and stressful.
Whether a report is a genuine vulnerability or not, it now
requires more time from maintainers to make a determination
than is necessary. I've heard from multiple maintainers how specifically
*report length* weighs negatively on maintainer time, whether these are
“[slop vulnerability reports](https://sethmlarson.dev/slop-security-reports)” or just overly-thorough reporters.

<!-- more -->

[David Lord](https://davidism.com/), the maintainer of Flask and Pallets, captures this problem concisely,
**that the best security reports respect maintainer time**:

<center>
<blockquote class="mastodon-embed" data-embed-url="https://mas.to/@davidism/116122805055218394/embed" style="background: #FCF8FF; border-radius: 8px; border: 1px solid #C9C4DA; margin: 0; max-width: 540px; min-width: 270px; overflow: hidden; padding: 0;"> <a href="https://mas.to/@davidism/116122805055218394" target="_blank" style="align-items: center; color: #1C1A25; display: flex; flex-direction: column; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Roboto, sans-serif; font-size: 14px; justify-content: center; letter-spacing: 0.25px; line-height: 20px; padding: 24px; text-decoration: none;"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32" viewBox="0 0 79 75"><path d="M63 45.3v-20c0-4.1-1-7.3-3.2-9.7-2.1-2.4-5-3.7-8.5-3.7-4.1 0-7.2 1.6-9.3 4.7l-2 3.3-2-3.3c-2-3.1-5.1-4.7-9.2-4.7-3.5 0-6.4 1.3-8.6 3.7-2.1 2.4-3.1 5.6-3.1 9.7v20h8V25.9c0-4.1 1.7-6.2 5.2-6.2 3.8 0 5.8 2.5 5.8 7.4V37.7H44V27.1c0-4.9 1.9-7.4 5.8-7.4 3.5 0 5.2 2.1 5.2 6.2V45.3h8ZM74.7 16.6c.6 6 .1 15.7.1 17.3 0 .5-.1 4.8-.1 5.3-.7 11.5-8 16-15.6 17.5-.1 0-.2 0-.3 0-4.9 1-10 1.2-14.9 1.4-1.2 0-2.4 0-3.6 0-4.8 0-9.7-.6-14.4-1.7-.1 0-.1 0-.1 0s-.1 0-.1 0 0 .1 0 .1 0 0 0 0c.1 1.6.4 3.1 1 4.5.6 1.7 2.9 5.7 11.4 5.7 5 0 9.9-.6 14.8-1.7 0 0 0 0 0 0 .1 0 .1 0 .1 0 0 .1 0 .1 0 .1.1 0 .1 0 .1.1v5.6s0 .1-.1.1c0 0 0 0 0 .1-1.6 1.1-3.7 1.7-5.6 2.3-.8.3-1.6.5-2.4.7-7.5 1.7-15.4 1.3-22.7-1.2-6.8-2.4-13.8-8.2-15.5-15.2-.9-3.8-1.6-7.6-1.9-11.5-.6-5.8-.6-11.7-.8-17.5C3.9 24.5 4 20 4.9 16 6.7 7.9 14.1 2.2 22.3 1c1.4-.2 4.1-1 16.5-1h.1C51.4 0 56.7.8 58.1 1c8.4 1.2 15.5 7.5 16.6 15.6Z" fill="currentColor"/></svg> <div style="color: #787588; margin-top: 16px;">Post by @davidism@mas.to</div> <div style="font-weight: 500;">View on Mastodon</div> </a> </blockquote> <script data-allowed-prefixes="https://mas.to/" async src="https://mas.to/embed.js"></script>
</center>

Here's my proposal: require security reports respect maintainer time
in your security policy. This especially applies to “initial” security reports,
where the reporter is most likely to send disproportionately more information
than is needed to make an initial determination.

The best part about this framing is you don't have to mention the elephant in
the room. Here's a few example security policy requirements to include:

* Initial reports must be six or fewer sentences describing the issue
  and optionally a short proof-of-concept script. Follow-ups may be longer
  if the initial report is deemed a vulnerability.
* Initial reports must not contain a severity (such as: "critical") or CVSS score. This calculation
  will be completed after the report is accepted by maintainers.
* Reports must not make a determination whether a behavior of the software
  represents a vulnerability.

Notice I didn't even have to mention LLMs or generative AI, so there’s
no ambiguity about whether a given report follows the policy or not.
While you have reporters reading your security policy, you might also add suggestions that also benefit
maintainers remediating vulnerabilities faster:

* If applicable, submitting a patch or an expected behavior along with a
  proof-of-concept makes remediating a vulnerability easier.
* We appreciate vulnerability reporters that are willing to review
  patches prior to publication.
* If you would like to be credited as a reporter, please mention that in your
  report.

After this is added to a project security policy (preferably under its own linkable heading)
then any security report that doesn't respect maintainer time
can be punted back to the reporter with a canned response:

> Your report doesn't meet our security policy: https://...
> Please amend your report to meet our policy so we may efficiently
> make a determination and remediation. Thank you!

Now your expectations have been made clear to reporters and valuable maintainer
time is saved. From here the security report can evolve more like
a dialogue which requires maintainer time and energy **proportionate
to the value that the report represents to the project**.

I understand this runs counter to how many vulnerability teams work today.
Many reporters opt to provide as much context and detail up-front in a single report,
likely to reduce back-and-forth or push-back from projects.
If teams reporting vulnerabilities to open source projects
want to be the most effective, they should meet the pace and style
that best suites the project they are reporting to.

Please note that *many* vulnerability reporters are
acting in good faith and aren't trying to burden maintainers. If you believe
your peer is acting in good faith, maybe give them a pass if the report doesn't
*strictly* meet the requirements and save the canned response for the bigger offenders.

Have any thoughts about this topic? Have you seen this in any open source security policies already? [Let me know](mailto:sethmichaellarson@gmail.com)! Thanks to [OSTIF](https://ostif.org) founder Derek Zimmer for reviewing this blog post
prior to publication.
