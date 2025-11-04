# GameCube Nintendo Classics and storage size

If you're into GameCube collecting and archiving you may already know
that GameCube ISOs or "ROMs" are around ~1.3 GB in size, regardless of
the game that is contained within the `.iso` file. This is because
GameCube ROMs are all copies of the same disk format: the
[GameCube Game disc](https://en.wikipedia.org/wiki/Nintendo_optical_discs#GameCube_Game_Disc) (DOL-6).

The GameCube Game disc is a 8cm
miniDVD-based disc with a static storage capacity of 1.5 GB. Compare this to cartridges which using
[memory-mapping controllers (MMC)](https://en.wikipedia.org/wiki/Memory_management_controller_(Nintendo)) can
encase different amounts of storage ROM depending on the size of the game data itself.

<!-- more -->

This was a concern raised by some GameCube players on Switch. Given the [prices of microSD Express storage](https://sethmlarson.dev/nintendo-switch-2-physical-game-price-differences) (~28 ¢/GB)
and the size of the GameCube game library (>650 total, 45 first-party) meant storage requirements could increase quickly for new GameCube titles.

Luckily, looking at the data about the GameCube Nintendo Classics application on the Switch we can see that
the ROMs in use are "trimmed", such that their size is less than 1.3 GB:

| Date       | Titles                                                                                                             | Games |  Storage | Storage/Game |
|------------|--------------------------------------------------------------------------------------------------------------------|:-----:|---------:|-------------:|
| 2025-06-03 | <nobr>F-Zero GX</nobr><br><nobr>Legend of Zelda:</nobr> <nobr>The Wind Waker</nobr><br><nobr>Soulcalibur II</nobr> |   3   |   3.5 GB |      1.16 GB |
| 2025-07-03 | Super Mario Strikers                                                                                               |   4   |   ??? GB |       ??? GB |
| 2025-08-21 | Chibi-Robo!                                                                                                        |   5   |   6.9 GB |      1.38 GB | 
| 2025-10-30 | Luigi's Mansion                                                                                                    |   6   |   7.2 GB |       1.2 GB |

Luigi's Mansion in particular is known to only require ~100 MB of data on the 1.3 GB disc. Animal Crossing
for the GameCube is also legendarily small due to starting life as an N64 game, requiring only 50 MB of data.

It'll be interesting to see what happens for the first [multi-disc game](https://gamicus.fandom.com/wiki/List_of_multi-disc_GameCube_games) to be added
to Nintendo Classics. Notably, Namco already has a GameCube game in Nintendo Classics: Soulcalibur II.
For this reason, I suspect that the first multi-disc game will be one of these
three published by Namco:

* Baten Kaitos Origins
* Baten Kaitos: Eternal Wings and the Lost Ocean
* Tales of Symphonia
