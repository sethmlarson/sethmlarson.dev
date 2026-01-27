# Use “\A...\z”, not “^...$” with Python regular expressions

Two years ago I discovered a potential foot-gun
with the Python standard library “`re`” module.
[<nobr>I blogged about</nobr> this behavior](https://sethmlarson.dev/regex-%24-matches-end-of-string-or-newline),
and turns out that
I wasn't only one who didn't know this:
The article was #1 on HackerNews and the
most-read article on my blog in 2024.
In short the unexpected behavior is that the pattern “`^Hello$`” matches both “`Hello`” and “`Hello\n`”,
and sometimes you don't intend to match a trailing newline.

<!-- more -->

This article serves as a follow-up!
Back in 2024
[I created a table](https://sethmlarson.dev/regex-%24-matches-end-of-string-or-newline#:~:text=Pattern matches) showing that `\z` was a partially viable
alternative to `$` for matching end-of-string
without matching a trailing newline... for every regular expression
implementation **EXCEPT** Python and EMCAScript. 

But that is no longer true, [Python 3.14](https://docs.python.org/3/whatsnew/3.14.html#re) now supports `\z`! This means `\z` is [one step closer](https://github.com/python/cpython/issues/133306)
to being the universal recommendation to match
the end of string without matching a newline.
Obviously no one is upgrading their Python
version just for this new feature, but it's good to know that
the gap is being closed. Thanks to David Wheeler
for doing deeper research in the [OpenSSF Best Practices
WG](https://best.openssf.org) and [publishing this report](https://best.openssf.org/Correctly-Using-Regular-Expressions).

Until Python 3.13 is deprecated and long gone: using `\Z` (as an alias for `\z`) works fine for Python regular expressions.
Just note that this behavior isn't the same [across regular expression
implementations](https://best.openssf.org/Correctly-Using-Regular-Expressions#guidance), for example EMCAScript, Golang, and Rust
don't support `\Z` and for PHP, Java, and .NET `\Z` *actually
matches trailing newlines!*