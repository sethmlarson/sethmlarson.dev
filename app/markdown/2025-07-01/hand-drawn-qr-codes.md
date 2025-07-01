# Hand-drawn QR codes

I really like QR codes. Recently I purchased a new sticky-note-like
pad from a [new local stationery store in Minneapolis](https://www.moonamoono.com/).
The sheets have a 10x10 grid and 2x10 grid.

<center><img style="border: 2px black solid; max-width:75%" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_2362.jpg"></center>

I knew what I wanted to do, I wanted to create a QR code on a sheet.
The smallest QR code (besides micro QR codes) is <nobr>"version 1"</nobr> which uses 21x21 pixels.
We'll have to split the squares in half and then use some of the margin.

Version 1 QR codes can hold URLs up to 17 bytes long using the lowest
data quality setting. Unfortunately `https://sethmlarson.dev` is 23 bytes
long, so I'll have to improvise. I went with `sethmlarson.dev` instead, as this
will prompt many QR code scanners to "search" for the term resulting in my website.

> Note that a lovely reader [informed me](https://mastodon.social/@joshix@fosspri.de/114778118868222197) shortly after publication that indeed
> I can include my full domain name in a version 1 QR code by using all capital
> letters instead of lowercase. TIL that the "alphanumeric" character set for QR
> codes actually contains symbols for URLs like `:` and `/`.
>
> Expect an updated QR code published after lunch today. :)

I created my reference using the [`qrcode` package](https://pypi.org/project/qrcode/) on the Python Package Index. Don't forget
the `-n` option with `echo` to not include a trailing newline.

```
$ echo -n "HTTPS://SETHMLARSON.DEV" | qr --error-correction=L
```

I drew the corner squares (known as "position patterns") and then started trying
to scan the QR code as a gradually filled in other pixels. Once I had drawn the
"timing lines" between the top left and bottom left position I could
see that my scanner "wanted" to see something in my drawing.

<center><img style="border: 2px black solid; max-width:75%" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_2355.jpg"></center>

I continued adding the top timing line and data and then the scanner could
start to see the whole square as a QR code. If you look closely I even
made a mistake here in the data a bit, but in the end this didn't matter
even on the lowest error-correction level.

<center><img style="border: 2px black solid; max-width:75%" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_2356.jpg"></center>

Finally, my QR code was complete! Scanning the QR code was quite finicky because
the paper was curling up off the flat surface. I could only get the scan to work
when I held the paper flat. However, hanging the QR code from my monitor worked
extremely well, even when scanning from a distance.

<center><img style="border: 2px black solid; max-width:75%" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_2367.jpg"></center>

I hope this inspires you to try hand-drawing something on grid paper <nobr>🖤🤍</nobr>
If you're looking for more grid-based inspiration, take a look at [GRID WORLD](https://alex.miller.garden/grid-world/), a web art piece by Alexander Miller.
