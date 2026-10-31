# Extracting Billy Hatcher “Joycarry Game” ROMs with Python

Billy Hatcher and the Giant Egg contains a feature called “[Joycarry Games](https://www.youtube.com/watch?v=buM3nXVG9zQ)” similar to
Animal Crossing’s NES game [“Advance Play” feature](https://sethmlarson.dev/extracting-nes-and-famicom-roms-from-animal-crossing#what-if-i-only-have-a-game-boy-advance). I wanted
to extract the ROMs for these mini-games [just like I did
for Animal Crossing](https://sethmlarson.dev/extracting-nes-and-famicom-roms-from-animal-crossing).
Doing so wasn’t as straightforward; the ROMs aren’t available directly
in the disc filesystem like they are in Animal Crossing. To extract the ROMs I ported an
existing Rust program to Python (“*rewrite-it-in-Python*”, anyone?) that receives and saves the ROMs from
the game running in [Dolphin using the GBA TCP](https://dolphin-emu.org/blog/2021/07/21/integrated-gba/) and Joyboot
protocols.

<!-- more -->

These games are simple, and I only really played one as a kid: Puyo Pop. The game
is similar to “[Dr. Robotnik’s Mean Bean Machine](https://en.wikipedia.org/wiki/Dr._Robotnik%27s_Mean_Bean_Machine)”, which was a [favorite of mine](https://sethmlarson.dev/extracting-genesis-and-game-gear-roms-from-sega-gamecube-collections).
This was the only way I could take that game “on-the-go”, often downloading the game to my
GBA before road trips to see my grandparents.

<p style="text-align: center">
<img style="border: 2px black solid; max-width: 100%; box-sizing: border-box" loading="lazy" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/gba-joyboot-client/billy-hatcher-ja.png"/>
<br>
<em><small>Joycarry Game menu in Billy Hatcher with “ChuChu Rocket! Challenge” selected</small></em>
</p>

The Python program is a port of [this MIT licensed Rust program](https://github.com/Icedude907/gba-joyboot-client) by
Icedude907 with added functionality to
save the EWRAM data after the ROM has been transmitted to the program
via GBA TCP. I’ve distributed this program [via a GitHub Gist](https://gist.github.com/sethmlarson/db751b59722f3b201da63097f086c3f6).

Using the program requires the Dolphin emulator and dumping the ROM
of the Billy Hatcher GameCube disc you intend to download Joyboot ROMs from.
In the case of Billy Hatcher you also need to have unlocked the
[five different eggs](https://billyhatcher.fandom.com/wiki/GBA) hidden in
levels. The fastest way to get around this is
to [download a 100% save file](https://gc-saves.com/container/15) for your game’s region
and place the file into Dolphin’s save file folder.

To extract the ROMs, launch Dolphin and set the controller in port 4 to be “GBA (TCP)”; Billy Hatcher
in particular only works if the GC-to-GBA link cable is plugged
into port 4. Start Dolphin playing Billy Hatcher, navigate to the
world map, and then select “Joycarry Game”. From here you can select
each game to be downloaded to our “GBA”, and the program should
display information about receiving the ROM data.

## Language setting and Joycarry ROMs

Something I did not know was that two of the five Joycarry ROMs,
“[ChuChu Rocket! Challenge](https://billyhatcher.fandom.com/wiki/GBA#Chu_Chu_Rocket!_Challenge)”
and “[Puyo Pop](https://billyhatcher.fandom.com/wiki/GBA#Puyo_Pop)”, have translations for both English and Japanese. Which Joyboot
ROM translation is sent to you depends on the game region
and which language is selected in the menu.

<div class="row">
<div class="col-6">
<p style="text-align: center;">
<img style="border: 2px black solid; max-width: 100%;" loading="lazy" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/gba-joyboot-client/chuchu-en.png">
<img style="border: 2px black solid; max-width: 100%;" loading="lazy" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/gba-joyboot-client/chuchu-ja.png">
<br>
<small><em>“ChuChu Rocket! Challenge”</em></small>
</p>
</div>
<div class="col-6">
<p style="text-align: center;">
<img style="border: 2px black solid; max-width: 100%;" loading="lazy" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/gba-joyboot-client/puyo-pop-en.png">
<img style="border: 2px black solid; max-width: 100%;" loading="lazy" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/gba-joyboot-client/puyo-pop-ja.png">
<br>
<small><em>“Puyo Pop”</em></small>
</p>
</div>
</div>

The NTSC region (GEZE8P) of the
game only supports English (no language selector in options)
and only has English Joycarry ROMs. The NTSC-J region (GEGJ8P) supports Japanese
and English, sending the corresponding Joycarry ROM depending on
which language is selected. The PAL region (GEZP8P) supports English, French,
German, Spanish, Italian, and ... *Japanese!* I checked each language,
and the English Joycarry ROM is sent for all languages except Japanese.

Here are the SHA256 checksums of each ROM by [game title](https://problemkaputt.de/gbatek-gba-cartridge-header.htm) and language:

| ROM Title | Language | SHA256 |
|-|-|-|
| `CHU2 AGB` | EN | `131258b587b4724ea06a5a0fbdce4d6ec05c8e63ef6b10a6000dfa8efd57c435` |
| `CHU2 AGB` | JP | `5adc33400eead9ce3d327377b7ce150a48e632abc2494370acb0b6ed61c1337a` |
| `NIGHTS` | EN | `944fadb8fac3abf8c7db38f837677be3d3a664c56e6c8eb58e9e1949a10ac5f9` |
| `BILLYHATCHER` | EN | `128afd1c40a65831bd013c2c91abdadd816155df2b1a5456a7af6d260d48108e` |
| `BILLYHATCHER` | EN | `2af4d14151981c2341c193cd2cc3d38e10dee1336ebedcd264f8e8bcb5e1f87e` |
| `MINNADE PUYO` | EN | `e769bd190bee6735a97cd239f587e3921108073a6f20ab20b8d62ba9c447cc12` |
| `MINNADE PUYO` | JP | `521f6a2a0876f2685205c0cfbfde934c14b8b3a6b5c173f4aa9fdfe93aed80a5` |

<em>Happy Halloween!</em> 🎃👻