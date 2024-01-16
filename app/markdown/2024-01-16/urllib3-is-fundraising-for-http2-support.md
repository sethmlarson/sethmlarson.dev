# urllib3 is fundraising for HTTP/2 support

> **TLDR:** [urllib3 is raising **~$40,000 USD**](https://opencollective.com/urllib3) to release HTTP/2 support and ensure long-term sustainable maintenance of the project after a sharp decline in financial support for 2023.

## What is urllib3?

<div class="row">
<div class="col-9">
<p><a href="https://urllib3.readthedocs.io/">urllib3</a> is an HTTP client library for Python and is depended on by widely used projects like pip, Requests, major cloud and service provider SDKs, and more. urllib3 is one of the most used Python packages overall, <a href="https://www.pepy.tech/projects/urllib3?versions=*">installed over 4 billion times in 2023</a> with <nobr><a href="https://github.com/urllib3/urllib3/network/dependents">1.5 million dependent repos on GitHub</a></nobr>, up 50% from just last year.</p>
</div>
<div class="col-3">
<center>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 8 8">
    <rect x="0" y="0" width="2" height="5" fill="#D03A20"/>
    <rect x="0" y="6" width="2" height="2" fill="#D03A20"/>
    <rect x="3" y="0" width="2" height="5" fill="#F09837"/>
    <rect x="3" y="6" width="2" height="2" fill="#F09837"/>
    <rect x="6" y="0" width="2" height="2" fill="#587934"/>
    <rect x="6" y="3" width="2" height="5" fill="#587934"/>
</svg>
</center>
</div>
</div>

## Project update

2023 was a transformative year for urllib3, headlined by the [first stable release of v2.0](https://sethmlarson.dev/urllib3-2.0.0) after multiple years of development by our maintainers and community. This major release is only the beginning of our plans to overhaul the library’s capabilities by removing constraints on our HTTP implementation while preserving backwards compatibility.

<div class="row">
<div class="col-6">
<p>We’ve been able to accomplish this incredible work in 2023 thanks to financial support from <a href="https://tidelift.com/subscription/pkg/pypi-urllib3">Tidelift</a>, the <a href="https://engineering.atspotify.com/2022/06/say-hello-to-the-recipients-of-the-2022-spotify-foss-fund/">Spotify 2022 FOSS Fund</a>, and our other sponsors which allowed us to offer bounties on tasks to fairly compensate maintainers and contributors for their time investments with the project.</p>
<p>Unfortunately, compared to past years <strong>we’ve experienced a sharp drop in financial support from non-Tidelift sources heading into 2024.</strong></p>
</div>
<div class="col-6">
<center>
<table style="text-align: left;">
  <tr>
   <td>Year
   </td>
   <td>Non-Tidelift Funding
   </td>
  </tr>
  <tr>
   <td>2019
   </td>
   <td>$18,580
   </td>
  </tr>
  <tr>
   <td>2020
   </td>
   <td>$100*
   </td>
  </tr>
  <tr>
   <td>2021
   </td>
   <td>$9,950
   </td>
  </tr>
  <tr>
   <td>2022
   </td>
   <td>$14,493
   </td>
  </tr>
  <tr>
   <td>2023
   </td>
   <td><strong>$2,330</strong>
   </td>
  </tr>
</table>

<p><small><i>* December 2020 was the first time we offered <nobr>ad-hoc</nobr> financial support via GitHub Sponsors. Before this we only accepted grants for funding.</i></small></p>
</center>
</div>
</div>

Our team has worked hard to set the stage for HTTP/2 support with urllib3 v2.0, and we plan to land HTTP/2
support without compromising on the sustainability of the project. Backwards-compatible HTTP/2 support in
urllib3 would immediately benefit millions of users, among them the largest companies in the world, and
requires adding more long-term maintenance burden to maintainers. **This important work and its maintenance
should not be uncompensated.**

To ensure timely and sustainable development of HTTP/2 for urllib3 we're launching a fundraiser with a goal
of raising our **[Open Collective balance to $50,000 USD](https://opencollective.com/urllib3)**. HTTP/2 support has
just started being developed and we're hoping to release stable support once our fundraising goal has been reached.
**Donations to [Open Collective](https://opencollective.com/urllib3)** directly or to platforms like **[GitHub Sponsors](https://github.com/sponsors/urllib3/)**
or **[Thanks.dev](https://thanks.dev/)** will all be counted towards this fundraising goal.

Our team has a long track record of using our financial resources to complete larger projects like [secure URL parsing](https://sethmlarson.dev/sponsored-work-on-urllib3), [TLS 1.3](https://sethmlarson.dev/review-of-2019-for-urllib3#releases-and-changes), [modernizing our test suite framework](https://quentin.pradet.me/blog/ive-been-paid-to-work-on-open-source.html), and [finding security issues across multiple projects](https://quentin.pradet.me/blog/i-got-paid-to-work-on-open-source-2.html). All receipts are [published publicly on our Open Collective](https://opencollective.com/urllib3/expenses) with links to the work items being accomplished and blogged about by our maintainers. If you or your organization has questions about this fundraiser please email [sethmichaellarson@gmail.com](mailto:sethmichaellarson@gmail.com) or ask in our [community Discord](discord.gg/urllib3).

There’s more information below about the work we’ve done so far for HTTP/2 support and what else we plan to do in 2024 during our fundraiser. _Thanks for supporting open source software!_

## Funding update

<div class="row">
<div class="col-6 col-12-sm">

<p>
urllib3 received <strong>$17,830 US dollars in financial support </strong>in 2023 from all sources and <strong>distributed $24,350 to contributors and maintainers</strong>. Our primary supporter continues to be<a href="https://tidelift.com/subscription/pkg/pypi-urllib3"> Tidelift</a>, who provided $15,500 to core maintainers Seth, Quentin, and Illia.
</p>
<p>
We distributed $1,800 to community contributors through our <a href="https://urllib3.readthedocs.io/en/stable/contributing.html#getting-paid-for-your-contributions">bounty program</a>, less than last year but still a sizable amount. We are looking to leverage our bounty program more in 2024 to implement HTTP/2 and WebAssembly features.
</p>
<p>
Our Open Collective <a href="https://sethmlarson.dev/urllib3-in-2022#open-collective">started the year with nearly $19,000 USD</a> and ended the year with $12,179. This statistic clearly shows the gap in funding, comparing this year's fundraising of $2,330 to the average across 4 prior years of over $10,000 per year.
</p>

</div>
<div class="col-6 col-12-sm">
<center>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600">

<g transform="translate(164.91133392333984,18)">
<g id="sankey_flows">
<path id="flow6" d="M20 297.85874C74.59433 297.85874 74.59433 345.54608 129.18866 345.54608" fill="none" stroke-width="129.69208" stroke="#ff9da7" opacity="0.45"><title>2022 OC Balance → Open Collective: $18,932</title></path>
<path id="flow2" d="M20 134.32997C74.59433 134.32997 74.59433 180.88772 129.18866 180.88772" fill="none" stroke-width="106.18145" stroke="#76b7b2" opacity="0.45"><title>Tidelift → Tidelift Lifters: $15,500</title></path>
<path id="flow15" d="M149.18866 383.04183C203.783 383.04183 203.783 473.09624 258.37733 473.09624" fill="none" stroke-width="83.43122" stroke="#9c755f" opacity="0.45"><title>Open Collective → 2023 OC Balance: $12,179</title></path>
<path id="flow0" d="M20 -0.96575v82.205L129.18866 82.205v-82.205z" fill="#76b7b2" stroke-width="0.5" stroke="#76b7b2" opacity="0.45"><title>Tidelift → Tidelift Partnerships*: $12,000</title></path>
<path id="flow1" d="M149.18866 0v82.205L258.37733 82.205v-82.205z" fill="#76b7b2" stroke-width="0.5" stroke="#76b7b2" opacity="0.45"><title>Tidelift Partnerships* → Seth Larson: $12,000</title></path>
<path id="flow3" d="M149.18866 151.44463C203.783 151.44463 203.783 105.85263 258.37733 105.85263" fill="none" stroke-width="47.29527" stroke="#76b7b2" opacity="0.45"><title>Tidelift Lifters → Seth Larson: $6,904</title></path>
<path id="flow4" d="M149.18866 197.70892C203.783 197.70892 203.783 207.64202 258.37733 207.64202" fill="none" stroke-width="45.2333" stroke="#76b7b2" opacity="0.45"><title>Tidelift Lifters → Quentin Pradet: $6,603</title></path>
<path id="flow13" d="M149.18866 306.56036v22.43511L258.37733 327.86588v-22.43511z" fill="#9c755f" stroke-width="0.5" stroke="#9c755f" opacity="0.45"><title>Open Collective → Illia Volochii: $3,275</title></path>
<path id="flow12" d="M149.18866 298.59675C203.783 298.59675 203.783 238.22228 258.37733 238.22228" fill="none" stroke-width="15.92722" stroke="#9c755f" opacity="0.45"><title>Open Collective → Quentin Pradet: $2,325</title></path>
<path id="flow5" d="M149.18866 227.15201C203.783 227.15201 203.783 298.60433 258.37733 298.60433" fill="none" stroke-width="13.65288" stroke="#76b7b2" opacity="0.45"><title>Tidelift Lifters → Illia Volochii: $1,993</title></path>
<path id="flow14" d="M149.18866 335.16085C203.783 335.16085 203.783 379.62326 258.37733 379.62326" fill="none" stroke-width="12.33075" stroke="#9c755f" opacity="0.45"><title>Open Collective → Bounty Program: $1,800</title></path>
<path id="flow11" d="M149.18866 285.66659C203.783 285.66659 203.783 134.46682 258.37733 134.46682" fill="none" stroke-width="9.9331" stroke="#9c755f" opacity="0.45"><title>Open Collective → Seth Larson: $1,450</title></path>
<path id="flow7" d="M20 412.90711C74.59433 412.90711 74.59433 415.00245 129.18866 415.00245" fill="none" stroke-width="9.22066" stroke="#bab0ab" opacity="0.45"><title>GitHub Sponsors → Open Collective: $1,346</title></path>
<path id="flow8" d="M20 465.16457C74.59433 465.16457 74.59433 421.6679 129.18866 421.6679" fill="none" stroke-width="4.11025" stroke="#4e79a7" opacity="0.45"><title>Sourcegraph → Open Collective: $600</title></path>
<path id="flow9" d="M20 514.10985C74.59433 514.10985 74.59433 425.02118 129.18866 425.02118" fill="none" stroke-width="2.59631" stroke="#f28e2c" opacity="0.45"><title>Thanks.dev → Open Collective: $379</title></path>
<path id="flow16" d="M149.18866 425.55551C203.783 425.55551 203.783 561.20193 258.37733 561.20193" fill="none" stroke-width="1.59615" stroke="#9c755f" opacity="0.45"><title>Open Collective → OSC Host Fees: $233</title></path>
<path id="flow10" d="M20 561.01713C74.59433 561.01713 74.59433 426.33646 129.18866 426.33646" fill="none" stroke-width="1" stroke="#e15759" opacity="0.45"><title>Donations → Open Collective: $5</title></path>
</g>
<g id="sankey_nodes">
<g class="node">
<rect id="r0_border" class="for_r0" x="0" y="-0.96575" height="188.38645" width="20" stroke="rgb(58, 90, 87)" stroke-width="2" fill="none"></rect>
<rect id="r0" class="for_r0" x="0" y="-0.96575" height="188.38645" width="20" fill="#76b7b2" fill-opacity="1"><title>Tidelift:
$27,500</title></rect>
</g>
<g class="node">
<rect id="r1_border" class="for_r1" x="129.18866" y="0" height="82.205" width="20" stroke="rgb(58, 90, 87)" stroke-width="2" fill="none"></rect>
<rect id="r1" class="for_r1" x="129.18866" y="0" height="82.205" width="20" fill="#76b7b2" fill-opacity="1"><title>Tidelift Partnerships*:
$12,000</title></rect>
</g>
<g class="node">
<rect id="r2_border" class="for_r2" x="258.37733" y="0" height="139.43337" width="20" stroke="rgb(44, 79, 39)" stroke-width="2" fill="none"></rect>
<rect id="r2" class="for_r2" x="258.37733" y="0" height="139.43337" width="20" fill="#59a14f" fill-opacity="1"><title>Seth Larson:
$20,354</title></rect>
</g>
<g class="node">
<rect id="r3_border" class="for_r3" x="129.18866" y="127.797" height="106.18145" width="20" stroke="rgb(58, 90, 87)" stroke-width="2" fill="none"></rect>
<rect id="r3" class="for_r3" x="129.18866" y="127.797" height="106.18145" width="20" fill="#76b7b2" fill-opacity="1"><title>Tidelift Lifters:
$15,500</title></rect>
</g>
<g class="node">
<rect id="r4_border" class="for_r4" x="258.37733" y="185.02537" height="61.16052" width="20" stroke="rgb(116, 98, 36)" stroke-width="2" fill="none"></rect>
<rect id="r4" class="for_r4" x="258.37733" y="185.02537" height="61.16052" width="20" fill="#edc949" fill-opacity="1"><title>Quentin Pradet:
$8,928</title></rect>
</g>
<g class="node">
<rect id="r5_border" class="for_r5" x="258.37733" y="291.77789" height="36.08799" width="20" stroke="rgb(86, 60, 79)" stroke-width="2" fill="none"></rect>
<rect id="r5" class="for_r5" x="258.37733" y="291.77789" height="36.08799" width="20" fill="#af7aa1" fill-opacity="1"><title>Illia Volochii:
$5,268</title></rect>
</g>
<g class="node">
<rect id="r6_border" class="for_r6" x="0" y="233.0127" height="129.69208" width="20" stroke="rgb(125, 77, 82)" stroke-width="2" fill="none"></rect>
<rect id="r6" class="for_r6" x="0" y="233.0127" height="129.69208" width="20" fill="#ff9da7" fill-opacity="1"><title>2022 OC Balance:
$18,932</title></rect>
</g>
<g class="node">
<rect id="r7_border" class="for_r7" x="129.18866" y="280.70004" height="145.65355" width="20" stroke="rgb(76, 57, 47)" stroke-width="2" fill="none"></rect>
<rect id="r7" class="for_r7" x="129.18866" y="280.70004" height="145.65355" width="20" fill="#9c755f" fill-opacity="1"><title>Open Collective:
$21,262</title></rect>
</g>
<g class="node">
<rect id="r8_border" class="for_r8" x="0" y="408.29678" height="9.22066" width="20" stroke="rgb(91, 86, 84)" stroke-width="2" fill="none"></rect>
<rect id="r8" class="for_r8" x="0" y="408.29678" height="9.22066" width="20" fill="#bab0ab" fill-opacity="1"><title>GitHub Sponsors:
$1,346</title></rect>
</g>
<g class="node">
<rect id="r9_border" class="for_r9" x="0" y="463.10944" height="4.11025" width="20" stroke="rgb(38, 59, 82)" stroke-width="2" fill="none"></rect>
<rect id="r9" class="for_r9" x="0" y="463.10944" height="4.11025" width="20" fill="#4e79a7" fill-opacity="1"><title>Sourcegraph:
$600</title></rect>
</g>
<g class="node">
<rect id="r10_border" class="for_r10" x="0" y="512.81169" height="2.59631" width="20" stroke="rgb(119, 70, 22)" stroke-width="2" fill="none"></rect>
<rect id="r10" class="for_r10" x="0" y="512.81169" height="2.59631" width="20" fill="#f28e2c" fill-opacity="1"><title>Thanks.dev:
$379</title></rect>
</g>
<g class="node">
<rect id="r11_border" class="for_r11" x="0" y="561" height="1" width="20" stroke="rgb(110, 43, 44)" stroke-width="2" fill="none"></rect>
<rect id="r11" class="for_r11" x="0" y="561" height="1" width="20" fill="#e15759" fill-opacity="1"><title>Donations:
$5</title></rect>
</g>
<g class="node">
<rect id="r12_border" class="for_r12" x="258.37733" y="373.45788" height="12.33075" width="20" stroke="rgb(58, 90, 87)" stroke-width="2" fill="none"></rect>
<rect id="r12" class="for_r12" x="258.37733" y="373.45788" height="12.33075" width="20" fill="#76b7b2" fill-opacity="1"><title>Bounty Program:
$1,800</title></rect>
</g>
<g class="node">
<rect id="r13_border" class="for_r13" x="258.37733" y="431.38063" height="83.43122" width="20" stroke="rgb(44, 79, 39)" stroke-width="2" fill="none"></rect>
<rect id="r13" class="for_r13" x="258.37733" y="431.38063" height="83.43122" width="20" fill="#59a14f" fill-opacity="1"><title>2023 OC Balance:
$12,179</title></rect>
</g>
<g class="node">
<rect id="r14_border" class="for_r14" x="258.37733" y="560.40385" height="1.59615" width="20" stroke="rgb(116, 98, 36)" stroke-width="2" fill="none"></rect>
<rect id="r14" class="for_r14" x="258.37733" y="560.40385" height="1.59615" width="20" fill="#edc949" fill-opacity="1"><title>OSC Host Fees:
$233</title></rect>
</g>
</g>
<g id="sankey_labels" font-family="Inter, sans-serif" font-size="18px" fill="#000000">
<rect id="label0_bg" class="for_r0" x="-113.328" y="65.58885" width="109.87333" height="55.78228" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label0" class="for_r0" text-anchor="end" x="-9.59133" y="93.22748" font-weight="400" font-size="17.0856px" dy="-5.78113">Tidelift<tspan x="-9.591333084106443" dy="25.26228" font-weight="400" font-size="23.594399999999993px">$27,500</tspan></text>
<rect id="label1_bg" class="for_r1" x="55.51866" y="16.05225" width="167.33998" height="49.50551" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label1" class="for_r1" text-anchor="middle" x="139.18866" y="41.1025" font-weight="400" font-size="14.86943px" dy="-5.19275">Tidelift Partnerships*<tspan x="139.18866455078125" dy="21.98551" font-weight="400" font-size="20.533974468085106px">$12,000</tspan></text>
<rect id="label2_bg" class="for_r2" x="281.83199" y="42.6334" width="107.72331" height="53.27159" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label2" class="for_r2" text-anchor="start" x="287.96866" y="69.71669" font-weight="400" font-size="16.06387px" dy="-6.22579">Seth Larson<tspan x="287.96866218566896" dy="23.75159" font-weight="400" font-size="22.183445106382976px">$20,354</tspan></text>
<rect id="label3_bg" class="for_r3" x="80.71033" y="154.3175" width="116.95667" height="52.24543" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label3" class="for_r3" text-anchor="middle" x="139.18866" y="180.88772" font-weight="400" font-size="15.36986px" dy="-5.71272">Tidelift Lifters<tspan x="139.18866455078125" dy="22.72543" font-weight="400" font-size="21.225038297872338px">$15,500</tspan></text>
<rect id="label4_bg" class="for_r4" x="281.83199" y="190.88008" width="121.18999" height="48.85609" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label4" class="for_r4" text-anchor="start" x="287.96866" y="215.60563" font-weight="400" font-size="14.4302px" dy="-4.86805">Quentin Pradet<tspan x="287.96866218566896" dy="21.33608" font-weight="400" font-size="19.927417872340424px">$8,928</tspan></text>
<rect id="label5_bg" class="for_r5" x="281.83199" y="286.13322" width="94.40666" height="47.08235" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label5" class="for_r5" text-anchor="start" x="287.96866" y="309.82189" font-weight="400" font-size="13.9069px" dy="-4.83117">Illia Volochii<tspan x="287.96866218566896" dy="20.56234" font-weight="400" font-size="19.20476255319149px">$5,268</tspan></text>
<rect id="label6_bg" class="for_r6" x="-152.91132" y="270.92576" width="149.45667" height="52.97096" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label6" class="for_r6" text-anchor="end" x="-9.59133" y="297.85874" font-weight="400" font-size="15.86056px" dy="-6.07548">2022 OC Balance<tspan x="-9.591333084106443" dy="23.45097" font-weight="400" font-size="21.902675744680852px">$18,932</tspan></text>
<rect id="label7_bg" class="for_r7" x="69.08533" y="325.69755" width="140.20667" height="54.46354" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label7" class="for_r7" text-anchor="middle" x="139.18866" y="353.52681" font-weight="400" font-size="16.1937px" dy="-5.97177">Open Collective<tspan x="139.18866455078125" dy="23.94354" font-weight="400" font-size="22.36272680851064px">$21,262</tspan></text>
<rect id="label8_bg" class="for_r8" x="-127.27799" y="389.63301" width="123.82334" height="46.25318" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label8" class="for_r8" text-anchor="end" x="-9.59133" y="412.90711" font-weight="400" font-size="13.34613px" dy="-4.41661">GitHub Sponsors<tspan x="-9.591333084106443" dy="19.73321" font-weight="400" font-size="18.430376170212764px">$1,346</tspan></text>
<rect id="label9_bg" class="for_r9" x="-99.92799" y="441.96934" width="96.47333" height="46.0955" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label9" class="for_r9" text-anchor="end" x="-9.59133" y="465.16457" font-weight="400" font-size="13.23947px" dy="-4.33775">Sourcegraph<tspan x="-9.591333084106443" dy="19.57551" font-weight="400" font-size="18.28308085106383px">$600</tspan></text>
<rect id="label10_bg" class="for_r10" x="-91.66133" y="490.93797" width="88.20667" height="46.04881" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label10" class="for_r10" text-anchor="end" x="-9.59133" y="514.10985" font-weight="400" font-size="13.20787px" dy="-4.31439">Thanks.dev<tspan x="-9.591333084106443" dy="19.52879" font-weight="400" font-size="18.239445106382977px">$379</tspan></text>
<rect id="label11_bg" class="for_r11" x="-82.36133" y="538.36766" width="78.90666" height="45.96971" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label11" class="for_r11" text-anchor="end" x="-9.59133" y="561.5" font-weight="400" font-size="13.1544px" dy="-4.27485">Donations<tspan x="-9.591333084106443" dy="19.44972" font-weight="400" font-size="18.165599999999998px">$5</tspan></text>
<rect id="label12_bg" class="for_r12" x="281.83199" y="356.30116" width="120.77333" height="46.34919" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label12" class="for_r12" text-anchor="start" x="287.96866" y="379.62326" font-weight="400" font-size="13.41105px" dy="-4.4646">Bounty Program<tspan x="287.96866218566896" dy="19.82919" font-weight="400" font-size="18.520017021276594px">$1,800</tspan></text>
<rect id="label13_bg" class="for_r13" x="281.83199" y="448.02708" width="141.25667" height="49.54335" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label13" class="for_r13" text-anchor="start" x="287.96866" y="473.09624" font-weight="400" font-size="14.89502px" dy="-5.21167">2023 OC Balance<tspan x="287.96866218566896" dy="22.02336" font-weight="400" font-size="20.56931744680851px">$12,179</tspan></text>
<rect id="label14_bg" class="for_r14" x="281.83199" y="538.04545" width="108.60668" height="46.01792" rx="4.5" fill="#fff" fill-opacity="0.8" stroke="none" stroke-width="0" stroke-opacity="0"></rect>
<text id="label14" class="for_r14" text-anchor="start" x="287.96866" y="561.20193" font-weight="400" font-size="13.187px" dy="-4.29896">OSC Host Fees<tspan x="287.96866218566896" dy="19.49792" font-weight="400" font-size="18.210617872340425px">$233</tspan></text>
</g>
</g></svg>
<br><br><p><small><i>* Seth Larson was also paid $7,000 by Tidelift for a packaging security standards project and $5,000 as a part of their "lifter advocate" program. Neither of these projects are directly related to urllib3 but are listed for completeness.</i></small></p>
</center>
</div>
</div>

## Maintenance update

<p>
<strong>2023 marks the <a href="https://pypi.org/project/urllib3/0.2/">15th anniversary</a> of urllib3 being first published to PyPI! 🥳</strong> Not many open source projects stand the test of time and continue to see the widespread usage that urllib3 does every day. We attribute our longevity to quickly elevating contributors from our community into project maintainers <strong>which we believe is a critical property of a sustainable open source project. </strong>Financial rewards through our bounty program is a crucial piece of our approach to staying sustainable for the long-term.
</p>

<div class="row">
<div class="col-7">
<p>
This year we welcomed a new core maintainer to our team, <strong><a href="http://github.com/illia-v">Illia Volochii</a></strong>! 🎉 Illia has been putting in high quality and consistent work to get v2.0 out the door. Illia started contributing to urllib3 in 2022 and after landing multiple high-quality pull requests was asked to join the team of collaborators and begin reviewing PRs and issues and helping with the release process.
</p>
<p>
After adding Illia we now have three core maintainers including Seth Larson and Quentin Pradet, in addition to multiple collaborators and community contributors.
</p>
</div>
<div class="col-5">
<center>
<img src="http://github.com/illia-v.png" style="max-width: 100%;"/>
</center>
</div>
</div>
<p>
We landed <a href="https://github.com/urllib3/urllib3/graphs/contributors?from=2023-01-01&to=2023-12-31&type=c">160 commits from 13 unique contributors</a> during 2023 which is up from ~130 commits during 2022. We published <a href="https://github.com/urllib3/urllib3/releases">16 releases</a> to PyPI in 2023, up from 8 in 2022.
</p>
<p>
From a security perspective, we continue to lead the pack for Python packages in terms of implementing security standards. urllib3 is the <a href="https://github.com/sethmlarson/pypi-scorecards#openssf-scorecards-for-top-python-packages">highest rated project</a> according to <a href="https://securityscorecards.dev/">OpenSSF Scorecard</a> with a score of <a href="https://deps.dev/pypi/urllib3">9.6 out of 10</a> overall. We also were an <a href="https://github.com/urllib3/urllib3/pull/3028">early adopter of Trusted Publishers</a>, adopting the new feature days after they were announced during PyCon US 2023.
</p>
<p>
We remediated two <a href="https://github.com/urllib3/urllib3/security/advisories/GHSA-v845-jxx5-vc9f">moderate-severity</a> <a href="https://github.com/urllib3/urllib3/security/advisories/GHSA-g4mx-q9vg-27p4">vulnerabilities</a> in 2023 and made the fixes available in both the new v2.0 and security-fix only v1.26.x release streams. <strong>Support for the previous major version of urllib3 is provided thanks to funding from Tidelift.</strong>
</p>

## Support for HTTP/2

When you first read this post you might have thought:

> *“Hasn't HTTP/2 been around for a long time?”* 🤔

And you'd be right! HTTP/2 was published in 2015 in RFC 7540 and is now used for the
[majority of web requests](https://blog.cloudflare.com/http3-usage-one-year-on). HTTP/2 and has been around for so long that there's
an already HTTP/3!

So why are we only *just now* starting to add support for HTTP/2 to urllib3? The reason
is that the standard library module `http.client` only supports HTTP/1 and before urllib3 v2.0
was released urllib3 was **strongly tied to `http.client` APIs**. By breaking backwards compatibility in a few
key ways (while maintaining compatibility where it matters for most users) we've been able
to set the stage for adding HTTP/2 to urllib3! 🚀

urllib3 is in good company: many of Python's stable HTTP clients don't support HTTP/2 like
Requests (which uses urllib3 under the hood), aiohttp, and httplib2.

Even though we're waiting to release HTTP/2 support until after our fundraiser concludes,
we aren't waiting to get started. Our team has already started some of the required prep-work to implement HTTP/2. 
Want to follow along? We have a [top-level tracking issue for HTTP/2 support](https://github.com/urllib3/urllib3/issues/3000) on GitHub.

Over the past two months Quentin has migrated our test suite from the
venerable Tornado web backend to using the [Hypercorn](https://pgjones.gitlab.io/hypercorn/)
server and [Quart](https://quart.palletsprojects.com/en/latest/) microframework. Our test
application communicates with the server using [ASGI](https://asgi.readthedocs.io/en/latest/),
which is perfect for our use-case: low-level enough to satisfy the needs of the test suite and
high-level enough to abstract the differences between HTTP/1 and HTTP/2. Now that the test
suite runs with both HTTP/1 and HTTP/2, we can start developing HTTP/2 with an extensive
initial battery of test cases.

## Support for Webassembly and Emscripten

When PyScript was [first announced at PyCon US 2022](https://www.youtube.com/watch?v=qKfkCY7cmBQ) during a keynote by Peter Wang,
Seth was sitting front row to witness Python moving to the web. Later that same day in the PyScript open space there were experiments for making HTTP
requests with urllib3 and Pyodide together using a synchronous call to the JavaScript `fetch()` API. At the time, despite having assistance
from PyScript maintainers, there didn't seem to be a way forwards *yet*.

Fast-forward to today, the [pyodide-http](https://github.com/koenvo/pyodide-http) project has figured out how to make a synchronous or streaming HTTP exchange using
the `fetch()` and `XMLHttpRequest` JavaScript APIs along with Web Workers. Now that a synchronous approach to HTTP requests
was possible we could add support to urllib3!

Thanks to **Joe Marshall**, urllib3 [now has experimental support for the Emscripten platform](https://github.com/urllib3/urllib3/pull/3195), complete with
bundling a small JavaScript stub for Web Worker support and testing against Chrome and Firefox in our CI.
What's next is to thoroughly test and document the feature. We're aiming to release stable Emscripten support for urllib3 in 2024.

The most exciting part of this is that once a core dependency like urllib3 has been made compatible with Emscripten we'll likely see a wave of other
packages that immediately become compatible too, bringing even more of the Python package ecosystem to the web 🥳

## Stable release of urllib3 v2.0

urllib3 had its [first stable release of v2.0](https://sethmlarson.dev/urllib3-2.0.0) in April 2023 and later the v2.1.0 release to remove many long-deprecated features like the `[secure]` extra which had become redundant with new improvements to the `ssl` standard library module and the `urllib3.contrib.securetransport` module which was needed on macOS due to unavailability of an OpenSSL library on the platform to perform HTTPS with PyPI.

This release also put the project in a good place for future improvements like those discussed above.
The biggest blocker to adopting new HTTP implementations were vestigial APIs from urllib3 primarily subclassing the standard libraries `http.client` (or for Python 2: `httplib`) modules.

By removing and discouraging these implicit APIs we're better able to adopt alternate HTTP implementations such as the `h2` library for HTTP/2 and JavaScript's `fetch` API for Emscripten.

### Increasing adoption of urllib3 v2.x

The initial adoption of urllib3 v2.x was lower than expected, due to the following factors:

* By default, RedHat Enterprise Linux 7 (RHEL 7), AWS Lambda, Amazon Linux 2 and [Read the Docs](https://about.readthedocs.com) were all compiling the `ssl` module with OpenSSL 1.0.2. While botocore still pinned urllib3 to 1.26.x, Amazon Linux 2 was more popular than we expected and many users were not pinning or resolving their dependencies correctly and thus were receiving an incompatible version of urllib3.
* Various third-party packages like dockerpy, request-toolbelt and vcrpy were relying on implementation details of urllib3 that were deprecated or removed in v2.0 so couldn’t upgrade right away.
* And finally, we intentionally removed the `strict` parameter from `HTTPResponse` which had no effect since Python 3. This affected only a few users.

After a few weeks, we had around 3 millions daily downloads for v2.0. That's a lot of downloads, but only accounted for **30% of 1.26.x downloads** at the time without any obvious upward trend. The only exception was Read the Docs that [encouraged users to move to Ubuntu 22.04 and Python 3.11](https://blog.readthedocs.com/migrate-configuration-v2/) shortly after the urllib3 2.0 release. To avoid a prolonged split in the ecosystem, we took various actions to help migrating to 2.x:

* Helped some libraries upgrade, including [requests](https://github.com/psf/requests/pull/6434), [docker-py](https://github.com/docker/docker-py/pull/3116), [vcrpy](https://github.com/kevin1024/vcrpy/issues/693), and [requests-toolbelt](https://github.com/requests/toolbelt/pull/355).
* We added [common migration issues](https://urllib3.readthedocs.io/en/stable/v2-migration-guide.html#common-upgrading-issues) to the v2 migration guide.
* With help from a LibreSSL developer and a Gentoo user, we[ added back LibreSSL support](https://github.com/urllib3/urllib3/pull/3024)<span style="text-decoration:underline;">.</span>
* To allow [google-auth-library-python](https://github.com/googleapis/google-auth-library-python/pull/1290#issuecomment-1548289723) and the rest of the Google ecosystem to upgrade, we added back pyOpenSSL to allow in-memory certificate support.

Our friend and Requests maintainer, Nate Prewitt [allowed urllib3 v2.0 for Python 3.10+ users of botocore](https://github.com/boto/botocore/pull/3034). This work on Requests inspired [snowflake-connector-python](https://github.com/snowflakedb/snowflake-connector-python/pull/1799) to follow suit.

Today, most popular libraries support urllib3 2.0 and later, at least with Python 3.10 and above. And the libraries that don't support it yet [get requests from users](https://github.com/elastic/elastic-transport-python/issues/102). urllib3 2.x is [reliably above 70% of 1.26.x downloads](https://www.pepy.tech/projects/urllib3?versions=2.*&versions=1.26.*) and growing. Additionally, Python 3.10+ users already download 2.x more than 1.26.x, making us confident that the ecosystem split will eventually disappear in favor of the newest major version of urllib3.

👋 That's all for now, if you want to discuss this article you can [join our community Discord](https://discord.gg/urllib3). Please share this article to help spread the word of our fundraiser and coming HTTP/2 support.
