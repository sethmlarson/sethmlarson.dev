import h11
import typing
from flask import Flask, request, Response


COLUMN_WIDTH = 45


app = Flask(__name__)


def flask_request():
    method = request.method.encode("ascii")
    headers = [
        (k.encode("utf-8"), v.encode("utf-8")) for k, v in request.headers.items()
    ]
    target = request.full_path.encode("ascii")
    if target == b"/?":
        target = b"/"
    return method, target, headers


def http_request() -> typing.List[str]:
    method, target, headers = flask_request()
    conn = h11.Connection(h11.CLIENT)
    data = conn.send(h11.Request(method=method, target=target, headers=headers))
    return prefix_all_lines("> ", data_decode(data))


def http_response(cl: str) -> typing.List[str]:
    conn = h11.Connection(h11.SERVER)
    conn.receive_data(b"HTTP/1.0\r\nhost: sethmlarson.dev\r\n\r\n")
    headers = []
    for key, value in response_headers(cl).items():
        headers.append((key.encode("ascii"), value.encode("ascii")))
    data = conn.send(
        h11.Response(status_code=418, reason=b"I'm a teapot", headers=headers)
    )
    return prefix_all_lines("< ", data_decode(data))


HEADERS = {
    "server": "sethmlarson.dev",
    "location": "Minneapolis, MN",
    "content-type": "text/plain; charset=utf-8",
    "connection": "close",
}
BODY = [
    "---------------------------------------------",
    "Hello! My name's Seth Michael Larson and I",
    "maintain a few Python open source libraries",
    "for HTTP and URLs. I'm passionate about",
    "networking, CI, code quality, data security, ",
    "and improving people's lives.",
    "---------------------------------------------",
    "Email:    sethmichaellarson@gmail.com",
    "Github:   https://github.com/sethmlarson",
    "Twitter:  https://twitter.com/sethmlarson",
    "Keybase:  https://keybase.io/sethmlarson",
    "GPG:      51B0 6736 1740 F5FC",
    "Slides:   https://speakerdeck.com/sethmlarson",
    "                           (",
    "            _           ) )   OSS libraries:",
    "         _,(_)._        ((    - urllib3",
    "    ___,(_______).        )   - httpx",
    "  ,'__.   /       \\    /\\_    - hstspreload",
    " /,' /  |''|       \\  /  /    - rfc3986",
    "| | |   |__|       |,'  /     - whatwg-url",
    " \\`.|                  /      - virtualbox",
    "  `. :           :    /       - selectors2",
    "    `.            :.,'        - psl",
    "      `-.________,-'          - irl",
    "",
    "(scan at a high angle, sorry mobile users!)",
    "███████ █ █ █████  █  ███████",
    "█     █  ████ █     █ █     █",
    "█ ███ █ ███  ██    █  █ ███ █",
    "█ ███ █ ███ ██████  █ █ ███ █",
    "█ ███ █ █  ██   ██ █  █ ███ █",
    "█     █   ██ ██ █ ███ █     █",
    "███████ █ █ █ █ █ █ █ ███████",
    "          █ █    ██ █        ",
    "████  █ █ █████  █  ██  ███ █",
    " ██ ██ █  █ █   ██ ██ █ █  ██",
    "  ██  ██ ████    █ >  █ ██ █ ",
    "   ███ █ ██  █  k   @ █ █   █",
    "███ █ █  ██ █ ██ G  █ +   █  ",
    " ██ ██  ██ ██   ██ ████  █ ██",
    " █  █ ██   █ ██ ██ ██ ███ ███",
    "█ █ █  ██ ██  █ █  █  █ ██   ",
    "█ █  ████ █ █  █  ████ █    █",
    " █  ██   ██  █     ██ ██ ██  ",
    "█   █ █ ██   █ ██ █ █   ██   ",
    "  █ █  ███ █   ████   ██ ██ █",
    " ███ ██  █   ██   █████████ █",
    "        █ █   █     █   █████",
    "███████  ██     █   █ █ █  █ ",
    "█     █    ██████   █   ██   ",
    "█ ███ █    █   ███  █████████",
    "█ ███ █ ██ █ ███   █ █      █",
    "█ ███ █ ██  █ █  █████ █ ██ █",
    "█     █ █   ██ ██   ██ █   █ ",
    "███████ ████    ██████ █ █ █ ",
    "",
    "Src: https://github.com/sethmlarson/website",
    "Teapot art credit: vlinders@rcl.wau.nl",
    "",
]


def data_decode(data: bytes) -> typing.List[str]:
    data = data.replace(b"\r", b"\\r").replace(b"\n", b"\\n").replace(b"\t", b"\\t")
    data = data.decode("utf-8")
    return fit_into_column(data)


def prefix_all_lines(prefix: str, lines: typing.List[str]) -> typing.List[str]:
    return [prefix + x for x in lines]


def fit_into_column(data: str) -> typing.List[str]:
    column = COLUMN_WIDTH - 2
    rows = []
    while len(data) > column:
        rows.append(data[:column])
        data = data[column:]
    if data:
        rows.append(data)
    return rows


def response_body(cl: str = None) -> str:
    if cl is None:
        cl = content_length()
    return "\n".join(http_request() + http_response(cl) + BODY)


def response_headers(cl: str = None):
    if cl is None:
        cl = content_length()
    headers = HEADERS.copy()
    headers["content-length"] = cl
    return headers


def content_length() -> str:
    cl = len(response_body(cl="9999").encode("utf-8"))
    if cl > 9999 or cl < 1000:
        raise ValueError()
    return str(cl)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path):
    resp = Response(response_body())
    resp.status_code = 418
    for key, value in response_headers().items():
        resp.headers[key] = value
    return resp
