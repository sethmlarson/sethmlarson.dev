# Nintendo GameCube and Switch “Wrapped” 2025 🎮🎁

<blockquote style="text-align: center">
This is my last blog post for 2025 💜 Thanks for reading, see you in 2026!
</blockquote>

<!-- more -->

One of my goals for 2025 was to *play more games!*
I've been collecting play activity for my [Nintendo Switch,
Switch 2](https://sethmlarson.dev/nintendo-switch-play-activity-ocr), and my [Nintendo GameCube](https://sethmlarson.dev/setting-discord-status-from-physical-gamecube-console).
I've published a [combined SQLite database](https://github.com/sethmlarson/nintendo-play-activity-ocr/)
with this data for 2025 with games, play sessions,
and more. Feel free to dig into this data yourself, I've
included some queries and my own thoughts, too.

<!-- more -->

Here are the questions I answered with this data:

* [What were my favorite games this year?](#what-were-my-favorite-games-this-year)
* [Which game system did I play the most?](#what-were-my-favorite-games-this-year)
* [Which games did I play the most?](#which-game-system-did-i-play-the-most)
* [Which games did I play most per-session?](#which-games-did-i-play-most-per-session)
* [When did I start and stop playing each game?](#when-did-i-start-and-stop-playing-each-game)
* [Which game was I most consistently playing?](#which-game-was-i-most-consistently-playing)
* [When did I play games?](#when-did-i-play-games)
* [Which day of the week did I play most?](#which-day-of-the-week-did-i-play-most)

## What were my favorite games this year?

Before we get too deep into quantitative analysis,
let's start with the games I enjoyed the most
and defined this year for me.

<div class="row">
<div class="col-6">
<p>My favorite game for the GameCube in 2025 is <strong>Pikmin 2</strong>.
The Pikmin franchise has always held a close place in my
heart being a lover of plants, nature, and <a href="https://www.pikminwiki.com/Dandori">dandori</a>.</p>
<p>One of my major video-gaming projects in 2025 was
to <a href="https://sethmlarson.dev/pikmin-2-international-treasure-hoard">gather every unique treasure in Pikmin 2</a>. I called this
the “International Treasure Hoard” following a similar naming
to the “National PokéDex”. This project required buying both
the Japanese and PAL versions of Pikmin 2 which I was excited
to add to my collection.</p>
<p>The project was inspired by a YouTube short from
a Pikmin content creator I enjoy named “<a href="https://www.youtube.com/channel/UCJIx6QNSYoUNH3GTLxPN3qw">JessicaIn3D</a>”.
The video shows how there are three different treasure
hoards in Pikmin 2, one per region, meaning its impossible
to collect every treasure in a single game.</p>
</div>
<div class="col-6">
<p>
<center>
<iframe width="315" height="560" style="border: 2px black solid;" src="https://www.youtube.com/embed/cgZVmnyNP6A" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<br><small><em>“You Can't Collect Every Treasure In Pikmin 2” <nobr>by <a href="https://www.youtube.com/channel/UCJIx6QNSYoUNH3GTLxPN3qw">JessicaIn3D</a></nobr></em></small>
</center>
</p>
</div>
</div>

The project took 4 months to complete, running from June to October. I <a href="https://gist.github.com/sethmlarson/6e83d8d0e4d6412ec8f9c27ec165fa51">published a script</a> which analyzed Pikmin 2 save file data
using [this documentation on the save file format](https://pikmintkb.com/wiki/Pikmin_2_save_file).
From here the HTML table in the project page could be automatically updated
as I made more progress. I [published regular updates](https://sethmlarson.dev/pikmin-2-international-treasure-hoard#updates) to the project page
as the project progressed, too.

<p>
<center>
<img style="border: 2px black solid; max-width: 80%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_3968_out.jpg"/>
<br><small><em>Pikmin 2 for the GameCube (NTSC-J, NTSC-M, and PAL) and the Switch.</em></small>
</center>
</p>

My favorite game for the Switch family of consoles in 2025 is **Kirby Air Riders**. This game
is pure chaotic fun with a heavy dose of nostalgia for me. I was [one of the very few](https://en.wikipedia.org/wiki/Kirby_Air_Ride#Reception)
that played the original game on the Nintendo GameCube 22 years ago.
I still can't believe this gem of a game only sold 750,000 units in the United States.
It's amazing to see what is essentially the game my brother and I dreamed of as
a sequel: taking everything great about the original release and adding online play, a more expansive world,
and near-infinite customization and unlockables.

This game is fast-paced and fits into a busy life easily: a single play session of
City Trail or Air Ride mode lasts less than 7 minutes from start to finish.
I'll frequently pick this game up to play a few rounds between work and whatever
the plans of the evening are. Each round is different, and you can pursue whichever
strategy you prefer (combat, speed, gliding, legendary-vehicle hunting) and expect
to have a fighting chance in the end.

<p>
<center>
<img style="border: 2px black solid; max-width: 80%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_3971_out.jpg"/>
<br><small><em>Kirby Air Ride for the GameCube (NTSC-J and NTSC-M) and Kirby Air Riders for the Switch 2.</em></small>
</center>
</p>

## Which game system did I play the most?

Even with the Switch and Switch 2 bundled into one category
I **played the GameCube more in 2025**. This was a big year for
me and GameCube: I finally modded a platinum cube and my
childhood indigo cube with the [FlippyDrive](https://docs.flippydrive.com) and [ETH2GC](https://github.com/webhdx/ETH2GC).
I've got a lot more in store for the GameCube next year, too.

|System|Duration|
|-|-|
|GameCube|41h 55m|
|Switch|35h 45m|

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT game_system, SUM(duration) AS d
FROM sessions
WHERE STRFTIME('%Y', date) = '2025'
GROUP BY game_system
ORDER BY d DESC;
```

</details></blockquote>

Here's the same data stylized like the GitHub contributor graph.
Blue squares represent days when I played GameCube and red squares I played the Switch or Switch 2, starting in June 2025:

<blockquote>
<center>
<svg viewBox="0 0 884 152" style="max-width: 100%">
  <rect fill="#00f" fill-opacity="1.0" x="0" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="0" y="22" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="0" y="44" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="0" y="66" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="0" y="88" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="0" y="110" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="0" y="132" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="22" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="22" y="22" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="22" y="44" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="22" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="22" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="22" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="22" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="44" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="44" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="44" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="44" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="44" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="44" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="44" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="66" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="66" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="66" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="66" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="66" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="66" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="66" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="88" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="88" y="22" width="20" height="20"/>
  <rect fill="#000" x="114" y="0" width="2" height="152"/>
  <rect fill="#000" fill-opacity="0.1" x="122" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="122" y="66" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="122" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="122" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="122" y="132" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="144" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="144" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="144" y="44" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="144" y="66" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="144" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="144" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="144" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="166" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="166" y="22" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="166" y="44" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="166" y="66" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="166" y="88" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="166" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="166" y="132" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="188" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="188" y="22" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="188" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="188" y="66" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="188" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="188" y="110" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="188" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="210" y="0" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="210" y="22" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="210" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="210" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="210" y="88" width="20" height="20"/>
  <rect fill="#000" x="236" y="0" width="2" height="152"/>
  <rect fill="#000" fill-opacity="0.1" x="244" y="110" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="244" y="132" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="266" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="266" y="22" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="266" y="44" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="266" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="266" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="266" y="110" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="266" y="132" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="288" y="0" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="288" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="288" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="288" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="288" y="88" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="288" y="110" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="288" y="132" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="310" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="310" y="22" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="310" y="44" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="310" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="310" y="88" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="310" y="110" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="310" y="132" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="332" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="332" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="332" y="44" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="332" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="332" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="332" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="332" y="132" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="354" y="0" width="20" height="20"/>
  <rect fill="#000" x="380" y="0" width="2" height="152"/>
  <rect fill="#000" fill-opacity="0.1" x="388" y="22" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="388" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="388" y="66" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="388" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="388" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="388" y="132" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="410" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="410" y="22" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="410" y="44" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="410" y="66" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="410" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="410" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="410" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="432" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="432" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="432" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="432" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="432" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="432" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="432" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="454" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="454" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="454" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="454" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="454" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="454" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="454" y="132" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="476" y="0" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="476" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="476" y="44" width="20" height="20"/>
  <rect fill="#000" x="502" y="0" width="2" height="152"/>
  <rect fill="#000" fill-opacity="0.1" x="510" y="66" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="510" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="510" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="510" y="132" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="532" y="0" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="532" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="532" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="532" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="532" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="532" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="532" y="132" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="554" y="0" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="554" y="22" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="554" y="44" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="554" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="554" y="88" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="554" y="110" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="554" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="576" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="576" y="22" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="576" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="576" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="576" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="576" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="576" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="598" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="598" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="598" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="598" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="598" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="598" y="110" width="20" height="20"/>
  <rect fill="#000" x="624" y="0" width="2" height="152"/>
  <rect fill="#000" fill-opacity="0.1" x="632" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="654" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="654" y="22" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="654" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="654" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="654" y="88" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="654" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="654" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="676" y="0" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="676" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="676" y="44" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="676" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="676" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="676" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="676" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="698" y="0" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="698" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="698" y="44" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="698" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="698" y="88" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="698" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="698" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="720" y="0" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="720" y="22" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="720" y="44" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="720" y="66" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="720" y="88" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="720" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="720" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="742" y="0" width="20" height="20"/>
  <rect fill="#000" x="768" y="0" width="2" height="152"/>
  <rect fill="#f00" fill-opacity="1.0" x="776" y="22" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="776" y="44" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="776" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="776" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="776" y="110" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="776" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="798" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="798" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="798" y="44" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="798" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="798" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="798" y="110" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="798" y="132" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="820" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="820" y="22" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="820" y="44" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="820" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="820" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="820" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="820" y="132" width="20" height="20"/>
  <rect fill="#f00" fill-opacity="1.0" x="842" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="842" y="22" width="20" height="20"/>
  <rect fill="#00f" fill-opacity="1.0" x="842" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="842" y="66" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="842" y="88" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="842" y="110" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="842" y="132" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="864" y="0" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="864" y="22" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="864" y="44" width="20" height="20"/>
  <rect fill="#000" fill-opacity="0.1" x="864" y="66" width="20" height="20"/>
</svg>
</center>
</blockquote>

I also played **Sonic Adventure**
on a newly-purchased **SEGA Dreamcast** for the first time in 2025, too.
Unfortunately I don't have a way to track play data for the Dreamcast (yet?)
but my experience with the Dreamcast and Sonic Adventure will likely
get its own short blog post eventually, stay tuned.

## Which games did I play the most?

I played 9 unique titles this year (including region and platform
variants), but which ones did I play the most?

| Game                |  Duration |
|---------------------|----------:|
| Pikmin 2            |   27h 11m |
| Animal Crossing     |   16h 47m |
| Kirby Air Riders    |   16h 15m |
| Mario Kart World    |   10h 25m |
| Super Mario Odyssey |    4h 45m |
| Pikmin 4            |     1h 5m |
| Overcooked! 2       |       45m |
| Kirby's Airride     |       15m |
| Sonic Origins       |       10m |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT game_name, SUM(duration) AS d
FROM sessions
WHERE STRFTIME('%Y', date) = '2025'
GROUP BY game_name
ORDER BY d DESC;
```

</details></blockquote>

That's a lot of **Pikmin 2**, huh? This year collected [all 245
unique treasures](https://sethmlarson.dev/pikmin-2-international-treasure-hoard) across the three regions of Pikmin 2 (JP, US, and PAL)
including a 100% complete save file for the Japanese region. This is the first
time I collected all treasures for a single Pikmin 2 play-through.

We can break down how much time was spent in each region and system
for Pikmin 2:

| System    | Region |  Duration |
|-----------|--------|----------:|
| GameCube  | US     |    9h 24m |
| GameCube  | JP     |    9h 17m |
| GameCube  | PAL    |     6h 9m |
| Switch    | US     |    2h 20m |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT game_system, game_region, SUM(duration) AS d
FROM sessions
WHERE STRFTIME('%Y', date) = '2025'
AND game_name = 'Pikmin 2'
GROUP BY game_system, game_region
ORDER BY d DESC;
```

</details></blockquote>

You can see I even started playing the Switch edition of Pikmin 2 but bailed on that
idea pretty early. Playing through the same game 3 times in a year was already enough :)
The US and JP versions were ~9 hours each with PAL receiving less play time.
This is due to PAL only having 10 unique treasures, so I was able to speed-run
most of the game.

## Which games did I play most per session?

This query sorta indicates “binge-ability”,
when I did play a title how long was that play session
on average? **Super Mario Odyssey** just barely took the top spot
here, but the two Switch 2 titles I own
were close behind.


| Name                                |  Duration |
|-------------------------------------|----------:|
| Super Mario Odyssey                 |       57m |
| Mario Kart World                    |       56m |
| Kirby Air Riders                    |       51m |
| Pikmin 2                            |       49m |
| Animal Crossing                     |       47m |
| Overcooked! 2                       |       45m |
| Pikmin 4                            |       32m |
| Kirby's Airride                     |       15m |
| Sonic Origins                       |        5m |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT game_name, SUM(duration)/COUNT(DISTINCT date) AS d
FROM sessions
WHERE STRFTIME('%Y', date) = '2025'
GROUP BY game_name
ORDER BY d DESC;
```

</details></blockquote>

## When did I start and stop playing each game?

I only have enough time to *focus* on one game at a time,
so there is a pretty linear history of which game is
top-of-mind for me at any one time.
From this query we can construct a linear history:

* Pikmin 2 (June→Oct)
* Animal Crossing (July→Aug)
* Super Mario Odyssey (Oct)
* Pikmin 4 (Nov, “[Decor Pikmin](https://www.pikminwiki.com/Decor_Pikmin_(Pikmin_4))”)
* Mario Kart World (July→Nov)
* Kirby Air Riders (Nov→Dec)

I still want to return to Super Mario Odyssey, I was having a
great time with the game! It's just that
and Kirby Air Riders came out and stole my attention.


| Game                                | First played | Last played |
|-------------------------------------|--------------|-------------|
| Pikmin 2                            | 2025-06-01   | 2025-10-06  |
| Mario Kart World                    | 2025-07-20   | 2025-11-17  |
| Animal Crossing                     | 2025-07-29   | 2025-09-08  |
| Sonic Origins                       | 2025-08-11   | 2025-08-25  |
| Super Mario Odyssey                 | 2025-10-13   | 2025-10-21  |
| Kirby Air Riders                    | 2025-11-07   | 2025-12-21  |
| Pikmin 4                            | 2025-11-10   | 2025-11-12  |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT (
  game_name,
  MIN(date) AS fp,
  MAX(date)
)
FROM sessions
WHERE STRFTIME('%Y', date) = '2025'
GROUP BY game_name
ORDER BY fp ASC;
```

</details></blockquote>

## Which game was I most consistently playing?

We can take the data from the “Days” column above
and use that as a divisor for the number of unique days
each game was played. This will give a sense of how often
I was playing a game within the time span that I was “active”
for a game:

| Game                                | %    | Days Played |        Span |
|-------------------------------------|------|------------:|------------:|
| Pikmin 4                            | 100% |           2 |           2 |
| Super Mario Odyssey                 | 63%  |           5 |           8 |
| Animal Crossing                     | 51%  |          21 |          41 |
| Kirby Air Riders                    | 43%  |          19 |          44 |
| Pikmin 2                            | 26%  |          33 |         127 |
| Sonic Origins                       | 14%  |           2 |          14 |
| Mario Kart World                    | 9%   |          11 |         120 |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT (
  game_name,
  COUNT(DISTINCT date) AS played,
  (
    STRFTIME('%j', MAX(date))
    -STRFTIME('%j', MIN(date))
  ) AS days
)
FROM sessions
WHERE STRFTIME('%Y', date) = '2025'
GROUP BY game_name
ORDER BY MIN(date) ASC;
```

</details></blockquote>

If we look at total year gaming “saturation” for 2025 and June-onwards (214 days):

| Days Played | % Days (2025) | % Days (>=June) |
|-------------|---------------|-----------------|
| 89          | 24%           | 42%             |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT COUNT(DISTINCT date)
FROM sessions
WHERE STRFTIME('%Y', date) = '2025';
```

</details></blockquote>

## When did I play games?

Looking at the year, I didn't start playing games on either system
this year until June. That lines up with me receiving my
GameCube FlippyDrives which I had pre-ordered in 2024.
After installing these modifications to my GameCube I began
playing games more regularly again :)

| Month     | Duration |
|-----------|---------:|
| June      |   10h 4m |
| July      |   9h 40m |
| August    |  18h 26m |
| September |   7h 22m |
| October   |   10h 0m |
| November  |   15h 5m |
| December  |    7h 0m |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT STRFTIME('%m', date) AS m, SUM(duration)
FROM sessions
WHERE STRFTIME('%Y', date) = '2025'
GROUP BY m
ORDER BY m ASC;
```

</details></blockquote>

August was the month with the most play! This was due entirely to
playing [Animal Crossing Deluxe](https://www.youtube.com/watch?v=YXmvaUAQSpM) (~16 hours), a mod by [Cuyler](https://www.youtube.com/@Cuyler) for Animal Crossing on the
GameCube. Animal Crossing feels the best when you play for short sessions
each day which I why I was playing so often.

| Game             |  Duration |
|------------------|----------:|
| Animal Crossing  |   15h 41m |
| Mario Kart World |    2h 15m |
| Pikmin 2         |       19m |
| Sonic Origins    |       10m |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT game_name, SUM(duration)
FROM sessions
WHERE STRFTIME('%Y-%m', date) = '2025-08'
GROUP BY game_name;
```

</details></blockquote>

## Which day of the week did I play most?

Unsurprisingly, weekends tend to be the days on average with the longest
play sessions. **Sunday** just barely takes the highest average play
duration per day. Wednesday, Thursday, and Friday have the lowest play activity as these days
are reserved for board-game night, seeing family, and date night respectively :)

| Day  |  Duration | Days | Average |
|------|----------:|-----:|--------:|
| Sun  |   16h 16m |   15 |   1h 5m |
| Mon  |   13h 52m |   17 |     48m |
| Tues |    14h 9m |   16 |     53m |
| Wed  |   11h 17m |   15 |     45m |
| Thur |    6h 35m |    9 |     43m |
| Fri  |    5h 45m |    8 |     43m |
| Sat  |    9h 42m |    9 |   1h 4m |

<blockquote><details><summary>SQLite query</summary>

```sql
SELECT STRFTIME('%w', date) AS day_of_week,SUM(duration),COUNT(DISTINCT date),SUM(duration)/COUNT(DISTINCT date)
FROM sessions WHERE STRFTIME('%Y', date) = '2025'
GROUP BY day_of_week
ORDER BY day_of_week ASC;
```

</details></blockquote>
