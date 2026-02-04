# Dumping Nintendo e‑Reader Card “ROMs”

<div class="row">
<div class="col-12-sm col-9">
<!-- more -->
<p>The <a href="https://en.wikipedia.org/wiki/Nintendo_e‑Reader">Nintendo e‑Reader</a>
was a peripheral released for the Game Boy Advance in 2001. The Nintendo e‑Reader
allowed scanning <nobr>“dotcode strips”</nobr> to access extra content within games
or to <a href="https://niwanetwork.org/wiki/List_of_e‑Reader_applications">play mini-games</a>.
Today I'll show you how to use the <a href="https://www.epilogue.co/product/gb-operator">GB Operator</a>, a Game Boy ROM dumping tool,
in order to access the ROM encoded onto e‑Reader card dotcodes.</p>

<!-- more -->

<p>I'll be demonstrating using a new entrant to e‑Reader game development
for the venerable platform: <a href="https://www.retrodotcards.com/">Retro Dot Codes</a> by <a href="https://www.mattgreer.dev/">Matt Greer</a>.
Matt <a href="https://www.mattgreer.dev/blog/E-Reader/">regularly posts</a> about his process developing and printing e‑Reader cards
and games in 2026. I was a recipient for one of his free e‑Reader card giveaways
and purchased Retro Dot Cards “<a href="https://www.retrodotcards.com/series-one">Series 1</a>” pack
which I'm planning to open and play for the blog.</p>

<h2>Dumping a Nintendo e-Reader card contents</h2>

<p>The process is straightforward but requires a working GBA
or equivalent (GBA, GBA SP, Game Boy Player, DS, or <a href="#nintendo-e-reader-and-analogue-pocket">Analogue Pocket *</a>),
a Nintendo e-Reader cartridge, and a GBA ROM dumper like GB Operator.
Launch the e‑Reader cartridge using a Game Boy Advance, Analogue Pocket,
or Game Boy Player. The e-Reader software prompts you to scan the dotcodes.

<p>
The Solitaire card stores its program data on two <a href="https://www.problemkaputt.de/gbatek-gba-cart-e-reader-dotcode-format.htm#:~:text=Data%20Size">“long” dotcode strips</a>
consisting of 28 “blocks” per-strip encoding 104 bytes-per-block for a total of 5824 bytes on two strips (2×28×104=5824). <span class="hidden-lg">If you want to see approximately how large a dotcode strip is, open this page in a desktop browser.</span>
After scanning each side of the Solitaire card you can play Solitaire on your console:</p>

<p>
<center>
<iframe style="border: 2px black solid; max-width: 100%; height: auto;" src="https://www.youtube.com/embed/yrCnlQbR8Qw?si=KJpApK3h3RxtaBHu" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>
</p>

<p>I'll be honest, I was never into <a href="https://en.wikipedia.org/wiki/Microsoft_Solitaire">Solitaire</a> as a kid, I was more “<a href="https://en.wikipedia.org/wiki/Full_Tilt!_Pinball#Space_Cadet">Space Cadet Pinball</a>” on Windows...
Anyways, let's archive the “ROM” of this game so even if we lose the physical card we can
still play.</p>

<p>Turn off your device and connect the e‑Reader cartridge to the GB Operator.
Following the <a href="https://sethmlarson.dev/backup-game-boy-roms-and-saves-on-ubuntu">steps I documented for Ubuntu</a>, start “Epilogue Playback”
software
and dump the e‑Reader ROM and critically: the save data. The Nintendo e‑Reader
supports saving your already scanned game in the save data of the cartridge so you
can play again next time you boot without needing to re-scan the cards.</p>

<p>Now we have a <code>.sav</code> file. This file works as an archive of the
program, as we can load our e-Reader ROM and this save into a GBA emulator to play again.
<strong>Success!</strong>
</p>

<h2>Examining e-Reader Card ROMs</h2>

<p>Now that we have the <code>.sav</code> file for the Solitaire ROM, let's see
what we can find inside. The file itself
is mostly empty, consisting almost entirely of <code>0xFF</code> and <code>0x00</code> bytes:</p>

<div class="codehilite">
<pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="n">data</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"Solitaire.sav"</span><span class="p">,</span> <span class="s2">"rb"</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">),</span> <span class="nb">hex</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
<span class="go">(131072, '0x20000')</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">sum</span><span class="p">(</span><span class="n">b</span> <span class="o">==</span> <span class="mh">0xFF</span> <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="n">data</span><span class="p">)</span>
<span class="go">118549</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">sum</span><span class="p">(</span><span class="n">b</span> <span class="o">==</span> <span class="mh">0x00</span> <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="n">data</span><span class="p">)</span>
<span class="go">8200</span>
</code></pre>
</div>

