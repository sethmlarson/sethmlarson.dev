# How many RSS subscribers do I have?

RSS is super rad way to consume internet content (“[like a newspaper](https://www.citationneeded.news/curate-with-rss)”). This blog gets [syndicated](https://indieweb.org/POSSE) via RSS and an email newsletter. Unlike with my newsletter, it's not clear how many
people are reading my blog using RSS compared to
my newsletter. That's a good thing, privacy is important and I don't *need* to know who you are to enjoy my blog :)

But what if I was interested in a rough number of subscribers to the RSS feed?
<!-- more -->
Turns out RSS feed scrapers sometimes include the number of subscribers in their `User-Agent` HTTP header. Like this:

```
User-Agent: Feedly/1.0 (poller; 131 subscribers;)
```

Multiple RSS reader scrapers do this, including Inoreader, Feedly, Feedbin, Newsblur, Old Reader, and a few more.
So if I download the access logs for my RSS feed URLs I can approximate the number
of readers using this Python script:

```python
import re

# Assuming you can parse a list of 'User-Agents'
# from your logs: put them here.
user_agents = [...]

subs_re = re.compile(r"([0-9]+)\s+subscribers?")
subs_per_feed = {}
for user_agent in user_agents:
    # Count subscribers and deduplicate feeds
    # by the remaining text in 'User-Agent':
    subs = int(subs_re.search(user_agent).group(1))
    feed_id = re.sub(subs_re, "", user_agent)
    subs_per_feed[feed_id] = max(subs_per_feed.get(feed_id, 0), subs)

print(subs_per_feed)
print(sum(subs_per_feed.values()))
```

For my own RSS feed this gives a value of `257` known RSS subscribers. <br> [Thanks for reading via RSS](http://sethmlarson.dev/feed)! 👋
