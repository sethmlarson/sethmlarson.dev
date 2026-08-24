# Playing the “Second Quest” of Legend of Zelda: Four Swords Adventures

[The Legend of Zelda: Four Swords Adventures](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Four_Swords_Adventures) (FSA) was released for the Nintendo
GameCube in 2004 in Japan and America and 2005 globally. The game is split into eight areas with three levels per area.
Data miners discovered that there were 8 levels that were cut late into development of the game that were
all mostly playable. These cut levels can be seen on [The Cutting Room Floor](https://tcrf.net/The_Legend_of_Zelda:_Four_Swords_Adventures/Unused_Rooms).

In 2021 a game modding and localizing group named “[Eternal Dream Arabization](https://www.patreon.com/EternalDream)”
and [$$$Link](https://x.com/SSSLink64) created a mod for FSA which restored and made these previously unseen levels completable.
The group used [EFSAdvent](https://www.jaytheham.com/efsa) ([source code](https://github.com/Venomalia/EFSAdvent)),
a level editing tool for FSA, to make the levels completable by fixing issues
and adding Force Gems where necessary.

<!-- more -->

The mod itself is a collection of map files to be inserted into the game ROM
and Action Replay codes that overwrite the map file loaded when entering
the final level in each respective area. Here is the full list of cut levels in order:

* River Flow (1-3)
* Rainy Forest (2-3)
* Mountain Road (3-3)
* Graveyard (4-3)
* Four Descents into the Darkness (5-3) 
* Oasis (6-3)
* Through the Blizzard (7-3)
* Clouds Across the Wind (8-2)

This game is one of the least played titles in the Legend of Zelda series,
selling fewer than 500,000 copies globally and hasn't yet been re-released on any platform.
(Edited August 24th, 2026) I was able to find a YouTube creator
who has published all the cut levels being played. The video by Gdmc5 was published
a few weeks before publishing this article. Below
is the video of all levels being played:

<p><center>
<iframe style="border: 2px solid black" width="560px" height="315px" src="https://www.youtube.com/embed/qLEruB2OU1c?si=wNkUlfo9a98Y1nzo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center></p>

## How to play

If you'd like to play these cut levels yourself below is a
complete guide on how to do so using an emulator like Dolphin
and on real GameCube hardware using Swiss. To start you need:

* A legally obtained ROM of Legend of Zelda: Four Swords Adventures.
  I used FlippyDrive’s built-in [Disk Backup utility](https://docs.flippydrive.com/backup.html) to dump the ROMs from disks I own.
* An install of [Python](https://www.python.org/) and [pyisotools](https://pypi.org/project/pyisotools)
* [FSA Second Quest level files](https://www.patreon.com/EternalDream/posts/zelda-four-beta-60032999) (`FSA_SecondQuest.7z`). I've [mirrored these
  files on GitHub](https://github.com/sethmlarson/loz-four-swords-adventures-second-quest) in case they are ever removed from Patreon.
* An emulator like Dolphin or a modded GameCube with Swiss
* If using a Japanese ROM of FSA+, the FSA+ English Translation Port
  must be applied in addition to Second Quest level files

Start by making a copy the ROM, as we'll be modifying the contents
using `pyisotools`. Create a new directory with a Python virtual environment
(`python -m venv venv`). Activate the virtual environment (`source venv/bin/activate`).
Install `pyisotools` and its dependencies using pip, I used the following lock file
to do so:

```
python -m pip install \
  altgraph==0.17.5 \
  astroid==4.0.4 \
  beautifulsoup4==4.15.0 \
  bs4==0.0.2 \
  certifi==2026.6.17 \
  cffi==2.0.0 \
  chardet==7.4.3 \
  charset-normalizer==3.4.7 \
  cryptography==49.0.0 \
  dill==0.4.1 \
  dolreader==1.1.1 \
  idna==3.18 \
  isort==8.0.1 \
  mccabe==0.7.0 \
  packaging==26.2 \
  pillow==12.3.0 \
  platformdirs==4.10.0 \
  pycparser==3.0 \
  pygithub==2.9.1 \
  pyinstaller==6.21.0 \
  pyinstaller-hooks-contrib==2026.6 \
  pyisotools==2.4.7 \
  pyjwt[crypto]==2.13.0 \
  pylint==4.0.6 \
  pynacl==1.6.2 \
  pyside6==6.11.1 \
  pyside6-addons==6.11.1 \
  pyside6-essentials==6.11.1 \
  qdarkstyle==3.2.3 \
  qtpy==2.4.3 \
  requests==2.34.2 \
  shiboken6==6.11.1 \
  sortedcontainers==2.4.0 \
  soupsieve==2.8.4 \
  tomlkit==0.15.0 \
  typing-extensions==4.16.0 \
  urllib3==2.7.0
```

If you're not interested in copy-and-pasting this command you
can full-send install using `python -m pip install pyisotools`
and cross your fingers.

From here we're going to add the modded map files to the ISO.
Use the extract (`E`) command with `pyisotools` to extract the ISO
to a directory:

```
python -m pyisotools './The Legend of Zelda- Four Swords FOR NINTENDO GAMECUBE (v1.00).iso' E --dest .
```

This will create a directory called `root/` in the current directory
with the extracted files. Copy the files from `FSA_SecondQuest` into
the `root/files/GC4Sword_usa/Boss` directory:

```
cp FSA_SecondQuest/boss*.arc root/files/GC4Sword_usa/Boss
```

If you are using the Japanese ROM for FSA, at this point you'd
also do the file replacements for the `FS+_EN_Translation_Port`
files, too. For the English ROM this is not necessary.

Now we build (`B`) an ISO again using these new files. Make sure you've made
a copy of your ROM before doing this to avoid needing to dump the ROM
from the disk again.

```
python -m pyisotools root/ B --dest './The Legend of Zelda- Four Swords FOR NINTENDO GAMECUBE (v1.00).iso'
```

Now we have a modified ROM that is ready to be played! To load into
the cut levels we'll need to use Action Replay cheat codes depending
on our platform, either Dolphin or Swiss.

## Action Replay codes

I've tested the Action Replay codes supplied by the project, and they didn't work
as expected, so after testing I used the [Action Replay codes from
The Cutting Room Floor](https://tcrf.net/The_Legend_of_Zelda:_Four_Swords_Adventures/Unused_Rooms#:~:text=Cheat%20Codes) instead.
I also added the Action Replay code to the US version for unlocking all areas and levels
immediately so you can quickly visit each level. For the JP region I could not
find an associated Action Replay code, but there are [100% completed
save files available](https://gc-saves.com/container/86) for each region.
Remember for Dolphin you must explicitly "Enable Cheats" for these codes to work.

<blockquote>
<details>
<summary>Action Replay codes (US)</summary>
<p>All Adventure Mode Levels Unlocked (Codejunkies)</p>
<pre><code>0450ECA8 FFFFFFFF
0450ED70 FFFFFFFF
0450EE38 FFFFFFFF
</code></pre>
<p>Replace Level 3 with Cut Sub-Stages (The Cutting Room Floor)</p>
<pre><code>04466054 3031322E
04466084 3032322E
044660B4 3033322E
044660E4 3034322E
04466114 3035322E
04466144 3036322E
04466174 3037322E
044661A4 3038322E
044811EC 31322E63
0448121C 32322E63
0448124C 33322E63
0448127C 34322E63
044812AC 35322E63
044812DC 36322E63
0448130C 37322E63
0448133C 38322E63
04481524 31325F31
04481554 32325F31
04481584 33325F31
044815B4 34325F31
044815E4 35325F31
04481614 36325F31
04481644 37325F31
04481674 38325F31
04538A14 30313200
04538A24 30323200
04538A34 30333200
04538A44 30343200
04538A54 30353200
04538A64 30363200
04538A74 30373200
04538A84 30383200
</code></pre>
</details>
</blockquote>

<blockquote>
<details>
<summary>Action Replay codes (JP)</summary>
<p>Replace Level 3 with Cut Sub-Stages (The Cutting Room Floor)</p>
<pre><code>04466054 3031322E
04466084 3032322E
044660B4 3033322E
044660E4 3034322E
04466114 3035322E
04466144 3036322E
04466174 3037322E
044661A4 3038322E
044811EC 31322E63
0448121C 32322E63
0448124C 33322E63
0448127C 34322E63
044812AC 35322E63
044812DC 36322E63
0448130C 37322E63
0448133C 38322E63
04481524 31325F31
04481554 32325F31
04481584 33325F31
044815B4 34325F31
044815E4 35325F31
04481614 36325F31
04481644 37325F31
04481674 38325F31
04538A14 30313200
04538A24 30323200
04538A34 30333200
04538A44 30343200
04538A54 30353200
04538A64 30363200
04538A74 30373200
04538A84 30383200
</code></pre>
</details>
</blockquote>

## Swiss cheats config files

Swiss cheat codes need to be supplied in their own format.
These are the same Action Replay codes as above, but in the
Swiss cheats format. These files should be placed into the
`swiss/cheats` folder on your microSD card (which you may
need to create) and on boot, the cheats need to be enabled
by pressing `Y` prior to launching the game through Swiss.

<blockquote>
<details>
<summary>Swiss cheats config (US, <code>G4SE01.txt</code>)</summary>
<pre><code>G4SE01
Legend of Zelda, The - Four Swords Adventures (USA)

All Adventure Mode Levels Unlocked [Codejunkies]
0450ECA8 FFFFFFFF
0450ED70 FFFFFFFF
0450EE38 FFFFFFFF

Replace Level 3 with Cut Sub-Stages [The Cutting Room Floor]
04466054 3031322E
04466084 3032322E
044660B4 3033322E
044660E4 3034322E
04466114 3035322E
04466144 3036322E
04466174 3037322E
044661A4 3038322E
044811EC 31322E63
0448121C 32322E63
0448124C 33322E63
0448127C 34322E63
044812AC 35322E63
044812DC 36322E63
0448130C 37322E63
0448133C 38322E63
04481524 31325F31
04481554 32325F31
04481584 33325F31
044815B4 34325F31
044815E4 35325F31
04481614 36325F31
04481644 37325F31
04481674 38325F31
04538A14 30313200
04538A24 30323200
04538A34 30333200
04538A44 30343200
04538A54 30353200
04538A64 30363200
04538A74 30373200
04538A84 30383200
</code></pre>
</details>
</blockquote>

<blockquote>
<details>
<summary>Swiss cheats config (JP, <code>G4SJ01.txt</code>)</summary>
<pre><code>G4SJ01
Legend of Zelda, The - Four Swords Adventures+ (Japan)

All Adventure Mode Levels Unlocked [Codejunkies]
0450ECA8 FFFFFFFF
0450ED70 FFFFFFFF
0450EE38 FFFFFFFF

Replace Level 3 with Cut Sub-Stages [The Cutting Room Floor]
04466054 3031322E
04466084 3032322E
044660B4 3033322E
044660E4 3034322E
04466114 3035322E
04466144 3036322E
04466174 3037322E
044661A4 3038322E
044811EC 31322E63
0448121C 32322E63
0448124C 33322E63
0448127C 34322E63
044812AC 35322E63
044812DC 36322E63
0448130C 37322E63
0448133C 38322E63
04481524 31325F31
04481554 32325F31
04481584 33325F31
044815B4 34325F31
044815E4 35325F31
04481614 36325F31
04481644 37325F31
04481674 38325F31
04538A14 30313200
04538A24 30323200
04538A34 30333200
04538A44 30343200
04538A54 30353200
04538A64 30363200
04538A74 30373200
04538A84 30383200
</code></pre>
</details>
</blockquote>