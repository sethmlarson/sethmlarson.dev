# Extracting NES & N64 ROMs from Zelda Collector's Edition

Gaming as a hobby is **about to become much more expensive** in the United States due to tariffs.
I cannot recall a time in the past where a **console's price has increased during its generation**, and yet the <nobr>Xbox Series X & S</nobr>, the <nobr>Nintendo Switch</nobr>, and most recently the <nobr>Playstation 5</nobr>
have had price hikes. <nobr>These are not normal times.</nobr>

So here's another entry in my mini-series ([#1](https://sethmlarson.dev/extracting-nes-and-famicom-roms-from-animal-crossing), [#2](https://sethmlarson.dev/extracting-genesis-and-game-gear-roms-from-sega-gamecube-collections)) of extracting ROMs from GameCube games, this time
the <nobr>“Zelda Collector's Edition”</nobr> which contains 2 NES and 2 N64 Zelda titles.

<!-- more -->

This article only took so long because I was trying to actually implement
the Nintendo “TGC” archive format, but it turns out that even the popular
tools handling TGC can't parse the NES ROMs out of the archives included
in the Zelda Collector's Edition game properly. ¯\\\_(ツ)\_/¯

So instead I [created a script](https://gist.github.com/sethmlarson/1352edca04fbcfb62656249d7603745b) which looks for NES and N64 ROM header magic strings (`NES\x1A` and `\x80\x37\x12\x40`)
and used [known lengths](https://datomatic.no-intro.org/) for these ROMs instead of the TGC format for framing information.
*So much easier!*

| Game                                                                                                      | Length | MD5 |
|-----------------------------------------------------------------------------------------------------------|-|-|
| [Legend of Zelda](https://www.pricecharting.com/game/nes/legend-of-zelda)                                 | 131088 | `BF8266F0FA69A5A8DAF5F23C2876A1AD` |
| [Zelda II - The Adventure of Link](https://www.pricecharting.com/game/nes/zelda-ii-the-adventure-of-link) | 262160 | `32308B00B9DEC4DF130C7BF703340FF3` |
| [Legend of Zelda - Ocarina of Time](https://www.pricecharting.com/game/nintendo-64/zelda-ocarina-of-time) | 33554432 | `CD09029EDCFB7C097AC01986A0F83D3F` |
| [Legend of Zelda - Majora's Mask](https://www.pricecharting.com/game/nintendo-64/zelda-majora%27s-mask)   | 33554432 | `AC0751DBC23AB2EC0C3144203ACA0003` |

You know the drill by now: buying these games costs over $150 USD and <nobr>“Zelda Collector's Edition”</nobr> for
the GameCube [only costs ~$50 USD](https://www.pricecharting.com/game/gamecube/zelda-collector%27s-edition).
Pretty good savings, especially for two of the most celebrated Zelda titles. However, the price is
high enough that you might consider buying a year of “Nintendo Switch Online + Expansion Pack” if you already have the console.

I still haven't beaten “Ocarina of Time” or “Majora's Mask”, even though I know they are both masterpieces.
The only Legend of Zelda
games I've beaten end-to-end are “[Wind Waker](https://www.pricecharting.com/game/gamecube/zelda-wind-waker)” and “[Four Swords Adventures](https://www.pricecharting.com/game/gamecube/zelda-four-swords-adventures)”, can you tell I'm a GameCube player?
Let me know what your favorite Legend of Zelda title is.
