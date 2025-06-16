# UN Open Source Week 2025: Security for the Long-Haul

This presentation was given during the [United Nations Open Source Week](https://www.un.org/digital-emerging-technologies/content/open-source-week-2025) "Maintain-a-thon"
hosted by the [Sovereign Tech Agency](https://sovereign.tech) and [Alpha Omega](https://alpha-omega.dev). Thanks to both the Sovereign Tech Agency
and Alpha Omega for supporting my attendance at this event and Alpha Omega for
supporting security in the Python ecosystem.

<p>
<center>
<img style="max-width: 100%" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAcIAAAHCAQAAAABUY/ToAAAChUlEQVR4nO3aS26EMAyAYUtzAI7E1TkSB6iUgt8Epmq7bH8voMzkYzZW4jiV8cvYBIlEIpFIJPIPSfF4DVnHhxwfH7Hu/tnxeFzGHqNWJPIu9WHsLh0t+tf5WVzaYCRykrvkKEc2bFv0cj6e33qCIpHvpU5UOkrH2zuQyB9IqdD1MCO+RSLfSL1lztlcdn5h2WeV1NfrJ/KfS49eNd0vlZZI5Czn2CLndLxn3zQEiezS9nGWWrrYWTXuF0+8JVdLJPIuLXLF25YqnbQ4F6l2wTX7kEi/LyNL7cjDTLdjVMVUjSORkX2L3r0NEIV4yLH7KyMPkchZan5578ik80A+odnPIJF3WS1tH5/SmwSSGZmtbySySw/LPh9fs5X03uW8fiKRSmx62upEpL0ty2+r1ef1E4k0KdHX9lESNXhvCPQ2NxJ5lbfjWclHydaAVeNI5KOUqRfQGgJLtSjPtz2c1iKRFroARn8gJ69Iy+ENzHXMe0Ek0rLvDJ+3Ir/a7k3r8pQWSORVZjXeUE9BkTo5QSKfZNXbmn2S76hTklwU5x0dEmn3M5ZYCvuJyDSNzXU8Ehn3l/HYs/k7nLeGwIcgkQ+yksxXQYmhtqOr9tKIQCKvUrIQbw0BketS2IstJHKSdcRvO7o9z/nHiMdoEiCRz3K07Bt54m8o29xPe0Ek8hqSve6o0M9RS+WhCBL5IMUjGgIp4/Qtp7FRqYpEdqkPusRJHJXImsez1bbsqyUSeZGx+a+zkZqt7FsNJPIbUiPKqXZAUps+JPIrWcte/AOAPuZSOG6rIBI58mFEI1vyvMSyb9jQV/wCEnmXHtlA0rdZ+R1FVD+HQyJn+YtAIpFIJBKJ/CPyE4xxc4lzmop+AAAAAElFTkSuQmCC"/>
<br><small><i>Use this QR code to share with your neighbors!</i></small>
</center></p>

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

## Low-Energy Security: Keeping the lights on

There are three "keep-the-lights on" practices for low-energy security:

* Finding energy by onboarding new contributors
  * Fewer contributors interested based on new development
  * Need to find new sources of contributors: users, dependents, foundation/group
  * "Working group" of projects sharing resources: Jazzband, Django-Commons, Flask-Eco
* Vulnerability handling
  * Time-sensitive, secret, work is isolating
  * Backwards compatibility
  * Release process
* Security best practices
  * Tools, scanners, linters
  * New security features (repository, package manager, accounts, email)
  * Can users handle a request themselves? -> Let them!

## Onboarding new contributors

* Community is important even when a project is feature-complete
  or in "security-only" mode. Look inwards, up and down the dependency chain,
  or for security-focused contributors in your ecosystem.
* Contributors guide, make the status of the project clear.
* You are not alone in security work: ask for help!
* Recognition is the currency of open source volunteerism.
  Gather and celebrate the good and bad.
* Listen to yourself when processes don't match your energy level. Avoid burnout.
  If something is not working: fix it to maintain your energy long-term.
* xz-utils backdoor: who do you trust? Volunteers can't be expected to filter out
  patient, highly-resourced attackers.

```
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!! <blink>Expat is UNDERSTAFFED and WITHOUT FUNDING.</blink>                 !!
!!                 ~~~~~~~~~~~~                                              !!
!!  ...                                                                      !!
!!                                                                           !!
!! For details, please reach out via e-mail to sebastian@pipping.org so we   !!
!! can schedule a voice call on the topic, in English or German.             !!
!!                                                                           !!
!! THANK YOU!                        Sebastian Pipping -- Berlin, 2024-03-09 !!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
```

## Vulnerability handling

Security policy with how to submit vulnerability reports (form or email)
in `SECURITY.md`.

Not actively exploited? Walk, don't run. 90 days is industry standard.
Use the 90 days when you need to! Put the deadline on your calendar.

Highly recommend using repository features when available (GitHub Security Advisories
or Confidential Issues / Merge Requests on GitLab).

Cyber Resilience Act (CRA): many open source projects not likely to have much
obligation. Open Source Stewards (such as non-profits, foundations, companies
publishing open source software) required to have vulnerability handling.

## Questions for discussion

* Who can be helpful in solving these challenges?
* How can we get users engaged and able to contribute upstream to security?
* How to celebrate and reward long-term maintenance of open source software?
* How to establish trust among new contributors, especially those with less online presence?
* How to find and onboard contributors interested in security work safely?
