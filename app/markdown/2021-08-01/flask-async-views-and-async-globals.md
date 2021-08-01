# The problem with Flask async views and async globals

Starting in v2.0 [Flask has added async views](https://flask.palletsprojects.com/en/2.0.x/async-await)
which allow using `async` and `await` within a view function. This allows you to use other async
APIs when building a web application with Flask.

If you're planning on using Flask's async views there's a consideration to be aware of for using
globally defined API clients or fixtures that are async.

## Creating an async Flask application

In this example we're using the [async Elasticsearch Python client](https://elasticsearch-py.readthedocs.io/en/latest/async.html)
as our global fixture. We initialize a simple Flask application with a single
async view that makes a request with the async Elasticsearch client:

```python
# app.py
from flask import Flask, jsonify
from elasticsearch import AsyncElasticsearch

app = Flask(__name__)

# Create the AsyncElasticsearch instance in the global scope.
es = AsyncElasticsearch(
    "https://localhost:9200",
    api_key="..."
)

@app.route("/", methods=["GET"])
async def async_view():
    return jsonify(**(await es.info()))
```

Running with `gunicorn` via `$gunicorn app:app` and then visiting the app via `http://localhost:8000`.
After the first request everything looks fine:

```json
{
  "cluster_name": "d31d9d6abb334a398210484d7ac8567b",
  "cluster_uuid": "K5uyniiMT9u2grNBmsSt_Q",
  "name": "instance-0000000001",
  "tagline": "You Know, for Search",
  "version": {
    "build_date": "2021-04-20T20:56:39.040728659Z",
    "build_flavor": "default",
    "build_hash": "3186837139b9c6b6d23c3200870651f10d3343b7",
    "build_snapshot": false,
    "build_type": "docker",
    "lucene_version": "8.8.0",
    "minimum_index_compatibility_version": "6.0.0-beta1",
    "minimum_wire_compatibility_version": "6.8.0",
    "number": "7.13.1"
  }
}
```

However when you refresh the page to send a second request you receive
an `InternalError` and the following traceback: 

```
Traceback (most recent call last):
  ...
  File "/app/app.py", line 13, in async_route
    return jsonify(**(await es.info()))
  File "/app/venv/lib/.../elasticsearch/_async/client/__init__.py", line 288, in info
    return await self.transport.perform_request(
  File "/app/venv/lib/.../elasticsearch/_async/transport.py", line 327, in perform_request
    raise e
  File "/app/venv/lib/.../elasticsearch/_async/transport.py", line 296, in perform_request
    status, headers, data = await connection.perform_request(
  File "/app/venv/lib/.../elasticsearch/_async/http_aiohttp.py", line 312, in perform_request
    raise ConnectionError("N/A", str(e), e)

ConnectionError(Event loop is closed) caused by:
  RuntimeError(Event loop is closed)
```

## Why is this happening?

The error message mentions the event loop is closed, huh? To understand why this is happening you
need to know how `AsyncElasticsearch` is implemented and how async views in Flask work.

### No global event loops

Async code relies on something called an event loop. So any code using `async` or `await` can't execute
without an event loop that is "running". The unfortunate thing is that there's no running event
loop right when you start Python (ie, the global scope).

This is why you can't have code that looks like this:

```python
async def f():
    print("I'm async!")

# Can't do this!
await f()
```

instead you have to use `asyncio.run()` and typically an `async` main/entrypoint function to use `await` like so:

```python
import asyncio

async def f():
    print("I'm async!")

async def main():
    await f()

# asyncio starts an event loop here:
asyncio.run(main())
```

(There's an exception to this via `python -m asyncio` / `IPython`, but really this is running the REPL after starting an event loop)

So if you need an event loop to run any async code, how can you define an
`AsyncElasticsearch` instance in the global scope?

### How AsyncElasticsearch allows global definitions

The magic of global definitions for `AsyncElasticsearch` is delaying the full initialization
of calling `asyncio.get_running_loop()`, creating `aiohttp.Session`, sniffing, etc
until after we've received our first `async` call. Once an `async` call is made
we can almost guarantee that there's a running event loop, because if there
wasn't a running event loop the request wouldn't work out anyways.

This is great for async programs especially, as typically a single event loop gets
used throughout a single execution of the program and means you can create your `AsyncElasticsearch`
instance in the global scope how users create their synchronous `Elasticsearch` client in the global scope.

Using multiple event loops is tricky and would likely break many other libraries like `aiohttp`
in the process for no (?) benefit, so we don't support this configuration. Now
how does this break when used with Flask's new async views?

### New event loop per async request

The simple explanation is that Flask uses WSGI to service HTTP requests and responses which
doesn't support asynchronous I/O. Asynchronous code requires a running event loop to execute, so Flask
needs to get a running event loop from somewhere in order to execute an async view.

To do so, Flask will create a new event loop and start running the view within this new event loop
for every execution of the async view. This means all the async and await calls within the view
will see the same event loop, but any other request before or after this view will see a different event loop.

The trouble comes when you want to use async fixtures that are in the global scope, which in my
experience is common in small to medium Flask applications. Very unfortunate situation! So what can we do?

## Fixing the problem

The problem isn't with Flask or the Python Elasticsearch client, the problem is the incompatibility between WSGI
and async globals. There are a couple of solutions, both of which involve [Async Server Gateway Interface (ASGI)](https://asgi.readthedocs.io),
WSGI's async-flavored cousin which was designed with async programs in mind.

### Use an ASGI framework and server

One way to avoid the problem with WSGI completely is to simply use a native ASGI web application framework instead.
There are a handful of popular and widely used ASGI frameworks you can choose from:

If you're looking for an experience that's very similar to Flask you can use [Quart](https://pgjones.gitlab.io/quart)
which is inspired by Flask. Quart even has a [guide about how to migrate from a Flask
application to using Quart](https://pgjones.gitlab.io/quart/how_to_guides/flask_migration.html)!
Flask's own documentation for async views actually [recommends using Quart](https://flask.palletsprojects.com/en/2.0.x/async-await/#when-to-use-quart-instead)
in some cases due to the performance hit from using a new event loop per request.

If you're looking to learn something new you can check out [FastAPI](https://fastapi.tiangolo.com)
which includes a bunch of builtin functionality for documenting APIs, strict model declarations,
and data validation.

Something to keep in mind when developing an ASGI application is you need an [ASGI-compatible server](https://asgi.readthedocs.io/en/latest/implementations.html#servers).
Common choices include [Uvicorn](https://www.uvicorn.org), [Hypercorn](https://pgjones.gitlab.io/hypercorn/index.html), and [Daphne](http://github.com/django/daphne).
Another option is to use the [Gunicorn](http://gunicorn.org) with [Uvicorn workers](https://www.uvicorn.org/#running-with-gunicorn).

All the options mentioned above function pretty similarly so pick whichever one you like.
My personal choice has historically been Gunicorn with Uvicorn workers because of how widely used and
mature Gunicorn relative to how new the other libraries are.

You can do so like this:

```
$ gunicorn app:app -k uvicorn.workers.UvicornWorker
```

### Use WsgiToAsgi from asgiref

If you really love Flask and want to continue using it you can also use
the [asgiref](https://github.com/django/asgiref) package provides an easy wrapper
called `WsgiToAsgi` that converts a WSGI application to an ASGI application.

```python
from flask import Flask, jsonify
from elasticsearch import AsyncElasticsearch

# Same definition as above...
wsgi_app = Flask(__name__)
es = AsyncElasticsearch(
    "https://localhost:9200",
    api_key="..."
)

@wsgi_app.route("/", methods=["GET"])
async def async_view():
    return jsonify(**(await es.info()))

# Convert the WSGI application to ASGI
from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(wsgi_app)
```

In this example we're converting the WSGI application `wsgi_app` into an ASGI application `asgi_app`
which means when we run the application a single event loop will be used for every request
instead of a new event loop per request.

This approach will still require you to use an ASGI-compatible server.
