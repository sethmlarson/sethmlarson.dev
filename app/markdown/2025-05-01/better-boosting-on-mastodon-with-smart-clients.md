# Better boosting on Mastodon with smart clients

If you've been on Mastodon for long enough it's likely you've heard the phrase <nobr>“you are the algorithm”</nobr> in reference to the fact that Mastodon by default doesn't provide algorithmic curation of your timeline. Instead, Mastodon implements a simple linear timeline and users are expected to "boost" posts so they reach a wider audience, specifically their own followers. I'll be calling Mastodon's approach "boost curation" in this post.

Don't get me wrong, I'm a fan of understandable systems and a [critic of algorithmic curation](https://sethmlarson.dev/for-you-is-not-for-me). I do wonder if Mastodon's allergy to algorithm curation does not play well for folks who have different expectations of social media, such as wanting more "town-square" moments [1] where a substantial number of users are talking about one or two topics that interest them all at once.

Here are some other downsides of boost curation compared to algorithmic curation:

* Boosts are only applied during your waking hours, meaning your followers in different timezones than you don't ever "benefit" from your curation.
* Boosts immediately put content to the top of feeds, meaning whatever you see during a given interaction with Mastodon is likely to be one or two people boosting tons of posts in succession rather than a blend of boosted posts and new posts from your followers.
* Boosts can mean that a post is seen more than once by a single person over the course of a day. This phenomenon might exacerbate the feeling of there being less content on Mastodon compared to other social media platforms.
* Once a post is no longer being boosted it almost immediately craters because everyone's feeds move on to new content. With algorithmic curation this post would have chances for "second-winds" by being offered to readers outside the linear timeline.

So what can be done about the above issues while maintaining a linear algorithm-less timeline?

## Breaking assumptions for smarter boosts

Many other networked systems have methods for clients to "collaborate" and achieve a goal that helps users without actually needing to know intimate details about other implementations (which is impossible in a diverse ecosystem of clients) or to share additional information between clients. An example that comes to mind here is the different [TCP congestion control algorithms](https://en.wikipedia.org/wiki/TCP_congestion_control) which collaborate to maximize bandwidth without needing to directly share information.

What if selecting "boost" in a Mastodon client didn't mean the post was reposted *immediately* to your followers, only that the post would be reposted *eventually* at the clients' discretion? To keep control in the users' hands, clients could offer an override to repost immediately, like a double-tap?

With this assumption broken, the client is now allowed to be "smart" by choosing the timing when the boost is applied to a post. The following simple logic could be implemented:

* If the post was created recently, wait for a bit to see if the post garners any other boosts. This is done because the post is likely already at the "top" of relevant feeds.
* If the post hadn't been boosted recently and the client hadn't boosted another post recently: boost the post. By only boosting one post at a time the client isn't clogging everyone's feeds with only boosts from a single account.
* If not, delay for some amount of time and reevaluate.

The above basic routine could be refined mostly by how the "delay" is calculated.
The delay could be a simple whole number or more complicated, like taking into account information about your followers or recent posts on the same topic. To avoid [thundering herds](https://en.wikipedia.org/wiki/Thundering_herd_problem) between like-minded clients this delay could be treated
almost like a "retry" where a random jitter is applied.

Are there any Mastodon clients that already implement something similar to this that I'm not aware of? What pitfalls or other choices could a client make to make this behavior better? Send me your thoughts on this topic or Mastodon in general.

> [1] Note that there are downsides to being a social media town-square, such as [context collapse](https://en.wikipedia.org/wiki/Context_collapse).
