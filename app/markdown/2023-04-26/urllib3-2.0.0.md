# urllib3 v2.0.0 is now generally available

urllib3 v1.0 was first published 12 years ago in 2011 and has served the Python community beyond anyone's dreams.
Since that time, urllib3 has been installed [over 8 billion times](https://pepy.tech/project/urllib3) to become the most installed Python package,
used in [1.3 million GitHub repositories](https://github.com/urllib3/urllib3/network/dependents),
and has been [sent to another planet](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile#list-of-qualifying-repositories-for-mars-2020-helicopter-contributor-achievement).

It's my honor to present the next major release of urllib3. This major release has been in progress
since 2020 and will be the foundation of future improvements to the package. Everyone on our team of contributors is excited to finally share what we've accomplished with you all.

This release was made possible thanks to work from many people, but especially the following individuals:

<div class="row">
<div class="col-3 col-4-sm"><center><a href="https://github.com/pquentin"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/pquentin.png"/><br>Quentin Pradet</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/hramezani"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/hramezani.png"/><br>Hasan Ramezani</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/illia-v"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/illia-v.png"/><br>Illia Volochii</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/sethmlarson"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/sethmlarson.png"/><br>Seth Michael Larson</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/franekmagiera"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/franekmagiera.png"/><br>Franek Magiera</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/hugovk"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/hugovk.png"/><br>Hugo van Kemenade</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/jalopezsilva"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/jalopezsilva.png"/><br>Jorge Lopez Silva</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/V1NAY8"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/V1NAY8.png"/><br>Sai Vinay</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/venthur"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/venthur.png"/><br>Bastian Venthur</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/bluetech"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/bluetech.png"/><br>Ran Benita</a></center></div>
<div class="col-3 col-4-sm"><center><a href="https://github.com/nateprewitt"><img style="object-fit: contain; max-width: 100%;" src="https://github.com/nateprewitt.png"/><br>Nate Prewitt</a></center></div>
</div>

I'd also like to thank everyone who's supported our team financially like [Tidelift](https://tidelift.com/subscription/pkg/pypi-urllib3),
[Spotify](https://spotify.github.io/), [GitCoin Grants](https://bounties.gitcoin.co/grants/65/urllib3),
and all the individual and organization donations on [GitHub Sponsors](https://github.com/sponsors/urllib3/) and [OpenCollective](https://opencollective.com/urllib3).
Our team has published yearly reports on how these financial contributions help us pay maintainers fairly for their time and expertise,
attract new contributors, and allow for maintainers to take extended leave from their day jobs to complete larger bodies of
work. All of this was necessary to get v2.0.0 across the finish line and have been a testament to how supporting open source projects
financially can make a huge difference.

**Now, let's get started with urllib3 v2.0.0! 🚀**

```shell
$ python -m pip install 'urllib3>=2'
```

After getting excited about all the new features detailed below, [please read the Migration Guide](https://urllib3.readthedocs.io/en/latest/v2-migration-guide.html)
that the team has put together. This will help you learn about the relevant changes in v2.0.0 and what to do to migrate
packages and applications to use the new major release.

## Top-level `urllib3.request()` function

This has been the most requested feature when I talk to users about urllib3.
Many folks want to make a simple HTTP request and don't want to worry about any of the underlying complexity.
The popularity of the Requests library and its APIs high-level APIs are proof of this.

Starting in v2.0.0 you can use `urllib3.request()` to make HTTP requests:

```python
import urllib3

resp = urllib3.request("GET", "https://example.com")

print(resp.status)
# 200
print(resp.headers.get("Content-Type"))
# text/html; charset=UTF-8
```

## JSON requests and responses

JSON is everywhere on the web, so having native support for JSON
both on the request and response APIs of urllib3 will allow users
easily interact with the many HTTP APIs that use JSON:

```python
import urllib3

resp = urllib3.request(
    "POST", "https://httpbin.org/anything",
    # The 'json' parameter encodes the JSON into the body
    # and sets the 'Content-Type' to 'application/json'.
    json={"key": "value"}
)

# The HTTPResponse.json() method decodes JSON in the body
# and loads the data into a Python object.
print(resp.json())
```

```json
{
  "headers": {
    "Accept-Encoding": "identity",
    "Content-Length": "15",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-urllib3/2.0.0"
  },
  "json": {
    "key": "value"
  },
  "method": "POST",
  "url": "https://httpbin.org/anything"
}
```

## Strictly type-hinted APIs

The entire urllib3 v2.0.0 package now has strict type hints included with every install.
This means that auto-complete and type-checking tooling like mypy will natively work with the urllib3 module making it even easier to use with confidence.
As a part of adding type hints to our entire API, we also [wrote an extensive case study](https://sethmlarson.dev/tests-arent-enough-case-study-after-adding-types-to-urllib3)
for adding type hints to urllib3 and what we learned (and fixed!) along the way.

## The future

I noted earlier that 2.0.0 is the base that we're building future improvements on.
We already [have many items on our roadmap](https://github.com/urllib3/urllib3/milestone/9) we're hoping to tackle now that 2.0.0 is available.
Beyond those already listed, many other larger projects become possible, such as migrating away from the standard library
HTTP implementation, HTTP/2 and HTTP/3 support, and including an authentication framework. Stay tuned!
