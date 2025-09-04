import re
import urllib3
import bs4
import pathlib
import opml

http = urllib3.PoolManager()
archive_dir = pathlib.Path(__file__).parent.absolute()
articles_opml_path = archive_dir / "articles.opml"
articles_opml = opml.OpmlDocument.loads(articles_opml_path.read_text())
source_url = "https://sethmlarson.dev/links"

for outline in articles_opml.outlines:
    url = outline.url
    try:
        resp = http.request("GET", url, redirect=True, timeout=2)
    except Exception as e:
        print("err:", e)
        continue
    if resp.status != 200:
        continue
    bs = bs4.BeautifulSoup(resp.data, "html.parser")
    webmention_urls = []
    webmention_urls.extend([el.get("href", None) for el in bs.find_all(name="link", attrs={"rel": True}) if "webmention" in el.get("rel", ())])
    webmention_urls.extend([el.get("href", None) for el in bs.find_all(name="a", attrs={"rel": True}) if "webmention" in el.get("rel", ())])
    webmention_urls = set(filter(None, webmention_urls))

    for webmention_url in webmention_urls:
        resp = http.request(
            "POST", webmention_url,
            fields={"source": source_url, "target": url},
            timeout=10,
        )
        print(url, "-->", webmention_url, resp.status)
