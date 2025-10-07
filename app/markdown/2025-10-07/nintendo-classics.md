# Is the "Nintendo Classics" collection a good value?

[Nintendo Classics](https://en.wikipedia.org/wiki/Nintendo_Classics) is a collection of hundreds of retro
video games from Nintendo (and Sega) consoles from the NES to the GameCube.
Nintendo Classics is included with the <nobr>[Nintendo Switch Online](https://en.wikipedia.org/wiki/Nintendo_Switch_Online)</nobr> (NSO)
subscription, which starts at $20/year (~$1.66/month) for individual users.

Looking at the prices of retro games these days, this seems like an
incredible value for players that want to play these games.
This post is [sharing a dataset](https://github.com/sethmlarson/nintendo-classics) that I've curated about <nobr>Nintendo Classics</nobr> games
and mapping their value
to actual physical prices of the same games, with some
interesting queries.
<!-- more -->

For example, here's a graph showing the total value (in $USD) of Nintendo Classics over time:

<p><center><canvas id="line-total"></canvas></center></p>

The dataset was generated from the [tables provided on Wikipedia](https://en.wikipedia.org/wiki/Nintendo_Classics) (CC-BY-SA). The dataset doesn't contain pricing information, instead
only links to corresponding [Pricecharting](https://www.pricecharting.com) pages.
This page only shares approximate aggregate price information, not prices of individual games.
This page will be automatically updated over time as Nintendo announces more games
are coming to <nobr>Nintendo Classics</nobr>.
This page was last updated **<nobr>October 7th, 2025</nobr>**.

## How many games and value per platform?

There are 8 unique platforms on <nobr>Nintendo Classics</nobr>
each with their own collection of games. The below
table includes the value of both added and announced-but-not-added
games. You can see that the total value of games in <nobr>Nintendo Classics</nobr>
is *many thousands of dollars* if genuine physical copies were purchased instead. Here's a graph showing the total value of each platform changing over time:

<p><center><canvas id="line-platform"></canvas></center></p>

And here's the data for all published and announced games as a table:

| Platform               | Games | Total Value | Value per Game |
|------------------------|------:|------------:|---------------:|
| NES                    |    91 |       $1980 |            $21 |
| SNES                   |    83 |       $3600 |            $43 |
| Game Boy (GB/GBC)      |    41 |       $1615 |            $39 |
| Nintendo 64  (N64)     |    42 |       $1130 |            $26 |
| Sega Genesis           |    51 |       $2910 |            $57 |
| Game Boy Advance (GBA) |    30 |        $930 |            $31 |
| GameCube               |     9 |        $640 |            $71 |
| Virtual Boy            |    14 |       $2580 |           $184 |
| All Platforms          |   361 |      $15385 |            $42 |

<details>
<summary>View SQL query</summary>
<div class="codehilite">
<pre><span></span><code><span class="k">SELECT</span><span class="w"> </span><span class="n">platform</span><span class="p">,</span><span class="w"> </span><span class="k">COUNT</span><span class="p">(</span><span class="o">*</span><span class="p">),</span><span class="w"> </span><span class="k">SUM</span><span class="p">(</span><span class="n">price</span><span class="p">),</span><span class="w"> </span><span class="k">SUM</span><span class="p">(</span><span class="n">price</span><span class="p">)</span><span class="o">/</span><span class="k">COUNT</span><span class="p">(</span><span class="o">*</span><span class="p">)</span>
<span class="k">FROM</span><span class="w"> </span><span class="n">games</span>
<span class="k">GROUP</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">platform</span><span class="p">;</span>
</code></pre>
</div>
</details>

## How much value is in each Nintendo Classics tier?

There are multiple "tiers" of <nobr>Nintendo Classics</nobr> each with
a different up-front price (for the console itself)
and ongoing price for the Nintendo Switch Online (NSO) subscription.

Certain collections require specific hardware, such as Virtual Boy
requiring either the recreation ($100) or cardboard ($30) Virtual Boy
headset and GameCube collection requiring a Switch 2 ($450). All other collections
work just fine with a Switch Lite ($100). All platforms beyond NES, SNES, Game Boy,
and Game Boy Color require NSO + Expansion Pass.

| Platforms          | Requires                  | Price         |  Games  |  Games Value |
|--------------------|---------------------------|---------------|:-------:|-------------:|
| NES, SNES, GB, GBC | Switch Lite & NSO \*      | $100 + $20/Yr |   215   |        $7195 |  
| +N64, Genesis, GBA | Switch Lite & NSO+EP      | $100 + $50/Yr |   338   |       $12165 |
| +Virtual Boy       | Switch Lite, NSO+EP, & VB | $130 + $50/Yr |   352   |       $14745 |
| +GameCube          | Switch 2 & NSO+EP         | $450 + $50/Yr |   361   |       $15385 |

\* I wanted to highlight that Nintendo Switch Online (NSO) without Expansion Pack
has the option to actually pay $3 monthly rather than $20 yearly.
This doesn't make sense if you're paying for a whole year anyway, but
if you want to just play a game in the NES, SNES, GB, or GBC collections
you can pay $3 for a month of NSO and play games for very cheap.

## How often are games added to Nintendo Classics?

<nobr>Nintendo Classics</nobr> tends to add a few games per platform every year.
Usually when a platform is first announced a whole slew of games are
added during the announcement with a slow drip-feed of games coming later.

Here's the break-down per year how many games were added to each platform:

| Platform       | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|----------------|------|------|------|------|------|------|------|------|
| NES            | 30   | 30   | 8    | 2    | 5    | 4    | 12   |      |
| SNES           |      | 25   | 18   | 13   | 9    | 1    | 9    | 8    |
| N64            |      |      |      | 10   | 13   | 8    | 8    | 3    |
| Genesis        |      |      |      | 20   | 17   | 8    | 3    | 3    |
| Game Boy       |      |      |      |      |      | 19   | 16   | 6    |
| GBA            |      |      |      |      |      | 13   | 12   | 5    |
| GameCube       |      |      |      |      |      |      |      | 9    |
| Virtual Boy    |      |      |      |      |      |      |      |      |
| All Platforms  | 30   | 55   | 26   | 55   | 43   | 53   | 60   | 34   |

<details>
<summary>View SQL query</summary>
<div class="codehilite">
<pre><span></span><code><span class="k">SELECT</span><span class="w"> </span><span class="n">platform</span><span class="p">,</span><span class="w"> </span><span class="n">STRFTIME</span><span class="p">(</span><span class="s1">'%Y'</span><span class="p">,</span><span class="w"> </span><span class="n">added_date</span><span class="p">)</span><span class="w"> </span><span class="k">AS</span><span class="w"> </span><span class="k">year</span><span class="p">,</span><span class="w"> </span><span class="k">COUNT</span><span class="p">(</span><span class="o">*</span><span class="p">)</span>
<span class="k">FROM</span><span class="w"> </span><span class="n">games</span>
<span class="k">GROUP</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">platform</span><span class="p">,</span><span class="w"> </span><span class="k">year</span>
<span class="k">ORDER</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">platform</span><span class="p">,</span><span class="w"> </span><span class="k">year</span><span class="w"> </span><span class="k">DESC</span><span class="p">;</span>
</code></pre>
</div>
</details>

## What are the rarest or valuable games in Nintendo Classics?

There are a bunch of valuable and rare games available in <nobr>Nintendo Classics</nobr>.
Here are the top-50 most expensive games that are available in the collection:

<table><thead><th>Platform</th><th>Game</th><th>Added Date</th></thead>
<tr><td>Virtual Boy</td><td><a href="https://www.pricecharting.com/game/virtual-boy/jack-bros">Jack Bros.</a></td><td>TBA</td></tr>
<tr><td>Virtual Boy</td><td><a href="https://www.pricecharting.com/game/jp-virtual-boy/virtual-bowling">Virtual Bowling</a></td><td>TBA</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/sega-genesis/crusader-of-centy">Crusader of Centy</a></td><td>2023-06-27</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/jp-sega-mega-drive/pulseman">Pulseman</a></td><td>2023-04-18</td></tr>
<tr><td>Virtual Boy</td><td><a href="https://www.pricecharting.com/game/virtual-boy/space-invaders-virtual-collection">Space Invaders Virtual Collection</a></td><td>TBA</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/jp-sega-mega-drive/alien-soldier">Alien Soldier</a></td><td>2022-03-16</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/earthbound">EarthBound</a></td><td>2022-02-09</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/sega-genesis/musha">MUSHA</a></td><td>2021-10-25</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/harvest-moon">Harvest Moon</a></td><td>2022-03-30</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/wild-guns">Wild Guns</a></td><td>2020-05-20</td></tr>
<tr><td>Virtual Boy</td><td><a href="https://www.pricecharting.com/game/jp-virtual-boy/insmouse-no-yakata?q=yakata+virtual+boy">Innsmouth no Yakata</a></td><td>TBA</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/pal-sega-mega-drive/mega-man-the-wily-wars">Mega Man: The Wily Wars</a></td><td>2022-06-30</td></tr>
<tr><td>GB/GBC</td><td><a href="https://www.pricecharting.com/game/gameboy/mega-man-5">Mega Man V</a></td><td>2024-06-07</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/sutte-hakkun">Sutte Hakkun</a></td><td>2025-01-24</td></tr>
<tr><td>NES</td><td><a href="https://www.pricecharting.com/game/nes/fire-n-ice">Fire 'n Ice</a></td><td>2021-02-17</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/kirbys-dream-land-3">Kirby's Dream Land 3</a></td><td>2019-09-05</td></tr>
<tr><td>NES</td><td><a href="https://www.pricecharting.com/game/nes/donkey-kong-jr-math">Donkey Kong Jr. Math</a></td><td>2024-07-04</td></tr>
<tr><td>GB/GBC</td><td><a href="https://www.pricecharting.com/game/gameboy-color/survival-kids">Survival Kids</a></td><td>2025-05-23</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/demon%27s-crest">Demon's Crest</a></td><td>2019-09-05</td></tr>
<tr><td>GameCube</td><td><a href="https://www.pricecharting.com/game/gamecube/chibi-robo">Chibi-Robo!</a></td><td>2025-08-21</td></tr>
<tr><td>GameCube</td><td><a href="https://www.pricecharting.com/game/gamecube/pokemon-xd-gale-of-darkness">Pokémon XD: Gale of Darkness</a></td><td>TBA</td></tr>
<tr><td>GB/GBC</td><td><a href="https://www.pricecharting.com/game/gameboy/castlevania-legends">Castlevania Legends</a></td><td>2023-10-31</td></tr>
<tr><td>NES</td><td><a href="https://www.pricecharting.com/game/nes/scat-special-cybernetic-attack-team">S.C.A.T.: Special Cybernetic Attack Team</a></td><td>2020-09-23</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-famicom/star-fox-2">Star Fox 2</a></td><td>2019-12-12</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-famicom/kirby-no-kira-kira-kids">Kirby's Star Stacker</a></td><td>2022-07-21</td></tr>
<tr><td>GBA</td><td><a href="https://www.pricecharting.com/game/gameboy-advance/f-zero-climax">F-Zero Climax</a></td><td>2024-10-11</td></tr>
<tr><td>GameCube</td><td><a href="https://www.pricecharting.com/game/gamecube/pokemon-colosseum">Pokémon Colosseum</a></td><td>TBA</td></tr>
<tr><td>GB/GBC</td><td><a href="https://www.pricecharting.com/game/gameboy/mega-man-4">Mega Man IV</a></td><td>2024-06-07</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/uncharted-waters-new-horizons">Uncharted Waters: New Horizons</a></td><td>2025-03-28</td></tr>
<tr><td>Virtual Boy</td><td><a href="https://www.pricecharting.com/game/virtual-boy/wario-land">Virtual Boy Wario Land</a></td><td>TBA</td></tr>
<tr><td>NES</td><td><a href="https://www.pricecharting.com/game/nes/shadow-of-the-ninja">Shadow of the Ninja</a></td><td>2020-02-19</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/super-metroid">Super Metroid</a></td><td>2019-09-05</td></tr>
<tr><td>GBA</td><td><a href="https://www.pricecharting.com/game/gameboy-advance/mr-driller-2">Mr. Driller 2</a></td><td>2025-09-25</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/joe-and-mac-2-lost-in-the-tropics">Joe & Mac 2: Lost in the Tropics</a></td><td>2019-09-05</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/breath-of-fire-ii">Breath of Fire II</a></td><td>2019-12-12</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-famicom/umihara-kawase">Umihara Kawase</a></td><td>2022-05-26</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/sega-genesis/gunstar-heroes">Gunstar Heroes</a></td><td>2021-10-25</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/sega-genesis/ristar">Ristar</a></td><td>2021-10-25</td></tr>
<tr><td>Virtual Boy</td><td><a href="https://www.pricecharting.com/game/jp-virtual-boy/virtual-fishing">Virtual Fishing</a></td><td>TBA</td></tr>
<tr><td>NES</td><td><a href="https://www.pricecharting.com/game/nes/vice-project-doom">Vice: Project Doom</a></td><td>2019-08-21</td></tr>
<tr><td>N64</td><td><a href="https://www.pricecharting.com/game/jp-nintendo-64/sin-and-punishment">Sin and Punishment</a></td><td>2021-10-25</td></tr>
<tr><td>N64</td><td><a href="https://www.pricecharting.com/game/nintendo-64/pokemon-stadium-2">Pokémon Stadium 2</a></td><td>2023-08-08</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/sega-genesis/castlevania-bloodlines">Castlevania: Bloodlines</a></td><td>2021-10-25</td></tr>
<tr><td>Genesis</td><td><a href="https://www.pricecharting.com/game/sega-genesis/phantasy-star-iv">Phantasy Star IV</a></td><td>2021-10-25</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/the-peace-keepers">The Peace Keepers</a></td><td>2020-09-23</td></tr>
<tr><td>GB/GBC</td><td><a href="https://www.pricecharting.com/game/gameboy-color/kirby-tilt-and-tumble">Kirby Tilt 'n' Tumble</a></td><td>2023-06-05</td></tr>
<tr><td>N64</td><td><a href="https://www.pricecharting.com/game/nintendo-64/zelda-majora%27s-mask">The Legend of Zelda: Majora's Mask</a></td><td>2022-02-25</td></tr>
<tr><td>Virtual Boy</td><td><a href="https://www.pricecharting.com/game/virtual-boy/mario-clash">Mario Clash</a></td><td>TBA</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/super-valis-iv">Super Valis IV</a></td><td>2020-12-18</td></tr>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/wrecking-crew-98">Wrecking Crew '98</a></td><td>2024-04-12</td></tr>
</table>

<details>
<summary>View SQL query</summary>
<div class="codehilite">
<pre><span></span><code><span class="k">SELECT</span><span class="w"> </span><span class="n">platform</span><span class="p">,</span><span class="w"> </span><span class="n">name</span><span class="p">,</span><span class="w"> </span><span class="n">price</span><span class="w"> </span><span class="k">FROM</span><span class="w"> </span><span class="n">games</span>
<span class="k">ORDER</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">price</span><span class="w"> </span><span class="k">DESC</span><span class="w"> </span><span class="k">LIMIT</span><span class="w"> </span><span class="mi">50</span><span class="p">;</span>
</code></pre>
</div>
</details>

## Who publishes their games to Nintendo Classics?

Nintendo Classics has more publishers than just Nintendo
and Sega.
Looking at which third-party publishers are publishing their games to Nintendo Classics
can give you a hint at what future games might make their
way to the collection:

| Publisher                  | Games | Value |
|----------------------------|------:|------:|
| Capcom                     |    17 | $1055 |
| Xbox Game Studios          |    13 |  $245 |
| Koei Tecmo                 |    13 |  $465 |
| City Connection            |    11 |  $240 |
| Konami                     |    10 |  $505 |
| Bandai Namco Entertainment |     9 |  $190 |
| Sunsoft                    |     7 |  $155 |
| Natsume Inc.               |     7 |  $855 |
| G-Mode                     |     7 |  $190 |
| Arc System Works           |     6 |  $110 |

<details>
<summary>View SQL query</summary>
<div class="codehilite">
<pre><span></span><code><span class="k">SELECT</span><span class="w"> </span><span class="n">publisher</span><span class="p">,</span><span class="w"> </span><span class="k">COUNT</span><span class="p">(</span><span class="o">*</span><span class="p">)</span><span class="w"> </span><span class="k">AS</span><span class="w"> </span><span class="n">num_games</span><span class="p">,</span><span class="w"> </span><span class="k">SUM</span><span class="p">(</span><span class="n">price</span><span class="p">)</span>
<span class="k">FROM</span><span class="w"> </span><span class="n">games</span><span class="w"> </span><span class="k">WHERE</span><span class="w"> </span><span class="n">publisher</span><span class="w"> </span><span class="k">NOT</span><span class="w"> </span><span class="k">IN</span><span class="w"> </span><span class="p">(</span><span class="s1">'Nintendo'</span><span class="p">,</span><span class="w"> </span><span class="s1">'Sega'</span><span class="p">)</span>
<span class="k">GROUP</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">publisher</span>
<span class="k">ORDER</span><span class="w"> </span><span class="k">BY</span><span class="w"> </span><span class="n">num_games</span><span class="w"> </span><span class="k">DESC</span><span class="w"> </span><span class="k">LIMIT</span><span class="w"> </span><span class="mi">20</span><span class="p">;</span>
</code></pre>
</div>
</details>

## What games have been removed from Nintendo Classics?

There's only been one game that's been removed from Nintendo Classics
so far. There likely will be more in the future:

<table><thead><th>Platform</th><th>Game</th><th>Added Date</th><th>Removed Date</th></thead>
<tr><td>SNES</td><td><a href="https://www.pricecharting.com/game/super-nintendo/super-soccer">Super Soccer</a></td><td>2019-09-05</td><td>2025-03-25</td></tr>
</table>

<details>
<summary>View SQL query:</summary>
<div class="codehilite">
<pre><span></span><code><span class="k">SELECT</span><span class="w"> </span><span class="n">platform</span><span class="p">,</span><span class="w"> </span><span class="n">name</span><span class="p">,</span><span class="w"> </span><span class="n">added_date</span><span class="p">,</span><span class="w"> </span><span class="n">removed_date</span>
<span class="k">FROM</span><span class="w"> </span><span class="n">games</span><span class="w"> </span><span class="k">WHERE</span><span class="w"> </span><span class="n">removed_date</span><span class="w"> </span><span class="k">IS</span><span class="w"> </span><span class="k">NOT</span><span class="w"> </span><span class="k">NULL</span><span class="p">;</span>
</code></pre>
</div>
</details>

This site uses the [MIT](https://github.com/chartjs/Chart.js/blob/master/LICENSE.md) licensed [ChartJS](https://github.com/chartjs/Chart.js) for the line chart visualization.

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.5.0/dist/chart.umd.min.js" integrity="sha256-Lye89HGy1p3XhJT24hcvsoRw64Q4IOL5a7hdOflhjTA=" crossorigin="anonymous"></script>
<script>
  const ctx = document.getElementById('line-platform');

  new Chart(ctx, {
    type: 'line',
    options: {
scales: {
  x: {
    grid: {
      display: false
    }
  },
  y: {
    grid: {
      display: false
    }
  }
}
    },
    data: {"labels": ["2018-09", "2018-10", "2018-11", "2018-12", "2019-01", "2019-02", "2019-03", "2019-04", "2019-05", "2019-06", "2019-07", "2019-08", "2019-09", "2019-12", "2020-02", "2020-05", "2020-07", "2020-09", "2020-12", "2021-02", "2021-05", "2021-07", "2021-10", "2021-12", "2022-01", "2022-02", "2022-03", "2022-04", "2022-05", "2022-06", "2022-07", "2022-08", "2022-09", "2022-10", "2022-11", "2022-12", "2023-01", "2023-02", "2023-03", "2023-04", "2023-05", "2023-06", "2023-07", "2023-08", "2023-09", "2023-10", "2023-11", "2023-12", "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09"], "datasets": [{"label": "NES", "data": [330, 370, 410, 490, 560, 605, 650, 725, 880, 910, 950, 1035, 1035, 1115, 1225, 1235, 1255, 1375, 1410, 1600, 1605, 1605, 1605, 1605, 1605, 1635, 1660, 1660, 1665, 1665, 1675, 1675, 1675, 1675, 1675, 1675, 1675, 1675, 1680, 1680, 1680, 1690, 1690, 1690, 1690, 1725, 1725, 1725, 1725, 1745, 1745, 1745, 1745, 1745, 1970, 1970, 1970, 1970, 1970, 1980, 1980, 1980, 1980, 1980, 1980, 1980, 1980, 1980, 1980], "fill": false}, {"label": "SNES", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 780, 1050, 1070, 1370, 1430, 1560, 1735, 1850, 1950, 2040, 2040, 2040, 2040, 2350, 2675, 2675, 2780, 2780, 2935, 2935, 2935, 2935, 2935, 2935, 2935, 2935, 2950, 2950, 2950, 2950, 2950, 2950, 2950, 2950, 2950, 2950, 2950, 3000, 3000, 3100, 3100, 3100, 3100, 3100, 3150, 3150, 3150, 3150, 3415, 3415, 3585, 3585, 3585, 3585, 3590, 3590, 3590], "fill": false}, {"label": "Sega Genesis", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 805, 890, 890, 890, 1285, 1360, 1360, 1695, 1695, 1695, 1815, 1815, 1815, 1880, 1880, 1880, 1880, 2345, 2345, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2825, 2865, 2865, 2865, 2865, 2865, 2910, 2910, 2910, 2910, 2910, 2910], "fill": false}, {"label": "Nintendo 64", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 285, 340, 365, 425, 460, 490, 525, 545, 585, 600, 600, 615, 685, 685, 705, 705, 705, 730, 730, 730, 730, 805, 805, 845, 860, 930, 930, 945, 945, 980, 980, 1015, 1015, 1015, 1015, 1075, 1075, 1075, 1090, 1090, 1090, 1090, 1120, 1120, 1120, 1120, 1130], "fill": false}, {"label": "Game Boy Advance", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 150, 190, 190, 240, 315, 315, 315, 345, 345, 345, 345, 410, 460, 475, 475, 475, 555, 595, 620, 620, 760, 760, 760, 760, 790, 790, 810, 810, 810, 810, 810, 930], "fill": false}, {"label": "Game Boy", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 240, 295, 295, 295, 400, 505, 530, 535, 670, 670, 670, 670, 670, 730, 730, 785, 1195, 1195, 1195, 1195, 1195, 1235, 1280, 1280, 1280, 1355, 1355, 1615, 1615, 1615, 1615, 1615], "fill": false}, {"label": "GameCube", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 130, 170, 320, 320], "fill": false}, {"label": "Virtual Boy", "data": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], "fill": false}]}
  });
