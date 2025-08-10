# Extracting 20+ NES & Famicom ROMs from Animal Crossing

[Animal Crossing](https://nookipedia.com/wiki/Animal_Crossing) for the GameCube was a game far ahead of its
time and one of my personal favorites growing up. One of the
most beloved features was the addition of playable [NES games](https://nookipedia.com/wiki/NES_game)
as rare collectible furniture items.

This feature was implemented by including NES and Famicom Disk System emulators
and the actual game ROMs on the Animal Crossing disk.
The NES emulator included
with Animal Crossing is frequently referenced as being one of the
most accurate NES emulators available, but comes with the requirement
of playing or emulating a GameCube to access the feature.

<!-- more -->

What if
you wanted to play these ROMs on a different emulator without having
to jump into your Animal Crossing town, is that possible?

## What game ROMs are available?

<div class="row">
<div class="col-6">
<p>There are <strong>21 total
NES and <nobr>Famicom Disk System (FDS) ROMs</nobr></strong> across the first generation of Animal
Crossing games. Different games are included <a href="https://nookipedia.com/wiki/NES_game">depending on the
edition of the game</a> (<nobr>Doubutsu no Mori</nobr>, <nobr>Doubutsu no Mori+</nobr>, <nobr>Animal Crossing</nobr>, or <nobr>Doubutsu no Mori e+</nobr>)
with <strong><nobr>Animal Crossing</nobr> containing the most unique games at 19</strong>.
Different ROMs are sometimes used <a href="https://nookipedia.com/wiki/NES_game#ROMs">depending on the game's region</a>.</p>

<p>I've included a full list of games available along with two
other data columns. The first being the "loose" game price from <a href="https://www.pricecharting.com/">Pricecharting</a>
at the time of publication. Buying physical copies of
all the games included in Animal Crossing
<strong>costs just over $500 USD!</strong></p>

<p>The second column is whether the game is available as a part of
the <a href="https://www.nintendo.com/us/store/products/nintendo-entertainment-system-nintendo-switch-online-switch/">"Nintendo Entertaminment System™ Nintendo Switch Online" subscription</a>,
here abbreviated as "NSO".</p>
</div>
<div class="col-6">
<table style="font-variant-numeric: tabular-nums; margin-left: auto; margin-right: auto;">
<thead>
<tr>
  <th>Game</th>
  <th>Price</th>
  <th>NSO?</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Balloon Fight</td>
  <td><a href="https://www.pricecharting.com/game/nes/balloon-fight">$30</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Baseball</td>
  <td><a href="https://www.pricecharting.com/game/nes/baseball">$5</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Clu Clu Land</td>
  <td><a href="https://www.pricecharting.com/game/nes/clu-clu-land">$40</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Clu Clu Land D (1)</td>
  <td><a href="https://www.pricecharting.com/game/famicom-disk-system/clu-clu-land">$42</a></td>
  <td>No</td>
</tr>
<tr>
  <td>Donkey Kong</td>
  <td><a href="https://www.pricecharting.com/game/nes/donkey-kong">$47</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Donkey Kong 3</td>
  <td><a href="https://www.pricecharting.com/game/nes/donkey-kong-3">$18</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Donkey Kong Jr.</td>
  <td><a href="https://www.pricecharting.com/game/nes/donkey-kong-jr-math">$151</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Excitebike</td>
  <td><a href="https://www.pricecharting.com/game/nes/excitebike">$11</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Golf</td>
  <td><a href="https://www.pricecharting.com/game/nes/golf">$7</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Gomoku Narabe Renju (2)</td>
  <td><a href="https://www.pricecharting.com/game/famicom/renju-gomoku-narabe">$3</a></td>
  <td>No</td>
</tr>
<tr>
  <td>Ice Climber</td>
  <td><a href="https://www.pricecharting.com/game/nes/ice-climber">$24</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>The Legend of Zelda</td>
  <td><a href="https://www.pricecharting.com/game/nes/legend-of-zelda">$27</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Mahjong (2)</td>
  <td><a href="https://www.pricecharting.com/game/famicom/mahjong">$8</a></td>
  <td>No</td>
</tr>
<tr>
  <td>Pinball</td>
  <td><a href="https://www.pricecharting.com/game/nes/pinball">$4</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Punch-Out!!</td>
  <td><a href="https://www.pricecharting.com/game/nes/punch-out">$19</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Super Mario Bros.</td>
  <td><a href="https://www.pricecharting.com/game/nes/super-mario-bros">$15</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Tennis</td>
  <td><a href="https://www.pricecharting.com/game/nes/tennis">$9</a></td>
  <td>Yes</td>
</tr>
<tr>
  <td>Wario's Woods</td>
  <td><a href="https://www.pricecharting.com/game/nes/wario%27s-woods">$44</a></td>
  <td>Yes</td>
</tr>
<tr style="background-color: #e9e9e9; font-weight: 700;">
  <td>Total</td>
  <td>$504</td>
  <td></td>
</tr>
</tbody>
</table>
<p></p>
</div>
</div>

> **NOTE (1):** You will need to convert the QD file (`.qd`) for "Clu Clu Land: Welcome to New Clu Clu Land" into an FDS file (`.fds`)
to play the ROM with an emulator. Here's a [simple Python script](https://gist.github.com/infval/18d65dd034290fb908f589dcc10c6d25) that I found on GitHub
that worked perfectly.

> **NOTE (2):** If you happen to also own Animal Forest+ (but not Animal Forest e+) you can also obtain
"[Mahjong](https://www.pricecharting.com/game/famicom/mahjong)" and
"[Renju Gomoku Narabe](https://www.pricecharting.com/game/famicom/renju-gomoku-narabe)"
(ごもくならべ) Famicom games.

## Extracting the ROMs

So if we've archived the Animal Crossing ROM from the physical disk using
CleanRip or the FlippyDrive backup tool,
what can we do to extract the NES and FDS ROM files?

When I went looking for answers, originally I tried tracking
down the exact offsets within the Animal Crossing ROM
using the [Animal Crossing decompilation project](https://github.com/ACreTeam/ac-decomp)
as a reference. This turned out to be unnecessary, as I discovered
that the ROM data was likely compressed.

Knowing that the ROM data was compressed, on a hunch I checked
the ROM for all Yaz0-compressed blobs. Yaz0 is commonly used by
Nintendo for compressing assets. Sure enough, the ROMs were all
compressed using Yaz0 which uses a highly identifiable magic string
of "`Yaz0`".
This meant we could extract all ROM files by decompressing all
Yaz0 blobs and then look for NES and FDS ROM headers.

Below is the entire script I used to archive the NES ROMs from the
Animal Crossing ISO, including an implementation of the [Yaz0](http://www.amnoid.de/gc/yaz0.txt)
compression scheme:

<p>
<details>
<summary>Click to show <code>animal-crossing-nes-roms.py</code> source code</summary>
<div class="codehilite">
<pre><span></span><code><span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">import</span> <span class="nn">mmap</span>
<span class="kn">import</span> <span class="nn">hashlib</span>
<span class="kn">import</span> <span class="nn">struct</span>

<span class="c1"># MD5 hashes from https://datomatic.no-intro.org</span>
<span class="c1"># Headerless, as header is changed from non-AC releases.</span>
<span class="n">known_roms</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">"0033972cb952bbbc4f04217decdaf3a7"</span><span class="p">:</span> <span class="s2">"Mahjong (Japan) (Rev 2) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"0dd95c3047bb0336823c39fefb7639c3"</span><span class="p">:</span> <span class="s2">"Donkey Kong (World) (Rev 1) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"1ca706896a8d4f2a2b5480d941130a4a"</span><span class="p">:</span> <span class="s2">"Donkey Kong Jr. Math (USA, Europe).nes"</span><span class="p">,</span>
    <span class="s2">"1de41e13a2e691a8cc13b757a46ae3b8"</span><span class="p">:</span> <span class="s2">"Clu Clu Land (World) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"27b4479df4228d48986698ffb94e9f6b"</span><span class="p">:</span> <span class="s2">"Punch-Out!! (USA).nes"</span><span class="p">,</span>
    <span class="s2">"28c4a5b81feb4033acee9d67852d8ffc"</span><span class="p">:</span> <span class="s2">"Gomoku Narabe Renju (Japan) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"2bf3976d15ec25a756846465a16b064c"</span><span class="p">:</span> <span class="s2">"Excitebike (Japan, USA) (En) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"44d401f92e1da528ca4a9d7083acc9d2"</span><span class="p">:</span> <span class="s2">"Clu Clu Land (Japan) (En) (GameCube, Virtual Console).qd"</span><span class="p">,</span>
    <span class="s2">"5f37d85ba0f296bd471cd674d63cb640"</span><span class="p">:</span> <span class="s2">"Legend of Zelda, The (USA) (Rev 1) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"8e3630186e35d477231bf8fd50e54cdd"</span><span class="p">:</span> <span class="s2">"Super Mario Bros. (World).nes"</span><span class="p">,</span>
    <span class="s2">"70c309cb6b9ead20c06d554cf48b3993"</span><span class="p">:</span> <span class="s2">"Balloon Fight (USA).nes"</span><span class="p">,</span>
    <span class="s2">"108fea367dc5ba9a691b3500fc1464b4"</span><span class="p">:</span> <span class="s2">"Baseball (USA, Europe) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"6631ceac1aaef8efb063a34da86bacb1"</span><span class="p">:</span> <span class="s2">"Donkey Kong Jr. (World) (Rev 1) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"a2b5bddb4c7a5a39c8fac13e64494c9a"</span><span class="p">:</span> <span class="s2">"Donkey Kong 3 (World).nes"</span><span class="p">,</span>
    <span class="s2">"bec7fa447c1c8e13a87bd4a5685ce563"</span><span class="p">:</span> <span class="s2">"Wario's Woods (USA).nes"</span><span class="p">,</span>
    <span class="s2">"bfab5f738adb919f1ba389f5c38deb67"</span><span class="p">:</span> <span class="s2">"Pinball (Japan, USA) (En) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"c9c94df2ebb19bd6d717b2cfbf977574"</span><span class="p">:</span> <span class="s2">"Ice Climber (USA, Europe, Asia) (En).nes"</span><span class="p">,</span>
    <span class="s2">"c432b613606c41bafa4a09470d75e75f"</span><span class="p">:</span> <span class="s2">"Soccer (Japan, USA) (En).nes"</span><span class="p">,</span>
    <span class="s2">"cbb2c477a37b28517e330d1c562049f8"</span><span class="p">:</span> <span class="s2">"Tennis (Japan, USA) (En) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"d67ee6a0a7af959c417ce894470a49cb"</span><span class="p">:</span> <span class="s2">"Mario Bros. (World) (Animal Crossing).nes"</span><span class="p">,</span>
    <span class="s2">"f0d94f25db202c935cd8f1cdde10a0aa"</span><span class="p">:</span> <span class="s2">"Golf (USA, Asia) (En).nes"</span><span class="p">,</span>
    <span class="c1"># Multiboot ROMs</span>
    <span class="s2">"594b8e60e9406a570c9990e9bbc4340f"</span><span class="p">:</span> <span class="s2">"Clu Clu Land (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"aa6bdfc4fce58b19d1a8a9f2f11042d9"</span><span class="p">:</span> <span class="s2">"Donkey Kong (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"ee8a23328607687b50a6706c7fdfc2e1"</span><span class="p">:</span> <span class="s2">"Donkey Kong Jr. (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"d3d227a1ca88b0629ef333d544686c41"</span><span class="p">:</span> <span class="s2">"Excitebike (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"684e46cb0c672e06664ae742825ae89c"</span><span class="p">:</span> <span class="s2">"Mario Bros. (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"c1c6eb0d42591c46f2e4dc68145e4c81"</span><span class="p">:</span> <span class="s2">"Pinball (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"34217e69f45e52d1550a8b241ce27404"</span><span class="p">:</span> <span class="s2">"Super Mario Bros. (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"a81a5d9b9268da64ea8426bdc6a987ba"</span><span class="p">:</span> <span class="s2">"Soccer (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"146bdf7f70335a2ad67b59ef9e07bfaf"</span><span class="p">:</span> <span class="s2">"Tennis (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"62c26ddf7579b5179b2a67073bc7e4a4"</span><span class="p">:</span> <span class="s2">"Balloon Fight (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"b0c8f4dfe47c3649760748ad5c96a649"</span><span class="p">:</span> <span class="s2">"Baseball (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"a7b95f64a01e7cc18968b1c501741414"</span><span class="p">:</span> <span class="s2">"Donkey Kong 3 (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"f92aeb4bc274cb08c2eabe9dd3aadcb4"</span><span class="p">:</span> <span class="s2">"Golf (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"f7adee0901bb73b6f1c1fbeb36b4ab4c"</span><span class="p">:</span> <span class="s2">"Ice Climber (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
    <span class="s2">"1c8dcf20e4ce979cb9962c835c39a5c9"</span><span class="p">:</span> <span class="s2">"Donkey Kong Jr. Math (USA, Europe) (Animal Crossing).mb"</span><span class="p">,</span>
<span class="p">}</span>


<span class="k">def</span> <span class="nf">main</span><span class="p">():</span>
    <span class="n">animal_crossing_iso</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
    <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">animal_crossing_iso</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s2">"r+b"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">,</span> <span class="n">mmap</span><span class="o">.</span><span class="n">mmap</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">fileno</span><span class="p">(),</span> <span class="mi">0</span><span class="p">)</span> <span class="k">as</span> <span class="n">fm</span><span class="p">:</span>
        <span class="n">offset</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
        <span class="c1"># Find all 'Yaz0' headers.</span>
        <span class="k">while</span> <span class="o">-</span><span class="mi">1</span> <span class="o">!=</span> <span class="p">(</span><span class="n">offset</span> <span class="o">:=</span> <span class="n">fm</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="sa">b</span><span class="s2">"Yaz0"</span><span class="p">,</span> <span class="n">offset</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">data</span> <span class="o">=</span> <span class="n">yaz0</span><span class="p">(</span><span class="n">fm</span><span class="p">[</span><span class="n">offset</span> <span class="p">:</span> <span class="n">offset</span> <span class="o">+</span> <span class="mh">0x80000</span><span class="p">])</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="c1"># NES ROM</span>
            <span class="k">if</span> <span class="n">data</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="sa">b</span><span class="s2">"NES</span><span class="se">\x1a</span><span class="s2">"</span><span class="p">):</span>
                <span class="c1"># Calculate the MD5 without the NES header.</span>
                <span class="n">rom_md5</span> <span class="o">=</span> <span class="n">hashlib</span><span class="o">.</span><span class="n">md5</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="mi">16</span><span class="p">:])</span><span class="o">.</span><span class="n">hexdigest</span><span class="p">()</span>
            <span class="c1"># Famicom Disk System ROM</span>
            <span class="k">elif</span> <span class="n">data</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="sa">b</span><span class="s2">"</span><span class="se">\x01</span><span class="s2">*NINTENDO-HVC*</span><span class="se">\x01</span><span class="s2">"</span><span class="p">):</span>
                <span class="n">rom_md5</span> <span class="o">=</span> <span class="n">hashlib</span><span class="o">.</span><span class="n">md5</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">hexdigest</span><span class="p">()</span>
            <span class="c1"># GBA Joyboot ROM</span>
            <span class="k">elif</span> <span class="n">data</span><span class="p">[</span><span class="mh">0xAC</span><span class="p">:</span><span class="mh">0xB3</span><span class="p">]</span> <span class="o">==</span> <span class="sa">b</span><span class="s2">"AGBJ01</span><span class="se">\x96</span><span class="s2">"</span><span class="p">:</span>
                <span class="n">rom_md5</span> <span class="o">=</span> <span class="n">hashlib</span><span class="o">.</span><span class="n">md5</span><span class="p">(</span><span class="n">data</span><span class="p">)</span><span class="o">.</span><span class="n">hexdigest</span><span class="p">()</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">continue</span>

            <span class="k">if</span> <span class="n">rom_md5</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">known_roms</span><span class="p">:</span>
                <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Unknown ROM MD5: </span><span class="si">{</span><span class="n">rom_md5</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                <span class="k">continue</span>

            <span class="n">filename</span> <span class="o">=</span> <span class="n">known_roms</span><span class="p">[</span><span class="n">rom_md5</span><span class="p">]</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Extracted ROM: </span><span class="si">{</span><span class="n">filename</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
            <span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">filename</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s2">"wb"</span><span class="p">)</span> <span class="k">as</span> <span class="n">rom_fp</span><span class="p">:</span>
                <span class="n">rom_fp</span><span class="o">.</span><span class="n">truncate</span><span class="p">()</span>
                <span class="n">rom_fp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">yaz0</span><span class="p">(</span><span class="n">data</span><span class="p">:</span> <span class="nb">bytes</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bytes</span><span class="p">:</span>
    <span class="c1"># Implementation of Yaz0 following</span>
    <span class="c1"># this reference: http://www.amnoid.de/gc/yaz0.txt</span>
    <span class="p">(</span><span class="n">buf_length</span><span class="p">,)</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s2">"&gt;xxxxLxxxxxxxx"</span><span class="p">,</span> <span class="n">data</span><span class="p">[:</span><span class="mi">16</span><span class="p">])</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="mi">16</span><span class="p">:]</span>
    <span class="n">src</span> <span class="o">=</span> <span class="n">dst</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">buf</span> <span class="o">=</span> <span class="nb">bytearray</span><span class="p">(</span><span class="n">buf_length</span><span class="p">)</span>
    <span class="k">while</span> <span class="n">dst</span> <span class="o">&lt;</span> <span class="n">buf_length</span> <span class="ow">and</span> <span class="n">src</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
        <span class="n">bit_header</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="n">src</span><span class="p">]</span>
        <span class="n">src</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">8</span><span class="p">):</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="p">(</span><span class="n">dst</span> <span class="o">&lt;</span> <span class="n">buf_length</span> <span class="ow">and</span> <span class="n">src</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)):</span>
                <span class="k">break</span>
            <span class="k">if</span> <span class="n">bit_header</span> <span class="o">&amp;</span> <span class="mh">0x80</span><span class="p">:</span>
                <span class="n">buf</span><span class="p">[</span><span class="n">dst</span><span class="p">]</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="n">src</span><span class="p">]</span>
                <span class="n">dst</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="n">src</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">byte1</span><span class="p">,</span> <span class="n">byte2</span> <span class="o">=</span> <span class="n">struct</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s2">"&gt;BB"</span><span class="p">,</span> <span class="n">data</span><span class="p">[</span><span class="n">src</span> <span class="p">:</span> <span class="n">src</span> <span class="o">+</span> <span class="mi">2</span><span class="p">])</span>
                <span class="k">assert</span> <span class="n">byte1</span> <span class="o">&gt;=</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">byte2</span> <span class="o">&gt;=</span> <span class="mi">0</span>
                <span class="n">src</span> <span class="o">+=</span> <span class="mi">2</span>
                <span class="n">copy_src</span> <span class="o">=</span> <span class="n">dst</span> <span class="o">-</span> <span class="p">((</span><span class="n">byte1</span> <span class="o">&amp;</span> <span class="mh">0x0F</span><span class="p">)</span> <span class="o">&lt;&lt;</span> <span class="mi">8</span> <span class="o">|</span> <span class="n">byte2</span><span class="p">)</span> <span class="o">-</span> <span class="mi">1</span>
                <span class="n">num_bytes</span> <span class="o">=</span> <span class="n">byte1</span> <span class="o">&gt;&gt;</span> <span class="mi">4</span>
                <span class="k">if</span> <span class="n">num_bytes</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">num_bytes</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="n">src</span><span class="p">]</span> <span class="o">+</span> <span class="mh">0x12</span>
                    <span class="n">src</span> <span class="o">+=</span> <span class="mi">1</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">num_bytes</span> <span class="o">+=</span> <span class="mi">2</span>
                <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">num_bytes</span><span class="p">):</span>
                    <span class="n">buf</span><span class="p">[</span><span class="n">dst</span> <span class="o">+</span> <span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">buf</span><span class="p">[</span><span class="n">copy_src</span> <span class="o">+</span> <span class="n">i</span><span class="p">]</span>
                <span class="n">dst</span> <span class="o">+=</span> <span class="n">num_bytes</span>
            <span class="n">bit_header</span> <span class="o">&lt;&lt;=</span> <span class="mi">1</span>
    <span class="k">return</span> <span class="nb">bytes</span><span class="p">(</span><span class="n">buf</span><span class="p">)</span>


<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">"__main__"</span><span class="p">:</span>
    <span class="n">main</span><span class="p">()</span>
</code></pre>
</div>
</details>
</p>

The source code above is also [available as a Gist](https://gist.github.com/sethmlarson/1fa8c95b9f7afbdb85252e4d321b1d5b), licensed
MIT. After running this script with an Animal Crossing ISO you'll find
all the NES and Famicom Disk System ROMs in your current directory:

```shell
# Running the script with Python!
$ python animal-crossing-nes-roms.py ./AnimalCrossing\ \(v1.00\).iso

# All of the ROMs are extracted in the CWD.
Extracted ROM: 'Clu Clu Land (World) (Animal Crossing).nes'
Extracted ROM: 'Balloon Fight (USA).nes'
...
Extracted ROM: 'Super Mario Bros. (World).nes'
Extracted ROM: 'Legend of Zelda, The (USA) (Rev 1) (Animal Crossing).nes'
```

<div class="row">
<div class="col-6">
<p>This script can be improved by adding more MD5 checksums of ROMs from different regions like Japan and the EU.
Currently I've only tested using the North American copy of Animal Crossing.</p>

<p>These ROMs can now be used just like any other ROM with NES emulators. If you're
playing on desktop and want to try your ROMs out you can use <a href="https://koute.github.io/pinky-web/">Pinky</a>, a WASM-based
NES emulator. If you want to play on mobile I recommend using the <a href="https://delta-emu.com/">Delta emulator</a>.</p>

<p>It feels quite magical to be playing NES games from a childhood copy of Animal Crossing
on a modern iPhone. Wario's Woods was always my favorite, so I look forward to playing
the game more often and keeping that nostalgic connection alive.</p>

<p>If you're looking for more ways to find legal ROMs of games, WULFF DEN <a href="https://www.youtube.com/watch?v=IQNXmOidh1g">published
a video</a> recently linking to a
<a href="https://github.com/farmerbb/RED-Project/wiki#game-compilations">list of other "ROM extraction" methods</a> like this one.</p>
</div>
<div class="col-6">
<center>
<p>
<img style="max-width: 100%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_2733_2.png"/>
<br><small><i>Playing Wario's Woods on the Delta emulator</i></small></center></p>
</div>
</div>

## What if I only have a Game Boy Advance?

You're in luck! Animal Crossing also had a feature called
"[Advance Play](https://nookipedia.com/wiki/Game_Boy_Advance#Advance_Play)"
which meant most NES games could be saved to your GBA via a mode called
"Multiboot" or "Joyboot". Animal Crossing used separate
ROMs that were compiled for the GBA CPU instead of the NES CPU.

These ROMs are detected by looking for the string `AGBJ01\x96` at offset `0xAC`, corresponding
to the Game Boy Advance ROM header that was chosen for these ROMs.

> **NOTE:** To run these on a GBA emulator or with a GBA flash cartridge you need to
convert the `.mb` files into `.gba` files. [This script](https://gist.github.com/mid-kid/149e7415e5da89cca5e2dd36459eeac5) worked for
converting the files to `.gba`.
