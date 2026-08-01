# Extracting “Ocarina of Time: Master Quest” ROM from the Legend of Zelda: Wind Waker bonus disc

Another day, another extracting ROMs from GameCube
titles mini-tutorial. This time it’s the PAL
Legend of Zelda: Wind Waker Bonus Disc that I
[recently purchased from Kraków, Poland](/pal-gamecube-haul-from-krakow-poland). This
disc contains two N64 games: [Legend of Zelda:
Ocarina of Time](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Ocarina_of_Time) and the “[Master Quest](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Ocarina_of_Time#Master_Quest)”
version of Ocarina of Time. Let’s extract those ROMs
from the GameCube ROM so we can play on other emulators.

<!-- more -->

Going from a GameCube disc to an ISO ROM is the usual
process, for me that means using the [FlippyDrive Disc Backup
Utility](https://docs.flippydrive.com/backup.html) but CleanRip on a GameCube or Wii also works.
To extract the individual files from the ISO open
the ISO in Dolphin, right-click the ISO, `Properties`,
`Filesystem`, and extract the `zlj_f.tgc` file into
your working directory.

According to [The Cutting Room Floor](https://tcrf.net/The_Legend_of_Zelda:_Ocarina_of_Time_Bonus_Disc) both N64 ROMs
are included in the file `zlj_f.tgc`. TGC is an
archive format that Nintendo uses often in this generation
of games. Thanks to resources like <nobr>[No Intro](https://no-intro.org/)</nobr>
we have the known-good ROM lengths and hashes for both Ocarina of
Time and Master Quest for all regions. Using this information
(along with the N64 ROM header) we can find the embedded N64 ROMs
within `zlj_f.tgc` without understanding the TGC format at all:

```python
# License: MIT

import hashlib

ROM_HEADER = b"\x80\x37\x12\x40"
ROM_LENGTH = 0x2000000
ROM_HASHES = {
    "1618403427e4344a57833043db5ce3c3": "Legend of Zelda, The - Ocarina of Time - Master Quest (Europe) (En,Fr,De) (Zelda Collection).n64",
    "2c27b4e000e85fd78dbca551f1b1c965": "Extracted Legend of Zelda, The - Ocarina of Time (Europe) (GameCube).n64",
    # If you see 'Unknown ROM', paste the MD5 into
    # https://datomatic.no-intro.org/index.php
    # searching on 'hash-data' and add the values here.
}

def main():
    data = open("zlj_f.tgc", "rb").read()

    # Find the embedded ROMs from the N64 ROM header.
    offset1 = data.find(ROM_HEADER)
    offset2 = (offset1 + 4) + data[(offset1 + 4):].find(ROM_HEADER)
    for offset in (offset1, offset2):

        # Determine which ROM we have based on MD5.
        rom = data[offset:offset + ROM_LENGTH]
        rom_md5 = hashlib.md5(rom).hexdigest()
        to_file = ROM_HASHES.get(rom_md5, None)
        if to_file is None:
            print(f"Unknown ROM ({rom_md5})")
            continue

        with open(to_file, "wb") as f:
            f.truncate()
            f.write(rom)
        print(f"Extracted {to_file} ({rom_md5})...")


if __name__ == "__main__":
    main()
```

The script above only knows about the ROM hashes for
the PAL revision of the Bonus Disc, so if you see `Unknown ROM (...)`,
don't panic! You can search the MD5 you receive on <nobr>[No Intro](https://datomatic.no-intro.org/index.php?page=search&s=64)</nobr>
by filtering on `hash-data` to discover whether the ROM
is correct and add the value to `ROM_HASHES` in the script.

With my Master Quest ROM in hand I can load the game into
[Delta Emulator](/getting-started-with-gamesir-pocket-taco-iphone-delta-emulator) and play on my iPhone:

<p><center>
<img style="max-width: 100%; box-sizing: content-box; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/loz-wind-waker-bonus-disk/loz-oot-master-quest.png">
<br><small><em>Legend of Zelda: Ocarina of Time Master Quest running in the Delta Emulator</em></small>
</center></p>

I won’t be playing much because I have never played
Ocarina of Time before and want to play the [upcoming remake
for the Nintendo Switch 2](https://www.nintendo.com/us/store/products/the-legend-of-zelda-ocarina-of-time-switch-2/) with a completely blank slate.
I’m excited to try one of the most universally acclaimed
games ever made for the first time soon! :)

## What’s new in the blogroll?

I [publish a blogroll](/blogroll) containing links to
websites that I've enjoyed recently.

Pokémon cards were on the mind the past few weeks! My
brother is a collector so we've been discussing the
different artists and sets that he's interested in.
While I was doing research I came across two websites
that seemed useful for this: collating [Pokémon set symbols](https://pokesymbols.com/tcg/sets)
and [Pokémon card artwork by artist](https://www.artofpkm.com).
A comedic graphic design YouTuber
“Elliot” also published a [new video about Pokémon’s
graphic designs](https://www.youtube.com/watch?v=p0m5nuygU5w) which I found entertaining.

I purchased “[htmx 4: the game](https://swag.htmx.org/en-usd/products/htmx-4-the-game)”, the first JavaScript library published
exclusively to the Nintendo Game Boy platform. The package (hah)
arrives today and I plan to post about the experience with the
game and discussing the form factor as a software distribution mechanism,
look forward to that blog post soon.

I found a [Game Boy Link Cable to internet adapter](https://gblink.io/) hardware project
which looks intriguing if you've got friends
that are far away that you still want to play Generation 3 Pokémon
with (*Pokémon Emerald forever*). This hardware enables trading, battling, record mixing, and
more by pretending to be your peer in a GBA Link Cable connection.