<p>We know from the data limits of 2 dotcode strips
that there's only 5824 bytes maximum for program data.
If we look at the <a href="https://www.caitsith2.com/ereader/ereader%20save%20format.txt">format of e‑Reader save files</a>
documented at <a href="https://www.caitsith2.com">caitsith2.com</a> we can see what
this data means. I've duplicated the page below, just in case:</p>

<p></p><details>
<summary><code>ereader save format.txt</code></summary><p></p>

<pre><code>
US E-reader save format

Base Address = 0x00000 (Bank 0, address 0x0000)

Offset  Size        Description
0x0000  0x6FFC      Bank 0 continuation of save data.
0x6FFD  0x6004      All 0xFF
0xD000  0x0053      43617264 2D452052 65616465 72203230
                    30310000 67B72B2E 32333333 2F282D2E
                    31323332 302B2B30 31323433 322F2A2C
                    30333333 312F282C 30333233 3230292D
                    30303131 2F2D2320 61050000 80FD7700
                    000001
0xD053  0x0FAD      All 0x00s
0xE000  0x1000    Repeat 0xD000-0xDFFF
0xF000  0x0F80      All 0xFFs
0xFF80  0x0080      All 0x00s


Base Address = 0x10000 (Bank 1, address 0x0000)

Offset  Size        Description
0x0000  0x04        CRC (calculated starting from 0x0004,  and amount of data to calculate is
                      0x30 + [0x002C] + [0x0030].)
0x0004  0x24        Program Title (Null terminated) - US = Straight Ascii,  Jap = Shift JIS
0x0028  0x04        Program Type
                        0x0204 = ARM/THUMB Code/data (able to use the GBA hardware directly, Linked to 0x02000000)
                        0x0C05 = 6502 code/data (NES limitations, 1 16K program rom + 1-2 8K CHR rom, mapper 0 and 1)
                        0x0400 = Z80 code/data (Linked to 0x0100)
0x002C  0x04        Program Size
                        = First 2 bytes of Program data, + 2
0x0030  0x04        Unknown
0x0034  Program Size    Program Data (vpk compressed)
                First 2 bytes = Size of vpk compressed data
0xEFFF  0x01        End of save area in bank 1. Resume save data in bank 0.

The CRC is calculated on Beginning of Program Title, to End of Program Data.
If the First byte of Program Title is 0xFF, then there is no save present.
If the CRC calculation does not match stored CRC, then the ereader comes up with
an ereader memory error.

CRC calculation Details

CRC table is calculated from polynomial 0x04C11DB7 (standard CRC32 polynomial)
with Reflection In.  (Table entry 0 is 0, and 1 is 0x77073096...)

CRC calculation routine uses Initial value of 0xAA478422.  The Calculation routine
is not a standard CRC32 routine, but a custom made one, Look in "crc calc.c" for
the complete calculation algorithm.

Revision history

v1.0 - First release
V1.1 - Updated/Corrected info about program type.
v1.2 - Updated info on Japanese text encoding
v1.3 - Info on large 60K+ vpk files.
</code></pre>

<p></p></details><p></p>

<p>From this format specification we can see that
the program data starts around offset <code>0x10000</code>
with the CRC, the program title, type, size,
and the program data which is compressed
using the <a href="https://github.com/tehzz/vpk0">VPK0 compression algorithm</a>.
Searching through our save data, sure enough we see some
data at the offsets we expect like the program title and the
VPK0 magic bytes <code>vpk0</code>:</p>

<div class="codehilite">
<pre><span></span><code><span class="gp">&gt;&gt;&gt; </span><span class="nb">hex</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="sa">b</span><span class="s2">"Solitaire</span><span class="se">\x00</span><span class="s2">"</span><span class="p">))</span>
<span class="go">'0x10004'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">hex</span><span class="p">(</span><span class="n">data</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="sa">b</span><span class="s2">"vpk0"</span><span class="p">))</span>
<span class="go">'0x10036'</span>
</code></pre>
</div>

<p>We know that the VPK0-compressed blob length encoded to the two bytes
before the magic header in little-endian. Let's grab that value
and write the VPK0-compressed blob to a new file:</p>

