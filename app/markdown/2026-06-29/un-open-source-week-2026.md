# United Nations Open Source Week 2026

I was [among the delegation](https://www.sovereign.tech/news/un-open-source-week-2026-maintainer-delegation) of “open source
experts” invited to the [UN Open Source Week 2026](https://www.unopensource.org/)
in New York City by the Sovereign Tech Agency.
Thank you to the [Sovereign Tech Agency](https://www.sovereign.tech/) for
inviting and supporting my stay and travel for the event.
Thanks to [Alpha-Omega](https://alpha-omega.dev) for sponsoring my position at the
Python Software Foundation.

UN Open Source Week is a week-long event with a different focus
for each day. In order, the focuses were: Maintain-a-thon (UN Tech Over), Open Source × AI,
Digital Public Infrastructure Day, OSPOs for Good, and Community Day.
The event is structured into a series of presentations, panels,
parallel sessions, interactive break-outs that start in the morning
and carry on through into the evening at local partnered events.

<!-- more -->

## Themes

After speaking with many folks and attending a week of sessions,
there were themes that carried through the entirety of the event:

* Power, resources, and talent around LLM technologies are currently concentrated into the control
and geographical borders of few. Many countries and organizations are
struggling with access to these technologies.
A substantial portion of the answer is Open Source software and models of various definitions, but
compute and talent are more difficult problems. Better efficiencies, distributed training
and inference, sharing compute resources, and programs to transfer
skills to other communities were among discussed solutions.
* LLMs are changing many of the social norms for
Open Source participation which disrupts processes that have
been in place for decades. Upstream and downstream processes
will need to be developed to handle these changes.
* There were acknowledgements that many people were on edge or scared, that the
metaphorical “tomorrow” was less clear to see than it was
a few years ago. 

There was also plenty of hope in the sessions, too. Similar to last year,
I left feeling that Open Source was a critical component for overcoming
the challenges ahead and that organizations around the world knew this
acutely.

Multiple speakers asked those involved with Open Source projects
to see how their projects aligned with the [17 Sustainable Development Goals](https://sdgs.un.org/goals),
including quality education, clean energy, industry and infrastructure, and
many more. Having done this exercise, I highly recommend others do so, too.

## Maintain-a-thon 2.0

The Sovereign Tech Agency was the partner hosting the
second “[Maintain-a-thon](https://www.sovereign.tech/news/maintain-a-thon-2026)” as a part of the first day
of UN Open Source Week. This year the day was split into
two parallel tracks: “Technical Maintenance” and “Capacity & Stewardship”.

<center>
<img style="border: 2px black solid; max-width: 100%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_5454.JPG">
<br><small><em>Giving context for LLMs and vulnerability reports for the Python programming language.</em></small>
</center>

[Mirko Swillus](https://www.linkedin.com/in/mirko-swillus/) and I hosted a session in the Technical Maintenance track
titled “The Vulnerability Flood: Open Source Security in the Age of LLMs”.
The session would discuss how LLMs were affecting vulnerability handling
and security teams and how we might better plan for potential futures.
We began the session by setting context around how
LLMs were already changing security, such as:

* publicly available models are able to discover vulnerabilities.
* LLMs can detect whether patches are security-relevant, regardless
  of whether an advisory is published (embargoes are less useful).
* time-to-exploit for vulnerabilities is decreasing.
* “AI slop” vulnerability reports and how in recent months quality has improved.
* how projects like the Python programming language are thinking today about
  “steering” these LLM-assisted contributions in a positive direction through
  security policies and threat models.

The session proceeded into an interactive exercise to draw potential topics for deeper small-group
discussions from participants using sticky notes. The three topic-clusters ended up being
“People”, “Process”, and unsurprisingly “AI”.

The “People” group
discussed offering mental health programs for Open Source maintainers
to better handle stress, burnout, and succession planning and highlighted
the difficulties in defining what it even means to be a maintainer in terms
of a “job description”.

The “AI” group discussed the critical junction for handling unmaintained software
in a world of agents and faster time-to-exploits, focusing on the question: “Fix or rewrite?”.
Clearly rewrites should be a last-resort and are fraught with challenges, such
as introducing more bugs and security issues due to a large volume of new code.
The group highlighted challenges and potential solutions around LLM use for
Open Source projects in handling the flood of security reports.

The “Process” group discussed the weakening value of secrecy when it comes to
vulnerability reports discovered using LLMs. Historically secrecy was kept to
protect users, but if public models are able to find issues then who does
this aspect of coordinated-vulnerability disclosure actually help? (Attackers).
The Linux kernel is already experimenting with having less secrecy involved in vulnerability
handling. 

<blockquote>
<details>
<summary>Notes from the AI group</summary>

Small python dep that keeps getting reports, is there a point where it should get rebuilt (with AI), rewrite it in rust for memory safety, identify the jenga block

Is it so bad that it needs a complete overhaul, how is the architecture? (pre-ai assumption)

Programme Bench (ai benchmark, does an ai rewrite something reliably)

Depends on the size of the project, often 90% isn’t used

What happens when there are no maintainers?

Is the project well maintained enough? Does it have governance model that lets ai take over?

We’ve seen ai rewrites that also change licenses at the same time

When you make something from the ground up you learn it better, if you take something over, learning all the edge cases can be more work that rewriting from scratch.

In any case, whoever takes over, new maintainers have to learn the edge cases and understanding.

You could feed all git history into a model to ensure it learns all the failures and fixes over time.

If we believe that AI is good enough to do an AI rewrite properly

Rewrites are hard, introduces more problems that were there anymore

Project moved in a direction from paid hosted models to free self hosted models, dealing with resource constraints. Easier to pitch AI projects from an ethics POV if it’s using self-hosted “open source” ai models. Feels better and better perceived about using “open source” models, but worried about how it scales.

Choosing to engage with AI can cross red lines with committers and users that causes lots of issues.

Pitching OSS projects as “AI powered” often upsets users.

Getting users past “it has AI in the name”

Resource constraints can make it needed to use AI because there are no people and no funding, locally run ai powered approaches come across more reasonably.

Humanitarian sectors are slow to adopt this technology and generally slower moving in general.

Airflow - Big open source projects - big number of incoming requests, hard to tell if incoming is human or agents. Processing issue trackers using AIs, ensuring things are triage and keeping them up to date.

More process == more overhead. Having experienced developers looking at the triage process rather than the initial untrusted issues.

Reducing the friction of adoption of AI - generation vs assistive

Calling “ai” things - Machine learning to be clear if it’s generative llms.

Can fix faster be useful for accessibility of using software where there user previously never had any software experience

</details>
</blockquote>

<blockquote>
<details>
<summary>Notes from the People group</summary>

Mental Health Programme for FOSS Maintainers

How do we create awareness, so that people sign up for this? 

Outspoken and explicit “Job Descriptions” for single maintainers

so that is easier to understand which functions can be trained and educated
Clear path for becoming a mentor 

Sunsetting Projects 

Support structures for sunsetting projects & find replacements 

Ment or Students

Learn from best practices (french DINUM, 2-3 years)

</details>
</blockquote>

## Open Source × AI Day Reception

At the reception for Open Source × AI Day there was an additional
panel session focusing on LLMs and security. One of the most interesting
talking points of this panel was the restrictions being placed on “Frontier”
models with cybersecurity capabilities. Earlier in the week, GLM-5.2,
an open weights model had been released and folks already had begun testing
the model’s cybersecurity capabilities and found them to be
already quite capable.

The panel noted how open weights models appear to be fast-following “Frontier”
capabilities with a delay between 6-12 months, implying that we may not
need to wait long for an open weights model with Mythos-like capabilities
to become available. This is based on speculation, but there are many implications for 
this are... interesting, to put it lightly. :)
