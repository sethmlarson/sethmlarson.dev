# Building software for connection (#1: Local-First)

<center><blockquote>This is the first article in a series about <em>software for connection</em>.</blockquote></center>

Feeling connected to others is a basic human need,
so it is no surprise we want software to enable human connection.
The surprise is that despite computing device ownership and internet usage 
being at an all-time high, [feelings of loneliness](https://www.hhs.gov/sites/default/files/surgeon-general-social-connection-advisory.pdf) have also never been higher.

The shape of today's “<em>software for connection</em>” uses 
centralized servers in the cloud, algorithmic curation, and incentives 
optimized 
for users to
connect with 
<em>the 
platform</em> <nobr>(aka “<em>engagement</em>” and</nobr> “<em><a href="https://en.wikipedia.org/wiki/Parasocial_interaction">parasociality</a></em>”), not necessarily 
<em>with other humans</em>. Software for connection has followed in the same rut created by
big tech, as can be seen in protocols, browsers, and infrastructure.

The software we 
have today feels 
like a *tiny fraction
of what should be possible* in a world full of people with personal 
computing devices in their pockets.
There's no problem with a well-traveled road (it's the road that led 
you 
here, after all ❤️), but maybe you'll join me for a walk [down a less-traveled path](https://www.poetryfoundation.org/poems/44272/the-road-not-taken)
to explore how software can connect people outside the common paradigms
and what assumptions and restrictions we can drop to enable
different methods of connection.

<div class="row">
<div class="col-5 col-12-sm">
<center>
<p><img style="border: black solid 2px; max-width: 100%;" src="https://dodo.
ac/np/images/thumb/3/32/DnM%2B_Box.png/844px-DnM%2B_Box.png"/>
<br>
<small>Dōbutsu no Mori+ cover art (<a href="https://archive.
org/details/doubutsu-no-mori-plus-scans">archive.org</a>)</small></p>
</center>
</div>
<div class="col-7 col-12-sm">
<p>This 7-part series explores 
the feeling of “<em>connection without connectivity</em>”
through the design of an offline video-game: <em>Animal Crossing</em></p>

<p>Animal Crossing, known in Japan as <nobr>“<a href="https://nookipedia.com/wiki/Doubutsu_no_Mori%2B">Dōbutsu no Mori+</a>”</nobr>
(<nobr>どうぶつの森+</nobr>), was released on the GameCube in December 2001.
According to director <nobr><a href="https://en.wikipedia.org/wiki/Katsuya_Eguchi">Katsuya
Eguchi</a></nobr> <nobr>(江口 勝也),</nobr>
Animal Crossing features three themes:</p>

<blockquote style="padding-left: 0.25em; padding-right: 0.25em
"><center><nobr>“family, 
friendship, and 
community”</nobr></center></blockquote>

<p>Animal Crossing is able to fulfill
these themes without <nobr><a href="https://en.wikipedia.org/wiki/GameCube_accessories#Modem_and_Broadband_adapters">
internet-connectivity</a></nobr>,
<nobr>LAN-play</nobr>, or even concurrent local multiplayer.
</p>

</div>
</div>

## Sharing spaces, not concurrently

This first article is about <em>space</em>, a place where people can
convene and feel togetherness. Spaces can be large or small, public
or private, or somewhere in between.

Sharing a space with others,
not necessarily at the same time, can evoke feelings of connection by
experiencing
changes to the space that others have made. By making your own changes to
a shared space, you are connecting to others in the future.

Animal Crossing didn't support any kind of concurrent multiplayer,
but that didn't stop the game from feeling like a <em>multiplayer experience</em>.
In the game, players would collect bugs and fish, decorate their house,
and plant trees and flowers. The many animal villagers
that lived in the town would “remember” past conversations with other
players, making the world feel more alive.

Because each player shared the same space with other players,
everyone can see the changes made to the town over time. Katsuya
Eguchi [remarked](https://web.archive.org/web/20160310171909/http://www.gamasutra.com/view/feature/2688/crossing_into_the_mainstream_.php)
on Animal Crossing being a shared space for his family to connect across time:

> “[My family is] playing games, and I'm playing games,
> but we're not really doing it together. It'd be nice to have a play experience
> where even though we're not playing at the same time, we're still sharing
> things together. ...[I wanted] to create a space where my family and I 
> could interact more, even if we weren't playing together.”

*What does this mean for modern software?* From this we learn that 
*concurrency is not needed to feel connected*. 
Today's internet-connected software 
typically requires a persistent connection,
often because *data doesn't exist on the same hardware that's running the 
software*.

Requiring a persistent connection presents accessibility problems: internet 
access isn't distributed evenly throughout the world. Even in places where internet connectivity is common,
a persistent connection isn't always possible (airplanes, subways, 
tunnels, inside a building, infrastructure outage).

Removing the need for real-time synchronization and data access
means that internet-connectivity *becomes optional*. Users can
then
*engage and create with the software at any time*, regardless of connectivity.
This empowers the user to weave the software into their own life and schedule
at an engagement level that works for them.

<div class="row">
<div class="col-8">
<p><a href="https://localfirstweb.dev/">Local-First Software</a> is a 
software design
paradigm that brings the benefits of colocated data and user interface 
to software. More details about the benefits of Local-First Software
are <a href="https://www.inkandswitch.com/local-first/">outlined by Ink and 
Switch</a>.</p>
<p>When adopting this paradigm, the onus is on the software to create a connected experience
with the data that the software has on hand. Compare this to
software demanding users be online and using the software
<em>as often as possible</em> to feel connected to a space.</p>
</div>
<div class="col-4">
<center>
<p>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800" 
style="max-width: 100%; margin-top: -2em; margin-bottom: -2em;">
  <defs>
    <g id="p">
      <path d="M-120 -270a120 120 0 0 1 240 0 480 120 -50 01-120 270 480 120 50 01-120-270"/>
      <circle cx="0" cy="-270" r="60" stroke-width="40" stroke="#fff" fill="none"/>
    </g>
  </defs>
  <use href="#p" transform="translate(400,535) rotate(-90)" fill="#ccc"/>
  <use href="#p" transform="translate(400,535) rotate(-45)" fill="#999"/>
  <use href="#p" transform="translate(400,535) rotate(0)" fill="#666"/>
  <use href="#p" transform="translate(400,535) rotate(45)" fill="#333"/>
  <use href="#p" transform="translate(400,535) rotate(90)" fill="#e6000e"/>
</svg>
<br><small><em>Local-First Software logo. The SVG is 
<a href="https://github.com/mylofi/localfirstweb.dev/blob/main/assets/images/logo.svg?short_path=47a4e07">impressively compact</a>.</em></small>
</p>
</center>
</div>
</div>

Future articles will discuss more implications for <em>software for connection</em> where connectivity is optional. If you've enjoyed this article it's likely you'll enjoy
the others, I hope you'll follow along for more. Thanks for reading!
