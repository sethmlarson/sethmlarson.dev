# Tests aren’t enough: Case study after adding type hints to urllib3

Since Python 3.5 was released in 2015 including [PEP 484](https://www.python.org/dev/peps/pep-0484) and the [typing module](https://docs.python.org/3/library/typing.html) type hints have grown from a nice-to-have to an expectation for popular packages.  To fulfill this expectation our team has committed to [shipping type hints for the v2.0 milestone](https://urllib3.readthedocs.io/en/stable/v2-roadmap.html). What we didn’t realize is the amount of value we’d derive from this project in terms of code correctness.

We wanted to share the journey, what we learned, and problems we encountered along the way as well as celebrate this enormous milestone for the urllib3 project.

[Hasan Ramenzani](https://github.com/hramezani) has taken on the mantle of being the primary contributor to urllib3’s type hints along with help from other team members and community contributors [Ran Benita](https://github.com/bluetech), [Ezzeri Esa](https://github.com/savarin), and [Quentin Pradet](https://github.com/pquentin). Thanks to them for all their work!


### Why type hints?

Python doesn’t have a concept of “[type safety](https://en.wikipedia.org/wiki/Type_safety)”: if a function accepts a string parameter and you pass an integer parameter instead the language will not complain (although the function likely won’t work as intended!) Even when using type hints the “type safety” they provide is completely opt-in with tools like Mypy or Pyright. You can continue incorrectly passing an integer parameter, your tools just won’t be very happy about it.


### Tests aren't a substitute for type hints

When we originally started this journey our primary goal was to provide a good experience for users who wanted to use type checking tools with urllib3. We weren’t expecting to find and fix many defects.

After all, urllib3 has over 1800 test cases, 100% test line coverage, and is likely some of the most pervasive third-party Python code in the [solar system](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/personalizing-your-profile#list-of-qualifying-repositories-for-mars-2020-helicopter-contributor-badge).

Despite all of the above, the inclusion of type checking to our CI has yielded many improvements
to our code that likely wouldn't have been discovered otherwise. For this reason we recommend
projects evaluate adding type hints and strict type checking to their development workflow
instead of relying on testing alone.

For a great visual explanation of how types help catch issues differently than tests see this [PyCon Cleveland 2018 talk](https://www.youtube.com/watch?v=pMgmKJyWKn8&t=288s) by Carl Meyer.


## How we developed and iterated on type hints

This section should serve as a guide to developers looking to add type hints to a medium-to-large size project. This effort took many months for our team to complete so make sure to allocate enough time.


### Incrementally adding types to existing projects

We wanted to add Mypy to our continuous integration to ensure new contributors wouldn’t accidentally break type hints but we also wanted to add Mypy incrementally so it wouldn’t grind all our development to a halt.

If you’ve ever tried running Mypy on a single file in a project without any type hints you’re unlikely to only receive errors from the file you ran Mypy on.  Instead you’re likely to receive type errors from files where you imported other APIs, both within the project and third-party modules.

This makes adding type hints seem like a daunting task, either needing to be added all at once or with tons of temporary `# type: ignore` annotations along the way to ensure Mypy continues to pass in CI.

[Our solution](https://github.com/urllib3/urllib3/pull/1924#discussion_r474283738) to this was to maintain a list of files in our project that we knew had correct type hints. Mypy would be run one by one on every file and the list of issues that were detected by Mypy would be gathered up, de-duplicated, and crucially we’d filter out files that weren’t on the “known-good” list.

This meant that once a file was complete we’d add the path to the known-good list to ensure that future contributions wouldn’t regress on our type hints.


### Reviewing type hint additions

Reviewing large diffs in GitHub, especially ones where very small changes are made to large numbers of lines, is a difficult task because of how little context is given within the GitHub UI by default (usually 2-3 lines above and below the diff). Take your time here as a mistake may leak out to users if you aren’t adding types to your test suite too.

If it wasn’t obvious why a `# type: ignore` annotation was added a comment would be added to Github by the author to let reviewers know why the decision was made. This made for a less back-and-forth on individual changed lines.


### Type your tests!

Once we completed the addition of type hints to the source code of urllib3 we set our sights on the test suite. This may seem strange as our users are very unlikely to directly benefit from us adding type hints there, however there’s one big benefit: **we’re able to find issues with types from a user perspective!**

In our case the test suite contained more use-cases than what we originally thought for multiple APIs which meant we had to change or loosen the type hints in those cases. Doing this work up-front meant we were less likely to release type hints that were too strict which would likely cause issues for users.


### Backwards-compatibility types

Many times we had to make a decision about whether to advertise support for a certain type, especially types which were allowed for backwards compatibility but not what we want users to start using in newly written code. Consciously excluding a type is a good way to push users in the right direction without introducing breaking changes.


### Use strict mode if possible

Mypy includes a `--strict` parameter which [enables all the optional error checking flags](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict). This provides the best coverage of typing errors and also means when you upgrade Mypy you’ll automatically start checking errors that were added in the latest version.

Remember to pin the version of Mypy you’re using for your project so you won’t be caught flat-footed when CI starts failing due to new type errors being checked in a new Mypy release.


### Specify error codes on type ignore annotations

Instead of adding a blanket annotation to ignore all type issues every type: ignore annotation should [specify the error codes](https://mypy.readthedocs.io/en/stable/error_codes.html) to narrow down the error that Mypy is ignoring. This means the code will continue to be checked for all other error and if the error ever changes then Mypy will be able to signal the situation.

You can see which error code to use by using the `--show-error-codes` option with Mypy.

Reference: [urllib3#2363](https://github.com/urllib3/urllib3/pull/2363)


### Anything but Any

Using [typing.Any](https://docs.python.org/3/library/typing.html#typing.Any) in a particularly complicated type situation is a tempting option. Resist the easy-out using `Any` because complicated situations for you are likely to translate to complicated situations for your users.

Python typing has come a long way since it was introduced: read up on the new features available for modeling complex types and try your best to keep `Any` out of your code.


## What we found and learned

Our whole team learned a bunch about how Mypy and Python typing works during this project. Below are some of the interesting issues and features that we found that are worthy of sharing:


### Bytes comparison warnings

Python includes a warning called “[BytesWarning](https://docs.python.org/3/library/exceptions.html#BytesWarning)” which among other uses can warn against using equality (==) to compare bytes and string types. This warning can help you find subtle type issues in your own code and third-party libraries.

Quentin attempted to enable this feature for urllib3 and immediately we saw some issues with urllib3 code and the brotlicffi package ([brotlicffi#177](https://github.com/python-hyper/brotlicffi/pull/177)). The fixes in urllib3 ([urllib3#2145](https://github.com/urllib3/urllib3/pull/2145)) were mostly related to how we handle headers, we accept both bytes and strings for header names but this leads to issues when header retrieval occurs.

After fixing all the issues we were able to enable [the -bb option](https://docs.python.org/3/using/cmdline.html#cmdoption-b) which raises an error for bytes comparisons instead of only issuing a warning.


### Adding type hints to trustme

urllib3 uses the package [trustme](https://github.com/python-trio/trustme) for generating realistic CA certificates on-demand for our test suite. As a part of the effort to add type hints to our test suite we also wanted to add type hints to packages used by our test suite to avoid using `# type: ignore`.

The trustme package at the time supported Python 2 so we got to use [Mypy’s Python 2 mode](https://mypy.readthedocs.io/en/stable/python2.html) and [Python 2 compatible type hints using comments](https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code).

[Ran Benita](https://github.com/bluetech) created a pull request ([trustme#341](https://github.com/python-trio/trustme/pull/341)) adding the types which was reviewed, merged, and released by [Quentin Pradet](https://github.com/pquentin). It’s a small world!


### Untested but documented feature with Retry.allowed_methods

Comparing the types to the documentation for a parameter helped us discover a feature that didn’t have a test case but was documented within a docstring. After we discovered this we added the case to our test suite to ensure we never regressed on our advertised feature.

Reference: [urllib3#2215](https://github.com/urllib3/urllib3/pull/2215#pullrequestreview-659872235)


### Bad default parameter values

This case shows how few people are using our `PoolManager.connection_from_X()` APIs as the default value for the only parameter would immediately cause an exception. Mypy helped us find and fix this issue which had been silently missed in our codebase for some time.

Reference: [urllib3#2232](https://github.com/urllib3/urllib3/pull/2232/files#r640945296)


### Mypy providing better protections for method=None case

Mypy alerted us to a missing check to see that `method` was non-`None` before calling a function with a parameter. Previously this behavior was only protected by knowing how the function should be called.

Reference: [urllib3#2215](https://github.com/urllib3/urllib3/pull/2215/files/89570ab096910dbea51e07f4597eadf121a0a8e5#r632553317)


### Boolean literals and context managers

Mypy has special handling for returning boolean literals from the context manager `__exit__()` method. If your `__exit__()` method returns a raw `True` or `False` you must annotate with Literal[True] or Literal[False] as using `bool` signals that the context manager may or may not swallow exceptions.

Reference: [urllib3#2232](https://github.com/urllib3/urllib3/pull/2232/files#r640959011)


### Mypy-friendly code is also human-friendly

Mypy signaled on a line of code that was difficult for even a human to understand from a quick glance. By simplifying the code it became easier for both humans and Mypy alike to understand what was intended.

Reference: [urllib3#2251](https://github.com/urllib3/urllib3/pull/2251#discussion_r644330444)


### Function signatures not matching mimicked API

Mypy found a mismatch between the APIs of our custom `SSLTransport` class which is meant to be used like a socket during TLS-in-TLS tunneling and the `socket` API:

Reference: [urllib3#2443](https://github.com/urllib3/urllib3/pull/2443/files#r722368505)


### Making types more general should require additional test cases

Whenever loosening a type from strict to general make sure your test suite grows to cover that case as well. In our example we loosened `socket_options` from `List[...]` to `Sequence[...]` as technically passing a tuple was acceptable and being done by some users.

Reference: [urllib3#2232](https://github.com/urllib3/urllib3/pull/2232/files#r642150627)


### Use @overload for filtered values types

Instead of using `f(x: Union[int, str]) -> Union[int, str]` take advantage of the [`@overload` decorator](https://docs.python.org/3/library/typing.html#typing.overload) to define the instances where certain input types always result in a certain output type for each case. This allows Mypy to give much better results when the interface is being used.

Reference: [urllib3#2251](https://github.com/urllib3/urllib3/pull/2251#discussion_r644770648)


### Explicit return None when a function can return other values

It’s always good practice to `return None` when you intend the result of the function to a variable. Mypy helpfully enforces this good practice when there are values being returned in other parts of the function but the default “drop through” return None isn’t explicitly added.

Reference: [urllib3#2255](https://github.com/urllib3/urllib3/pull/2255)


### Don’t expose Generators unless you want Generator functionality

Generators have additional behaviors over iterables so if the API isn’t meant to be used like a generator then it’s best to keep this fact a secret and annotate with `Iterable[X]` instead of `Generator[X, None, None]`.

Reference: [urllib3#2255](https://github.com/urllib3/urllib3/pull/2255#discussion_r661652500)


### Missing type hints in the standard library

Some of the less-traveled parts of the standard library don't have complete type coverage. These types
are distributed in a library called [typeshed](https://github.com/python/typeshed) so if you uncover a missing
or incorrect type hint for the standard library they should be fixed here.

References: [typeshed#6176](https://github.com/python/typeshed/pull/6176), [urllib3#2458](https://github.com/urllib3/urllib3/pull/2458)


## Conclusion

Adding type hints to urllib3 was clearly a huge amount of work, hundreds of engineer hours across several months. What we once thought would be a purely developer-facing change ended up making the codebase more robust than ever. Several non-trivial logic errors were fixed and our team is more confident reviewing and merging PRs. This is a big win for our users and a very worthy investment.

Portions of this work, including writing this case study, was funded by generous support on [GitHub Sponsors](https://github.com/sponsors/urllib3), [GitCoin Grants](https://gitcoin.co/grants/65/urllib3), and [Open Collective](https://opencollective.com/urllib3). Thank you for your support!

