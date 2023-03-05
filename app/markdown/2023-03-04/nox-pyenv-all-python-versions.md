# Testing multiple Python versions with nox and pyenv

[Nox](https://nox.thea.codes) is an incredible tool, I use it for all my Python projects, highly recommend it.
One of the best features of nox and tools like it is [parameterization](https://nox.thea.codes/en/stable/config.html#parametrizing-sessions).
Usually this is done for the test suite portion where you want to run your test
suite on many different Python versions (and maybe other things like dependency versions):

```python
import nox

# An example nox task definition that runs on many supported Python versions:
@nox.session(
    python=["3.8", "3.9", "3.10", "3.11", "3.12", "pypy3"]
)
def test(session):
    session.install(".")
    session.install("-rdev-requirements.txt")

    session.run("pytest", "tests/")
```

**This is awesome!** Now you can run `nox -s test` to run all variations at once
or `nox -s test-3.11` to target a specific Python version. The only hangup for me was
when all of your Python versions were installed through [pyenv](https://github.com/pyenv/pyenv).
Pyenv is another incredible tool that I highly recommend if you find yourself needing to install
and manage many Python versions.

Pyenv works by being higher priority in your `PATH` than your system Python, thus letting it
inject a `python` stub (and `python3`, `pip`, etc) into your shells:

```shell
$ whereis python
python: /home/sethmlarson/.pyenv/shims/python
```

For some reason I thought pyenv was only capable of having a single version stub available at one time
and thus was frustrated by having to cycle through the different Python versions. But that's **totally not
the case**, you can specify multiple Python versions into `pyenv global` and have them all available through
their `python3.{minor}` aliases which `nox` can discover:

```shell
# Enable all the Python versions everywhere!
$ pyenv global 3.8 3.9 3.10 3.11 3.12-dev

# Tell nox to run all test tasks available
$ nox -s test
nox > Running session test-3.8
nox > Creating virtual environment (virtualenv) using python3.8 in .nox/test-3-8
... (test output)
nox > Ran multiple sessions:
nox > * test-3.8: success
nox > * test-3.9: success
nox > * test-3.10: success
nox > * test-3.11: success
nox > * test-3.12: success
```

🥳 All tests ran against all Python versions! Thanks pyenv and nox 💜
