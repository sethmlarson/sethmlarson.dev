# Building software for connection (#2: Consensus)

<center><blockquote>This is the second article in a series about “<em>software for connection</em>”.</blockquote></center>

<p>In the <a href="/building-software-for-connection-local-first">previous article</a> we concluded that a persistent always-on internet
connection isn't required for software to elicit feelings of connection between humans.</p>

<div class="row">
<div class="col-7">
<p>Building on this conclusion: let's explore how Animal Crossing software was able to intercommunicate without requiring
a centralized server and infrastructure and the trade-offs for these design decisions.</p>

</div>
<div class="col-5">
<center>
<img style="max-width: 100%; border: 2px solid black" src="https://dodo.ac/np/images/e/e2/Tom_Nook%27s_Special_Delivery.png"/><br>
<small><em>Image of Tom Nook from an Animal Crossing online contest</em> (<a href="https://nookipedia.com/wiki/Secret_code">Nookipedia</a>)</small>
</center>
</div>
</div>

## Distributing digital goods without the internet

Animal Crossing has over 1,000 unique items that need to be collected
for a complete [catalog](https://nookipedia.com/wiki/Catalog), including furniture, wallpapers, clothing, parasols, and carpets.
Many of these items are quite rare or were only programmed to be accessible
through an official Nintendo-affiliated distribution such as a magazine or online contest.

Beyond official distributions, it's clear Animal Crossings' designer, Katsuya Eguchi,
wanted players to <em>cooperate</em> to complete their catalogs.
The game incentivized trading items between towns by assigning
one “[native fruit](https://nookipedia.com/wiki/Fruit)” (Apple, Orange, Cherry, Peach, or Pear) and
randomly making a subset of items harder to find than others depending
on a <a href="https://nookipedia.com/wiki/Group">hidden “item group” variable</a> (either A, B, or C).

Items could be exchanged between players when one player visits another town,
but this required physically bringing your memory card to another
players' GameCube. The GameCube might have come with a handle, but the 'cube wasn't exactly a *portable console*. Sharing a physical space isn't something you can do with everyone or on a regular basis.

<div class="row">
<div class="col-6">
<p>So what did Katsuya Eguchi design for Animal Crossing? To allow for item distributions from magazines and contests and to make <nobr>player-to-player</nobr> item sharing easier <nobr>Animal Crossing</nobr> included a feature called <nobr>“<a href="https://nookipedia.com/wiki/Secret_code">secret codes</a>”</nobr>.</p>

<p>This feature worked by allowing players to exchange 28-character codes with Tom Nook for items. Players could also generate codes for their friends to “send” an item from their own game to a different town. Codes could be shared by writing them on a paper note, instant message, or text message.</p>
</div>
<div class="col-6">
<center>
<p>
<iframe width="100%" height="300px" src="https://www.youtube.com/embed/c3Gsu3HPx0c" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<br><small><i>Huntr R. explaining how “secret codes” are implemented. A 
surprising amount of cryptography!</i></small>
</p>
</center>
</div>
</div>

<h2>The forgotten durability of offline software</h2>

<div class="row">
<div class="col-9 col-12-sm">
<p>
This <a href="https://www.reddit.com/r/Gamecube/comments/1gqfbae">Reddit comment thread</a> from the GameCube subreddit was the initial inspiration for this entire series.
The post is about someone's niece who just started playing Animal Crossing for the first time.
The Redditor asked folks to send items to their nieces' town using the secret code system.
</p>
<p>This ended up surprising many folks that this system 
<em>still worked</em> in a game that was over 23 years old!
For reference, Nintendo Wi-Fi Connection and Nintendo Network were only available for 8 and 13 years respectively.
Below are a handful of the comments from the thread:</p>

<blockquote>
<ul>
<li>“That's still online???”</li>
<li>“It was online???!”</li>
<li>“For real does this still work lol?”</li>
<li>“...Was it ever online?”</li>
</ul>
</blockquote>
</div>
<div class="col-3 col-12-sm">
<center>
<p>
<img style="max-width: 100%" src="https://dodo.ac/np/images/1/19/Wario%27s_Woods_PG_Model.png"/>
<br><nobr>secret code</nobr> for my favorite Animal Crossing NES game <nobr><a href="https://nookipedia.com/wiki/NES_game">Wario's Woods</a>:</nobr><br><br>
<span style="font-family: monospace; 
font-size: 1.1em;
">Xvl5HeG&C9prXu<br>IWhuzBinlVlqOg</span>
</p>
</center>
</div>
</div>

It's hard not to take these comments as indicators that something is
*very wrong* with internet-connected software today. What had to go wrong for a 
system continuing to work to *be met with surprise*? Many consumers' 
experience with 
software products
today is that they become useless e-waste after some far-away service is 
discontinued a few years after purchase.

My intuition from this is that software that *requires centralized servers and infrastructure to function*
will have shorter lifetimes than software which is offline or only
opportunistically uses online functionality.

I don't think this is particularly insightful,
more dependencies always means less resilience. But if we're building software for human connection then the software
should optimally only be limited by the *availability of humans to connect*.

## What is centralization good for?

<div class="row">
<div class="col-6">
<center>
<p>
<svg xmlns="http://www.w3.org/2000/svg" style="max-width:100%;max-height:251px;" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="421px" viewBox="-0.5 -0.5 421 251"><defs/><g><g data-cell-id="0"><g data-cell-id="1"><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-1"><g><rect x="1" y="50" width="60" height="20" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-width="2" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 58px; height: 1px; padding-top: 60px; margin-left: 2px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">CODETYPE</div></div></div></foreignObject><text x="31" y="64" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">CODETYPE</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-2"><g><rect x="101" y="50" width="40" height="20" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-width="2" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 38px; height: 1px; padding-top: 60px; margin-left: 102px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">HIT%</div></div></div></foreignObject><text x="121" y="64" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">HIT%</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-3"><g><rect x="141" y="50" width="20" height="20" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-width="2" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 18px; height: 1px; padding-top: 60px; margin-left: 142px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">S?</div></div></div></foreignObject><text x="151" y="64" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">S?</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-4"><g><rect x="161" y="50" width="160" height="20" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-width="2" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 158px; height: 1px; padding-top: 60px; margin-left: 162px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">NPC CODE</div></div></div></foreignObject><text x="241" y="64" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">NPC CODE</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-5"><g><rect x="1" y="70" width="320" height="80" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-width="2" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 318px; height: 1px; padding-top: 110px; margin-left: 2px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">PLAYER NAME</div></div></div></foreignObject><text x="161" y="114" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">PLAYER NAME</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-7"><g><rect x="1" y="230" width="320" height="20" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-width="2" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 318px; height: 1px; padding-top: 240px; margin-left: 2px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">ITEM NUMBER</div></div></div></foreignObject><text x="161" y="244" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">ITEM NUMBER</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-11"><g><rect x="1" y="150" width="320" height="80" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-width="2" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 318px; height: 1px; padding-top: 190px; margin-left: 2px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">TOWN NAME</div></div></div></foreignObject><text x="161" y="194" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">TOWN NAME</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-12"><g><rect x="61" y="50" width="40" height="20" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-width="2" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 38px; height: 1px; padding-top: 60px; margin-left: 62px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">CHKSM</div></div></div></foreignObject><text x="81" y="64" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">CHKSM</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-13"><g><path d="M 351 50 L 346 50 Q 341 50 341 60 L 341 140 Q 341 150 336 150 L 333.5 150 Q 331 150 336 150 L 338.5 150 Q 341 150 341 160 L 341 240 Q 341 250 346 250 L 351 250" fill="none" stroke="#000" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke-width="2" stroke-miterlimit="10" transform="translate(341,0)scale(-1,1)translate(-341,0)" pointer-events="all"/></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-14"><g><path d="M 91 -50 L 86 -50 Q 81 -50 81 -40 L 81 20 Q 81 30 76 30 L 73.5 30 Q 71 30 76 30 L 78.5 30 Q 81 30 81 40 L 81 100 Q 81 110 86 110 L 91 110" fill="none" stroke="#000" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke-width="2" stroke-miterlimit="10" transform="translate(81,0)scale(-1,1)translate(-81,0)rotate(90,81,30)" pointer-events="all"/></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-15"><g><rect x="61" y="0" width="60" height="20" fill="none" stroke="none" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 58px; height: 1px; padding-top: 10px; margin-left: 62px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">1 byte</div></div></div></foreignObject><text x="91" y="14" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">1 byte</text></switch></g></g></g><g data-cell-id="0E_N90nrnBhNrJIXYFuZ-16"><g><rect x="361" y="130" width="60" height="40" fill="none" stroke="none" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 58px; height: 1px; padding-top: 150px; margin-left: 362px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: monospace; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">20 bytes total</div></div></div></foreignObject><text x="391" y="154" fill="light-dark(#000, #fff)" font-family="monospace" font-size="12px" text-anchor="middle">20 bytes t...</text></switch></g></g></g></g></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.drawio.com/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg><br>
<small><em>Data layout of secret codes before being encrypted (<a href="https://github.com/ACreTeam/ac-decomp/blob/66325624aad8ab2d9950d9e3e70641aa2e65c238/src/game/m_mail_password_check.c#L338">Animal Crossing decompilation project</a>)</em></small></p>
</center>

</div>
<div class="col-6">
<p>Animal Crossings' secret code system is far from perfect. The system is easily abusable, as the same secret codes can be
reused over-and-over by the same user to duplicate items without ever expiring. The only limit was that 3 codes could be used per day.</p>
<p>Secret codes are tied to a specific
town and recipient name, but even this stopgap can be defeated by <a href="https://nookipedia.com/wiki/Community:Project_Hyrule">setting your name
and town name to specific values</a> to share codes across many different players.</p>
<p>
</div>
</div>

Not long after Animal Crossing's release
the secret code algorithm was [reverse-engineered](https://togenyanweb.appspot.com/Yokai/eplus/eplus.html) so secret codes 
for any item could be created for any town and recipient name as if they came from an official Nintendo distribution.
This was possible because the secret code system relied on "[security through obscurity](https://en.wikipedia.org/wiki/Security_through_obscurity)".

Could *centralization* be the answer to preventing these abuses?

The most interesting property that a centralized authority approach
provides is *global consensus*: forcing everyone to play by the same rules. By storing
the “single source-of-truth” a central authority is able to prevent abuses
like the ones mentioned above.

For example, a centralized “secret code issuing server” could generate
new unique codes per-use and check each code's validity
against a database to prevent users from generating their
own illegitimate codes or codes being re-used multiple times.

The problem with
centralized consensus is it tends to be *viral* to cover the entire software state.
A centralized server can generate codes perfectly, but how can that same server
*know* that the items you're exchanging for codes were obtained legitimately? To know this
the server would *also need to track item legitimacy*, leading to software which requires
an internet connection to operate.

This is optimal from a correctness perspective, but as was noted earlier,
I suspect that if such a server was a mandatory part of the secret code system
in Animal Crossing that the system *would likely not be usable today*.

This seems like a trade-off, *which future would you rather have?*

## Redesigning Animal Crossing secret codes

If I were designing Animal Crossings' secret code system with modern hardware, what would it look like?
How can we keep the offline fall-back while providing consensus and being less
abusable, especially for official distributions.

I would likely use a [public-key cryptographic](https://en.wikipedia.org/wiki/Public-key_cryptography) system for official distributions,
embedding a certificate that could be used to “verify” that specific secret codes
originated from the expected centralized entity. Codes that are accepted would be
recorded to prevent reusing the same code multiple times in the same town.
Using public-key cryptography prevents the
system from being reverse-engineered to distribute arbitrary items until the certificate
private key was cracked.

For sharing items between players I would implement a system where each town
generated a public and private key and the public key was shared to other towns
whenever the software was able to, such as when a player visited the other town.
Players would only be able to send items to players that they have visited
(which for Animal Crossing *required physical presence*, more on this later!)

Each sender could store a [nonce](https://en.wikipedia.org/wiki/Cryptographic_nonce) value for
each potential recipient. Embedding that nonce into the secret code would allow
the recipients' software to verify that the specific code hadn't been used yet.
The nonce wouldn't have to be long to avoid simple reusing of codes.

Both above systems would require much more data to be embedded into each “secret
code” compared to the 28-character codes from the GameCube. For this I would
use QR codes to embed over 2KB of data into a single QR code. Funnily enough,
Animal Crossing New Leaf and onwards [use QR code technology](https://nookipedia.com/wiki/QR_code) for players to share design patterns.

This design is still abusable if users can modify their software or hardware
but doesn't suffer from the trivial-to-exploit flaws of Animal Crossing's secret code system.

## Decentralized global consensus?

<div class="row">
<div class="col-7">
<p>What if we could have the best of both worlds: we want consensus
that is both <em>global</em> and <em>decentralized</em>. At least today, we are out of luck.</p>
<p>Decentralized global consensus is <a href="https://bitcoin.org/bitcoin.pdf">technologically feasible</a>, but the existing solutions
(mostly blockchains)
are expensive (both in energy and capital) and can't handle throughput on any sort of 
meaningful scale.</p>
</div>
<div class="col-5">
<p>
<center>
<svg xmlns="http://www.w3.org/2000/svg" style="max-width:100%;max-height:192px;" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="245px" viewBox="-0.5 -0.5 245 192"><defs/><g><g data-cell-id="0"><g data-cell-id="1"><g data-cell-id="WkH8meBGehNytEoZtZKf-1"><g><ellipse cx="60" cy="130" rx="60" ry="60" fill="transparent" stroke="#000" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" pointer-events="all"/></g></g><g data-cell-id="WkH8meBGehNytEoZtZKf-2"><g><ellipse cx="140" cy="130" rx="60" ry="60" fill="transparent" stroke="#000" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" pointer-events="all"/></g></g><g data-cell-id="WkH8meBGehNytEoZtZKf-3"><g><ellipse cx="100" cy="60" rx="60" ry="60" fill="transparent" stroke="#000" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" pointer-events="all"/></g></g><g data-cell-id="WkH8meBGehNytEoZtZKf-4"><g><rect x="10" y="130" width="60" height="10" fill="none" stroke="none" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 58px; height: 1px; padding-top: 135px; margin-left: 11px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: &quot;monospace&quot;; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">Efficient</div></div></div></foreignObject><text x="40" y="139" fill="light-dark(#000, #fff)" font-family="&quot;monospace&quot;" font-size="12px" text-anchor="middle">Efficient</text></switch></g></g></g><g data-cell-id="WkH8meBGehNytEoZtZKf-5"><g><rect x="50" y="30" width="100" height="10" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212));" stroke="none" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 98px; height: 1px; padding-top: 35px; margin-left: 51px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: &quot;monospace&quot;; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">Decentralized</div></div></div></foreignObject><text x="100" y="39" fill="light-dark(#000, #fff)" font-family="&quot;monospace&quot;" font-size="12px" text-anchor="middle">Decentralized</text></switch></g></g></g><g data-cell-id="WkH8meBGehNytEoZtZKf-6"><g><rect x="140" y="130" width="60" height="10" fill="none" stroke="none" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 58px; height: 1px; padding-top: 135px; margin-left: 141px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: &quot;monospace&quot;; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">Global</div></div></div></foreignObject><text x="170" y="139" fill="light-dark(#000, #fff)" font-family="&quot;monospace&quot;" font-size="12px" text-anchor="middle">Global</text></switch></g></g></g><g data-cell-id="WkH8meBGehNytEoZtZKf-7"><g><path d="M 180 60 L 105.55 101.84" fill="none" stroke="#000" style="stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke-miterlimit="10" pointer-events="stroke"/><path d="M 100.97 104.41 L 105.36 97.93 L 105.55 101.84 L 108.79 104.03 Z" fill="#000" style="fill: light-dark(rgb(0, 0, 0), rgb(255, 255, 255)); stroke: light-dark(rgb(0, 0, 0), rgb(255, 255, 255));" stroke="#000" stroke-miterlimit="10" pointer-events="all"/></g></g><g data-cell-id="WkH8meBGehNytEoZtZKf-8"><g><rect x="164" y="45" width="80" height="10" fill="#fff" style="fill: light-dark(#fff, var(--ge-dark-color, #121212));" stroke="none" pointer-events="all"/></g><g><g transform="translate(-0.5 -0.5)"><switch><foreignObject style="overflow: visible; text-align: left;" pointer-events="none" width="100%" height="100%" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: unsafe center; justify-content: unsafe center; width: 78px; height: 1px; padding-top: 50px; margin-left: 165px;"><div style="box-sizing: border-box; font-size: 0; text-align: center; color: #000; "><div style="display: inline-block; font-size: 12px; font-family: &quot;monospace&quot;; color: light-dark(#000, #fff); line-height: 1.2; pointer-events: all; white-space: normal; word-wrap: normal; ">Impossible?</div></div></div></foreignObject><text x="204" y="54" fill="light-dark(#000, #fff)" font-family="&quot;monospace&quot;" font-size="12px" text-anchor="middle">Impossible?</text></switch></g></g></g></g></g></g><switch><g requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"/><a transform="translate(0,-5)" xlink:href="https://www.drawio.com/doc/faq/svg-export-text-problems" target="_blank"><text text-anchor="middle" font-size="10px" x="50%" y="100%">Text is not SVG - cannot display</text></a></switch></svg>
<br><small>Pick two: Decentralized, Global, and Efficient</small>
</center>
</p>
</div>
</div>

There are many other decentralized consensus systems that 
are able to form “pockets” of *useful peer-to-peer consensus* using a fraction of
the resources, such as email, [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent), [ActivityPub](https://activitypub.rocks/), and [Nostr](https://nostr.com/).
These systems are only possible by adding *some centralization* or by only guaranteeing *local consensus*.

## When is global consensus needed?

Obviously global consensus is important for certain classes of software like 
financial, civics, and infrastructure, but I wonder how the necessity
of consensus in software changes for software with different risk
profiles.

For software which has fewer risks associated with misuse is there as much
need for global consensus?
How can *software for connection* be designed to reduce risk and require
less consensus to be effective? If global consensus and centralized 
servers become unnecessary, can we expect *software for connection* to be usable 
on much longer timescales, *essentially for as long as there are users?*
