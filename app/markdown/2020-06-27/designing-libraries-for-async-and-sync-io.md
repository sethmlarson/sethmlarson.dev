# Designing Libraries for Async and Sync I/O

I wanted to publish this blog post as an extension of my PyCon 2020 poster
of the same name with more information than I could fit in the poster.

I've also recently completed a migration of the
[Elasticsearch client library](https://github.com/elastic/elasticsearch-py)
to [support both sync and async I/O](https://elasticsearch-py.readthedocs.io/en/master/async.html)
using some of these techniques.

I hope that my findings will help you on your own journeys :)

## Setting the Stage

At PyCon 2016 there was a talk named “Building Protocol Libraries The Right Way”
by Cory Benfield that laid out how protocol libraries can be reusable across
projects, more easily verified, and work with both asynchronous and synchronous
I/O by following the sans-I/O design pattern.

Since that talk there have been many protocol implementations using this principle
including HTTP/1.1, 2 and 3, WebSockets, and more. Now that the protocol libraries
are here let’s start developing libraries designed for async and sync I/O!

## Problems You May Run Into

On the way towards supporting sync and async here is a list of problems
that most projects will run into:

- Don’t want API differences between async and sync or to maintain two
  code-bases of similar code.
- Properties and constructors must be synchronous.
- Supporting multiple async libraries is a lot of work.
- Async functions are different from sync standard library functions.
- Classes may be instantiated without a running event loop.

### Figure out where I/O Happens in your API

The first steps are to figure out which parts of your API need
to handle I/O and what that means for the rest of your API.
Any function that handles I/O all the way down the chain will need
to be async. Explore library structure without putting too much work
into filling in details. Make sure that the types of your API match
up with how users would have to interact with the library, think about
async context managers and generators.

### Async not compatible with Constructors or Properties

When you’re designing your API most functions can be async without issue,
however there is one important one that can’t be: `__init__()`. This can
cause problems when you have to call an async function as a part of setup.
A way around this is a factory function that can be async or delaying any
setup that requires async until after you're guaranteed to have an active
event loop (like within an async function).

The issue is even trickier because if your API is meant to be instantiated
within the global scope, for example to be used as a client within a web service.
Then you can’t make any async calls on instantiation because you won’t have an active
event loop.

```python
from fastapi import FastAPI
from elasticsearch import AsyncElasticsearch

app = FastAPI()

# Most users will want to define their APIs in the
# global scope where there isn't a running event loop ...
es = AsyncElasticsearch()

@app.get("/")
async def index():
    # ... so we can delay our async setup until an
    # async function called for the first time.
    resp = await es.search(...)
```

Using @property is also sync-only and so should either be converted to a
function or design your API such that all results are awaited /
populated before using properties.

## Useful Libraries for Async + Sync Support

Each library solves one of two problems:

- Support both async and sync in the same codebase
- Support multiple async libraries (Asyncio, Trio)

If you’d like to view a simple project using all of these tools together
I have created one on GitHub.

### Unasync

[Unasync](https://github.com/python-trio/unasync/)
is a library that tokenizes your Python code, transforms tokens for
async code into their synchronous counterparts, and then re-renders the new
synchronous code into a corresponding file.

See the code examples on the right for some of the tokens that unasync transforms:

```python
# Classed prefixed with 'AsyncX...' are helpfully
# renamed to 'SyncX...' for simpler imports.
class AsyncClass: ...   # -> class SyncClass: ...

# async/await is handled by removing the
# async and await keywords.
async def f(): ...              # -> def f(): ...
ret = await f()                 # -> ret = f()

# Async context managers are transformed
# into regular context managers.
async with ctx(): ...           # with ctx(): ...
async def __aenter__(): ...     # def __enter__(): ...
async def __aexit__(*_): ...    # def __exit__(*_): ...

# Async iterators are transformed into
# regular iterators.
await x.__aiter__()             # -> x.__iter__()
await iter.__anext__()          # -> iter.__next__()
async for x in y: ...           # -> for x in y: ...
StopAsyncIteration              # -> StopIteration

# Typing annotations, notice unasync also
# handles forward annotations within strings.
def f(): -> "AsyncClass": ...   # -> def f() -> "SyncClass": ...
typing.AsyncIterator            # -> typing.Iterator
typing.AsyncGenerator           # -> typing.Generator
typing.AsyncIterable            # -> typing.Iterable

# There are some async statements that don't
# have a direct sync counterpart so unasync
# can't do anything with them.
async def __await__(): ...      # -> ???
```

After adding support for both sync and async the next step is supporting
multiple async libraries. The libraries commonly used in the Python community
are asyncio, Trio, Twisted, and Curio.

Supporting all of these is a challenge but can be made easier with
the following two libraries:

### Sniffio

[Sniffio](https://github.com/python-trio/sniffio)
is a library that can detect which async library your code is running under.
The package can detect asyncio, Trio, and Curio. By detecting which library is
running you then know which library-specific APIs can be used safely.

This also means you can lazily import ‘trio’ only when Trio is detected as the
current async library. No need to make Trio a direct dependency.

```python
import sniffio

try:
    # Detect the current async library
    async_lib = sniffio.current_async_library()

    # Lazily-load so users don't need 'trio'
    # installed to use 'asyncio'.
    if async_lib == "asyncio":
        import asyncio
        # <asyncio-specific code>
    elif async_lib == "trio":
        import trio
        # <trio-specific code>
    else:
        raise RuntimeError(
            f"Unsupported async library: {async_lib!r}"
        )
except sniffio.AsyncLibraryNotFoundError:
    raise RuntimeError(
        "Couldn't detect async library"
    ) from None
```

A pattern I’ve found useful is to group all library-specific code into one file
each that all have an identical API. That way you can call sniffio’s detection
one time and know which set of APIs should be used for the duration of the program.

### AnyIO

[AnyIO](https://github.com/agronholm/anyio)
is a library that provides a single interface that can be used
interchangeably from asyncio, Trio, and Curio programs.

For most projects trying to support multiple async libraries this
should be your first stop.

The interfaces that are provided include:

- Structured Concurrency Primitives
- Synchronization Primitives
- Networking (TCP / TLS / UDP)
- Asynchronous File I/O
- Signals and Threads

```python
import anyio

# Task Groups
async with anyio.create_task_group() as group:
    async def f(x):
        await anyio.sleep(x)
    for x in range(10):
        await group.spawn(f, x)

# Timeouts
async with anyio.move_on_after(1):
    # Operation will be cancelled
    # if it takes longer than 1 second.

# Cancellation
async with anyio.open_cancel_scope() as cancel_scope:
    stuff_that_can_be_cancelled()
if cancel_scope.cancel_called:
    ... # Cancellation handling

# Synchronization primitives
anyio.create_lock()
anyio.create_queue()
anyio.create_capacity_limiter()
anyio.create_event()
anyio.create_condition()

# Networking: TCP, TLS, UDP
sock = await anyio.connect_tcp()
await sock.start_tls()

sock = await anyio.create_udp_socket()
await sock.send()
await sock.receive()
```

AnyIO also provides its own pytest plugin ‘pytest-anyio’ that makes
writing test cases for multiple async libraries a breeze.

AnyIO uses Sniffio under the hood to detect which async library is being
used and provide the correct implementation.

You can read AnyIO’s documentation for a list of all features and usages.

