# Regex character “$” doesn't mean “end-of-string”

This article is about a bit of surprising behavior I recently discovered
using Python's regex module (`re`) while [developing SBOM tooling for CPython](https://github.com/python/release-tools/pull/92#discussion_r1484470272).

Folks who've worked with regular expressions before might know about `^` meaning "start-of-string"
and correspondingly see `$` as "end-of-string". So the pattern `cat$` would match the string `"lolcat"` but not `"internet cat video"`.

The behavior of `^` made me think that `$` was similar, but they aren't always symmetrical
and the behavior is *platform-dependent*. Specifically for Python with multiline mode *disabled*
the `$` character can match either the end of a string *or a trailing newline before the end of a string*.

So if you're trying to match a string without a newline at the end, **you can't only use `$` in Python!**
Next logical question is how does one match the end of a string without a newline?

After doing more research on [Python](https://docs.python.org/3/library/re.html#regular-expression-syntax)
and [other regular expression syntaxes](https://www.regular-expressions.info/anchors.html)
I also found `\z` and `\Z` as candidates for "end-of-string" characters.

Multi-line mode is enabled with [`re.MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE) in Python, the docs have the following to say:

> When `re.MULTILINE` is specified the pattern character '$' matches at the end of the string and at the end of each
> line (immediately preceding each newline). By default, '$' only matches at the end of the string and immediately before the newline (if any) at the end of the string.

Let's see how these features work together across multiple platforms:

| Pattern matches `"cat\n"`? | `"cat$"` multiline | `"cat$"` no multiline | `"cat\z"` | `"cat\Z"`   |
|----------------------------|---|---|---|-----------|
| PHP                        | ✅ | ✅ | ❌ | ✅         |
| ECMAScript                 | ✅ | ❌ | ⚠️ | ⚠️        |
| Python                     | ✅ | ✅ | ⚠️ | ❌         |
| Golang                     | ✅ | ❌ | ❌ | ⚠️        |
| Java 8                     | ✅ | ✅ | ❌ | ✅         |
| .NET 7.0                   | ✅ | ✅ | ❌ | ✅         |
| Rust                       | ✅ | ❌ | ❌ | ⚠️        |

* ✅: Pattern matches the string `"cat\n"`
* ❌: Pattern does not match the string `"cat\n"`
* ⚠️: Pattern is invalid or character not supported.

Summarizing the above table, if matching a trailing newline is acceptable then `$` with multiline mode works consistently across all platforms,
but if we wanted to *not match* a trailing newline then things get more complicated.

To not match a trailing newline, use `\z` on all platforms except Python and
ECMAScript where you'll need to use `\Z` or `$` without multiline mode respectively.
Hope you learned something about regular expressions today!

Note: The table of data was gathered from [regex101.com](https://regex101.com), I didn't test using the actual runtimes.
