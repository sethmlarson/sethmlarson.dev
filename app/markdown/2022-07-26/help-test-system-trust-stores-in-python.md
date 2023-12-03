# Help us test system trust stores in Python

<blockquote style="line-height: 1.5em">⚠️ If you're an IT or software team that uses Python along with corporate system certificates, an internal CA, or internal PyPI repository: **please read on to help improve Python**. If you know one or more teams that fits this description: **forward them this article**! We need lots of people to try the new pip feature to test our implementation of system trust stores in Python.</blockquote><br>

On July 21st [pip v22.2 was released](https://discuss.python.org/t/announcement-pip-22-2-release/17543) with a new experimental feature for using native system trust stores to verify HTTPS connections with `--use-feature=truststore`. This support is provided by a new Python package called '[truststore](https://github.com/sethmlarson/truststore)':

```bash
# No more 'local issuer not found' errors!

$ python -m pip install \
    --use-feature=truststore Flask
```

Now that the feature is available in pip **we need your help** proving the implementation works for
a large set of systems and environments. The long-term goal of the 'truststore' project is to make the default TLS experience better for libraries like pip, urllib3, and Requests.

## TLDR: How can I help?

- Install Python 3.10 or later in order to use 'truststore' and create a virtual environment.
- Follow the below instructions to install and run pip with truststore.
- If you can't install truststore due to certificate issues then [try the alternate installation instructions](#what-if-i-cant-upgrade-pip-because-of-custom-ca-certificates).
- If the instructions to run pip with truststore work then [leave a reaction on this GitHub issue](https://github.com/sethmlarson/truststore/issues/63).
- If pip with truststore fails for any reason, [please open an issue describing your environment](https://github.com/sethmlarson/truststore/issues).
- If your organization runs a private PyPI repository: try using `--index-url` combined with `--use-feature=truststore`
- If your organization modifies `certifi/cacert.pem` to inject a custom CA certificate, try running the below commands with an unmodified copy of certifi.
- **That's it!** Thanks for doing your part.

You can try running the following commands in a virtual environment:

```bash
# 'truststore' requires Python 3.10 or later to work.
$ python --version
3.10.5

# Upgrade to pip 22.2 and install 'truststore'
$ python -m pip install -U pip truststore

...
Successfully installed pip-22.2
Successfully installed truststore-0.4.0

# Check that pip is 22.2 or later
$ python -m pip --version
pip 22.2 from .../venv/lib/python3.10/site-packages/pip (python 3.10)

# Try the new feature! 🚀
$ python -m pip install -U --use-feature=truststore urllib3

...
Successfully installed urllib3-1.26.10
```

### What should I do afterwards?
 
- Spread this article to other people, teams, and organizations that you know use Python.
  - Retweet on [Twitter](https://twitter.com/sethmlarson/status/1551919041077542913)
  - Upvote on [HackerNews](https://news.ycombinator.com/item?id=32238989), [Reddit](https://www.reddit.com/r/Python/comments/w8jr7a/help_us_test_system_trust_stores_in_python/), and [Lobsters](https://lobste.rs/s/xhk30c/help_us_test_system_trust_stores_python)
- Follow the [truststore GitHub repository](https://github.com/sethmlarson/truststore). There will be updates and new releases there.
- Read the truststore [documentation](https://truststore.readthedocs.io) and [prior art](https://truststore.readthedocs.io/en/latest/#prior-art).
- Experiment with using truststore and give us feedback (but please don't deploy to production yet!)
- Learn about system trust stores and contribute to the project.

### What do errors from custom CA certificates typically look like?

Usually the error will have a message like the one below:

```python
SSLCertVerificationError(1,
  '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed:'
  '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)'
)
```

For pip there are usually retries so you may see the error more than once. If you see a different error and you're not sure what it means feel free to [open an issue describing your environment](https://github.com/sethmlarson/truststore/issues).

### What if I can't upgrade pip because of custom CA certificates?

An unfortunate "chicken and egg" situation. Can't upgrade pip from PyPI to use custom CA certificates because your custom CA certificate is causing errors. For this situation I suggest running the following commands which disables TLS certificate verification for PyPI but does integrity verification of the downloaded packages to ensure they haven't been modified in transit:

```bash
# Create a temporary requirements file to require hashes on install:
$ echo "\
truststore==0.4.0 \
    --hash=sha256:018f261a13c970eb814ac424db4a48d538310416ddad4231ca49033c210eb5cf \
    --hash=sha256:acf60559fda45368f48f98a174568d8fc9b8597faccfaa25f243a4acd48ad13d
pip==22.2 \
    --hash=sha256:8d63fcd4ee293e30b644827268a0a973d080e5c7425ef26d427f5eb2126c7681 \
    --hash=sha256:9abf423d5d64f3289ab9d5bf31da9e6234f2e9c5d8dcf1423bcb46b809a02c2c" > reqs.txt

# Install pip and truststore and verify hashes
$ python -m pip install --require-hashes \
  --trusted-host pypi.org \
  --trusted-host files.pythonhosted.org \
  -r reqs.txt

...
Successfully installed pip-22.2
Successfully installed truststore-0.4.0
```

After installing pip and truststore you should be able to use the `--use-feature=truststore` option in the instructions above.
