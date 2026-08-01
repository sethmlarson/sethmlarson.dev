# Let’s Play “htmx 4: the game”

Moments ago I just finished playing “[htmx 4: the game](https://four.htmx.org/)”, the first
JavaScript library [published exclusively for Game Boy and Game Boy Color](https://swag.htmx.org/products/htmx-4-the-game).
I've recorded my play session and published the video to YouTube:

<!-- more -->

<p>
<center>
<iframe width="560" height="315" style="border: 2px black solid; max-width: 100%;" src="https://www.youtube.com/embed/I688pAIVSK4?si=CWTFxji8OPUad8sN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</center>
</p>

When I first saw this announcement it was pure blog bait for me. Game Boy,
open source software, reverse-engineering, oh my. I purchased the cartridge
within moments of seeing the announcement.

The Game Boy cartridge arrived earlier today inside a custom cardboard box
and plastic case which I appreciate! The box was tight to open without ripping
the cardboard, I managed with the help of some tweezers. The game is on a
Game Boy cartridge with a label. The cartridge itself reads “Game” instead of “Game Boy”
to avoid running afoul of Nintendo trademarks and licensing.

<p>
<center>
<img style="max-width: 100%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/htmx-4/IMG_5939_small.jpeg">
</center>
</p>

I was unable to dump the ROM using my [Epilogue GB Operator](https://sethmlarson.dev/backup-game-boy-roms-and-saves-on-ubuntu), the cartridge
didn't fit into the slot unless I angled it weirdly and even then the
cartridge wouldn't give the GB Operator the consistent connection it
needs to dump the ROM. This was unfortunate, I wanted to dig into the
ROM itself more for this post, but that will have to be another day.
I suspect the tolerances for the cartridge are *just outside*
what the Epilogue will tolerate.
I switched over to my [Game Boy Player](https://en.wikipedia.org/wiki/Game_Boy_Player) to capture footage
of game play with my HDMI-modded GameCube. Here the cartridge
fit and worked just fine.

The game is **tough** (especially The Slop Factory, yeesh)
and took me over an hour to complete,
and I didn't even find all 4 HTMX letters in each stage...
hinting that there is *more to be discovered!* There
was pervasive lag while playing which the game’s story
blames on... React. *A likely story!* ;)

Going in I wasn't sure how they were going to distribute the
final source code... Would there be a QR code to the source code
(which would have been a disappointment) or would
the htmx team actually [make you type it in yourself
like a BASIC program from a magazine](https://en.wikipedia.org/wiki/Type-in_program)? 
I was so happy to see that the htmx team [went all the
way](https://youtu.be/I688pAIVSK4?si=kxSuQHs8hVwq3XFU&t=3297), it means I'm even more excited to dig into this ROM!

As a software distribution mechanism... including
ordering the game, waiting for delivery, beating
the game, and then typing in the source code by
hand from the Game Boy screen... Let's say it's
slightly less user-friendly than `npm install` :)
But that's the fun of a project like this.