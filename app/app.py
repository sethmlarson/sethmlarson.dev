import h11
import pathlib
import markdown2
from flask import Flask, render_template, request
import user_agents
import attr
import typing


base_dir = pathlib.Path(__file__).absolute().parent
markdown_dir = base_dir / "markdown"
app = Flask(__name__, template_folder=str(base_dir / "templates"))
md = markdown2.Markdown(extras={"fenced-code-blocks": None})

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
}


@attr.s
class BlogPost:
    title: str = attr.ib()
    date: str = attr.ib()
    month: str = attr.ib()
    markdown_path: pathlib.Path = attr.ib()


def load_blog_posts() -> typing.Dict[str, typing.List[BlogPost]]:
    """Loads all blog post metadata from the filesystem"""
    posts = {}
    dates = sorted(
        [x for x in markdown_dir.iterdir()],
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


@app.route("/pgp", methods=["GET"])
def get_pgp():
    return render_template("pgp.html")


@app.route("/blog", methods=["GET"])
def list_blog_posts():
    return render_template("blog-posts.html", blog_posts=BLOG_POSTS)


@app.route("/blog/<string:date>/<string:blog_post>", methods=["GET"])
def get_blog_post(date: str, blog_post: str):
    markdown_file = (markdown_dir / date / (blog_post + ".md")).absolute()
    if date == ".." or blog_post == ".." or not markdown_file.is_file():
        return 404
    with markdown_file.open(mode="r") as f:
        text = f.read()
        title, rest = text.split("\n", 1)
        title = title.lstrip("# ")
        html = md.convert(rest)

    return render_template(
        "blog.html", blog_title=title, blog_published_date=date, blog_content=html
    )


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path: str):
    return render_template("index.html", http_request=get_http_request())


def get_http_request() -> str:
    """Generate the decorative HTTP request"""
    ua = user_agents.parse(request.headers.get("User-Agent", ""))
    headers = dict(request.headers)
    if "User-Agent" in headers:
        headers["User-Agent"] = str(ua)
    conn = h11.Connection(h11.CLIENT)
    target = request.full_path.encode("utf-8")
    if target.endswith(b"?"):
        target = target[:-1]
    data_to_send = conn.send(
        h11.Request(
            method=request.method.encode("utf-8"),
            target=target,
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
