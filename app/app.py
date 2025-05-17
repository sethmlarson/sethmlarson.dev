import datetime
import functools
import pathlib
import re
import time
import typing
from urllib.parse import parse_qsl

import attr
import markdown2
from flask import (
    Flask,
    abort,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)
from werkzeug.contrib.atom import AtomFeed
from whitenoise import WhiteNoise
from bs4 import BeautifulSoup

base_dir = pathlib.Path(__file__).absolute().parent
markdown_dir = base_dir / "markdown"
static_dir = base_dir / "static"
app = Flask(__name__, template_folder=str(base_dir / "templates"))
app.wsgi_app = WhiteNoise(app.wsgi_app, root=str(static_dir), prefix="/static")
md = markdown2.Markdown(extras={"fenced-code-blocks": None, "tables": None})
max_cache_time = 31536000
long_cache_time = 1800
small_cache_time = 300
avatar_url = "https://github.com/sethmlarson.png"
reading_times = {}
favorite_posts = {
    "designing-for-real-world-https",
    "api-design-for-an-async-open",
    "tests-arent-enough-case-study-after-adding-types-to-urllib3",
    "experimental-python-3.10-apis-and-trust-stores",
    "strict-python-function-parameters",
    "utf-8",
    "for-you-is-not-for-me",
    "urllib3-is-fundraising-for-http2-support",
    "security-developer-in-residence-weekly-report-9",
    "security-developer-in-residence-weekly-report-13",
    "security-developer-in-residence-weekly-report-18",
    "pep-440",
    "security-for-package-maintainers",
    "people-in-your-software-supply-chain",
    "removing-maintainers-from-open-source-projects",
    "websites-without-servers-or-networking",
    "regex-$-matches-end-of-string-or-newline",
    "security-developer-in-residence-weekly-report-35",
    "backup-game-boy-roms-and-saves-on-ubuntu",
    "security-developer-in-residence-report-37",
    "youtube-without-youtube-shorts",
    "python-and-sigstore",
    "writing-for-the-internet",
    "how-to-i-pay-for-a-web-page",
    "slop-security-reports",
    "building-software-for-connection-local-first",
    "i-fear-for-the-unauthenticated-web",
}
hide_posts = {
    "hi-chew",
}