<div class="codehilite">
<pre><span></span><code><span class="o">&gt;&gt;&gt;</span> <span class="n">vpk_idx</span> <span class="o">=</span> <span class="n">data</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="sa">b</span><span class="s2">"vpk0"</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">vpk_len</span> <span class="o">=</span> <span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span>
<span class="o">...</span>   <span class="n">data</span><span class="p">[</span><span class="n">vpk_idx</span><span class="o">-</span><span class="mi">2</span><span class="p">:</span><span class="n">vpk_idx</span><span class="p">],</span> <span class="s2">"little"</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">"Solitaire.vpk"</span><span class="p">,</span> <span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
<span class="o">...</span>    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="n">vpk_idx</span><span class="p">:</span><span class="n">vpk_idx</span><span class="o">+</span><span class="n">vpk_len</span><span class="p">])</span>
</code></pre>
</div>

<p>In order to decompress the program data we'll need
a tool that can decompress VPK0. The <a href="https://github.com/AkBKukU/e-reader-dev">e‑Reader development
tools repository</a> points to <code>nevpk</code>.
You can download the <a href="https://github.com/breadbored/nedclib">source code</a>
for multi-platform support and compile using <code>cmake</code>:</p>

<div class="codehilite">
<pre><span></span><code>curl<span class="w"> </span>-L<span class="w"> </span>https://github.com/breadbored/nedclib/archive/749391c049756dc776b313c87da24b7f47b78eea.zip<span class="w"> </span><span class="se">\</span>
<span class="w">    </span>-o<span class="w"> </span>nedclib.zip
unzip<span class="w"> </span>nedclib.zip
cmake<span class="w"> </span>. && make

<span class="c1"># Now we can use nevpk to decompress the program.</span>
nevpk<span class="w"> </span>-d<span class="w"> </span>-i<span class="w"> </span>Solitaire.vpk<span class="w"> </span>-o<span class="w"> </span>Solitaire.bin
md5sum<span class="w"> </span>Solitaire.bin
3a898e8e1aedc091acbf037db6683a41<span class="w">  </span>Solitaire.bin
</code></pre>
</div>

<p>This <code>Solitaire.bin</code> file is the original binary that Matt compiled
before compressing, adding headers, and <a href="https://www.mattgreer.dev/blog/E-Reader-Printing/">printing the
program onto physical cards</a>. Pretty cool that we can
reverse the process this far!</p>

<h2>Nintendo e-Reader and Analogue Pocket</h2>

<p>The <a href="https://www.analogue.co/pocket">Analogue Pocket</a> is a hardware emulator
that uses an <a href="https://en.wikipedia.org/wiki/Field-programmable_gate_array">FPGA</a>
to emulate multiple retro gaming consoles, including the GBA. One of the prominent features
of this device is its cartridge slot, allowing you to play cartridges without
dumping them to ROM files first.
</p>
<p>But there's just one problem with using the Analogue Pocket with the Nintendo e-Reader.
The cartridge slot is placed low on the device, making it <a href="https://bsky.app/profile/sethmlarson.dev/post/3lbbgiit5xs2j">impossible to insert oddly-shaped cartridges</a>
like the Nintendo e-Reader. Enter the <em><a href="https://bsky.app/profile/retrodotcards.com/post/3lvvlzkmvc227">E-Reader Extender</a>!</em>
This project by <a href="https://bsky.app/profile/did:plc:gnjjybtogdtlktwcnraci7hi">Brian Hargrove</a>
extends the cartridge slot while giving your Analogue Pocket a big hug.
</p>

<h2>Playing Nintendo e-Reader games on Delta Emulator</h2>

<p>The best retro emulator is the one you bring with you,
for this reason the <a href="https://faq.deltaemulator.com/">Delta Emulator</a> is my emulator of choice as it runs on iOS.
However, there are challenges to running e-Reader games on
Delta: specifically that Delta <em>only allows one save file per
GBA ROM</em>. This means to change games you'd need to import
a new e-Reader save file.
Delta stores ROMs and saves by their ROM checksum (MD5).
</p>
</div>
<div class="col-3 hidden-sm" style="text-align: center;">
<p style="text-align: center;"><small><em>One of two dotcode strips for the Solitaire <nobr>e‑Reader card</nobr></em></small></p>
<img style="max-width: 100%; image-rendering: pixelated;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/solitaire.dotcode1.png"/>
</div>
</div>

