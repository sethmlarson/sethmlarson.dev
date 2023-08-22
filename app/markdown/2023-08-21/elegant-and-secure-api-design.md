# Reconciling elegance and secure-by-design in APIs

> I can only comment about the Python community as it's the one I'm most involved in, I'm certain that this applies to other programming language communities as well.

Python developers love the language and its long list of packages for their typically elegant API design. The phrase many use for this elegance is "Pythonic".
One downside for this that the community has been experiencing more recently is that this elegance can sometimes backfire on users who aren't aware of the
sharp edges on their tools and more specifically: malicious inputs.

Here are two things I've experienced:

* Python code with elegant/all-in-one APIs are preferred by the community. Many modules of vast complexity are exposed in a single-digit count of names. These feature-ful APIs are expected to handle all valid inputs and produce corresponding outputs.
* Vulnerabilities will be reported for your project if your API isn't secure by design, because it's _possible_ to use insecurely.

**These two points are in contention for many Python projects.** You could argue that the second point could be waved away with a carefully crafted security policy or placing more responsibility on users, but I think most would agree it's preferable to preserve API design elegance for the 99% without compromising on security. 

If you're representing a complicated or nuanced situation with an API, **it is okay for the API design to be similarly complicated or require explicit configuration for the nuance**. Here are some thoughts to keep in mind when designing an API:

* **Users should be making decisions where it matters.** Default to closed, not open, based on user intent. Don't assume that users trust entities uniformly, assume users only trust an entity for the minimum required for the operation to succeed.
* **Surprises in API behavior are more likely to be security vulnerabilities**. If you didn't expect a behavior, it's likely that all of your users aren't expecting it either. Expectations not matching intuition is a breeding ground for vulnerabilities. You may be able to use this as a justification for backwards incompatible changes if they are fixing security vulnerabilities.
* **Keep operations small, then think about enabling composition.** Don't let an API grow to be "all-in-one" or opaquely chain together distinct operations. This increases the chance for the API to be misused or for new features to cross security boundaries.
* **Standards/RFCs/docs only tell you what, not how.** Standards and documentation rarely tell you how to design a secure API. Adding secure API design after the fact will likely lead to backwards incompatible changes (that might still be worth it!)
* **It's okay to turn away complex feature requests to protect the majority of users.** Users that have rare or complicated use-cases of your project that might infringe on the security of your user-base should be carefully considered. We've seen these types of features on their own or in combination with other features cause unintended security issues. Saying no or pushing back on feature requests is always an option. If you decide to take on a complex new feature, make it opt-in instead of enabled by default.
* **More projects need to be thinking about secure usage.** Many projects may not be considering security when designing their APIs either due to lack of time, resources, or belief that their project isn't security-critical. In reality, many projects are hooked up to a web backend somewhere and may be receiving malicious inputs.

## Elegant and secure-by-default design?

Let's dive into some concrete API design examples. URL parsing is one situation where I see this coming up frequently. The situation with URLs is incredibly frustrating due to there being [multiple conflicting standards](https://daniel.haxx.se/blog/2022/09/08/http-http-http-http-http-http-http/) and users will raise issues against any implementation that doesn't fit _both standards_ (an impossible task, you'll have to disappoint someone!)

Let's do an exercise, imagine in your head what a URL looks like. I would be willing to bet that 90% or more of folks imagined something that looks like this:

```python
"https://example.com"
```

And unless you've had the misfortune of writing a URL parser I would be surprised if you imagined anything like this:

```python
"/../../../etc/passwd"

"https://example.com#@evil.com"

"example.com://evil.com"

"https://" + ("@" * 10_000) + "["
```

Any guesses which URLs attackers use for SSRF? Attackers commonly exploit the differences between URL parsers, or where URLs are parsed and then later used. But there are **very few differences** between URL parsers and standards for the most basic URLs that everyone's expecting (otherwise the web wouldn't work very well).

What if our URL parser could only be used by default for the most basic cases, but then you'd have to opt-in for the more complex cases?