</script>

<script>
  const ctx2 = document.getElementById('line-total');

  new Chart(ctx2, {
    type: 'line',
    options: {
scales: {
  x: {
    grid: {
      display: false
    }
  },
  y: {
    grid: {
      display: false
    }
  }
}
    },
    data: {"labels": ["2018-09", "2018-10", "2018-11", "2018-12", "2019-01", "2019-02", "2019-03", "2019-04", "2019-05", "2019-06", "2019-07", "2019-08", "2019-09", "2019-12", "2020-02", "2020-05", "2020-07", "2020-09", "2020-12", "2021-02", "2021-05", "2021-07", "2021-10", "2021-12", "2022-01", "2022-02", "2022-03", "2022-04", "2022-05", "2022-06", "2022-07", "2022-08", "2022-09", "2022-10", "2022-11", "2022-12", "2023-01", "2023-02", "2023-03", "2023-04", "2023-05", "2023-06", "2023-07", "2023-08", "2023-09", "2023-10", "2023-11", "2023-12", "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06", "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12", "2025-01", "2025-02", "2025-03", "2025-04", "2025-05", "2025-06", "2025-07", "2025-08", "2025-09"], "datasets": [{"label": "All Games ($USD)", "data": [330, 370, 410, 490, 560, 605, 650, 725, 880, 910, 950, 1035, 1815, 2165, 2295, 2605, 2685, 2935, 3145, 3450, 3555, 3645, 4735, 4875, 4900, 5300, 6080, 6185, 6330, 6685, 6890, 6905, 7025, 7040, 7110, 7175, 7195, 7585, 7700, 8190, 8240, 8910, 9015, 9115, 9150, 9360, 9375, 9445, 9510, 9645, 9720, 9855, 9910, 10435, 10700, 10725, 10775, 10975, 11055, 11110, 11390, 11420, 11665, 11730, 12020, 12150, 12195, 12345, 12475], "fill": false}]}
  });
</script>