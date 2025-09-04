import datetime
import re
import json
import pathlib
import sys

import opml
import urllib3
from mastodon import Mastodon


http_client = urllib3.PoolManager()
archive_dir = pathlib.Path(__file__).parent.absolute()
access_token = None
app_secrets = json.loads((archive_dir / "app-secrets.json").read_text())
app_id = app_secrets["app_id"]
app_key = app_secrets["app_key"]
app_state = "state"
mastodon_access_token = app_secrets["mastodon_access_token"]
mastodon = Mastodon(
    api_base_url="https://mastodon.social", access_token=mastodon_access_token
)
mastodon_field_url_re = re.compile(r"\"(https?://[^\"]+)\"")
tag_to_emoji = {
    "Life": "🏞️",
    "Retro Gaming": "🎮",
    "Social Media": "📱",
    "Software and OSS": "🖥️",
    "Security": "🔒",
    "Toys and Art": "🖼️",
}


def headers():
    fetch_access_token()
    return {"Authorization": f"Bearer {access_token}"}


def fetch_access_token():
    global access_token
    if access_token is not None:
        return
    secrets_file = archive_dir / "secrets.json"
    secrets = json.loads(secrets_file.read_text())
    access_token = secrets["access_token"]

    # Try an API request, if it doesn't work we
    # need to either refresh or go through the re-auth flow.
    resp = http_client.request(
        "GET",
        "https://www.inoreader.com/reader/api/0/user-info",
        headers={"Authorization": f"Bearer {access_token}"},
    )
    if resp.status != 200:
        refresh_token = secrets["refresh_token"]
        resp = http_client.request(
            "POST",
            "https://www.inoreader.com/oauth2/token",
            fields={
                "client_id": app_id,
                "client_secret": app_key,
                "grant_type": "refresh_token",
                "refresh_token": refresh_token,
            },
        )
        if resp.status != 200:
            raise RuntimeError(resp.status, resp.data)
        secrets = resp.json()
        secrets_file.write_text(json.dumps(secrets))

    access_token = secrets["access_token"]


_maybe_https_cache = {}


def normalize_url(url: str) -> str:
    """See if an HTTP URL can be HTTPS?"""
    global _maybe_https_cache
    url = url.rstrip("/")
    # Get rid of Inoreader specific garbage
    if "youtube.com" in url and "?cbrd=1&ucbcb=1" in url:
        url = url.replace("?cbrd=1&ucbcb=1", "")
    if url.startswith("https://"):
        return url
    https_url = url.replace("http://", "https://")
    if https_url not in _maybe_https_cache:
        try:
            http_client.request(https_url)
        except Exception:
            _maybe_https_cache[https_url] = False
        else:
            _maybe_https_cache[https_url] = True
    return https_url if _maybe_https_cache[https_url] else url


def feeds_opml_from_inoreader() -> None:
    feeds_opml = opml.OpmlDocument(
        title="feeds.opml",
        owner_name="Seth Larson",
        owner_email="sethmichaellarson@gmail.com",
        owner_id="https://sethmlarson.dev",
    )

    resp = http_client.request(
        "GET",
        "https://www.inoreader.com/reader/api/0/subscription/list",
        headers=headers(),
    )
    for sub in sorted(resp.json()["subscriptions"], key=lambda x: x["title"]):
        # Don't expose my private 404Media RSS feed.
        if sub["title"] == "404 Media":
            sub["url"] = "https://www.404media.co/rss/"
            sub["htmlUrl"] = "https://www.404media.co"

        feeds_opml.add_rss(
            text=sub["title"],
            xml_url=normalize_url(sub["url"]),
            html_url=normalize_url(sub["htmlUrl"]),
        )

    with (archive_dir / "feeds.opml").open(mode="w") as f:
        f.truncate()
        f.write(feeds_opml.dumps(pretty=True))


def articles_opml_from_inoreader():
    # Build the existing set of URLs to avoid
    # overwriting anything we've already recorded.
    existing_urls = {}
    articles_opml_path = archive_dir / "articles.opml"
    if articles_opml_path.exists():
        existing_doc = opml.OpmlDocument.loads(articles_opml_path.read_text())
        for outline in existing_doc.outlines:
            outline.url = normalize_url(outline.url)
            existing_urls[outline.url] = outline

    articles_opml = opml.OpmlDocument(
        title="articles.opml",
        owner_name="Seth Larson",
        owner_email="sethmichaellarson@gmail.com",
        owner_id="https://sethmlarson.dev",
    )

    def fetch_articles():
        # Inoreader has two ways of "saving" an article,
        # with stars and with a "saved web page". One
        # is easy from mobile one is easy from web.
        stream_ids = ["starred", "saved-web-pages"]

        # Deduplicate URLs because articles might be in both streams.
        deduplicated_urls = set()

        for stream_id in stream_ids:
            stream_url = f"https://www.inoreader.com/reader/api/0/stream/contents/user/-/state/com.google/{stream_id}?output=json&n=100"
            continuation = None
            while True:
                url = stream_url
                if continuation is not None:
                    url = url + f"&c={continuation}"

                resp = http_client.request("GET", url, headers=headers())
                if resp.status != 200:
                    raise RuntimeError(resp.status, resp.data)
                resp_data = resp.json()

                for item in resp_data["items"]:
                    # Deduplicate an article by URL before yielding.
                    article_url = normalize_url(item["canonical"][0]["href"])
                    if article_url in deduplicated_urls:
                        continue
                    deduplicated_urls.add(article_url)

                    yield item

                if not (continuation := resp_data.get("continuation", None)):
                    break

    for article in fetch_articles():
        author = article.get("author", None)
        title = f"“{article['title'].strip()}”"
        url = normalize_url(article["canonical"][0]["href"])
        if author:
            author = author.strip()
            title = f"{title} by {author}"
        created_at = datetime.datetime.fromtimestamp(
            int(article["crawlTimeMsec"]) // 1000, tz=datetime.UTC
        )
        tags = sorted(
            {
                cat.rsplit("/", 1)[-1]
                for cat in article["categories"]
                if "/label/" in cat
            }
        )

        # Avoid publishing gift ideas!
        if "Gift" in tags or "Video" in tags:
            continue

        # If this URL is already in our OPML then we use
        # the existing data, otherwise we add the new data.
        if url in existing_urls:
            outline = existing_urls[url]
            if tags:
                outline.categories = tags
            if outline.created is None:
                outline.created = created_at
            articles_opml.outlines.append(outline)
        else:
            # If an article has no tags then we skip it,
            # likely because I haven't processed it yet.
            if not tags:
                continue
            articles_opml.add_link(
                text=title,
                url=url,
                categories=tags,
                created=created_at,
            )

    with articles_opml_path.open(mode="w") as f:
        f.truncate()
        f.write(articles_opml.dumps(pretty=True))


