# Preparing for the wave of open source funding

<div class="row">
<div class="col-6">

<p>During PyCon US 2022 Dustin Ingram <a href="https://www.youtube.com/watch?v=i1QqhGsbX6Y">delivered an incredible talk</a> about securing the open source supply chain. This quote from Dustin's talk is addressing maintainers of projects in Python's supply chain like PyPI and pip:</p>

<p><blockquote>“<strong>Brace for interest and funding</strong> —<br><br>I hope you can ride that wave, make the most of it, and invest in your project.”</blockquote></p>

<p>In my opinion we are seeing the start of a similar wave of interest and funding for open source project maintainers.</p>

<p><strong>How can open source projects prepare for the wave?</strong></p>

</div>
<div class="col-6">

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0a/The_Great_Wave_off_Kanagawa.jpg" style="width: 100%; max-width: 100%; border-radius: 16px"/>
<center><small><a href="https://commons.wikimedia.org/wiki/File:The_Great_Wave_off_Kanagawa.jpg">After Katsushika Hokusai</a>, Public domain, via Wikimedia Commons</small></center>
</div>
</div>

### What can we learn from open source funds?

Taking a look at [Spotify's recent FOSS fund](https://engineering.atspotify.com/2022/06/say-hello-to-the-recipients-of-the-2022-spotify-foss-fund/), [Sentry's FOSS Fund 155](https://blog.sentry.io/2021/10/21/we-just-gave-154-999-dollars-and-89-cents-to-open-source-maintainers), and [Indeed's FOSS contributor fund](https://engineering.indeedblog.com/blog/2019/07/foss-fund-six-months-in/) we can see some hints about things that are important to organizations looking to support their open source dependencies. Projects were nominated to be funded from two sources:

- Developers nominating projects
- Dependency data across repositories

This means projects are being "discovered" in two ways: by humans and by machines. It's important to cater to both parties.

Looking at eligibility requirements we can see the following:

- **Project must be actively maintained**
- **Project must benefit meaningfully from financial support**
- **Project must have some mechanism for receiving funds**
- **Project must use an OSI-approved license**
- Project must be independently run (not by another company)
- Project must not run by someone employed by the company

I've highlighted the criteria that are most likely to be relevant to maintainers that are reading this article looking for funding.

### What can be learned from urllib3?

Over the time I've been lead maintainer starting in 2019 the [urllib3 project](https://urllib3.readthedocs.io) has raised **over $60,000 USD** to pay our maintainers and [contributors](https://sethmlarson.dev/blog/get-paid-to-contribute-to-urllib3). In addition to analysis of FOSS funds I'm also sharing what has worked for urllib3 over this time period.

We likely benefit from being one of the most downloaded Python packages, but there are many other widely used projects that aren't receiving their share of financial support.

## Making your project fundable

I've listed the sections below in order of priority if your end goal is to be sponsored by organizations or companies. Not all sections will be relevant for all projects, pick and choose what makes sense for you!

### Licensing

Companies are likely already excluding packages that don't use an [OSI-approved license](https://opensource.org/licenses/alphabetical) so if you're looking for corporate sponsors for your project it's likely a non-starter to not use an OSI-approved license. Some common licenses that aren't on this list are CC0, Unlicense, and SSPL.

You should also favor using a common OSI-approved license over an uncommon license for easier approval by tools unless you have a specific use-case. Common license choices include Apache-2.0, MIT, LGPL, and GPL. I always refer to [choosealicense.com](https://choosealicense.com) when deciding which license to use.

Everywhere you reference the license programmatically make sure you're using the [SPDX identifier](https://spdx.org/licenses) for the license or the canonical way of specifying the license for the given context (e.g. Python package specifiers).

### Tidelift

Your package may already be eligible for funding through [Tidelift](https://tidelift.com)! If you haven't checked already, [search for projects you maintain](https://tidelift.com/lifter/search) to see if Tidelift would pay you monthly to continue maintaining the packages you're already maintaining. Tidelift will also help you with security disclosures and help keep your project metadata correct.

urllib3 was one of the [original projects supported by Tidelift](https://tidelift.com/subscription/pkg/pypi-urllib3) and we've been close partners ever since. Highly recommend being a lifter with Tidelift!

### Open Collective

[Open Collective](https://opencollective.com) is a way to do fundraising and money management for communities and projects, including open source projects. Open Collective handles being the legal entity behind accepting donations from donators and only charges a small fee on donations, **meaning it doesn't cost you any money up front**! urllib3 runs [our collective](https://opencollective.com/urllib3) with the [Open Source Collective fiscal host](https://opencollective.com/opensource) which charges a 10% host fee on transactions. You can apply for your collective to use this fiscal host after you create your collective.

Our favorite feature about Open Collective is that all transactions are public meaning there's public accountability for how money is spent and distributed to maintainers and contributors.

### GitHub Sponsors

GitHub Sponsors is a great way to get noticed by individuals and organizations as the "Sponsor" functionality is integrated into dependency graph info. GitHub provides an ["Explore Sponsors" page](https://github.com/sponsors/explore) which allows showing all dependencies which can be supported.

All three of the example FOSS funds above did some of their distribution through GitHub Sponsors. This should highlight how important having GitHub Sponsors enabled for your project is for receiving funds.

When you're designing your GitHub Sponsors page make sure you explain why the project is important and in need of support, potentially linking to your project roadmap. For inspiration you can look at the [NumFOCUS GitHub Sponsor page](https://github.com/sponsors/numfocus).

If you set up an Open Collective [you can use the Open Source Collective as the fiscal host](https://docs.github.com/en/sponsors/receiving-sponsorships-through-github-sponsors/setting-up-github-sponsors-for-your-organization#submitting-your-bank-information) where GitHub Sponsors transfers funds. This is convenient as it means that multiple maintainers can create invoices with Open Collective rather than a single individual privately collecting funds and having to handle dispursal.

After you create a GitHub Sponsors page you should configure the settings to allow one-time donations and ensure the "minimum amount" field is unset so users can donate any amount.

If you're hosting your project on GitHub you should consider [configuring a `FUNDING.yml` file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository) to have a "Sponsor" button appear on the repository. There are many supported platforms but you can specify a simple URL for any unsupported platforms.

### Dependency chain metadata

If consumers aren't finding your package in their dependency chain then they're less likely to fund the project *even if you're a well-known package*.

A good way to check if your project's dependency metadata is correct is to check that there are "dependent packages" and "dependent repositories" on [Libraries.io](https://libraries.io) or if your project is hosted on GitHub there's a "Dependency Graph" feature for every public repository. If nothing is showing up for these fields you need to figure out why.

Often times for the Python ecosystem it's due to [GitHub not supporting new packaging metadata](https://github.com/orgs/community/discussions/6456). We worked around this for urllib3 by [creating a bogus `setup.py` file](https://github.com/urllib3/urllib3/pull/2615/files). Right after merging the PR to add this file our dependency chain metadata on GitHub started working again. 

### Logos

Logos are a great way to build recognition of your project with a visual component. Logos are used in so many places from READMEs, GitHub organization profile, Twitter, Open Collective, you name it.

You'll also notice that in the Spotify FOSS fund announcement blog post that **every project that was selected had a logo**. Obviously that *could* be a coincidence, but there's likely some human bias that a project with a logo is more likely to be successful, popular, and dependable.

For urllib3 we [solicited logo designs from our community](https://github.com/urllib3/urllib3/issues/1597) and received lots of ideas and submissions. Make sure that you get at a minimum an SVG or other vector-based rendering of the logo so you can scale it up and down. It's also good to consider how the logo will look in both light and dark mode.

### Roadmap

Have a public roadmap for your project, even if this roadmap is a simple list of issues you'd like to tackle next. Having a public roadmap means that organizations can clearly see which features would be possible if you had more time and energy to spend on the project. For bonus points you can link this roadmap from your funding page.

To see a great roadmap in action, take [Pydantic v2](https://pydantic-docs.helpmanual.io/blog/pydantic-v2/) as an example. Samuel did an excellent job outlining the timeline, motivation, and huge list of features that will be coming with the next release. The detail that went into this plan likely helped secure funding from large organizations like [Amazon](https://twitter.com/samuel_colvin/status/1549383169006239745) and [Explosion AI](https://twitter.com/samuel_colvin/status/1549024637463535624).

### Hype

When your project accomplishes something great, **where do you spread the word?** The changelog is a good place to start, but that's not shareable or subscribable. Think about creating a mailing list, blog with an RSS feed, or Twitter account. You don't need to limit yourself to only one list: Open Collective and GitHub Sponsors also support sending email updates to all subscribers.

You can reach an engaged and lasting audience by giving talks at conferences. Doesn't have to be an official talk either, you might be able to do a "lightning talk" or "open space" about the project at a conference instead. Another popular way to build hype is being a guest on a podcast. I've also given talks about [urllib3 at PyCascades](https://2021.pycascades.com/program/talks/shipping-breaking-changes-as-the-most-downloaded-python-package/) and local conferences.

For urllib3 we have a [Twitter account](https://twitter.com/sethmlarson), [provide project blog posts](https://sethmlarson.dev), and share news through Discord, Open Collective, and GitHub Sponsors.  In addition to these "official" news sources our team talks about our work for urllib3 and surrounding projects on Twitter frequently to show that there's real people behind all the git commits. 👋

### Community

If your project is popular enough you'd likely be able to create a community around the project. This could take the form of a Discord channel, Slack, GitHub Discussions, or something else. Whenever you're working on something related to your project, talk about it in the community. This is also a great place to share project announcements made on other platforms like Twitter, Reddit, or HackerNews for some coordinated upvotes and shares.

There are many benefits for fostering a community including getting to connect with new people, finding potential future contributors and maintainers, and spreading the load of support requests when someone needs help.

For urllib3 we list our [Discord channel](https://discord.gg/urllib3) in multiple places, including but not limited to [the README](https://github.com/urllib3/urllib3#readme) and when [creating a new issue](https://github.com/urllib3/urllib3/blob/main/.github/ISSUE_TEMPLATE/config.yml).

Discord has a program where you can [create a server for open source projects](https://discord.com/open-source) and apply for a free vanity URL. For example urllib3's Discord URL is "discord.gg/urllib3".

### Grants

These are arguably the most difficult but also usually the most lucrative method of getting funding for your project. Getting a grant requires finding a potential grant donor, writing the grant proposal, signing a contract, and then providing a way for the check to be wired to you.

It's unlikely that an organization would offer a grant to projects which don't have a track record of consistent development, maintenance, and professionalism as there's a lot of trust that goes into signing over a check in exchange for work. For this reason I don't recommend going this route immediately for maintainers that are just getting started.

My most recent example of doing work for a grant is when I added support for TLS 1.3 to urllib3 over two weeks thanks to a grant from [CERT Governmental Luxembourg](https://www.govcert.lu/). The grant amount was for nearly $11,000 USD which was [~50% of the income urllib3 for the year of 2019](https://sethmlarson.dev/blog/review-of-2019-for-urllib3). In this case, the grant donor actually approached our team first with the proposal. Typically the *grant seeker* would be looking for a donor, and not the other way around.

### Stickers

If you're planning on attending in-person events it might make sense to create stickers with that shiny logo of yours. Of course, these end up costing money rather than making, but quality stickers are a very popular item at conferences. **I couldn't keep up with the demand at PyCon US!**

Use a service like [Sticker Ninja](https://stickerninja.com) to create your stickers, just make sure that your logo stands out and is recognizable even to people who don't know what your project is. Keep in mind that Sticker Ninja only ships to the US, so you may need to find another service if you live elsewhere.
