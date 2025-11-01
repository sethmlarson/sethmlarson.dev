# RSS feed for new Nintendo Classics games

It's November! Many folks use this month to write
more, whether it's a [novel](https://nanowrimo.org) or [generating text](https://nanogenmo.github.io/).
I'm going to be trying to write and share more often, too.

So here's something I created for mostly me, but maybe you too.
I've [created a small RSS feed](https://github.com/sethmlarson/nintendo-classics) for new games being added to the
[Nintendo Classics collection](https://www.nintendo.com/us/online/nintendo-switch-online/classic-games/) over time. Nintendo uses this
collection as the drippiest-of-drip-feeds, so there's typically
only a few new games per month. So instead of checking
frequently I can follow this feed in my [feed reader](https://inoreader.com)
and be notified on new releases.

<!-- more -->

I thought this was interesting for a few reasons, one I implemented
“[Oxford commas](https://en.wikipedia.org/wiki/Serial_comma)” when joining a `list[str]` using f-strings like so, split apart for easier reading:

```python
def oxford_comma(x: list[str]) -> str:
    return (
        f"{', '.join(x[:-1])}"
        f"{',' if len(x) >= 3 else ''}" # Oxford comma!
        f"{' and ' if len(x) >= 2 else ''}"
        f"{x[-1]}"  # Last or only element.
    )
```

I'm sure this could be done in less space somehow, if you're able
to code-golf this smaller please [send me your code](mailto:sethmichaellarson@gmail.com) :)

Second interesting thing about the RSS feed is there's only one `<item>` or entry
in the feed at any one time. I suppose I could have implemented the latest N new groups
of releases, but I felt that wouldn't be useful for me who was already caught up
on what has been released in the past month or so.

Unsurprisingly, my feed reader had no issue with a single entry feed on the first crawl, but I've never
seen this in the wild so it'll be interesting to see how the reader reacts to
a new entry replacing the old one.
