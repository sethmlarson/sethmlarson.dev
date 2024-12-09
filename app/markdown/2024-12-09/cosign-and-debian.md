# New experimental Debian package for Cosign (Sigstore)

Cosign [has a new experimental package available](https://lists.debian.org/debian-go/2024/12/msg00005.html) for Debian
thanks to the work of [Simon Josefsson](https://josefsson.org/). Simon and I had an email
exchange about Sigstore and Cosign on Debian after [the discussion about PEP 761](https://discuss.python.org/t/pep-761-deprecating-pgp-signatures-for-cpython-artifacts/67180) (Deprecation and discontinuation of PGP signatures).

Debian and other downstream distros of Python and Python packages are incredibly important
consumers of verification materials. Because these distros actually verify materials for every
build of a package, this increases the confidence for **other users** using these same artifacts
even without those users directly verifying the materials themselves. We need more actors in the
ecosystem doing end-to-end verification to dissuade attackers from supply-chain attacks targeting
artifact repositories like python.org and PyPI.

## Trying Cosign in Docker

I gave the experimental package a try using the Debian Docker image to verify [CPython 3.14.0-alpha2's tarball and verification materials](https://www.python.org/downloads/release/python-3140a2/):

```shell
$ docker run --rm -it debian:bookworm

# Install the basics for later use.
apt-get install ca-certificates wget

# Add Simon's experimental package repo
# and install Cosign! :party:
$ echo "deb [trusted=yes] https://salsa.debian.org/jas/cosign/-/jobs/6682245/artifacts/raw/aptly experimental main" | \
    tee --append /etc/apt/sources.list.d/add.list
$ apt-get update
$ apt-get install cosign
$ cosign version

  ______   ______        _______. __    _______ .__   __.
 /      | /  __  \      /       ||  |  /  _____||  \ |  |
|  ,----'|  |  |  |    |   (----`|  | |  |  __  |   \|  |
|  |     |  |  |  |     \   \    |  | |  | |_ | |  . `  |
|  `----.|  `--'  | .----)   |   |  | |  |__| | |  |\   |
 \______| \______/  |_______/    |__|  \______| |__| \__|
cosign: A tool for Container Signing, Verification and Storage in an OCI registry.
```

Now we can test Cosign out with CPython's artifacts. [We expect](https://www.python.org/downloads/metadata/sigstore/) Hugo van Kemenade (`hugo@python.org`) as the
release manager for Python 3.14:

```shell
# Download the source and Sigstore bundle
$ wget https://www.python.org/ftp/python/3.14.0/Python-3.14.0a2.tgz
$ wget https://www.python.org/ftp/python/3.14.0/Python-3.14.0a2.tgz.sigstore

# Verify with Cosign!
$ cosign verify-blob \
    --certificate-identity hugo@python.org \
    --certificate-oidc-issuer https://github.com/login/oauth \
    --bundle ./Python-3.14.0a2.tgz.sigstore \
    --new-bundle-format \
    ./Python-3.14.0a2.tgz

Verified OK
```

Overall, this is working as expected from my point-of-view! Simon [had a few open questions](https://lists.debian.org/debian-go/2024/12/msg00005.html) mostly for Cosign's
upstream project. I am hopeful that this means we'll begin seeing Sigstore bundles and their derivatives (such as
[attestations from the Python Package Index](https://trailofbits.github.io/are-we-pep740-yet/)) be used for downstream verification by distros like Debian. Exciting times ahead!

## New Bundle Format

My first attempt didn't include the `--new-bundle-format` option and that resulted in an opaque error.
Hopefully this user-experience issue will be phased out and Cosign will "default" to the new bundle format?
I included this error strictly for folks searching for this error message and wanting to fix their issue.

```
Error: bundle does not contain cert for verification, please provide public key
main.go:74: error during command execution: bundle does not contain cert for verification, please provide public key
```

<blockquote>
  <center>
    This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">Alpha-Omega project</a>.
  </center>
</blockquote>