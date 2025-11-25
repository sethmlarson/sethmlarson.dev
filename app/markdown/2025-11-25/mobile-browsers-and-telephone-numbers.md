# Mobile browsers see telephone numbers everywhere

Just like Excel seeing everything as a date,
mobile browsers automatically interpret many numbers as telephone
numbers. When detected, mobile browsers replace the text in the HTML with
a clickable `<a href="tel:...">` value that when selected will call the
number denoted. This can be helpful sometimes, but frustrating other
times as random numbers in your HTML suddenly become useless hyperlinks.

Below I've included numbers that *may* be turned into phone numbers
so you can see for yourself why this may be
a problem and how many cases there are. Numbers that are detected as a phone number by
your browser are <span style="background-color: #00ccff">highlighted blue</span>
by this CSS selector:

```css
a[href^=tel] {
  background-color: #00ccff;
}
```

None of the values below are denoted as telephone number links
in the source HTML, they are all automatically created by the browser.
Also, if you're not using a mobile browser **then the
below numbers won't be highlighted**. <nobr>Try opening this</nobr>
page on a mobile phone.

<ul style="font-variant-numeric: tabular-nums; margin-left: auto; margin-right: auto; width: fit-content;">
<li>2</li>
<li>22</li>
<li>222</li>
<li>2222</li>
<li>22222</li>
<li>222222</li>
<li>2222222</li>
<li>22222222</li>
<li>222222222</li>
<li>2222222222</li>
<li>22222222222</li>
<li>111111111111</li>
<li>222222222222</li>
<li>555555555555</li>
<li>1111111111111</li>
<li>2222222222222 (???)</li>
<li>5555555555555</li>
<li>11111111111111</li>
<li>22222222222222</li>
<li>55555555555555</li>
<li>111111111111111</li>
<li>222222222222222</li>
<li>555555555555555</li>
<li>2-2</li>
<li>2-2-2</li>
<li>22-2-2</li>
<li>22-22-2</li>
<li>22-22-22</li>
<li>22-22-222</li>
<li>22-222-222</li>
<li>222-222-222</li>
<li>222-222-2222</li>
<li>222-2222-2222</li>
<li>2222-2222-2222</li>
<li>2222-2222-22222</li>
<li>2222-22222-22222</li>
<li>22222-22222-22222</li>
<li>2 222-222-2222</li>
<li>+1 222-222-2222</li>
<li>+2 222-222-2222 (<a href="https://en.wikipedia.org/wiki/List_of_telephone_country_codes">There is no +2 country code</a>...)</li>
<li>+28 222-222-2222 (Unassigned codes aren't used)</li>
<li>+1222-222-2222</li>
<li>+2222-222-2222</li>
<li>(+1)222-222-2222</li>
<li>(+2)222-222-2222</li>
<li>(1)222-222-2222</li>
<li>(2)222-222-2222</li>
<li>(1222-222-2222</li>
<li>(1 222-222-2222</li>
<li>1)222-222-2222</li>
<li>222–222–2222 (en-dashes)</li>
<li>222—222—2222 (em-dashes)</li>
<li>[1]222-222-2222</li>
<li>&lt;1&gt;222-222-2222</li>
</ul>

Are there any other combinations that get
detected as telephone numbers that I missed?
Send me a pull request or email.

## How to prevent automatic telephone number detection?

So how can you prevent browsers from parsing telephone numbers automatically?
Add this HTML to your `<head>` section:

```html
<meta name="format-detection" content="telephone=no">
```

This will disable automatic telephone detection, and then you can be explicit about
clickable telephone numbers by using the `tel:` URL scheme like so:

```html
<a href="tel:+222-222-222-2222">(+222)222-222-2222</a>
```

<script>
</script>