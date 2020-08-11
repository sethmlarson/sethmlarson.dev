# API Design for Optional Async Context Managed Resources

I had a [discussion on Twitter](https://twitter.com/zzzeek/status/1292831225586028544)
with Mike Bayer, author of SQLAlchemy, about API design regarding async functions that return a resource to optionally be used
as a async context manager. I wanted to do a quick write-up so the results of the discussion
wouldn't be lost to the Twitter aether. Here we go:

Take the Python function [`open()`](https://docs.python.org/3/library/functions.html#open). The function can be used in multiple ways:

```python
# Without a context manager,
# requires an explicit close():
f = open("file.txt")
f.read()
f.close()

# As a context manager, file is
# closed in __exit__():
with open("file.txt") as f:
    f.read()
```

Now what if we wanted the above but to be asynchronous?
What if we wanted to write an async function (named `async_open()`) which
has the same behavior as `open()` above but is all async?

First let's start with the "without async context manager" case:

```python
f = await async_open("file.txt")
```

Seems straightforward enough. All the async magic would be within
the function itself. Now what if we wanted to add the async context manager case?

An API which returns an async context manager is typically a synchronous
function itself so you don't have to write the following:

```python
async with (await async_open("file.txt")) as f:
    ...
```

The above API in my opinion looks clunky to use. You may already see
the problem between the two code samples above. We want `async_open` to
be both asynchronous and synchronous to fit both usages. Oh no!

The big question is where do we put the async code that happens
either when `await` is used or when `async with` is used without
the user signalling which will be used.

After a little bit of thinking I landed on the following:

```python
class AsyncFile:
    """The object that has all the file object
    methods like read() and close() but async!
    """
    async def read(self):
        print("read()")

    async def close(self):
        print("close()")


class AwaitOrAenter:
    """The special object that handles either
    an __await__() call for the non-context
    managed case or an __aenter__() call for
    the context managed case.
    """
    def __init__(self, filepath):
        self._filepath = filepath
        self._file = None

    async def _async_open(self):
        # ( Async magic and open an AsyncFile )
        self._file = AsyncFile()
        return self._file

    def __await__(self):
        return self._async_open().__await__()

    async def __aenter__(self):
        return await self._async_open()

    async def __aexit__(self, *_):
        await self._file.close()


def async_open(filepath):
    return AwaitOrAenter(filepath)
```

The above API can now be used in both of these cases:

```python
f = await async_open("file.txt")
await f.read()
await f.close()

async with async_open("file.txt") as f:
    await f.read()
```

Looks like the API works as intended! 🥳
