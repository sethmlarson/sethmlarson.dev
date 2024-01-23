# Removing maintainers from open source projects

Here's a tough but common situation for open source maintainers:

- You want a project you co-maintain to be more secure by reducing the attack surface.
- There are one or more folks in privileged roles who *previously were active contributors*, but now aren't active.
- You don't want to take away from or upset the folks who have contributed to the project before you.

**These three points feel like they're in contention.**
This article is here to help resolve this contention and potentially
spur some thinking about succession for open source projects.

## Why do people do open source?

Most rewards that come from contributing to open source are either **intrinsic** (helping others, learning new skills, interest in a topic, improve the world)
or for **recognition** (better access to jobs, proof of a skill-set, “fame” from a popular project). Most folks don't get
paid to work on open source for their first project, so *it's unlikely to be their initial motivation*.

Recognition is typically what feels “at stake” when removing a previous maintainer from operational roles on an open source project.

Let's split recognition into another two categories: **operational** and **celebratory**. Operational recognition is the category
of recognition that has security implications like access to sensitive information or publishing rights. Celebratory has no security implications,
it's there because we want to thank contributors for the work they've done for the project. Here's some examples of the two categories:

**Operational:**

  * Additional access on source control like GitHub (“commit bit”)
  * Additional access on package repository like PyPI
  * Listing email addresses for security contacts

**Celebratory:**

  * Author and maintainer annotation in package metadata
  * Elevating contributors into a triager role
  * Maintainer names listed in the README
  * Thanking contributors in release notes
  * Guest blog posts about the project

You'll notice that the celebratory recognition might be a good candidate for offsetting the removal of
incidental operational recognition (like your account being listed on PyPI).

## Suggestions for removing maintainers' with empathy

**Ensure the removal of operational recognition is supplanted by deliberate celebratory recognition.** Consider thanking
the removed individual publicly in a blog post, release notes, or social media for their contributions and accomplishments.
If there isn't already a permanent place to celebrate past maintainers consider adding a section to the documentation or README.

**Don't take action until you've reached out to the individual.** Having your access removed without any acknowledgement
feels bad and there's no way around that fact. Even if you don't receive a reply, sending a message and waiting some
time should be a bare minimum.

**Practice regular deliberate celebratory recognition**. Thank folks for their contributions,
call them out by name in release notes, list active and historical maintainers in the documentation.
This fulfills folks that are motivated by recognition and might inspire them to contribute again.

**Think more actively about succession.** In one of the many potential positive outcomes for an open source project, you will
be succeeded by other maintainers and someone else may one day be in the position that you are in today.

How can you prepare that individual to have a better experience than you are right now?
I highly recommend [Sumana Harihareswara's writing on this topic](https://www.harihareswara.net/posts/2023/maintainer-burnout-pycon-us-2023-followup/#succession-new-folks). There are tips like:

- Actively recruit maintainers by growing and promoting contributors.
- Talk about succession openly while you are still active on the project.
- Give privileges or responsibility to folks that repeatedly contribute positively, starting from triaging or reviewing code.
- Recognize when you are drifting away from a project and make it known to others, even if you intend to contribute in the future.
