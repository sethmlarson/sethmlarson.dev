import re
import datetime
import pathlib
import markdown2
import functools
from flask import (
    Flask,
    render_template,
    request,
    url_for,
    make_response,
    abort,
    redirect,
)
import attr
import time
import typing
from werkzeug.contrib.atom import AtomFeed
from whitenoise import WhiteNoise
from urllib.parse import parse_qsl


base_dir = pathlib.Path(__file__).absolute().parent
markdown_dir = base_dir / "markdown"
static_dir = base_dir / "static"
app = Flask(__name__, template_folder=str(base_dir / "templates"))
app.wsgi_app = WhiteNoise(app.wsgi_app, root=str(static_dir), prefix="/static")
md = markdown2.Markdown(extras={"fenced-code-blocks": None})
max_cache_time = 31536000
long_cache_time = 1800
small_cache_time = 300


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

    def url(self) -> str:
        return url_for(
            "get_blog_post",
            date=self.date,
            blog_post=self.markdown_path.name[:-3],
            _external=True,
        )

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
    resp = make_response("User-agent: *\nDisallow:")
    resp.headers["Content-Type"] = "text/plain"
    return resp


@app.route("/blog", methods=["GET"])
@cache_for(small_cache_time)
def list_blog_posts():
    return render_template("blog-posts.html", blog_posts=BLOG_POSTS_BY_DATE)


@app.route("/blog/rss", methods=["GET"])
@app.route("/rss", methods=["GET"])
@app.route("/atom", methods=["GET"])
@app.route("/feed", methods=["GET"])
@cache_for(long_cache_time)
def rss_blog_posts():
    feed = AtomFeed(
        title="sethmlarson.dev - Last 5 Blog Posts",
        feed_url=url_for("rss_blog_posts", _external=True),
        url=request.url_root,
    )
    total = 0
    for _, blog_posts in BLOG_POSTS_BY_DATE.items():
        for blog_post in blog_posts:
            if total == 5:
                break
            total += 1
            blog_utc = blog_post.utc()

            feed.add(
                blog_post.title,
                blog_post.render_html(),
                content_type="html",
                author="Seth Michael Larson",
                url=blog_post.url(),
                published=blog_utc,
                updated=blog_utc,
            )

        if total == 5:
            break

    return feed.get_response()


@app.route("/about", methods=["GET"])
@cache_for(small_cache_time)
def about():
    latest_blog = BLOG_POSTS_BY_DATE[sorted(BLOG_POSTS_BY_DATE, reverse=True)[0]][-1]
    return render_template("index.html", latest_blog=latest_blog)


@app.route("/", methods=["GET"])
@cache_for(small_cache_time)
def index():
    latest_blog = BLOG_POSTS_BY_DATE[sorted(BLOG_POSTS_BY_DATE, reverse=True)[0]][-1]
    return render_template("index.html", latest_blog=latest_blog)


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


@app.route("/blog/<string:blog_post>", methods=["GET"])
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

    blog_content_text = re.sub(r"<[^>]+>", "", html)

    # Insert anchors into all headers automatically
    for header_start, header, header_end in re.findall(r"(<h[1-5]>)([^<]+)(</h[1-5]>)", html):
        anchor_href = re.sub(r"[^a-z0-9]+", "-", header.lower()).strip("-")
        html = html.replace(header_start + header + header_end, f'{header_start[:-1]} id="{anchor_href}">{header}<a class="anchor" href="#{anchor_href}" aria-hidden="true">#</a>{header_end}')

    return render_template(
        "blog.html",
        blog_title=title,
        blog_published_date=blog.date,
        blog_content=html,
        blog_content_text=blog_content_text,
    )


@app.route("/blog/<string:date>/<string:blog_post>", methods=["GET"])
@cache_for(long_cache_time)
def redirect_to_new_blog_post_url(
    blog_post: str,
    date: str = None,
):
    return redirect(url_for("get_blog_post", blog_post=blog_post))


@app.route("/wordle-stats", methods=["GET"])
def redirect_to_wordle_stats():
    return redirect(url_for("get_blog_post", blog_post="wordle-stats"))
