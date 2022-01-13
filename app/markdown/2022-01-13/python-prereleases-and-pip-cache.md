# Python pre-releases and pip cache

Some time ago the urllib3 team noticed that our Python 3.11 test suite started failing with a strange error. On GitHub Actions all we could see was:

```bash
nox > Running session test-3.11
nox > Creating virtual environment (virtualenv) using python3.11 in .nox/test-3-11
nox > python --version
Python 3.11.0a3
nox > Command coverage run --parallel-mode -m pytest -r a
  --color=yes --tb=native --no-success-flaky-report test/
  failed with exit code -11

nox > Session test-3.11 failed.
Error: Process completed with exit code 1.
```

Notice that our test execution was exited with a return code of `-11` which corresponds to signal `SIGSEGV` also known as a segmentation fault. This means that somewhere in C-land an improper memory location was being accessed, not good! Without a better traceback we wouldn't be able to know where the error is occuring.

[Quentin](https://github.com/pquentin) and I both attempted to recreate the error locally with mixed results. I wasn't able to reproduce the error but Quentin was able to reproduce the error with tracebacks that were happening in both the `ssl` and `selectors` modules:

```bash
test/test_reproduce.py Fatal Python error: Segmentation fault

Thread 0x00007fee9a250640 (most recent call first):
  File "/home/install/lib/python3.11/ssl.py", line 1346 in do_handshake
  File "/home/urllib3/venv/lib/python3.11/site-packages/tornado/iostream.py", line 1391 in _do_ssl_handshake
  File "/home/urllib3/venv/lib/python3.11/site-packages/tornado/iostream.py", line 1478 in _handle_read
  File "/home/urllib3/venv/lib/python3.11/site-packages/tornado/iostream.py", line 696 in _handle_events
  File "/home/urllib3/venv/lib/python3.11/site-packages/tornado/platform/asyncio.py", line 189 in _handle_events
  File "/home/install/lib/python3.11/asyncio/events.py", line 80 in _run
  File "/home/install/lib/python3.11/asyncio/base_events.py", line 1858 in _run_once
  File "/home/install/lib/python3.11/asyncio/base_events.py", line 591 in run_forever
  File "/home/urllib3/venv/lib/python3.11/site-packages/tornado/platform/asyncio.py", line 199 in start
  File "/home/install/lib/python3.11/threading.py", line 968 in run
  File "/home/install/lib/python3.11/threading.py", line 1031 in _bootstrap_inner
  File "/home/install/lib/python3.11/threading.py", line 988 in _bootstrap

Extension modules: tornado.speedups, _brotli, _cffi_backend (total: 3)
zsh: segmentation fault (core dumped)  pytest
```

This looks like an issue in CPython, but we'll eventually discover this error was being caused by our pip cache!

## Finding and reporting the "bug"

After we could reproduce the error reliably, Quentin started [git bisecting CPython](https://www.metaltoad.com/blog/beginners-guide-git-bisect-process-elimination) to find the exact commit that introduced the issue. The error was narrowed down to [this single commit](https://github.com/python/cpython/commit/32a67246b0d1e08cd50fc3bfa58052cfeb515b2e) and after seeing that the PR mentioned that "there should be zero change in behavior" thus [an issue was opened on the Python issue tracker](https://bugs.python.org/issue46320) (BPO) to report what we'd been experiencing.

Within this issue [Eric Snow](https://github.com/ericsnowcurrently) (who was the author of the commit in question) answered quickly and was able to reproduce the error, however he mentioned that the commit changed CPython's Application Binary Interface (ABI) and after slightly rearranging the `PyThreadState` struct was able to make the error go away. Then Eric asked this critical question:

> Could it be that the wheel for one or more the dependencies was built against an earlier 3.11 release (with the previous PyThreadState layout)?

**The answer to this was yes!** Pip was caching a wheel built using CFFI and Python 3.11.0-alpha2 and was installing that same wheel for the now Python 3.11.0-alpha3 both on our local machines and in our test suite. By clearing the pip cache on our machines and our CI we were able to get a passing test suite. 🎉 Thanks Eric!

## When should you be testing Python pre-releases?

Testing your code against pre-releases of Python is important to ensure a smooth upgrade for both your upstream dependencies and your downstream users. **This is especially the case for release candidate builds of Python.**

Eric noted in the issue we filed:

> Thanks for testing against the alpha releases!!!  You're having a positive impact.

However, doing so super early on in the development cycle of a new Python version (like during the alpha or beta phases) comes with a few potential pitfalls, including running into ABI issues like the one mentioned above and needing to build binary dependencies from source distributions instead of wheels which can increase test suite execution time. **Figure out what is sustainable and makes sense for your project.**

If you maintain a Python library you should try at least to manually run your test suite once when the **first release candidate is published**. This means there's still time for the Python core team to fix issues and you're unlikely to run into strangeness like ABI changes between pre-releases.

The urllib3 team tries to start testing against in-development Python versions as soon as they're available given our unique position near the top of most dependency chains.

### When should I be weary ABI changes?

Unless you're testing alpha and beta releases you likely won't have to think about the Python ABI changing. Technically it's acceptable for the Python core devs to change the ABI between **two release candidates** but this is much less likely than in between alphas and betas.

## What are we doing to make this better?

Our team was using the [setup-python GitHub Action](https://github.com/actions/setup-python) which recently added support for automatically caching installed pip dependencies between runs. Because this GitHub Action is very popular we wanted to make testing pre-releases of Python easier by avoiding potential foot-guns like the one above.

We knew that pip's cache shouldn't be re-used across, at a minimum, different pre-release versions. We [opened an issue](https://github.com/actions/setup-python/issues/319) on the repository which was quickly noticed by [Hugo van Kemenade](https://github.com/hugovk) who had a [similar issue open](https://github.com/actions/setup-python/pull/303) to add the **requested Python version** (i.e. in YAML `python: "3.9"`) to the "cache key".

A "cache key" is the identifier that the setup-python action uses to lookup the archived pip cache so any changes to the cache key between two runs would essentially "invalidate" the cache and force pip to reinstall without cached dependencies. We discussed how our two issues were similar and could be solved by adding the **fully qualified version number** (i.e. `python --version` being `3.11.0a3`) to the cache key instead.
