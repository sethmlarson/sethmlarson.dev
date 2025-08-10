# Open Source Security work isn't “Special”

> I gave this [keynote](https://openssfcdna2025.sched.com/event/1zolR/keynote-security-work-isnt-special-seth-larson-security-developer-in-residence-python-software-foundation) at OpenSSF Community Day NA 2025 in Denver, Colorado.
> There is a recording published on [YouTube](https://www.youtube.com/watch?v=V9n2jmkeRf0).
> This talk was given as the [Security-Developer-in-Residence](https://www.python.org/psf/developersinresidence/) at the Python Software Foundation,
> a role which is sponsored by [Alpha-Omega](https://alpha-omega.dev). Thanks to Alpha-Omega for supporting security in the Python ecosystem.

<!-- more -->

To understand why security is special, we have to take a look at why open source is an amazing thing.
For many components of open source, users that have the time, desire, and expertise are able to contribute meaningfully to projects.
As a maintainer of an open source project, *this is awesome!*

<!-- more -->

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-17-21.png"/></center>

Users and contributors can work on the areas they are interested in, like triaging bug reports, engaging with the community, or writing great docs.
For smaller open source projects this is especially important, there’s only one or a few maintainers and they can’t do it all on their own sustainably.

But not for security, right? Security is *special*.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-17-28.png"/></center>

Only a select few are supposed to be able to handle vulnerability reports, configure the repository and package manager settings, and secure the release process.
This tight association between security work and maintainers is what I’d like to try to pull apart today.

Maintainers, especially for smaller projects, are almost always experts in the *domain of the project*, not necessarily in *security*.
But the expectations of open source projects means that maintainers feel compelled to do this work to keep their project and users safe.

And those expectations for security today, that **security work is done by few rather than many**, combined with the secretive nature of security work means that maintainers often feel isolated.

Maintainers don’t see how other projects are triaging vulnerabilities and can’t learn from each other. They can’t compare notes on what they are seeing and whether they are doing the right thing.
Isolation in security work breeds a culture of fear. Fear of doing the wrong thing and making your users unsafe.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-17-34.png"/></center>

This private conversation was published with permission from Marcelo, maintainer of [Starlette](https://github.com/encode/starlette), a popular Python library that powers FastAPI.

He was seeing security reports that seemed convincing but they were also confusing. He asked for my help and together we determined the reports were generated with an LLM and were meaningless. I later published an article about “[slop security reports](https://sethmlarson.dev/slop-security-reports)” that other projects were seeing too, including curl, Python, Django, and others. But none of us would know what the others were seeing without sharing.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-17-40.png"/></center>

Smaller projects are shaped by their tools, not the other way around.
Small projects don’t have the time and resources to make a square peg fit into a circular hole when it comes to any type of tooling, including security.
They don’t have time to create bots and wrappers and bend these tools to work for them, like many larger projects do.

This means that whatever is available or the default experience is probably what they work with, and often our tools encode the assumption that “only maintainers do security work”.

Of the top 10,000 open source packages with GitHub repositories identified by [Ecosystems dataset](https://ecosyste.ms/), 35% are owned by a GitHub user, not a GitHub organization.
This has huge implications for what features are available to those projects and who is able to do security work at all.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-17-46.png"/></center>

Security tools and vulnerability reports often introduce an asymmetry by creating work to do without resolving the issues identified.
Fixing security issues while weighing user expectations, performance, and backwards compatibility is a tough job.
This is the reason maintainers are often hesitant to adopt security scanners and tools, because adoption is easy but being on the hook to triage the findings forever is hard.

If a bunch of your limited time with a project is spent doing work that isn’t aligned with your interests in the project, this can lead to burnout which only makes the problem worse.

This image is from the changelog of [libexpat](https://libexpat.github.io) which states that the project is understaffed and without funding and is in need of help responding to findings from fuzzing the project within the standard 90 day grace period.

So what can we all do to make security work less “special” and more like other open source contributions?

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_2325.JPG"/></center>

I propose a new model for open source security contributions, where security work is completed by trusted individuals that aren’t necessarily maintainers on behalf of projects.
This model break the assumption that maintainers are the only ones that can do security work, especially for smaller projects.

These “security contributors” could be maintainers or contributors of other open source projects that know about security, they could be foundations offering up resources to their ecosystem, or engineers at companies helping their dependency graph.

Even if you’re not contributing security work directly to an open source project, I think there’s reframing, re-engineering, and rethinking work that we can all do to make this model successful.

Now I know what you might be thinking: “What about XZ?”
XZ often comes up during conversations involving trust in contributors to open source projects, but I’m not convinced it’s the show-stopper it’s often portrayed as.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-18-34.png"/></center>

The technologies to discover the backdoor trigger of XZ already exist but had not yet been adopted by the project, such as reproducible builds, build provenance, capability analysis, or using a canonical URL to download source code.

Malicious contributors have always been a problem for open source and the solution can’t be that we just stop trusting each other or accepting help from our community.
We lose something bigger than the XZ-utils backdoor if we let this incident define how open source security works going forward.

We have to be able to build trust amongst contributors and projects and security work can’t all fall on maintainers.
If we want *open source sustainability* then we cannot let XZ-utils define open source security.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-18-25.png"/></center>

So what can we all do to nurture this more sustainable model of open source security contribution?

We can all use our voices and experiences to build a more positive and healthy security culture and overcome the isolation inherent to security work.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-18-40.png"/></center>

Sharing and encouraging the sharing experiences shows others that they’re not the only ones that think this is difficult.
Seeing others sharing experiences shows that it’s okay to ask for help and to not be perfect, instead the focus should be on always improving.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-18-46.png"/></center>

If you’re a public contributor to open source security, making yourself visible and approachable is a great way to begin building trust in the communities you participate in.
Conferences and in-person meetups are excellent venues for promoting positive security culture and building trust amongst a community.

There is something about being in-person that really let’s people be vulnerable and talk honestly about what they are experiencing and their problems which sometimes is exactly what we need to hear.
When I’m at conferences I also like to offer up 1-on-1 time to discuss security issues with maintainers or help them adopt new security features.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-18-51.png"/></center>

TLS and public key infrastructure scale trust of the internet and web, we need more technologies that scale trust in open source contributions.

We should continue contributing to and adopting technologies that enable trust for open source projects and contributions.
This is especially meaningful when the technology is added to existing tooling like package managers and build tools.
Technologies like build reproducibility, build provenance, and capability analysis can all minimize the risk from adding more privileged contributors.

<center><img style="max-width: 70%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/Screenshot%20from%202025-07-02%2015-19-03.png"/></center>

We  need platforms and tools to update their underlying assumptions about who does security work for projects to support this new open source security contribution model.

Separating maintenance responsibilities and security work is beneficial for users wanting to help projects, too.
If we assume that the securing and maintaining are linked, then it becomes a more difficult task to be able to offer help to open source projects.
Some projects do not have the governance in place to transition from one to many maintainers. Some maintainers want to continue owning the project roadmap and vision.

Getting your manager on-board with you maintaining a project is a difficult and amorphous ask compared to more tightly defined “security work” for an open source dependency your team uses.
Open Source Program Offices (OSPOs) could use this model to concretely show how they are benefiting their whole open source supply-chain, and not only the larger projects that are able to receive grant funding.

I don’t think this change happens overnight, but we need to think about where we might go.
From my experience working in open source, security work isn’t the special sauce, it’s always trust.

Whether you’re an open source user, a contributor to OpenSSF or other security working groups, or a developer of tools for open source projects, I hope I’ve inspired you that we need to think beyond current models of how security work is done for open source projects to achieve sustainable open source security.
