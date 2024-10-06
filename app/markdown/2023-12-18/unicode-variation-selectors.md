# Mahjong tiles and Unicode variation selectors

It's been a while since I've written about Unicode, so here's
a short one about a Unicode feature I recently learned about
wrapped inside an opportunity to admire the Mahjong glyphs.

Quoting Wikipedia, [Mahjong](https://en.wikipedia.org/wiki/Mahjong) is a tile-based game that was developed in the 19th century in China and has spread throughout the world.
Similar to other classic games like [Chess](https://en.wikipedia.org/wiki/Chess_symbols_in_Unicode) and [French Playing Cards](https://en.wikipedia.org/wiki/Playing_Cards_(Unicode_block)), Mahjong has its [own block in Unicode](https://en.wikipedia.org/wiki/Mahjong_Tiles_(Unicode_block)) <span class="ucode">(U+1F000 - U+1F02F)</span> for all of the tiles.

<div class="row">
<div class="col-8 col-12-sm" style="margin-right: 0;">
<div class="row">
<div class="col-6 col-12-sm">
<div>Winds <small class="ucode">(U+1F000..U+1F003)</small></div>
<div class="mahjong">🀀🀁🀂🀃</div>
</div>
<div class="col-6 col-12-sm">
<div>Dragons <small class="ucode">(U+1F004..U+1F006)</small></div>
<div class="mahjong">🀄︎🀅🀆</div>
</div>
<div class="col-12">
Dots <small class="ucode">(U+1F019..U+1F021)</small><br>
<div class="mahjong">🀙🀚🀛🀜🀝🀞🀟🀠🀡</div>
</div>

<div class="col-12">
Bamboo <small class="ucode">(U+1F010..U+1F018)</small><br>
<div class="mahjong">🀐🀑🀒🀓🀔🀕🀖🀗🀘</div>
</div>

<div class="col-12">
Characters <small class="ucode">(U+1F007..U+1F00F)</small><br>
<div class="mahjong">🀇🀈🀉🀊🀋🀌🀍🀎🀏</div>
</div>

<div class="col-6 col-12-sm">
Flowers <small class="ucode">(U+1F022..U+1F025)</small><br>
<div class="mahjong">🀢🀣🀤🀥</div>
</div>
<div class="col-6 col-12-sm">
Seasons <small class="ucode">(U+1F026..U+1F029)</small><br>
<div class="mahjong">🀦🀧🀨🀩</div>
</div>


<div class="col-6 col-12-sm">
Reverse <small class="ucode">(U+1F02B)</small><br>
<div class="mahjong">🀫</div>
</div>
<div class="col-6 col-12-sm">
Red Dragon Emoji <small class="ucode">(U+1F004)</small><br>
<div class="mahjong" style="font-family: sans-serif;">🀄&#xFE0E</div>
</div>
</div>
</div>
<div style="margin-right: 0;">
<p>
The Mahjong Unicode block has a single emoji in it: the Mahjong Red Dragon (🀄).
So why then does it look like text in our table instead of how emojis usually look?
</p>
<p>
This effect is achieved using a feature called <strong><a href="https://unicode.org/faq/vs.html">Unicode variation selectors</a></strong>.
</p>
<p>
These codepoints are in the range <span class="ucode">U+FE00..U+FE0F</span>.
The variation selectors we're interested in today are <span class="ucode">U+FE0E and U+FE0F</span> for “text-style” and “emoji-style” respectively.
</p>
<p>
The variation selector works by being placed after the character being modified. So the Mahjong Red Dragon in text-style would be <code>"🀄\uFE0E"</code> in Python.
There's a <a href="https://www.unicode.org/Public/15.1.0/ucd/emoji/emoji-variation-sequences.txt">giant list of codepoints</a> that interact with the text and emoji variation characters, give them a look if you need this feature.
</p>
</div>
</div>
