# Working on urllib3 full-time for one week

The week of November 7th to the 11th, 2022 [Quentin Pradet](https://quentin.pradet.me) and I took time off of our regular day jobs at Elastic to work full-time on urllib3 v2.0. If you enjoy this article [Quentin also wrote about his experience](https://quentin.pradet.me/blog/i-got-paid-to-work-on-open-source-3.html).

We decided to do this for multiple reasons, the biggest being that v2.0 development had
stalled due to a lack of reviewer time to push community PRs across the finish line and a
lack of contiguous time to work on the more difficult remaining tasks on v2.0.

Taking a week together also meant we'd be able to review PRs and discuss roadblocks throughout the
week without the chance of life getting in the way for reviewers (as it tends to do). This made for a super enjoyable week of
open source development that you can't really replicate outside in-person sprints at conferences.

Without the generous support we receive from sponsors like [Spotify](https://engineering.atspotify.com/2022/06/say-hello-to-the-recipients-of-the-2022-spotify-foss-fund/) we wouldn't be able to
accomplish everything we did in the span of months, let alone a week. Thanks to everyone who supports our project!

## What I accomplished in a week

Going into the week Quentin and I had the goal of completing all the tasks necessary to release the first
alpha of urllib3 v2.0. We split up the tasks, so we could work concurrently and coordinated a time each day
to discuss and review each other's work from the previous day.

These were the three tasks I wanted to complete during the week:

- [Create BaseHTTPConnection APIs](https://github.com/urllib3/urllib3/issues/1985)
- [Write a Migration Guide for v1.26.x -> v2.0.0](https://github.com/urllib3/urllib3/issues/1973)
- Prepare for the first v2.0 alpha release

## BaseHTTPConnection API

The first task in the list we knew was going to be a large one due to how complicated the existing HTTPConnection API was
due to being a subclass of the standard library [`http.client.HTTPConnection` class](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection).
The task was to design the API, so it could be extended in the future to support other HTTP implementations beyond the one provided by the standard library.

This work was a follow-up to the [community-contributed pull request](https://github.com/urllib3/urllib3/pull/2649) to make the urllib3's `HTTPConnection.getresponse()` method return an instance of `urllib3.HTTPResponse`
instead of an `http.client.HTTPResponse`. Previously the `urllib3.HTTPConnectionPool` class would transform the standard library response class into
our own response class but that tied our own connection class very strongly to the standard library. Thanks to [@shadycuz](https://github.com/shadycuz) for contributing this change.

Breaking down the task into pieces I was left with the following items to complete:

- Enumerate all the ways the existing connection API was being used.
  so that future maintainers have to do less work understanding the architecture.
- Determine which access patterns expose internal APIs and thus shouldn't be allowed. 
- For each disallowed access pattern created a suitable alternative
- Create a `BaseHTTPConnection` and `BaseHTTPSConnection` protocols which can be used for type-hinting our `HTTPConnectionPool` classes.

The full set of changes [were made in this pull request](https://github.com/urllib3/urllib3/pull/2768).

### Enumerating existing HTTPConnection usage

This involved looking at `HTTPConnectionPool`, `HTTPResponse`, and our retries and utility functions. 
I documented many of my findings over the first day in a `notes/` directory. Information on the
`HTTPConnection` lifecycle can be [found in this document](https://github.com/urllib3/urllib3/blob/main/notes/connection-lifecycle.md).

I decided to make the following changes to not limit future development of urllib3:

- Removing accesses to `HTTPConnection.sock` for the inner `socket.socket` instance.
  to check whether the connection was alive, setting timeouts, etc.
- Removing extraneous methods and properties like `HTTPSConnection.set_cert()`, `HTTPSConnection.tls_in_tls_required`
- Removing methods that were only in place because of removed methods above like `HTTPSConnectionPool._prepare_conn()` which only existed to call `HTTPSConnection.set_cert()`.
- Adding `preload_content` and `decode_content` parameters explicitly to the `HTTPConnection.request()` method instead of
  using `**kwargs`.

### Creating the BaseHTTPConnection API

We have already been bitten hard by subclassing the standard library `http.client.HTTPConnection` library so we knew we didn't want to make the same mistake there again. You can read [Hynek's excellent article on subclassing, composition, and structural typing](https://hynek.me/articles/python-subclassing-redux) to learn more. Highly recommended to all Pythonistas!

Instead I opted to use the new `typing.Protocol` feature to define the structural type which the `urllib3.HTTPConnection` and `HTTPSConnection` classes then implement. We can then change all type hints on `HTTPConnectionPool` classes to use the `BaseHTTPConnection` protocol instead of `HTTPConnection` to ensure none of the APIs being accessed are private or leaking from the parent class.

The `typing.Protocol` feature is only available in Python 3.8 and later, but I didn't want to wait for that version to be our earliest supported version ([Python 3.7 still has ~6 months of support left](https://endoflife.date/python)) so I used `typing_extensions` and optional type hints to not cause issues for Python 3.7.

You can see the entire definition of the `BaseHTTPConnection` protocols [in this file](https://github.com/urllib3/urllib3/blob/main/src/urllib3/_base_connection.py).

### Changing default timeout sentinel

We currently use the "final enum value as typed sentinel" trick in order to represent the concept of a "default" timeout (ie `socket.getdefaulttimeout()`). It looked something like this previously:

```python
import enum
import typing

class DEFAULT_TIMEOUT_TYPE(enum.Enum):
    token = 0

DEFAULT_TIMEOUT: typing.Final[DEFAULT_TIMEOUT_TYPE] = DEFAULT_TIMEOUT_TYPE.token
TYPE_TIMEOUT = float | None | DEFAULT_TIMEOUT

def request(..., timeout: TYPE_TIMEOUT = DEFAULT_TIMEOUT):
    ...
```

Eventually on the `HTTPConnection` layer the `timeout` value will either be passed to `socket.settimeout()` if it's a `float` or `None` or if the value isn't given by the user the connection will use the configured default timeout via `socket.getdefaulttimeout()`. Can you imagine a scenario where the above logic might go wrong?

I ran into the problem while modifying the way `HTTPConnection` instances manage and update their socket's timeout value. If you run the following code there is no error:

```python
sock = socket.create_connection(...)
sock.settimeout(DEFAULT_TIMEOUT)  # There is no error here, the value is 0!
```

Now our socket has a timeout value of `0` instead of the value of `socket.getdefaulttimeout()`. Luckily this mistake was caught in tons of places throughout our test suite, but in addition to fixing the problem where our default timeout sentinel was getting set directly to the socket timeout I wanted to do one better and make this situation raise an error instead of silently moving on.

Looking at the [`socket.settimeout()` documentation](https://docs.python.org/3/library/socket.html#socket.socket.settimeout) it says: "**The value argument can be a nonnegative floating point number expressing seconds, or `None`**" Non-negative values aren't valid timeout values so we can change the sentinel's `token` value to be `-1` to receive an error instead of the socket silently accepting our default timeout sentinel value:

```python
class DEFAULT_TIMEOUT_TYPE(enum.Enum):
    token = -1  # This value was changed to -1

...

# Now setting the sentinel value directly in settimeout() raises an error.
>>> sock = socket.create_connection(...)
>>> sock.settimeout(DEFAULT_TIMEOUT)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Timeout value out of range
```

This change improves nothing for end-users because the behavior is the same, however it makes our timeout code more robust to future changes now that a situation we never want to occur raises an error instead of being silently accepted.

## Migration guide for v2.0

Creating the migration guide from v1.26.x to v2.0.0 involved combing through all of the changes to v2.0 which was much easier thanks to our use of a "newsfragment" changelog. The migration guide covered the following:

- Timeline for releases and the removal of deprecated changes
- Listing the most important changes that all developers should be aware of (removals, deprecations, changes to defaults).
- Write about how different users of urllib3 should migrate to v2.0. We wrote separate guides for dependent package maintainers and application developers.
- Affirming our continued support of the 1.26.x release stream for security fixes thanks to [financial support from Tidelift](https://tidelift.com/subscription/pkg/pypi-urllib3).
- Showing off all the new features!

You can read the [v2.0 migration guide on Readthedocs](https://urllib3.readthedocs.io/en/latest/v2-migration-guide.html#migrating-from-1-x-to-2-0).

## Prepare for the first v2.0 alpha release

This task was mostly curating the user-facing changelog that would go along with v2.0.0a1. This required reading through [~55 newsfragments](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) many of which contained multiple user-facing changes, and putting that into the "[Keep a Changelog](https://keepachangelog.com)" format that the urllib3 project uses today.

This alpha release was uploaded to PyPI on November 15th instead of on Friday or the weekend to allow developers to react to the new major version in case we broke builds somehow.

## Closing thoughts

As Quentin and I have both written about multiple times by now, getting paid to work on open source feels great for maintainers to have rare dedicated time to focus on a project and move mountains relative to the slow drip (or more often than not: **absence!**) of time that is normally allocated to open source work.
