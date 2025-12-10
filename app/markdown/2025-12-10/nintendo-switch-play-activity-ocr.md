# Extracting Nintendo Switch “Play Activity” with OCR

Despite considering myself a “gamer”,
I realized I had only played **~5 hours of video-games
in the whole year 2022** and ~6 hours in 2021. Honestly, these numbers
made me a bit sad to see... You can't “improve” what you don't measure, so
I started looking for low-effort ways to measure the amount
of play time while getting back into *actually playing video-games*.

<!-- more -->

I have already achieved what I wanted for GameCube by mid-2025 using
the [Memcard Pro GC](https://www.8bitmods.wiki/memcard-pro-gc)’s Wi-Fi and API.
I’ve [blogged about this setup](https://sethmlarson.dev/setting-discord-status-from-physical-gamecube-console)
which gathers date and duration data for playing GameCube,
but I wanted to cover my other consoles.

<h2>What about the Nintendo Switch?</h2>

<div class="row">
<div class="col-8">
<p>Surprisingly, Nintendo Switch offered no such data,
despite having an option called <nobr>“Play Activity”</nobr> in the
menus of the Nintendo Switch, Nintendo Account, and
many of their mobile apps. This was unfortunate, as I
was playing many more new Nintendo Switch games like
the <nobr><a href="https://en.wikipedia.org/wiki/Paper_Mario:_The_Thousand-Year_Door#Remake">Paper Mario: Thousand-Year Door</a></nobr> remake and <a href="https://en.wikipedia.org/wiki/Pikmin_4">Pikmin 4</a>,
and going back to games I had “missed” like <nobr><a href="https://en.wikipedia.org/wiki/Super_Mario_Odyssey">Super Mario Odyssey</a></nobr>.</p>

<p>That is... until the <a href="https://www.nintendo.com/us/mobile-apps/nintendo-store/">Nintendo Store app</a>
was released just a few weeks ago. This app
provides “Play Activity” data at a <strong>much higher resolution</strong> than any other Nintendo app or service.
You can find complete historical data across your Nintendo Account, going back as far as
the <em>Nintendo 3DS and Wii-U!</em> The data includes games played, dates, and play durations in 15 minute increments.</p>

<p>Shoutout to the <a href="https://www.youtube.com/@WulffDen">WULFF DEN podcast</a>
for talking about this, otherwise I would never have discovered this niché new feature.
But how can I query this data for my own purposes?</p>

</div>
<div class="col-4">
<center>
<img style="border: 2px black solid; max-width: 100%" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_3726.PNG">
<br><small><i>Example of data available in the Nintendo Store <nobr>“Play Activity”</nobr>.</i></small>
</center>
</div>
</div>


## Using Optical Character Recognition (OCR)

Basically the data was in the app, but couldn't be selected
and copy-pasted or exported. Instead, the data would have to be transferred
to a queryable format another way.

I took this as an opportunity to try out a technology I'd
never used before: Optical Character Recognition (OCR).
OCR basically turns pictures of letters and numbers into
actual strings of text. State of the art for OCR today
appears to be using machine-learning models.

After a bit of research, I landed on [EasyOCR](https://pypi.org/project/easyocr) which uses
PyTorch models that are already pre-trained. This appeared
to require downloading the model from the internet, which
bothered me a bit, but I decided that running the model
within a Docker container without network access (`--net=none`)
was *probably* enough to guarantee this library wasn't
sending my data off my machine.

I created a workflow ([source code available on GitHub](https://github.com/sethmlarson/nintendo-play-activity-ocr/)) that takes a directory of images mounted
as a volume, runs OCR on each image, and then returns the parsed
text as “JSON lines” for each image along with the checksum of
the image. This checksum is stored by the program processing the
OCR text to avoid running OCR on images more than once.

This is an example of the text that OCR is able to read from
one screenshot:

```python
[
  "20:13", "15",
  "Play Activity",
  "Animal Crossing: New Horizons",
  "5/9/2020",  "1 hr; 15 min.",
  "5/8/2020",  "1 hr. 0 min:",
  "5/5/2020",  "45 min:",
  "5/4/2020",  "1 hr. 30 min:",
  "5/3/2020",  "A few min.",
  ...
]
```

There's some unexpected elements here!
Notice how the phone time and battery are picked up by OCR
and how the play time durations all have either `.` or `:` at the end.
This extra punctuation seems to come from the vertical border
on the screen to the right of the text. The least consistent
readings are when there is text as a part of the game logo.

## Segmenting and parsing OCR data

OCR can consistently the actual text
from the application itself, so we can use the `Play Activity`
and `First played` labels as anchors to know where the other
data is. Using these anchors we can segment OCR text into:

* Phone UI (time, battery %)
* Game information (title, first played, last played)
* Game play activity (date, duration)

For some games the model really struggles to read the game title
consistently. To fix this I created a list of words that the OCR
model *does* consistently read and mapped those words to corresponding
game titles, such as “`Wonder`” → “`Super Mario Bros. Wonder`”.
This would be a problem if I played more games, but we’ll cross
that bridge when we come to it! ;)

The game play activity data parses fairly consistently. The date is always
`MM/DD/YYYY` and there are three forms
of duration that the application uses:

* `A few min`
* `XX min`
* `X hr Y min`

Parsing the date and duration text and accounting for the extra punctuation was accomplished
with a single regular expression:

```regexp
([1-9][0-9]?/[1-9][0-9]?/2[0-9]{3})
(A few min|(?:([0-9]+)\s*hr[:;,. ]+)?([0-9]+)\s*min)
```

This parses out into 4 groups, the date, a “flag” for detecting <nobr>“A few min”</nobr>,
and then hours and minutes. Because the resolution below 15 minutes isn't shown
by the application I assigned the <nobr>“A few min”</nobr> duration an approximate value of 5 minutes of play time.
The explicit hours and minutes values are calculated as expected.

So now we have the game name and a list of play activity days and durations
from a single image, do that to each image and insert the results into an SQLite database
that you can query:

```sql
SELECT STRFTIME('%Y', date) AS y, SUM(duration)/3600 AS d
FROM sessions GROUP BY y ORDER BY y ASC;
```

The results show just how little I was playing video
games in 2021 and 2022 and how I started playing more
again in 2023 onwards.

| Year | Play Activity (Hours) |
|------|-----------------------|
| 2020 | 151                   |
| 2021 | 6                     |
| 2022 | 5                     |
| 2023 | 30                    |
| 2024 | 33                    |
| 2025 | 66 ❤️                 |



Whenever I want fresh data I can take new screenshots of
the Nintendo Store app on my phone,
place the new screenshots in the `images/` folder,
and run the `index.py` script to only run OCR on the new images.

If this blog post was interesting to you, I'm planning to look at this data combined with my 
[GameCube play activity data](https://sethmlarson.dev/setting-discord-status-from-physical-gamecube-console)
before the end of 2025. *Stay tuned and play more games!*
