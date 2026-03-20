# Python library “Requests” needs you to test type hints

[Requests](https://github.com/psf/requests/) is a popular HTTP client library available
on the Python Package Index (PyPI). Sitting in the
top 10 packages by downloads on PyPI, this library
is used by many, many projects. This library
is known for its user-friendly and ergonomic
API for HTTP requests and responses. However,
the API implementation can sometimes confuse
static analysis tools like IDEs or type checkers,
causing issues for users.

<!-- more -->

Requests maintainer [Nate Prewitt](https://nateprewitt.dev/)
is [planning to add support](https://github.com/psf/requests/issues/7271) for [type hints](https://docs.python.org/3/library/typing.html)
to Requests in the next three months. Right now the feature is
available as a development branch but will later be
published to PyPI as a pre-release version. The goal
is to [find and fix issues](https://github.com/psf/requests/issues/7271) before rolling the change
out to users to avoid unnecessary breakage.

<!-- more -->

## What can you do to help?

Shipping large changes to codebases this popular is difficult
without breaking users. **This is where you
come in: Requests needs your help!**
If your project or application uses Requests as a dependency,
try installing and running the development branch with type
hints. This is especially useful if your project uses
type hints and a type checker like Mypy, Pyright, or Ty.

Here's how you can install the [development branch](https://github.com/psf/requests/pull/7272).
These instructions are [available in the pull request](https://github.com/psf/requests/issues/7271#how-to-test:~:text=How%20to%20test,-Install), too:

* `python -m pip install git+https://github.com/psf/requests.git@inline_types_rfc`
* `uv pip install git+https://github.com/psf/requests.git@inline_types_rfc`

After installation:

* Run your existing test suite
* Run Pyright or Mypy against your code that uses Requests
* Try your usual Requests patterns and see if anything doesn't typecheck

If you encounter issues after running your test suite or type checker
with the development branch: [please report them
on GitHub](https://github.com/psf/requests/issues/7271). Be sure to
[check the list of known issues](https://github.com/psf/requests/issues/7271#how-to-test:~:text=Known%20limitations) and 
search for a duplicate of
your issue before opening a new one. When reporting
an issue, be as descriptive as possible:

* What Python version? (`python --version`)
* What dependencies are you using? (`python -m pip freeze`)
* What type checker are you using, what settings? (Mypy, Pyright, Ty)

This will help Requests maintainers address your issue quickly
ahead of shipping the new type hints. Thanks much for your contributions
towards shipping this feature smoothly. 🙏
