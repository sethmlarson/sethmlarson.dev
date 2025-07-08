# Setting Discord status from physical GameCube console

<img style="border: 2px black solid; max-width: 100%" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/GC-to-Discord.jpeg"/>

Have you ever seen one of your friends playing
a game or listening to music in their Discord “status”? That feature is
called “[Rich Presence](https://discord.com/developers/docs/rich-presence/overview)”.

What if you want to show your Discord friends that *you're playing
your GameCube?* and I don't mean an emulator like [Dolphin](https://dolphin-emu.org/), I'm talking
about a physical console from 2001.

We can do just that with a simple Python script and a [Memcard Pro GC](https://www.8bitmods.wiki/memcard-pro-gc).
The Memcard Pro GC is an internet-connected GameCube Memory Card virtualizer. The Memcard Pro GC automatically switches
to a virtual Memory Card (VMC) for specific games when launched with
a <nobr>“Game ID”-aware</nobr> launcher like [Swiss](https://www.gc-forever.com/wiki/index.php?title=Swiss)
or the [FlippyDrive](https://www.gc-forever.com/wiki/index.php?title=FlippyDrive).

We can use this automatic VMC switching feature to “detect” when a game is being played
on a physical GameCube and update Discord with a new Rich Presence.

## Configuring the Memcard Pro GC

You can buy a [Black](https://8bitmods.com/memcard-pro-gc-for-gamecube-smoke-black/) or [White](https://8bitmods.com/memcard-pro-gc-for-gamecube-frost-white/)
Memcard Pro GC from 8BitMods for ~$45 USD plus shipping. They are oftentimes sold out, so you may need to be patient for a re-stock.

There is a [documented first-time setup](https://www.8bitmods.wiki/-O30-first-time-setup) page. If you're on
Ubuntu or Linux like me, you can use `mkfs` to format the microSD filesystem to exFAT:

```shell
# Find your microSD card. Make sure it's the right size
# and device so you don't accidentally overwrite your
# storage drive(s) / boot drive. You want the /dev directory
sudo fdisk -l

# Might need to fiddle with microSD card, un-and-remount,
# make sure it's not in read-only mode on the adapter.
sudo apt-get install exfat-fuse
sudo mkfs.exfat -n memcardprogc </dev/...>
```

You should see something like this when you're done:

```shell
Writing volume boot record: done
Writing backup volume boot record: done
Fat table creation: done
Allocation bitmap creation: done
Upcase table creation: done
Writing root directory entry: done
Synchronizing...
exFAT format complete!
```

After that put all the files on the new filesystem and plug the card
into a GameCube or Wii, power the console on, and let the device install the firmware.

> **NOTE:** When I set up the Memcard Pro GC I wasn't able to get the latest firmware at the time (v2.0.4) to work without
> the device endlessly boot-looping. I tried downgrading to an earlier version of the firmware (v2.0.0)
> and the device worked flawlessly. Maybe I'll try again if the firmware is updated again and see what happens.

Once the device is online do the setup for [connecting the device to WiFi](https://www.8bitmods.wiki/q4at-wireless-features).
From here you can access the “Settings” page on your phone or computer.

For automatic detection to work as expected we need to create a default
memory card that isn't associated with a Game ID (I used `MemoryCard1`) and to disable
the “Load Last Card when MemCard Boots” feature. Now on boot-up the Memcard Pro GC will
use the `MemoryCard1`
instead of whatever your last played game was by default.

Now we can create VMCs for every game which the Memcard Pro GC will automatically
do when we launch a new game through our Game ID launcher. This can be done
quickly in CubeBoot on the FlippyDrive by selecting games in your library one-by-one
but not launching into the game completely. This is enough to trigger the Memcard Pro GC
to load the VMC for a given Game ID.

> **NOTE:** If you plan to do anything with the FTP server with the Memcard Pro GC
> you need to configure a username and password, enable the server, and crucially
> completely power off and power on the console for the FTP server to start on boot.
> I lost around 30 minutes trying to get FTP to work to this oversight.

## Downloading assets

So we'll need two different assets from the [GameTDB](https://www.gametdb.com/).
First we'll need a list of valid Game IDs so our program can distinguish
between a VMC not associated with an actual game and the cover artwork
for the games we own.

Download the `wiidb.txt` database in your preferred language (I am using English)
and “Covers” for each region of games that your collection contains.
I own games from the USA (NSTC) and Japan (NSTC-J) regions, so I downloaded those
covers for those regions.

The covers from GameTDB are 160x224 pixels which is below the minimums
that Discord requires for Art Assets (512x512) so we can scale them up
with ImageMagick after we've unzipped the images into a directory.

First we need to isolate only the cover artworks for games in our library.
For this we can query the VMCs on our Memcard Pro GC after we've setup
VMCs for each game. Replace the IP address (`192.168.0.43`) with the one used for your own Memcard Pro GC:

```shell
$ curl -X POST \
  --data '{"limit":100,"start":0}' \
  http://192.168.0.43/api/query | \
  pcregrep -o1 'gameID":\s*"([A-Z0-9]{6})'
```

<details>
<summary>Example list of Game IDs</summary>
<pre><code>GPVE01
GC6E01
G8MJ01
G4SE01
GAFE01
GEZE8P
GKYE01
GLME01
GM4E01
GP5E01
GP6E01
GP7E01
GFTE01
GMPE01
G8ME01
GPIE01
GSNE8P
GZLE01
GALE01
GMSE01
GS8E7D
GXSE8P
GSOE8P
G9SE8P
G2XE8P
PZLE01
GPVJ01</code></pre>
</details>

Save this list into a file and make sure there's a trailing newline. Now we can use the list we generated to
select and resize only the game cover artworks we plan to use.
Assuming we have a directory of the original images named `covers/`
and an empty directory named `discord-icons/`

```shell
sudo apt-get install imagemagick

cat gameids.txt | while read gameid 
do
   convert covers/$gameid.png -scale 400% discord-icons/$gameid.png
done
```
We don't want ImageMagick to blur or interpolate the images, so we use `-scale` instead of `-resize`.
At this point you should have a directory full of upscaled images to use with your Discord application.

## Creating the Discord Application

To use “Rich Presence” you need a [Discord application](https://discord.com/developers/docs/quick-start/overview-of-apps).
There are plenty of tutorials on how to create one of these. I named
the application “GameCube” so the Discord status will say “*Seth is playing GameCube*”.
You'll need to upload all the newly resized game cover artwork images under the
`Rich Presence > Art Assets` section.

> **NOTE:** Uploading tons of Art Assets to Discord applications is kinda annoying.
> Super aggressive rate-limiting, upload them in small batches and take your time.
> Duplicates aren't a huge issue so don't sweat it!

Copy your Discord application ID into the script below.

## Querying the Memcard Pro GC

The Memcard Pro GC provides a simple JSON HTTP API
that can be queried for the current state of the VMC.
Requesting `GET /api/currentState` returns a JSON
body including the current Game ID and game name
for the VMC:

```json
{
  "gameName": "Paper Mario: The Thousand-Year Door",
  "gameID":	"G8ME0100",
  "currentChannel":	1,
  "rssi": -40
}
```

We can periodically call this API and then, using the
[`pypresence` library](https://pypi.org/project/pypresence/), we can update our Discord Rich
Status. We need to have fairly lax timeouts and retries
to avoid unnecessarily setting and clearing the Rich
Status due to things like the memory card not responding
fast enough, the Memcard Pro GC is a fairly low powered device:

<details>
<summary>Full Python script source code</summary>
<div class="codehilite">
<pre><span></span><code><span class="kn">import</span> <span class="nn">urllib3</span>
<span class="kn">import</span> <span class="nn">pypresence</span>
<span class="kn">import</span> <span class="nn">time</span>
<span class="kn">import</span> <span class="nn">re</span>
<span class="kn">import</span> <span class="nn">pathlib</span>

<span class="n">ROOT_DIR</span> <span class="o">=</span> <span class="n">pathlib</span><span class="o">.</span><span class="n">Path</span><span class="p">(</span><span class="vm">__file__</span><span class="p">)</span><span class="o">.</span><span class="n">absolute</span><span class="p">()</span><span class="o">.</span><span class="n">parent</span>
<span class="k">with</span> <span class="p">(</span><span class="n">ROOT_DIR</span> <span class="o">/</span> <span class="s2">"wiitdb.txt"</span><span class="p">)</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="n">mode</span><span class="o">=</span><span class="s2">"r"</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">GAME_ID_TO_NAMES</span> <span class="o">=</span> <span class="p">{</span>
        <span class="n">gid</span><span class="p">:</span> <span class="n">name</span>
        <span class="k">for</span> <span class="n">gid</span><span class="p">,</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">re</span><span class="o">.</span><span class="n">findall</span><span class="p">(</span>
            <span class="sa">r</span><span class="s2">"^([A-Z0-9]</span><span class="si">{6}</span><span class="s2">) = (.+?)$"</span><span class="p">,</span>
            <span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">(),</span>
            <span class="n">re</span><span class="o">.</span><span class="n">DOTALL</span> <span class="o">|</span> <span class="n">re</span><span class="o">.</span><span class="n">MULTILINE</span><span class="p">,</span>
        <span class="p">)</span>
    <span class="p">}</span>


<span class="k">class</span> <span class="nc">MemcardGCPresence</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">memcardgc_host</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">discord_app_id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">host</span> <span class="o">=</span> <span class="n">memcardgc_host</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">http</span> <span class="o">=</span> <span class="n">urllib3</span><span class="o">.</span><span class="n">HTTPConnectionPool</span><span class="p">(</span>
            <span class="n">memcardgc_host</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">discord</span> <span class="o">=</span> <span class="n">pypresence</span><span class="o">.</span><span class="n">Presence</span><span class="p">(</span>
            <span class="n">client_id</span><span class="o">=</span><span class="n">discord_app_id</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">discord</span><span class="o">.</span><span class="n">connect</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">active_game_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">consecutive_errors</span> <span class="o">=</span> <span class="mi">0</span>

    <span class="k">def</span> <span class="nf">poll_forever</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
                <span class="n">poll_start</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">poll_once</span><span class="p">()</span>

                <span class="c1"># Only set Discord status every 15 seconds.</span>
                <span class="n">poll_duration</span> <span class="o">=</span> <span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">-</span> <span class="n">poll_start</span>
                <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="nb">max</span><span class="p">([</span><span class="mi">0</span><span class="p">,</span> <span class="mi">15</span> <span class="o">-</span> <span class="n">poll_duration</span><span class="p">]))</span>
        <span class="k">finally</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">poll_once</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">resp</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">http</span><span class="o">.</span><span class="n">request</span><span class="p">(</span>
                <span class="s2">"GET"</span><span class="p">,</span>
                <span class="s2">"/api/currentState"</span><span class="p">,</span>
                <span class="n">timeout</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">redirect</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">retries</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="k">if</span> <span class="n">resp</span><span class="o">.</span><span class="n">status</span> <span class="o">!=</span> <span class="mi">200</span><span class="p">:</span>
                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s2">"Invalid HTTP status"</span><span class="p">)</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">resp</span><span class="o">.</span><span class="n">json</span><span class="p">()</span>
            <span class="n">game_id_with_revision</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s2">"gameID"</span><span class="p">]</span>
            <span class="c1"># We use the GameID without the revision</span>
            <span class="c1"># to determine the game cover artwork.</span>
            <span class="n">game_id</span> <span class="o">=</span> <span class="n">game_id_with_revision</span><span class="p">[:</span><span class="mi">6</span><span class="p">]</span>
            <span class="n">game_name</span> <span class="o">=</span> <span class="n">data</span><span class="p">[</span><span class="s2">"gameName"</span><span class="p">]</span>
        <span class="k">except</span> <span class="p">(</span>
            <span class="n">urllib3</span><span class="o">.</span><span class="n">exceptions</span><span class="o">.</span><span class="n">HTTPError</span><span class="p">,</span>
            <span class="ne">ValueError</span><span class="p">,</span>
            <span class="ne">KeyError</span><span class="p">,</span>
        <span class="p">):</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">consecutive_errors</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="k">if</span> <span class="p">(</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">active_game_id</span>
                <span class="ow">and</span> <span class="bp">self</span><span class="o">.</span><span class="n">consecutive_errors</span> <span class="o">&gt;</span> <span class="mi">3</span>
            <span class="p">):</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
            <span class="k">return</span>

        <span class="c1"># Game ID isn't a known game. Might be the default</span>
        <span class="c1"># memory card or a ROM hack that we don't know about.</span>
        <span class="k">if</span> <span class="n">game_id</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">GAME_ID_TO_NAMES</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">reset</span><span class="p">()</span>
            <span class="k">return</span>

        <span class="c1"># New game, set Rich Presence.</span>
        <span class="k">if</span> <span class="n">game_id_with_revision</span> <span class="o">!=</span> <span class="bp">self</span><span class="o">.</span><span class="n">active_game_id</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">discord</span><span class="o">.</span><span class="n">update</span><span class="p">(</span>
                <span class="n">activity_type</span><span class="o">=</span><span class="n">pypresence</span><span class="o">.</span><span class="n">ActivityType</span><span class="o">.</span><span class="n">PLAYING</span><span class="p">,</span>
                <span class="n">state</span><span class="o">=</span><span class="n">game_name</span><span class="p">,</span>
                <span class="n">start</span><span class="o">=</span><span class="nb">int</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()),</span>
                <span class="c1"># Discord lowercases all filenames.</span>
                <span class="n">large_image</span><span class="o">=</span><span class="n">game_id</span><span class="o">.</span><span class="n">lower</span><span class="p">(),</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">active_game_id</span> <span class="o">=</span> <span class="n">game_id_with_revision</span>

    <span class="k">def</span> <span class="nf">reset</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">active_game_id</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"Stopped playing </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">active_game_id</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">consecutive_errors</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">active_game_id</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">discord</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">close</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">http</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">http</span> <span class="o">=</span> <span class="kc">None</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">discord</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="k">pass</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">discord</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">discord</span> <span class="o">=</span> <span class="kc">None</span>


<span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">"__main__"</span><span class="p">:</span>
    <span class="n">memcardgc</span> <span class="o">=</span> <span class="n">MemcardGCPresence</span><span class="p">(</span>
        <span class="c1"># Default IP address for the Memcard Pro GC.</span>
        <span class="c1"># Update if necessary. Include your own</span>
        <span class="c1"># Discord App ID.</span>
        <span class="n">memcardgc_host</span><span class="o">=</span><span class="s2">"192.168.0.43"</span><span class="p">,</span>
        <span class="n">discord_app_id</span><span class="o">=</span><span class="s2">"&lt;Discord App ID&gt;"</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="n">memcardgc</span><span class="o">.</span><span class="n">poll_forever</span><span class="p">()</span>
</code></pre>
</div>
</details>

The above script is open source under the MIT license.

So now when you're playing your GameCube at home you can run
this script, and you should see your Discord
status change to the game you are playing. Magic!

Let me know what games you still play on your GameCube! :)
