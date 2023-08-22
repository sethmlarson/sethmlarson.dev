# Reconciling API elegance and secure-by-design

> **NOTE:** I can only comment about the Python community as it’s the one I’m most involved in. I’m certain that much of this applies to other programming language communities as well.

Python developers love the language and its long list of packages for their elegance in API design. The phrase many use for this elegance is “Pythonic”. One hitch for this that the community has been experiencing recently is that this expectation of elegance can sometimes backfire in the face of malicious inputs or users who aren’t aware of the sharp edges on the tools they’re using.

Here are two occurrences I’ve observed:

* Python code with simple/minimal APIs are preferred by the community. Many packages/modules of vast complexity are exposed in a single-digit count of names/functions. These highly featureful APIs are expected to handle all valid inputs and produce corresponding outputs.
* Vulnerabilities will be reported for your project if your API isn’t secure by design, because it’s _possible_ to use insecurely.

**The two points are in contention for many Python projects.** You could argue that the second point could be waved away with a carefully crafted security policy or pointing fingers at users, but I think most would agree it’s preferable to preserve API design elegance for the 99% without compromising on security. 

If you’re representing a complicated or nuanced situation with an API, it is okay for the API design to be similarly complicated or require explicit configuration for the nuance. Here are some thoughts to keep in mind when designing an API:

* **Users should be making decisions where it matters.** Default to closed, not open, based on user intent. Don’t assume that users trust entities uniformly, assume users only trust an entity for the minimum required for the operation to succeed.
* **Surprises in API behavior are more likely to be security vulnerabilities**. If you didn’t expect a behavior, it’s likely that all of your users aren’t expecting it either. Expectations not matching intuition is a breeding ground for vulnerabilities. You may be able to use this as a justification for backwards incompatible changes if they are fixing security vulnerabilities.
* **Keep operations small, then think about enabling composition.** Don’t let an API grow to be “all-in-one” or opaquely chain together distinct operations. This increases the chance for the API to be misused or for new features to cross security boundaries.
* **Standards/RFCs/docs only tell you what, not how.** Standards and documentation rarely tell you how to design a secure API. Adding secure API design after the fact will likely lead to backwards incompatible changes (that might still be worth it!)
* **It’s okay to turn away complex feature requests to protect the majority of users.** Users that have rare or complicated use-cases of your project that might infringe on the security of your user-base should be carefully considered. We’ve seen these types of features on their own or in combination with other features cause unintended security issues. Saying no or pushing back on feature requests is always an option.
* **More projects need to be thinking about secure usage.** Many projects may not be considering security when designing their APIs either due to lack of time, resources, or belief that their project is security-critical. In reality, many projects are hooked up to a web backend somewhere and may be receiving malicious inputs. Being more resilient to malicious inputs would go a long way towards a more secure open source ecosystem.


## Elegant and secure-by-default design

Let’s dive into some concrete API design examples. URL parsing is one situation where I see this coming up frequently. The situation with URLs is incredibly frustrating due to there being multiple conflicting standards and users will raise issues against any implementation that doesn’t fit both standards (an impossible task, you’ll have to disappoint someone!)

Let’s do an exercise, imagine in your head what a URL looks like. I would be willing to bet that 90% or more of folks imagined something that looks like this:

	[https://example.com](https://example.com)

And unless you’ve had the misfortune of writing a URL parser I would be surprised if you imagined anything like this:

	“/../../../etc/passwd”

	“https://example.com#@evil.com”

	“example.com://evil.com”

	“https://” + &lt;10,000 “@” characters> + “[“

Any guesses which URLs attackers use for SSRF and which URLs your codebase might be okay with rejecting anyways? Attackers commonly exploit the differences between URL parsers, or where URLs are parsed and then later used. But there are **very few differences** between URL parsers and standards for the most basic URLs that everyone’s expecting (otherwise the web wouldn’t work very well).

What if our URL parser could only be used by default for the most basic cases but then you’d have to opt-in for the more complex cases?

# Raises an error, URL must be absolute.

urlparser.parse(“/../../../etc/passwd”)  

# You have to opt-in to relative URLs, this returns a separate result class:

urlparser.parse(“/../../../etc/passwd”, allow_relative_urls=True)

# Raises an error due to invalid path resolution

	urlparser.parse(“[https://example.com/../../../etc/passwd](https://example.com/../../../etc/passwd)”)

	# Opt-in to path resolution that isn’t valid.

	urlparser.parse(“[https://example.com/../../../etc/passwd](https://example.com/../../../etc/passwd)”, allow_invalid_path_resolution=True)

# Path resolution is enabled by default because it produces safer URLs.

	result = urlparser.parse(“[https://example.com/](https://example.com/../../../etc/passwd)a/../b”)

	print(result.path)  # “/b”

	# If you want to disable path resolution, that’s an option.

	result = urlparser.parse(“[https://example.com/](https://example.com/../../../etc/passwd)a/../b”, path_resolution=False)

	print(result.path)  # “/a/../b”

# Raises an error due to the authority section being too long. Means that regular expressions can’t be abused.

	URLParser.parse(“https://” + &lt;10,000 “@” characters> + “[“)

I can also imagine a scenario for HTTP clients. It’s common for HTTP clients in Python (like urllib3, requests, aiohttp, etc) to resolve HTTP redirects automatically, even cross-origin ones (after correctly stripping authentication, of course). This behavior is what browsers exhibit too so it can be natural to expect the same from your programmatic HTTP clients. But what if there was a way to respect privacy and safety while delivering a better experience

For example, privacy can be eroded due to this automatic following of redirects. If the URL “[https://example.com](https://example.com)” started redirecting to a third-party site (ie “[https://evil.com](https://evil.com)”), but then seamlessly redirected back to the actual content that was previously hosted at [https://example.com](https://example.com), your HTTP client wouldn’t report any issue (and neither would your browser…) but I don’t think that this default experience is the most safe even if it’s the one that requires the least amount of configuration to get right. People _could_ be disabling redirects or checking the redirections that occurred on the resulting HTTP response object, but 99% of people don’t, so the default configuration isn’t as secure against this change in redirection.

What would an HTTP client which defends against this look like? For starters, having redirects disabled by default would alert users to changes in redirects because the HTTP client would start returning “30X” status codes instead of “200”.

But what if the user wanted to then opt-in to redirects for this domain? We don’t want to blindly allow all redirects to occur, that would put us back right where we started. Instead, let’s maintain a list of origins/domains that we trust and provide that as configuration to the HTTP client:

httpcli.trust_origin(host=“good.com”)  # Default scheme and port

resp = httpcli.request(“GET”, “[https://example.com](https://example.com)”)  # Now if this request redirects to good.com the request succeeds but a redirect to evil.com would fail.


## What does this type of API design cost?

Nothing in this world is free, and the above set of recommendations and examples aren’t either.


## Why talking about security isn’t enough

Seeing the above points implemented into open source software doesn’t happen for free or by accident. It requires a working knowledge of security models and threats, user intent, and API design. This all requires expertise, time, and resources, all of which that open source developers are in short supply of.

Thanks to the sponsorship of OpenSSF Alpha-Omega I work at the Python Software Foundation full-time to multiply my impact across the Python ecosystem by developing and helping implement security best-practices for Python’s millions of users. Being a partnered lifter at Tidelift I get paid for my time maintaining security-critical software and to write and speak about open source security, sustainability, and maintainership.

None of this work would get done without financial support from these organizations, so I am hopeful to see further financial support towards open source for a more secure future for software.
