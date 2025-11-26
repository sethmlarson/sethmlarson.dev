# WebKit browsers see telephone numbers everywhere

Just like Excel seeing everything as a date,
[WebKit mobile browsers](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariHTMLRef/Articles/MetaTags.html) automatically interpret many numbers as telephone
numbers. When detected, mobile browsers replace the text in the HTML with
a clickable `<a href="tel:...">` value that when selected will call the
number denoted. This can be helpful sometimes, but frustrating other
times as random numbers in your HTML suddenly become useless hyperlinks.

<!-- more -->

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

<p>
None of the values below are denoted as telephone number links
in the source HTML, they are all automatically created by the browser.
If you're not using WebKit, enable this check-box to show WebKit's behavior:
<code><input type="checkbox" name="webkit-mode" id="webkit-mode" onclick="webkitMode(this);">
<label for="webkit-mode">
WebKit Mode
</label></code>
</p>

<ul style="font-variant-numeric: tabular-nums; margin-left: auto; margin-right: auto; width: fit-content;">
<li>2</li>
<li>22</li>
<li>222</li>
<li>2222</li>
<li>22222</li>
<li>222222</li>
<li><span class="pn">2222222</span></li>
<li><span class="pn">22222222</span></li>
<li><span class="pn">222222222</span></li>
<li><span class="pn">2222222222</span></li>
<li><span class="pn">22222222222</span></li>
<li>111111111111</li>
<li>222222222222</li>
<li>555555555555</li>
<li><span class="pn">1111111111111</span></li>
<li>2222222222222 (???)</li>
<li><span class="pn">5555555555555</span></li>
<li><span class="pn">11111111111111</span></li>
<li><span class="pn">22222222222222</span></li>
<li><span class="pn">55555555555555</span></li>
<li>111111111111111</li>
<li>222222222222222</li>
<li>555555555555555</li>
<li>2-2</li>
<li>2-2-2</li>
<li>22-2-2</li>
<li>22-22-2</li>
<li>22-22-22</li>
<li><span class="pn">22-22-222</span></li>
<li><span class="pn">22-222-222</span></li>
<li><span class="pn">222-222-222</span></li>
<li><span class="pn">222-222-2222</span></li>
<li><span class="pn">222-2222-2222</span></li>
<li><span class="pn">2222-2222-2222</span></li>
<li><span class="pn">2222-2222-22222</span></li>
<li><span class="pn">2222-22222-22222</span></li>
<li>22222-22222-22222</li>
<li><span class="pn">2 222-222-2222</span></li>
<li><span class="pn">+1 222-222-2222</span></li>
<li>+2 <span class="pn">222-222-2222</span> (<a href="https://en.wikipedia.org/wiki/List_of_telephone_country_codes">There is no +2 country code</a>...)</li>
<li>+28 <span class="pn">222-222-2222</span> (Unassigned codes aren't used)</li>
<li><span class="pn">+1222-222-2222</span></li>
<li><span class="pn">+2222-222-2222</span></li>
<li><span class="pn">(+1)222-222-2222</span></li>
<li>(+2)<span class="pn">222-222-2222</span></li>
<li><span class="pn">(1)222-222-2222</span></li>
<li><span class="pn">(2)222-222-2222</span></li>
<li>(<span class="pn">1222-222-2222</span></li>
<li>(<span class="pn">1 222-222-2222</span></li>
<li>1)<span class="pn">222-222-2222</span></li>
<li><span class="pn">222–222–2222</span> (en-dashes)</li>
<li><span class="pn">222—222—2222</span> (em-dashes)</li>
<li>[1]<span class="pn">222-222-2222</span></li>
<li>&lt;1&gt;<span class="pn">222-222-2222</span></li>
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
function webkitMode(cb) {
  for (const el of document.getElementsByClassName("pn")) {
    if (cb.checked) {
      el.classList.add("pn-on");
    } else {
      el.classList.remove("pn-on");
    };
  }
};
</script>