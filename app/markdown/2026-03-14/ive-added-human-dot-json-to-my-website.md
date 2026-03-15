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
the protocol. I updated the script to parse the `<link>` element
properly using [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) (thanks Evan!). The script below is what I ended up with:

```python
import contextlib
import pathlib
import json
import datetime
import re
import urllib
import opml
import urllib3
import bs4

http = urllib3.PoolManager(
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
today = datetime.date.today().strftime("%Y-%m-%d")

human_json_path = pathlib.Path("app/static/human.json")
human_json = json.loads(human_json_path.read_text())
vouched_urls = {vouch["url"] for vouch in human_json["vouches"]}

doc = opml.OpmlDocument.load("archive/feeds.opml")
for outline in doc.outlines:
    mat = re.search(r"^(https?://[^/]+)(?:/|$)", outline.html_url or "")
    if not mat:
        continue
    base_url = mat.group(1)
    urls_to_try = [f"{base_url}/human.json"]

    with contextlib.suppress(Exception):
        # Find <link rel="human-json" ...>
        resp = http.request("GET", base_url)
        html = bs4.BeautifulSoup(resp.data, "html.parser")
        for el in html.find_all(
            name="link", attrs={"rel": "human-json"}, recursive=True
        ):
            if href := el.attrs.get("href", None):
                urls_to_try.append(urllib.parse.urljoin(base_url, href))

    # Try all candidate URLs.
    for url in urls_to_try:
        with contextlib.suppress(Exception):
            resp = http.request("GET", url)
            if resp.status < 300 and set(resp.json()) == {"version", "vouches", "url"}:
                # Use the URL that the domain specifies, not
                # our own. This helps with canonicalization,
                # (ie do we use 'www.example.com' or 'example.com'?)
                human_json_url = resp.json()["url"]
                if human_json_url in vouched_urls:
                    continue
                vouched_urls.add(human_json_url)
                human_json["vouches"].append({"url": human_json_url, "date": today})
                continue

human_json_path.write_text(json.dumps(human_json, indent=2))
```

Running this script turned up with two websites that I follow
already supporting the protocol:

* [https://evanhahn.com](https://evanhahn.com) ([human.json](https://evanhahn.com/human.json))
* [https://foosel.net](https://foosel.net) ([human.json](https://foosel.net/human.json))

Maybe this post will inspire you to add support to your own website?
If you do and I follow you via RSS, your website will appear automatically
after I regenerate my OPML files. If we're mutuals on Mastodon or Bluesky
give me a ping and I'll add you sooner.

I'm probably not going to use the browser extension myself, but if others
are using the data from this "network" then that is a win.
