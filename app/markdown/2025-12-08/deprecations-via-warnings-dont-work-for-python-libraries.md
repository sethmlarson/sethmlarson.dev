# Deprecations via warnings don’t work for Python libraries

Last week [urllib3 v2.6.0 was released](https://pypi.org/project/urllib3/2.6.0/) which contained removals for
several APIs that we've known were problematic since 2019 and
[have been deprecated since 2022](https://github.com/urllib3/urllib3/pull/2814). The deprecations
were marked in the documentation, changelog, and what I incorrectly believed
would be the most meaningful signal to users: [with a `DeprecationWarning`
being emitted](https://github.com/urllib3/urllib3/commit/19582a1f35ae810f97dc46897232770c810c197a#diff-008f01f06c84456177464927734cc849c073b1f3d13bfab947ff812a5b4ac965) for each use for the API.

<!-- more -->

The API that urllib3 recommended users use instead has the same
features and no compatibility issues between urllib3 1.x and 2.x:

```python
resp = urllib3.request("GET", "https://example.com")

# Deprecated APIs
resp.getheader("Content-Length")
resp.getheaders()

# Recommended APIs
resp.headers.get("Content-Length")
resp.headers
```

This API was emitting warnings for over 3 years in a top-3 Python package by downloads urging libraries
and users to stop using the API and **that was not enough**. We still received feedback
from users that this removal was unexpected and was breaking dependent libraries.
We ended up [adding the APIs back](https://github.com/urllib3/urllib3/pull/3732) and creating a hurried release to fix the issue.

It's not clear to me that
waiting longer would have helped, either. The libraries that were impacted
are actively developed, like the Kubernetes client, Fastly client, and Airflow
and I trust that if the message had reached them they would have taken action.

My conclusion from this incident is that [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning) in its current state does not
work for deprecating APIs, at least for Python libraries. That is
unfortunate, as `DeprecationWarning` and the [`warnings` module](https://docs.python.org/3/library/warnings.html)
are easy-to-use, language-“blessed”, and explicit without impacting users that don't
need to take action due to deprecations. Any other method of deprecating
API features is likely to be home-grown and different across each project
which is far worse for users and project maintainers.

## Possible solutions?

`DeprecationWarning` is called out in the [“ignored by default” list](https://docs.python.org/3/library/warnings.html#updating-code-for-new-versions-of-dependencies)
for Python. I could ask for more Python developers to run with warnings enabled, but solutions in the form of “if only we could all just” are a folly.
Maybe the answer is for each library to create its own
“deprecation warning” equivalent just to not be in the “ignored by default” list:

```python
import warnings

class Urllib3DeprecationWarning(UserWarning):
    pass

warnings.warn(
    "HTTPResponse.getheader() is deprecated",
    category=Urllib3DeprecationWarning,
    stacklevel=2
)
```

Maybe the answer is to do away with advance notice and adopt SemVer with many major versions, similar to
how Cryptography operates for API compatibility. Let me know if
you have other ideas.
