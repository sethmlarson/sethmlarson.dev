import h11
import datetime
import pathlib
import markdown2
from flask import Flask, render_template, request, url_for, make_response, abort, send_file
import functools
import user_agents
import attr
import typing
from werkzeug.contrib.atom import AtomFeed


base_dir = pathlib.Path(__file__).absolute().parent
markdown_dir = base_dir / "markdown"
static_dir = base_dir / "static"
app = Flask(__name__, template_folder=str(base_dir / "templates"))
md = markdown2.Markdown(extras={"fenced-code-blocks": None})
max_cache_time = 31536000
long_cache_time = 1800
small_cache_time = 300

common_headers = {
    "host",
    "upgrade-insecure-requests",
    "referer",
    "accept",
    "accept-language",
    "accept-encoding",
    "connection",
    "user-agent",
    "dnt",
    "age",
    "allow",
    "cache-control",
    "vary",
    "via",
    "x-xss-protection",
    "forwarded",
    "content-length",
    "x-forwarded-for",
    "x-forwarded-proto",
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
    title: str = attr.ib()
    date: str = attr.ib()
    month: str = attr.ib()
    markdown_path: pathlib.Path = attr.ib()

    def render_html(self) -> str:
        with self.markdown_path.open(mode="r") as f:
            text = f.read()
            _, text = text.split("\n", 1)
        return render_template(
            "blog.html",
            blog_title=self.title,
            blog_published_date=self.date,
            blog_content=md.convert(text),
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


def load_blog_posts() -> typing.Dict[str, typing.List[BlogPost]]:
    """Loads all blog post metadata from the filesystem"""
    posts = {}
    dates = sorted(
        [x for x in markdown_dir.iterdir() if x.name != "drafts"],
        key=lambda x: [int(y.lstrip("0")) for y in x.name.split("-")],
        reverse=True,
    )
    for date in dates:
        markdown_path = list(date.iterdir())[0]
        with markdown_path.open(mode="r") as f:
            title = f.readline().strip("\n# ")
        bp = BlogPost(
            title=title,
            date=date.name,
            month=date.name.rsplit("-", 1)[0],
            markdown_path=markdown_path,
        )
        posts.setdefault(bp.month, []).append(bp)
    return posts


BLOG_POSTS = load_blog_posts()


@app.route("/robots.txt", methods=["GET"])
@cache_for(max_cache_time)
def robots_txt():
    resp = make_response("User-agent: *\nDisallow:")
    resp.headers["Content-Type"] = "text/plain"
    return resp


@app.route("/pgp", methods=["GET"])
@cache_for(long_cache_time)
def get_pgp():
    return render_template("pgp.html")


@app.route("/blog", methods=["GET"])
@cache_for(small_cache_time)
def list_blog_posts():
    return render_template("blog-posts.html", blog_posts=BLOG_POSTS)


@app.route("/blog/rss", methods=["GET"])
@app.route("/rss", methods=["GET"])
@app.route("/atom", methods=["GET"])
@app.route("/feed", methods=["GET"])
@cache_for(small_cache_time)
def rss_blog_posts():
    feed = AtomFeed(
        title="Python ♥ HTTP - Last 5 Blog Posts",
        feed_url=url_for("rss_blog_posts", _external=True),
        url=request.url_root,
    )
    total = 0
    for month, blog_posts in BLOG_POSTS.items():
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


@app.route("/blog/<string:date>/<string:blog_post>", methods=["GET"])
@cache_for(small_cache_time)
def get_blog_post(date: str, blog_post: str):
    markdown_file = (markdown_dir / date / (blog_post + ".md")).absolute()
    if date == ".." or blog_post == ".." or not markdown_file.is_file():
        return abort(404)
    with markdown_file.open(mode="r") as f:
        text = f.read()
        title, rest = text.split("\n", 1)
        title = title.lstrip("# ")
        html = md.convert(rest)

    return render_template(
        "blog.html", blog_title=title, blog_published_date=date, blog_content=html
    )


@app.route("/")
def index():
    return render_template("index.html", http_request=get_http_request())


@app.route("/favicon.ico", methods=["GET"])
@cache_for(long_cache_time)
def favicon():
    return send_file(str(static_dir / "favicon.ico"), mimetype="image/x-icon")


def get_http_request() -> str:
    """Generate the decorative HTTP request"""
    ua = user_agents.parse(request.headers.get("User-Agent", ""))
    headers = dict(request.headers)
    if "User-Agent" in headers:
        headers["User-Agent"] = str(ua)
    conn = h11.Connection(h11.CLIENT)
    data_to_send = conn.send(
        h11.Request(
            method=request.method.encode("utf-8"),
            target=b"/",
            headers=[
                (k.encode("utf-8"), v.encode("utf-8"))
                for k, v in headers.items()
                if k.lower() not in ("authorization", "cookie")
            ],
        )
    ) + conn.send(h11.EndOfMessage())
    lines = []
    for i, binary_line in enumerate(data_to_send.split(b"\r\n")):
        if binary_line:
            line = binary_line.decode("utf-8")
            if len(line) >= 50:
                line = line[:50] + "..."

            if i == 0:
                method, rest = line.split(" ", 1)
                line = f'<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/{method}">{method}</a> {rest}'
            else:
                header, rest = line.split(": ", 1)
                if header.lower() in common_headers:
                    line = f'<a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/{header.title()}">{header.title()}</a>: {rest}'
                else:
                    line = f"{header.title()}: {rest}"

            lines.append(line)
    return "\n".join(lines)