def cache_for(seconds: int):
    def decorator(f):
        @functools.wraps(f)
        def decorated(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            if resp.status_code == 200:
                resp.headers["Cache-Control"] = f"max-age={seconds}, public, immutable"
            return resp

        return decorated

    return decorator


@attr.s
class BlogPost:
    slug: str = attr.ib()
    title: str = attr.ib()
    date: str = attr.ib()
    month: str = attr.ib()
    markdown_path: pathlib.Path = attr.ib()

    def render_html(self) -> str:
        with self.markdown_path.open(mode="r") as f:
            text = f.read()
            _, text = text.split("\n", 1)
        html = md.convert(text)
        blog_content_text = re.sub(r"<[^>]+>", "", html)
        return render_template(
            "blog.html",
            blog_title=self.title,
            blog_published_date=self.date,
            blog_content=html,
            blog_content_text=blog_content_text,
        )

    def render_rss_html(self):
        with self.markdown_path.open(mode="r") as f:
            text = f.read()
            _, text = text.split("\n", 1)
        html = md.convert(text)
        return html

    def url(self, utm_campaign=None) -> str:
        url = url_for(
            "get_blog_post",
            blog_post=self.markdown_path.name[:-3],
            _external=True,
            **({"utm_campaign": utm_campaign} if utm_campaign else {})
        )
        if "sethmlarson.dev" in url:
            url = url.replace("http://", "https://")
        return url

    def utc(self) -> datetime.datetime:
        return datetime.datetime.fromisoformat(f"{self.date}T00:00:00")


BLOG_POSTS_BY_SLUG: typing.Dict[str, BlogPost] = {}
BLOG_POSTS_BY_DATE: typing.Dict[str, BlogPost] = {}


def load_blog_posts() -> typing.Dict[str, typing.List[BlogPost]]:
    """Loads all blog post metadata from the filesystem"""
    global BLOG_POSTS_BY_SLUG, BLOG_POSTS_BY_DATE
    dates = sorted(
        [x for x in markdown_dir.iterdir() if x.name != "draft"],
        key=lambda x: [int(y.lstrip("0")) for y in x.name.split("-")],
        reverse=True,
    )
    for date in dates:
        markdown_path = list(date.iterdir())[0]
        with markdown_path.open(mode="r") as f:
            title = f.readline().strip("\n# ")
        bp = BlogPost(
            slug=markdown_path.name.replace(".md", ""),
            title=title,
            date=date.name,
            month=date.name.rsplit("-", 1)[0],
            markdown_path=markdown_path,
        )
        BLOG_POSTS_BY_DATE.setdefault(bp.date, []).append(bp)
        BLOG_POSTS_BY_SLUG.setdefault(bp.slug, bp)


load_blog_posts()


@app.route("/robots.txt", methods=["GET"])
@cache_for(max_cache_time)
def robots_txt():
    resp = make_response("""User-agent: *
Disallow:

User-agent: AdsBot-Google
User-agent: Amazonbot
User-agent: anthropic-ai
User-agent: Applebot
User-agent: AwarioRssBot
User-agent: AwarioSmartBot
User-agent: Bytespider
User-agent: CCBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: Claude-Web
User-agent: cohere-ai
User-agent: DataForSeoBot
User-agent: FacebookBot
User-agent: Google-Extended
User-agent: GoogleOther
User-agent: GPTBot
User-agent: ImagesiftBot
User-agent: magpie-crawler
User-agent: Meltwater
User-agent: omgili
User-agent: omgilibot
User-agent: peer39_crawler
User-agent: peer39_crawler/1.0
User-agent: PerplexityBot
User-agent: Seekr
User-agent: YouBot
Disallow: /""")
    resp.headers["Content-Type"] = "text/plain"
    return resp


@app.route("/blog", methods=["GET"])
@cache_for(small_cache_time)
def list_blog_posts():
    return render_template("blog-posts.html", blog_posts=BLOG_POSTS_BY_DATE, favorite_posts=favorite_posts, hide_posts=hide_posts)


@app.route("/links", methods=["GET"])
@cache_for(small_cache_time)
def links():
    return render_template("links.html")


RSS_RESPONSE = None


def load_rss_response():
    global RSS_RESPONSE
    if RSS_RESPONSE is not None:
        return RSS_RESPONSE

    feed = AtomFeed(
        title="Seth Larson",
        author={
            "name": "Seth Larson",
            "email": "sethmichaellarson@gmail.com",
            "uri": "https://sethmlarson.dev",
        },
        icon=avatar_url,
        logo=avatar_url,
        feed_url=url_for("rss_blog_posts", _external=True),
        url=request.url_root,
    )
    total = 0
    for _, blog_posts in BLOG_POSTS_BY_DATE.items():
        for blog_post in blog_posts:
            if total == 5:
                break
            if blog_post.slug in hide_posts:
                continue
            total += 1
            blog_utc = blog_post.utc()

            feed.add(
                blog_post.title,
                blog_post.render_rss_html(),
                content_type="html",
                author="Seth Larson",
                url=blog_post.url(utm_campaign="rss"),
                published=blog_utc,
                updated=blog_utc,
            )

        if total == 5:
            break

    RSS_RESPONSE = feed.get_response()
    return RSS_RESPONSE


@app.route("/feed.xml")
@app.route("/blog/rss", methods=["GET"])
@app.route("/rss", methods=["GET"])
@app.route("/atom", methods=["GET"])
@app.route("/feed", methods=["GET"])
@cache_for(long_cache_time)
def rss_blog_posts():
    return load_rss_response()


@app.route("/about", methods=["GET"])
@cache_for(small_cache_time)
def about():
    return redirect(url_for("index"))


@app.route("/", methods=["GET"])
@cache_for(small_cache_time)
def index():
    return render_template("index.html")


@app.route("/api/wordle-stats", methods=["GET"])
def api_wordle_stats():
    failed = False
    try:
        query = dict(parse_qsl(request.query_string))
        wins_in_1 = int(query.get(b"wins-1").strip())
        wins_in_2 = int(query.get(b"wins-2").strip())
        wins_in_3 = int(query.get(b"wins-3").strip())
        wins_in_4 = int(query.get(b"wins-4").strip())
        wins_in_5 = int(query.get(b"wins-5").strip())
        wins_in_6 = int(query.get(b"wins-6").strip())
        losses = int(query.get(b"losses").strip())
        max_streak = int(query.get(b"max-streak").strip())
        wins_total = sum(
            [wins_in_1, wins_in_2, wins_in_3, wins_in_4, wins_in_5, wins_in_6]
        )
        games_played = sum([wins_total, losses])
        if games_played == 0:
            win_percentage = 0
            average_guesses = 0
        else:
            win_percentage = int(100 * (wins_total / games_played))
            average_guesses = int(
                sum(
                    [
                        wins_in_1,
                        wins_in_2 * 2,
                        wins_in_3 * 3,
                        wins_in_4 * 4,
                        wins_in_5 * 5,
                        wins_in_6 * 6,
                        losses * 6,
                    ]
                )
                / games_played
            )
    except Exception as e:
        failed = True

    if failed:
        return redirect("https://www.nytimes.com/games/wordle")
    return redirect(
        f"https://www.nytimes.com/games/wordle?data={{%22time%22:{int(time.time() - (5 * 60))},%22statistics%22:{{%22currentStreak%22:0,%22maxStreak%22:{max_streak},%22guesses%22:{{%221%22:{wins_in_1},%222%22:{wins_in_2},%223%22:{wins_in_3},%224%22:{wins_in_4},%225%22:{wins_in_5},%226%22:{wins_in_6},%22fail%22:{losses}}},%22gamesPlayed%22:{games_played},%22gamesWon%22:{wins_total},%22averageGuesses%22:{average_guesses},%22winPercentage%22:{win_percentage}}},%22darkTheme%22:false,%22colorBlindTheme%22:null}}",
        code=307,
    )


@app.route("/blog/<string:date>/<string:blog_post>", methods=["GET"])
@app.route("/blog/<string:blog_post>", methods=["GET"])
@cache_for(long_cache_time)
def redirect_to_new_blog_post_url(
    blog_post: str,
    date: str = None,
):
    return redirect(url_for("get_blog_post", blog_post=blog_post))


@app.route("/static/avatar.jpeg", methods=["GET"])
def redirect_to_new_avatar_url():
    return redirect(avatar_url, 308)


@app.route("/elegant-secure-api-design", methods=["GET"])
def redirect_to_fixed_elegant_secure_api_design_url():
    return redirect(
        url_for("get_blog_post", blog_post="elegant-and-secure-api-design"), 308
    )


@app.route("/connection-without-connectivity-space", methods=["GET"])
def redirect_to_new_slug1():
    return redirect(
        url_for("get_blog_post", blog_post="building-software-for-connection-local-first"), 308
    )


@app.route("/supplychain")
def supplychain_google_meet():
    return redirect("https://meet.google.com/mxn-ouhp-jkh")


@app.route("/<string:blog_post>", methods=["GET"])
@cache_for(long_cache_time)
def get_blog_post(blog_post: str):
    try:
        blog = BLOG_POSTS_BY_SLUG[blog_post]
    except KeyError:
        return abort(404)
    with blog.markdown_path.open(mode="r") as f:
        text = f.read()
        title, rest = text.split("\n", 1)
        title = title.lstrip("# ")
        html = md.convert(rest)

    # Calculate reading time and cache the value.
    global reading_times
    if blog_post not in reading_times:
        word_count = len(
            re.findall(
                r"[a-zA-z0-9\-]+",
                BeautifulSoup(html, features="html.parser").get_text(separator=" "),
            )
        )
        reading_times[blog_post] = max(word_count // 200, 1)
    reading_time = reading_times[blog_post]

    blog_content_text = re.sub(r"<[^>]+>", "", html)

    # Insert anchors into all headers automatically
    for header_start, header, header_end in re.findall(
        r"(<h[1-5]>)([^<]+)(</h[1-5]>)", html
    ):
        anchor_href = re.sub(r"[^a-z0-9]+", "-", header.replace("'", "").lower()).strip(
            "-"
        )
        html = html.replace(
            header_start + header + header_end,
            f'{header_start[:-1]} id="{anchor_href}">{header}<a class="anchor" href="#{anchor_href}" aria-hidden="true">§</a>{header_end}',
        )

    # Inject custom HTML into the HTML <head> tags.
    html_head = ""
    if blog_post == "unicode-variation-selectors":
        html_head = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Emoji&family=Noto+Sans+Symbols+2&display=swap" rel="stylesheet">
<style>
  .ucode {
    font-feature-settings: 'tnum' 1;
  }
  .mahjong {
    font-family: 'Noto Sans Symbols 2', 'Noto Emoji', sans-serif;
    font-size: 5.3rem;
    line-height: 5rem;
    margin-bottom: 1rem;
  }
</style>
        """

    if blog_post == "significant-whitespace":
        reading_time = 0

    return render_template(
        "blog.html",
        reading_time=reading_time,
        blog_slug=blog_post,
        blog_title=title,
        blog_published_date=blog.date,
        blog_content=html,
        blog_content_text=blog_content_text,
        blog_is_favorite=blog_post in favorite_posts,
        total_blog_count=len(BLOG_POSTS_BY_SLUG),
        html_head=html_head,
    )
