# I’ve added human.json to my website

[Evan Hahn](https://evanhahn.com) [recently blogged](https://evanhahn.com/human-dot-json/) about adding
support for the “[`human.json` protocol](https://codeberg.org/robida/human.json)” to his website.
I read the specification and thought this
seemed like a straightforward protocol
to implement.
I've followed along, and added a [`/human.json` file to my
website](/human.json) and `rel="human-json"` in a `<link`>
element to the `<head>` section of my HTML. Easy!

<!-- more -->

Vouching was a little more involved because I wanted to
auto-discover who uses `human.json` from everyone that I follow using RSS.
Then my `vouches` can be kept up-to-date as more people implement
the protocol. The script below is what I ended up with:

```python
import pathlib
import json
import datetime
import re
import opml
import urllib3

today = datetime.date.today().strftime("%Y-%m-%d")

human_json_path = pathlib.Path("app/static/human.json")
human_json = json.loads(human_json_path.read_text())
vouched_urls = {vouch["url"] for vouch in human_json["vouches"]}

doc = opml.OpmlDocument.load("archive/feeds.opml")
for outline in doc.outlines:
    try:
        mat = re.search(r"^(https?://[^/]+)(?:/|$)", outline.html_url or "")
        if not mat:
            continue
        url = mat.group(1)
        resp = urllib3.request(
            "GET",
            f"{url}/human.json",
            headers={
                # Be a good internet netizen:
                # always set a User-Agent with
                # your domain and email.
                "User-Agent": "sethmlarson.dev/1.0 (sethmichaellarson@gmail.com)",
                "Accept": "application/json",
            },
            retries=0,
            timeout=5,
        )
        if resp.status < 300 and "vouches" in resp.json() and url not in vouched_urls:
            human_json["vouches"].append({"url": url, "date": today})
    except Exception as e:
        continue

human_json_path.write_text(json.dumps(human_json, indent=2))
```

Running this script turned up with two websites that I follow
already supporting the protocol:

* https://evanhahn.com ([human.json](https://evanhahn.com/human.json))
* https://foosel.net ([human.json](https://foosel.net/human.json))

Maybe this post will inspire you to add support to your own website?
If you do and I follow you via RSS, your website will appear automatically
after I regenerate my OPML files. If we're mutuals on Mastodon or Bluesky
give me a ping and I'll add you sooner.

I'm probably not going to use the browser extension myself, but if others
are using the data from this "network" then that is a win.
