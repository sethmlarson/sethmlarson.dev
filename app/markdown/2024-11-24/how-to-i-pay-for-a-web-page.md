# How do I pay for a web page?

Here's an unanswered question:

> I have money and I have a URL, how do I send money to the publisher of that URL?

URLs tell you where to get content on the web, but they don't tell you
anything about how to support the person who created the content.
This story might sound similar to paying open source maintainers,
where a user can almost abstract an entire project to a single download URL.

There are tons of people creating content for the web and plenty of ways to get
paid (Patreon, Kofi, GitHub Sponsors, YouTube Paid Membership),
but there's no *standardized* way to direct someone interested in paying for
the content of a page in the right direction.

We have HTML meta headers for many things, including where to find an RSS feed
or what my Fediverse handle is, but none for enumerating options to pay the creator of the content.
I wish I could click a button to easily send a "tip" to someone who created something I enjoy
or to browse other options for supporting them.

## Existing technology

### [Payment Request API](https://developer.mozilla.org/en-US/docs/Web/API/Payment_Request_API)

There are things like the web "Payment Request API" which gives you a JavaScript
API for generating a payment, but this doesn't fit my criteria.

For one: this means that every person creating content for the web needs to
add JavaScript to their page. This is a much higher bar than simply linking to existing payment methods
that a creator already likely uses to get paid. Being difficult means it's unlikely
for large numbers of people to do the work.

I also don't see being able to automate this because of the JavaScript.
Web creators likely have existing payment pages that they'd much rather link
out to instead of trying to handle payments themselves individually.

Lastly, this API exists and I don't see it being used by creators today.
That should say something about either its ease-of-use or return on investment
from potential supporters.

### Linking to payment methods in the page

Yeah, we could scrape the payment URLs we know about embedded in the page. But
there's a difference between potential URLs in the page due to non-creator
generated content (links in comments, etc) and whatever the "authoritative"
URLs are for paying the creator of the page. Being able to set `<meta>` tags
in `<head>` is typically a higher bar than setting arbitrary URLs in the `<body>`.

## What happens now?

I'm no stranger to standards, so maybe I do some research and
write a web standard proposal? Seems like fun! I'm imagining something like:

```html
<head>
    <!-- ... -->
    <meta property="financial-support" content="https://patreon.com/c/MatthewCarlson">
</head>
```

Because this is primarily for money, no doubt it will be abused to hell.
First-party browsers probably wouldn't do anything with this information
for the fear of legitimizing scammers' fake profiles.

The existence of the "Web Payments API" makes me think maybe it's not
a huge deal and that whenever money gets involved peoples' spidey-senses
start going off about whether a page is legitimate? Not sure.

Let me know what you think!