```python
# Raises an error, URL must be absolute.
parse_url("/etc/passwd")  

# You have to opt-in to relative URLs:
parse_url("/etc/passwd",
          allow_relative_urls=True)


# Raises an error due to invalid path resolution
parse_url("https://example.com/../../../etc/passwd")

# Opt-in to path resolution that isn't valid.
parse_url("https://example.com/../../../etc/passwd",
          allow_invalid_path_resolution=True)

# Authentication in URLs doesn't matter if you're not using it.
# Raises an error due to authentication.
parse_url("https://example.com@evil.com")

# Opt-in if you need user authentication
parse_url("https://example.com@evil.com",
          allow_user_info=True)

# Path resolution is enabled by default because it
# produces safer URLs.
result = parse_url("https://example.com/a/../b")
print(result.path)  # "/b"

# If you want to disable path resolution, that's an option.
result = parse_url("https://example.com/a/../b",
                   path_resolution=False)
print(result.path)  # "/a/../b"

# Raises an error due to the authority section being
# too long. Means that regular expressions can't be abused.
parse_url("https://" + ("@" * 10_000) + "[")
```

I can also imagine a scenario for HTTP clients. It's common for HTTP clients in Python (like urllib3, requests, aiohttp, etc) to resolve HTTP redirects automatically, even cross-origin ones (after correctly stripping authentication, of course). This is the same behavior as browsers, so it can feel natural to expect the same from your programmatic HTTP clients. But what if there was a way to respect privacy and safety while delivering a similar experience for most users?

If the URL "[https://example.com](https://example.com)" started redirecting to a third-party site (ie "[https://evil.com](https://evil.com)"), but then seamlessly redirected back to the actual content that was previously hosted at [https://example.com](https://example.com), your HTTP client wouldn't report any issue (and neither would your browser…).

I don't think that this default experience is the safest even if it's the one that requires the least amount of configuration to be "correct". Users _could_ be disabling redirects or checking the redirections that occurred on the resulting HTTP response object, but 99% of people don't, so the default configuration isn't as secure against this change in redirection.

What would an HTTP client which protects against this look like? For starters, having redirects disabled by default would alert users to changes in redirects because the HTTP client would start returning "30X" status codes instead of "200". This is a great starting point!

But what if the user wanted to then opt-in to redirects for this domain? We don't want to blindly allow all redirects to occur, that would put us back right where we started. Instead, let's maintain a list of origins/domains that we trust and provide that as configuration to the HTTP client:

```python
# Tell the client we explicitly trust 'good.com', even if it's
# not being requested directly.
client.trust_origin(("https", "good.com", 443))

# We trust 'example.com' for this request, because it's
# been requested directly. If this request redirects to
# 'good.com' the redirect can proceed
# but a redirect to 'evil.com' would fail.
resp = client.request("GET", "https://example.com")
```

A single additional line of code, but now we're protected against a whole set of unwanted behaviors. Not bad!

## What does this type of API design cost?

Nothing in this world is free, and the above set of recommendations and examples aren't either.

Some of the above approaches don't adhere to an approximation of the **robustness principle** for API design, ie "being liberal in what you accept but conservative in what you output", but [there's a growing belief](https://www.ietf.org/archive/id/draft-iab-protocol-maintenance-05.html) that the robustness principle actively contributes to bad behavior of implementations and likely increases the vulnerable surface area of APIs.

Having stronger requirements for inputs also means code is **less resilient to external changes**. If a changed situation requires a new user decision to resolve safely that would require the calling code to fail, and likely in a way that isn't recoverable for that operation (unless you're setting your retry durations to similar magnitudes as your SLA…). When code is being used in the same project or for interfacing with internal services, this sort of resiliency doesn't matter and **should fail loudly**. The problem usually comes when interfacing with the external internet/services where you may not have a controlled or consistent environment.

**Adopting these approaches means that some users will have to write more code.** Another phenomenon I've experienced over my time as an open source maintainer is an occasional allergy to writing a few extra lines of code in order to be explicit. Some users may complain about needing to do this or try to offer up "helper" APIs to avoid needing to be explicit. If you've made it this far you'll need to hold strong. Feel free to link users to this blog post, I'm happy to be _the bad guy_. :)

Finally, developing secure APIs require a working knowledge of security models and threats, user intent, and API design. This all requires time and resources, both of which open source developers are in short supply of.

Thanks to the sponsorship of [OpenSSF Alpha-Omega](https://alpha-omega.dev/) and the [Python Software Foundation](https://www.python.org/psf-landing/) I work full-time on multiplying my impact across the Python ecosystem by developing and helping implement security best-practices. Being a partnered lifter at [Tidelift](https://tidelift.com/), I get paid for my time maintaining and improving security-critical software and to write about open source security, sustainability, and maintainership.

Without support from these organizations, lots of the work I and many others have done to make open source more secure would not have been possible. Even more support will be needed to shore-up the security for the long-tail of open source projects.