def articles_opml_from_links():
    data = (archive_dir.parent / "app/templates/links.html").read_text()

    articles_opml_path = archive_dir / "articles.opml"
    articles_opml = opml.OpmlDocument(
        title="articles.opml",
        owner_name="Seth Larson",
        owner_email="sethmichaellarson@gmail.com",
        owner_id="https://sethmlarson.dev",
    )

    tag = ""
    for line in data.split("\n"):
        if match := re.match(r"<h2>([^>]+)</h2>", line):
            tag = match.group(1)
            continue
        if match := re.match(
            r"<li>“<a href=\"([^\"]+)\">([^>]+)</a>”(?: by <strong>([^>]+)</strong>)?</li>",
            line,
        ):
            url, title, author = match.groups()
            title = f"“{title.strip()}”"
            url = normalize_url(url)

            if author:
                author = author.strip()
                title = f"{title} by {author}"

            articles_opml.add_link(
                text=title,
                url=url,
                categories=[tag],
            )

    with articles_opml_path.open(mode="w") as f:
        f.write(articles_opml.dumps(pretty=True))


def update_links():
    articles_opml_path = archive_dir / "articles.opml"
    articles_opml = opml.OpmlDocument.loads(articles_opml_path.read_text())
    tags = set()
    for outline in articles_opml.outlines:
        try:
            tags.add(outline.categories[0])
        except IndexError:
            raise RuntimeError(f"Article {outline.text!r} has no tags")

    links_path = archive_dir.parent / "app/templates/links.html"
    lines = links_path.read_text().splitlines()
    new_lines = []
    sentinel_found = False

    for line in lines:
        # Look for the end of the section,
        # otherwise we drop the old content on the floor.
        if sentinel_found:
            if line.startswith("</p>"):
                sentinel_found = False
            else:
                continue

        # Look for our sentinel so we can insert our generated lines.
        if "#sentinel" in line:
            new_lines.append(line)  # Add our sentinel line first.
            sentinel_found = True
            new_lines.append('<table style="table-layout: fixed">')
            for outline in articles_opml.outlines:
                assert len(outline.categories) == 1
                tag = outline.categories[0]
                tag_emoji = tag_to_emoji[tag]
                title, author = re.match(
                    r"^“([^”]+)”(?: by (.*))?$", outline.text
                ).groups()
                new_lines.append(
                    f"<tr><td title=\"{tag}\">{tag_emoji}</td><td>“<a href=\"{outline.url}\">{title}</a>”{' by ' + author if author else ''}</td></tr>"
                )
            new_lines.append("</table>")
            continue

        new_lines.append(line)

    links_path.write_text("\n".join(new_lines))


def mastodon_follow_graph():
    mastodon_followers_path = archive_dir / "mastodon-followers.opml"
    mastodon_following_path = archive_dir / "mastodon-following.opml"
    # mastodon_followers_opml = opml.OpmlDocument.loads(mastodon_followers_path.read_text())

    def yield_accounts(page):
        while page is not None:
            for account in page:
                if account.bot:  # No bots, please.
                    continue
                yield account
            page = mastodon.fetch_next(page)

    def write_opml_for_accounts(filepath: pathlib.Path, accounts) -> None:
        accounts_opml = opml.OpmlDocument()
        accounts = sorted(accounts, key=lambda acc: acc.acct)
        for account in accounts:
            accounts_opml.add_link(
                text=account.acct,
                url=account.url,
            )
        with filepath.open(mode="w") as f:
            f.truncate()
            f.write(accounts_opml.dumps(pretty=True))

    me = mastodon.me()
    write_opml_for_accounts(
        mastodon_followers_path,
        yield_accounts(mastodon.account_followers(id=me, limit=1000)),
    )
    write_opml_for_accounts(
        mastodon_following_path,
        yield_accounts(mastodon.account_following(id=me, limit=1000)),
    )


if __name__ == "__main__":
    offline = "--offline" in sys.argv
    if not offline:
        feeds_opml_from_inoreader()
        articles_opml_from_inoreader()
        mastodon_follow_graph()
    # articles_opml_from_links()
    update_links()
