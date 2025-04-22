# Quick Mastodon toot templates for event hashtags

<div class="row">
<div class="col-6 col-sm-12">
<p>I'm a big fan of <a href="https://fosstodon.org/@sethmlarson">Mastodon</a> and I plan to cover PyCon US 2025
on Mastodon almost exclusively (<a href="https://treyhunner.com/2025/04/which-social-network-are-we-using-for-pycon/">and it sounds like I'm not alone</a>).</p>
<p>This was the plan last year, too, but
I found typing out all the hashtags every time definitely discouraged me from
posting about "in-the-moment" stuff.</p>
<p>The goal is to quickly capture a thought, interaction, or image,
share to Mastodon, and then <em>get back to enjoying the conference</em>. </p>
</div>
<div class="col-6 col-sm-12">
<center><img style="max-width: 100%; border: 2px solid black;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_1503.jpeg"/><br>
<small><em>Pre-populated event hashtags!</em></small></center>
</div>
</div>

So I went looking for a solution and found that Mastodon supports
share URLs with pre-filled content, like hashtags. What I wanted to do was add a URL to my phone home screen:

```
https://<instance domain name>/share?text=%0A%0A%23PyCon%20%23PyConUS%20%23PyConUS2025
```

The above percent-encoded `text` parameter is:

```
\n\n#PyCon #PyConUS #PyConUS2025
```

If we could save this URL direct to the home screen that would be
the end of the story.  Unfortunately, at least for iOS you can't save a web page that
has a query parameter in the URL (like `?text=...`), so the
solution needs to be slightly more complicated.

What I ended up doing is
adding this URL to a [GitHub Gist](https://gist.github.com/sethmlarson/f9dda0e61e050a9979755dcfdc9ff8c0)
and then saving the Gist webpage to my home screen. On iOS the process is:

* Navigate to the Gist in your mobile browser
* Use the "share" button within the browser
* Select "Add to Home Screen" in the share screen
* Give the page a name (I went with "#PyConUS2025").
* :tada:

Now I'm only ever two clicks away from a ready-to-use toot
template for PyCon US.
This technique is remixable for any hashtags or other
text you're tooting often. Use `urllib.parse.quote()` in Python to create percent-encoded text.
