# mGBA → Dolphin not working? You need a GBA BIOS

The GBA emulator “[mGBA](https://mgba.io/)” supports emulating the
[Game Boy Advance Link Cable](https://en.wikipedia.org/wiki/GameCube_%E2%80%93_Game_Boy_Advance_link_cable)
(not to be confused with the [Game Boy Advance /*Game*/ Link Cable](https://en.wikipedia.org/wiki/Game_Link_Cable#Third_generation))
and connecting to a running [Dolphin emulator](https://dolphin-emu.org) instance.
I am interested in this functionality for [Legend of Zelda: Four Swords Adventures](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Four_Swords_Adventures),
specifically the “[Navi Trackers](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Four_Swords_Adventures#Navi_Trackers)”
game mode that was announced for all regions but was only released in Japan
and Korea. In the future I want to explore the [English](https://forums.dolphin-emu.org/Thread-tetra-s-trackers-navi-tracker-translation-02-05-2023) [language](https://www.patreon.com/posts/zelda-four-beta-60032999) patches.

<!-- more -->

After [reading the documentation](https://dolphin-emu.org/blog/2021/04/24/mgba-and-dolphin-connectivity/) to connect the two emulators I configured the
controllers to be “GBA (TCP)” in Dolphin and ensured that Dolphin had the
permissions it needed to do networking (Dolphin is installed as a Flatpak).
I selected “Connect” on mGBA from the “Connect to Dolphin” popup screen
and there was zero feedback... no UI changes, errors, or success messages. Hmmm...

I found out in a random Reddit comment section that a GBA BIOS was needed to connect to Dolphin, so I set off
to legally obtain the BIOSes from my hardware.
I opted to use the [BIOS-dump ROM](https://github.com/mgba-emu/bios-dump) developed by the mGBA team
to dump the BIOS from my Game Boy Advance SP and DS Lite.

Below is a guide on how to [build the BIOS ROM from source](https://github.com/mgba-emu/bios-dump)
on Ubuntu 24.04, and then dump GBA BIOSes. Please note you'll likely need a GBA flash cartridge
for running homebrew on your Game Boy Advance. I used
an EZ-Flash Omega flash cartridge, but I've heard Everdrive GBA is also popular.

## Installing devKitARM on Ubuntu 24.04

To build this ROM from source you'll need [devKitARM](https://devkitpro.org/wiki/Getting_Started).
If you already have devKitARM installed you can skip these steps.
The devKitPro team supplies an [easy script](https://apt.devkitpro.org/install-devkitpro-pacman) for installing
devKitPro toolsets, but unfortunately the `apt.devkitpro.org` domain
appears to be behind an aggressive “bot” filter right now
so their instructions to use `wget` are not working as written.

Instead, download [their GPG key](https://apt.devkitpro.org/devkitpro-pub.gpg)
with a browser and then run the commands yourself:

```shell
apt-get install apt-transport-https

if ! [ -f /usr/local/share/keyring/devkitpro-pub.gpg ]; then
  mkdir -p /usr/local/share/keyring/
  mv devkitpro-pub.gpg /usr/local/share/keyring/
fi

if ! [ -f /etc/apt/sources.list.d/devkitpro.list ]; then
  echo "deb [signed-by=/usr/local/share/keyring/devkitpro-pub.gpg] https://apt.devkitpro.org stable main" > /etc/apt/sources.list.d/devkitpro.list
fi

apt-get update
apt-get install devkitpro-pacman
```

Once you've installed devKitPro pacman (for Ubuntu: `dkp-pacman`)
you can install the GBA development tools package group:

```shell
dkp-pacman -S gba-dev
```

After this you can set the `DEVKITARM` environment variable
within your shell profile to `/opt/devkitpro/devkitARM`.
Now you should be ready to build the GBA BIOS dumping ROM.

## Building the bios-dump ROM

Once devKitARM toolkit is installed the next step is much easier.
You basically download the source, run `make` with the `DEVKITARM` environment variable
set properly, and if all the tools are installed you'll quickly have
your ROM:

```shell
apt-get install build-essential curl unzip
curl -L -o bios-dump.zip \
    https://github.com/mgba-emu/bios-dump/archive/refs/heads/master.zip
unzip bios-dump.zip
cd bios-dump-master
export DEVKITARM=/opt/devkitpro/devkitARM/
make
```

You should end up with a GBA ROM file titled `bios-dump.gba`.
Add this `.gba` file to your microSD card for the flash cartridge.
Boot up the flash cartridge using the device you are trying to dump
BIOS of and after boot-up the screen should quickly show a success message
along with checksums of the BIOS file. As noted in the mGBA bios-dump README, there are two GBA BIOSes:

* `sha256:fd2547`: GBA, GBA SP, GBA SP “AGS-101”, GBA Micro, and Game Boy Player.
* `sha256:782eb3`: DS, DS Lite, and all 3DS variants

I own a GBA SP, a Game Boy Player, and a DS Lite, so I was able to 
dump three different GBA BIOSes, two of which are identical:

```shell
sha256sum *.bin
fd2547...  gba_sp_bios.bin
fd2547...  gba_gbp_bios.bin
782eb3...  gba_ds_bios.bin
```

From here I was able to configure mGBA with a GBA BIOS file (Tools→Settings→BIOS)
and successfully connect to Dolphin running four instances of mGBA; one for each
of the Links!

<div class="row">
<div class="col-8">
<p style="text-align: center;"><img style="border: 2px solid black; max-width: 100%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/G4SE01_2026-01-17_17-11-00.png"/></p>
</div>
<div class="col-4">
<p style="text-align: center;"><img style="border: 2px solid black; max-width: 100%;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/gba_bios-0.png"/></p>
<p style="text-align: center"><nobr>💚❤️💙💜</nobr></p>
<p>mGBA probably could have shown an error message
when the “connecting” phase requires a BIOS.
Looks like this behavior been known <a href="https://github.com/mgba-emu/mgba/issues/2210">since 2021</a>.</p>
</div>
</div>
