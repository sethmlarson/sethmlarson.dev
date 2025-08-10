# UN Open Source Week 2025: Security for the Long-Haul

<!-- more -->

This page was used during the [United Nations Open Source Week](https://www.un.org/digital-emerging-technologies/content/open-source-week-2025) "Maintain-a-thon"
hosted by the [Sovereign Tech Agency](https://sovereign.tech) and [Alpha Omega](https://alpha-omega.dev). Thanks to both the Sovereign Tech Agency
and Alpha Omega for supporting my attendance at this event and Alpha Omega for
supporting security in the Python ecosystem.

<!-- more -->

This page contains the content from the break-out session
I led during the "Maintain-a-thon" titled "Security for the Long-Haul".
The format was quite loose and in-the-moment, so apologies for
the extremely light amount of editing in this article.

## Why does long-haul security matter?

Open source projects that achieve widespread usage tend to
follow a similar trajectory:

1. Start an Open Source project
2. Scale an Open Source project
3. Sustain an Open Source project
4. Sunsetting an Open Source project

After open source projects stop growing in terms of users and new features
they often will reach a "stable" steady-state. In this state there are likely
fewer new features being developed and most changes to the project are
bug fixes or security fixes.

Security work is what I consider to be the "minimum viable maintenance"
for a software project that is still an "upstream". Without security fixes,
users will need to fork and maintain the project themselves or move
to an alternative project.

<p>
<center>
<svg xmlns="http://www.w3.org/2000/svg" style="cursor:pointer;max-width:100%;max-height:379px;" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="853px" viewBox="-0.5 -0.5 853 379" content="&lt;mxfile host=&quot;app.diagrams.net&quot; agent=&quot;Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36&quot; version=&quot;27.0.6&quot;&gt;&#10;  &lt;diagram name=&quot;Page-1&quot; id=&quot;sgQ4IJ0essKWkiFB76Bz&quot;&gt;&#10;    &lt;mxGraphModel dx=&quot;1356&quot; dy=&quot;852&quot; grid=&quot;1&quot; gridSize=&quot;10&quot; guides=&quot;1&quot; tooltips=&quot;1&quot; connect=&quot;1&quot; arrows=&quot;1&quot; fold=&quot;1&quot; page=&quot;1&quot; pageScale=&quot;1&quot; pageWidth=&quot;850&quot; pageHeight=&quot;1100&quot; math=&quot;0&quot; shadow=&quot;0&quot;&gt;&#10;      &lt;root&gt;&#10;        &lt;mxCell id=&quot;0&quot; /&gt;&#10;        &lt;mxCell id=&quot;1&quot; parent=&quot;0&quot; /&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-2&quot; value=&quot;&quot; style=&quot;endArrow=none;html=1;rounded=0;strokeWidth=3;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;120&quot; y=&quot;400&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;200&quot; y=&quot;360&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-3&quot; value=&quot;&quot; style=&quot;endArrow=none;html=1;rounded=0;strokeWidth=3;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;200&quot; y=&quot;360&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;280&quot; y=&quot;280&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-4&quot; value=&quot;&quot; style=&quot;endArrow=none;html=1;rounded=0;strokeWidth=3;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;280&quot; y=&quot;280&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;360&quot; y=&quot;120&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-5&quot; value=&quot;&quot; style=&quot;endArrow=none;html=1;rounded=0;strokeWidth=3;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;360&quot; y=&quot;120&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;440&quot; y=&quot;80&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-6&quot; value=&quot;&quot; style=&quot;endArrow=none;html=1;rounded=0;strokeWidth=3;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;440&quot; y=&quot;80&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;680&quot; y=&quot;100&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-8&quot; value=&quot;&quot; style=&quot;endArrow=none;dashed=1;html=1;dashPattern=1 3;strokeWidth=3;rounded=0;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;680&quot; y=&quot;100&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;920&quot; y=&quot;120&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-9&quot; value=&quot;&quot; style=&quot;endArrow=classic;html=1;rounded=0;strokeWidth=3;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;120&quot; y=&quot;400&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;720&quot; y=&quot;400&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-10&quot; value=&quot;&quot; style=&quot;endArrow=classic;html=1;rounded=0;strokeWidth=3;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;120&quot; y=&quot;400&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;120&quot; y=&quot;80&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-11&quot; value=&quot;TIME&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontFamily=Courier New;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;200&quot; y=&quot;410&quot; width=&quot;80&quot; height=&quot;40&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-12&quot; value=&quot;USAGE&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontFamily=Courier New;rotation=-90;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;50&quot; y=&quot;260&quot; width=&quot;80&quot; height=&quot;40&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-13&quot; value=&quot;&quot; style=&quot;endArrow=none;dashed=1;html=1;rounded=0;strokeWidth=3;&quot; edge=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry width=&quot;50&quot; height=&quot;50&quot; relative=&quot;1&quot; as=&quot;geometry&quot;&gt;&#10;            &lt;mxPoint x=&quot;560&quot; y=&quot;400&quot; as=&quot;sourcePoint&quot; /&gt;&#10;            &lt;mxPoint x=&quot;560&quot; y=&quot;90&quot; as=&quot;targetPoint&quot; /&gt;&#10;          &lt;/mxGeometry&gt;&#10;        &lt;/mxCell&gt;&#10;        &lt;mxCell id=&quot;lOKEbmHN3jcRTAGF_Sr3-14&quot; value=&quot;FEATURE&amp;lt;br&amp;gt;COMPLETE&quot; style=&quot;text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fontSize=32;fontFamily=Courier New;&quot; vertex=&quot;1&quot; parent=&quot;1&quot;&gt;&#10;          &lt;mxGeometry x=&quot;560&quot; y=&quot;200&quot; width=&quot;190&quot; height=&quot;80&quot; as=&quot;geometry&quot; /&gt;&#10;        &lt;/mxCell&gt;&#10;      &lt;/root&gt;&#10;    &lt;/mxGraphModel&gt;&#10;  &lt;/diagram&gt;&#10;&lt;/mxfile&gt;&#10;" onclick="(function(svg){var src=window.event.target||window.event.srcElement;while (src!=null&amp;&amp;src.nodeName.toLowerCase()!='a'){src=src.parentNode;}if(src==null){if(svg.wnd!=null&amp;&amp;!svg.wnd.closed){svg.wnd.focus();}else{var r=function(evt){if(evt.data=='ready'&amp;&amp;evt.source==svg.wnd){svg.wnd.postMessage(decodeURIComponent(svg.getAttribute('content')),'*');window.removeEventListener('message',r);}};window.addEventListener('message',r);svg.wnd=window.open('https://viewer.diagrams.net/?client=1&amp;page=0&amp;edit=_blank');}}})(this);"><defs/><g><g data-cell-id="0"><g data-cell-id="1"><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-2"><g><path d="M 50 328 L 130 288" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-3"><g><path d="M 130 288 L 210 208" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-4"><g><path d="M 210 208 L 290 48" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-5"><g><path d="M 290 48 L 370 8" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-6"><g><path d="M 370 8 L 610 28" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-8"><g><path d="M 610 28 L 850 48" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" stroke-dasharray="3 9" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-9"><g><path d="M 50 328 L 639.9 328" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/><path d="M 646.65 328 L 637.65 332.5 L 639.9 328 L 637.65 323.5 Z" fill="#000000" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="all" style="fill: light-dark(rgb(0, 0, 0), rgb(255, 255, 255)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-10"><g><path d="M 50 328 L 50 18.1" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/><path d="M 50 11.35 L 54.5 20.35 L 50 18.1 L 45.5 20.35 Z" fill="#000000" stroke="#000000" stroke-width="3" stroke-miterlimit="10" pointer-events="all" style="fill: light-dark(rgb(0, 0, 0), rgb(255, 255, 255)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-11"><g><rect x="130" y="338" width="80" height="40" fill="none" stroke="none" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 358px; margin-left: 131px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000000; "><div style="display: inline-block; font-size: 32px; font-family: &quot;Courier New&quot;; color: light-dark(#000000, #ffffff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">TIME</div></div></div></foreignObject><text x="170" y="368" fill="light-dark(#000000, #ffffff)" font-family="&quot;Courier New&quot;" font-size="32px" text-anchor="middle">TIME</text></switch></g></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-12"><g><rect x="-20" y="188" width="80" height="40" fill="none" stroke="none" transform="rotate(-90,20,208)" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)rotate(-90 20 208)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 208px; margin-left: -19px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000000; "><div style="display: inline-block; font-size: 32px; font-family: &quot;Courier New&quot;; color: light-dark(#000000, #ffffff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">USAGE</div></div></div></foreignObject><text x="20" y="218" fill="light-dark(#000000, #ffffff)" font-family="&quot;Courier New&quot;" font-size="32px" text-anchor="middle">USAGE</text></switch></g></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-13"><g><path d="M 490 328 L 490 18" fill="none" stroke="#000000" stroke-width="3" stroke-miterlimit="10" stroke-dasharray="9 9" pointer-events="stroke" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));"/></g></g><g data-cell-id="lOKEbmHN3jcRTAGF_Sr3-14"><g><rect x="490" y="128" width="190" height="80" fill="none" stroke="none" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 188px; height: 1px; padding-top: 168px; margin-left: 491px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000000; "><div style="display: inline-block; font-size: 32px; font-family: &quot;Courier New&quot;; color: light-dark(#000000, #ffffff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">FEATURE<br />COMPLETE</div></div></div></foreignObject><text x="585" y="178" fill="light-dark(#000000, #ffffff)" font-family="&quot;Courier New&quot;" font-size="32px" text-anchor="middle">FEATURE...</text></switch></g></g></g></g></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.drawio.com/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>
<br><small><i>Graph of an open source project usage over time.</i></small></center>
</p>

Projects and code spends most of its time in the "stable maintenance"
state, the early development phase is relatively short-lived.

Some projects may also find security work in-general
more difficult than others, either due to a lack of resources
or time. Smaller projects usually are low on maintainers.
Projects of specific topics (e.g. scientific computing)
may not see themselves as security-sensitive.

## What does ideal long-haul security look like?

* Project is able to consistently onboard new contributors interested in long-term maintenance.
* Vulnerabilities when found are reported, fixed, and published.
  Users are notified and able to upgrade or mitigate vulnerabilities.
* Project configuration, processes, and security tooling are kept secure and up-to-date.

## Challenges

* Contributors interested in security work might not be the same contributors
  interested in the project domain.
* Security work often requires project domain expertise (how does X feature work).
* Trust bringing on new maintainers, especially late in the project lifecycle (popular! xz-utils)
* Vulnerability reporting work is inherently isolated. Can't lean on your existing
  community by default.
* New security features for project (source forge, package repository, accounts) are not enabled by default.
* Fewer features for maintainers to work on to be excited, inspired, recognition.
* Many contributors want to work on domain-specific code, not necessarily security.
* Want to minimize effort keeping up-to-date with latest security practices / tools.
* Less energy to improve or change processes when a project
  is heading in the wrong direction.

## Questions for discussion

* Who can be helpful in solving these challenges?
* How can we get users engaged and able to contribute upstream to security?
* How to celebrate and reward long-term maintenance of open source software?
* How to establish trust among new contributors, especially those with less online presence?
* How to find and onboard contributors interested in security work safely?

## Notes from the Discussion

> **Beware! From this section onwards is a raw dump of notes from a Google document!** They have not been edited in any way, but if you're interested they are here.

### What I learned today

* Quantifying the fInancial risk, better feedback mechanism between the security funding versus the risk. Down the dependency graph beyond the product. Financial connection.
    * Can the top-down effort be done and then publishing the information instead of bottom-up. “Mega-phone” for the maintainers?
    * Stakeholders.
    * Game-theory: tragedy of the commons. Should this be a social / governance especially for smaller projects.
    * From a large corporation it’s hard to do that analysis and prove that you affect change.
    * Crises are much more visible.Reacting to crises.
    * OSPOs started as a charity. Now it’s evolved to be risk management.
    * Balance sheet, chief open source controller. Short-term risk/credit, tools that you use to manage a financial portfolio.
    * Will you pay the salary or the amount that you expect others to pay as well? Depending on corporations working together and coordinating.
    * CISOs being fired for zero-days, can we create pressure to manage your open source risk?
    * Cyber Resilience Act (CRA) if the way its implemented, security of their dependencies. Something will happen, either every company will support its dependencies or it will create an intermediate market.
* How do you give people that are domain-specific to give the tools they need to develop their projects securely?
    * “Security is somebody else’s problem”
    * People don’t care about security, they care about usability. Limited arsenal.
    * Better defaults for security.
    * People want to ship! “Have to conform to the ecosystem”, balance between openness and security.
    * CI is a big expense to provide to a community. Doesn’t seem readily possible to fund/credit this.
    * How much time is spent to be more efficient? Lots of work is done.
    * OSS-Fuzz, essentially donated CI for fuzzing
    * Homebrew: everything is CI.
    * Have to communicate “return on investment” on providing CI minutes.
    * Would love to write a case study about “how the UN digital infrastructure would be supported by funding”
    * What metrics do we use? Do ourselves or our customers use the project, tough sell otherwise. You need to quantify the failure, how much does it cost if we have a failure.
    * Repeated funding is the issue.
    * The credit programs are increasing, not decreasing.
* “Imagine what it’s like for the smaller projects?”
    * Won’t be able to advocate for themselves, even harder than smaller projects.
* Digital Public Infrastructure, problem solved through taxation. Treat as public infrastructure.
    * Small libraries don’t know their options.
    * What is our goal? Only remaining security problems for the projects being the ones we don’t know how to solve. Secure defaults.
* OSS-Fuzz: lays bare the lie that the work is done.
    * Contributor that is interested in OSS-Fuzz
* Success story for a small project that is well-supported: cryptography
    * Sqlite. Cryptography doesn’t take money, but they work with others to contribute.
    * “There’s not a lot that you have to do”.
    * Not a huge checklist: 8-10 things to have “good enough security”.
    * We wish these things were default on!
    * Keep your dependencies up to date. Don’t worry about Dependabot.
    * Upgrading incurs risk, too. Most people don’t have incredibly large test suites.
    * Renovate auto-merge.
    * “Hold-back feature for Dependabot” waiting for low-quality/backdoors to be shaken out.
* Corporate donated security work time if “maintainers are not contributors”
    * Private fork of the project that can be pulled in if needed.
    * How can I trust that the contributor is good to have this information?
    * Surprises me that it doesn’t happen more seeing corporate donation of time for security work.
    * OpenSSF meeting aligning corporate contributors to align bug fixes.
    * Pre-vetted set of engineers doing security work.
    * How would maintainers know to engage that process?
    * Security engineers would have to show up on the project and be proactive. Drive-by.
    * “I’ll help you with security” can be sketchy, how to legitimize.
    * Batphone for maintainers. Log4j had infra, xz-utils didn’t.
    * Not supposed to be solving the issues, would be mentoring the maintainers rather than solving the problems.
    * Narrowing the scope of what we offer.
* Percentage of maintainers that know about dependeabot/static analysis: there isn’t any knowledge, even for basics. Foundational education, what are these security features.
* How do you vet an open source contributor or maintainer?
    * Xz-utils taught us that you can’t trust just the content of the commits.
    * Homebrew institutes a real-name policy, with photo ID check that gets thrown away. Not aiming for nation-state coverage. 
    * Whole lot of vibes, blogs, socials, etc. Do the stuff that no one else wants to do.
    * LLMs are good at “creating vibes”? Do I care if the content of the commits.
    * Maintainer is on the hook for the contributions.
    * Conferences as security “vetting”. Whether that’s explicit or not based on travel availability.
    * Filtering out based on the geography, ability to pay, 
    * Foundations could sponsor travel grants.
    * How many communities write down what it takes to be a maintainer/release manager.
    * Drupal: try to have maintainers on each continent (timing, local knowledge, languages).
    * Not common to have documentation on how to become a release manager.
    * Release manager checklist for vetting new dependencies: can we release with them in a nice way.
    * Maintainers are allowed to opt-in to the security and having a badge.
    * cargo-vet
    * There is probably closure within PyPI. “Island analysis”
* Better defaults
    * Repository level defaults, branch protection, token
    * Project scaffolding w/ good defaults per language.
    * Package installers/publishers.
    * Whack-a-mole bad defaults.
        * Updating existing project templates is hard! ([cruft](https://cruft.github.io/cruft/)/cookiecutter - maybe look at [projen](https://projen.io/)?)
    * Make project management into pull requests.
        * Check the box for other people. Lightweight.
    * Creating a template and “making it easy”.
        * It’s a hobby, I don’t want to read best practices guides.
        * Make it explicit in their README.
        * Want the benefits of a project being used, but don’t want the responsibility.
    * Template that documents your intentions.
    * When we add a dependency, make an inference on a dependency. Moves responsibility to product developers.
        * Measuring activity levels.
        * Activity level is tricky.
        * Sqlite exhibits many of the characteristics of a project 
        * They take reports, but not code.
    * Choosing not to use a library versus using it.
    * Encouraging maintainers to state their intentions more clearly.
    * Be conservative about your technology choices. Transitive dependencies kinda hurts this, you are not the only decider.
* We haven’t solved xz-utils!
    * Damage limitations.

### What I wish existed

* Balance sheets for open source risk
* We’ve talked about the people maintaining open source software. Dependabot found a security vulnerability, how much of that library do I actually use. False-positives. Notification fatigue. Show off API usage per project. SBOM (SPDX) allows showing the exposure of a library.
* Batphone for maintainers, questions
* Best practice recommendations on how to vet new maintainers/security contributors.
* Deleting old insecure templates for projects.

### Summary for larger group

* Sustainability, we found ourselves talking about sustainability as a response. Don’t want to engage with security, want to have assets available to them.
* Sec defaults Existing tools and projects don’t use templates. Templates tend to get outdated over time. More secure defaults on the tools, project management tools and platforms are important to solve this issue.
* Vetting the trustworthiness of a maintainer or contributor is difficult. May be already happening implicitly, but many projects dont document this process.
* Identified a “bat phone” for maintainers as being useful, the problem would be projects not knowing. Solutions need to be proactive to reach small or disengaged projects.