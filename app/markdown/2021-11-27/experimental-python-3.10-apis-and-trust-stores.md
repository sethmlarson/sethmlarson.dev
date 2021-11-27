# Experimental APIs in Python 3.10 and the future of trust stores

**⚠️ The APIs mentioned below aren't documented in the Python docs or release notes and are experimental. I recommend not using them until they are stable.**

In Python 3.10.0 there were a few new APIs added to the `ssl` module related to certificate chains that weren't listed in the [Python 3.10 release notes](https://docs.python.org/3/whatsnew/3.10.html) due to being experimental. I discovered these APIs because I follow the `ssl` module closely as any changes to the module will likely create a feature request or additional test case for urllib3.

Let's see the new APIs in action and how their addition could mean a bright future for [trust stores](https://stackoverflow.com/a/318450/5763213) in Python:

## Using the new APIs

To see these APIs in action let's create a typical TLS connection to `example.com`:

```python
>>> import socket
>>> import ssl
>>>
>>> ctx = ssl.create_default_context()
>>> sock = socket.create_connection(("example.com", 443))
>>> sock = ctx.wrap_socket(sock, server_hostname="example.com")
>>>
>>> sock
<ssl.SSLSocket fd=3, family=AddressFamily.AF_INET6, ...>
```

Nothing out of the ordinary here yet. Now having looked at the PR that added these APIs, they're not yet available on an `SSLSocket` object directly. Instead they're exposed in [ssl.SSLObject](https://docs.python.org/3/library/ssl.html#ssl.SSLObject) which is a reduced-scope variant of `SSLSocket` meant to be used as an interface for TLS with memory buffers.

But we can access the internal `SSLObject` instance on an `SSLSocket` via the `_sslobj` property:

```python
>>> sslobj = sock._sslobj
>>> sslobj
<_ssl._SSLSocket object at 0x7f167d8a5c40>
```

From here we can start poking around with the new certificate APIs. The following are the new APIs I know about:

```python
import _ssl

_ssl.ENCODING_PEM = 1 # enum
_ssl.ENCODING_DER = 2 # enum

_ssl.Certificate # class

# see: SSLSocket.getpeercert(binary_form=True)
_ssl.Certificate.public_bytes(encoding: int) -> Union[bytes, str]

# see:  SSLSocket.getpeercert(binary_form=False)
_ssl.Certificate.get_info() -> Dict[str, Any]

ssl.SSLObject.get_unverified_chain() -> List[_ssl.Certificate]
ssl.SSLObject.get_verified_chain() -> List[_ssl.Certificate]
```

If we try using these APIs we can get the following information:

```python
>>> unverified_chain = sslobj.get_unverified_chain()
>>> verified_chain = sslobj.get_verified_chain()

# In our case, the 'unverified_chain' and 'verified_chain'
# are the same we'll discuss the difference below.
>>> assert unverified_chain == verified_chain

# The chains go in order from leaf -> root.
# verified_chain[0] is the same as sock.getpeercert()
>>> assert sock.getpeercert(True) == \
        verified_chain[0].public_bytes(_ssl.ENCODING_DER)

# The individual certificates in the chain have two methods:
# .get_info() and .public_bytes(encoding)
>>> verified_chain[0].public_bytes(_ssl.ENCODING_PEM)
'-----BEGIN CERTIFICATE-----\nMIIG1TC ...'

# Using _ssl.ENCODING_DER is the same as socket.getpeercert(True)
>>> verified_chain[0].public_bytes(_ssl.ENCODING_DER)
b'0\x82\x06\xd50\x82 ... \x05\x0f\xe3E#\xc0d_'

# _ssl.Certificate.get_info() is the same as sock.getpeercert(False)
>>> verified_chain[0].get_info()
{
  "OCSP": ["http://ocsp.digicert.com"],
  "caIssuers": ["http://cacerts.digicert.com/..."],
  "crlDistributionPoints": [
    "http://crl3.digicert.com/...crl",
    "http://crl4.digicert.com/...crl"
  ],
  "issuer": [
    [["countryName", "US"]],
    [["organizationName", "DigiCert Inc"]],
    [["commonName", "DigiCert TLS RSA SHA256 2020 CA1"]]
  ],
  "notAfter": "Dec 25 23:59:59 2021 GMT",
  "notBefore": "Nov 24 00:00:00 2020 GMT",
  "serialNumber": "0FBE08B0854D05738AB0CCE1C9AFEEC9",
  "subject": [
    [["countryName", "US"]],
    [["stateOrProvinceName", "California"]],
    [["localityName", "Los Angeles"]],
    [["organizationName", "..."]],
    [["commonName", "www.example.org"]]
  ],
  "subjectAltName": [
    ["DNS", "www.example.org"],
    ["DNS", "example.com"],
    ["DNS", "example.edu"],
    ["DNS", "example.net"],
    ["DNS", "example.org"],
    ["DNS", "www.example.com"],
    ["DNS", "www.example.edu"],
    ["DNS", "www.example.net"]
  ],
  "version": 3
}
```

### What is new with these APIs?

Before Python 3.10 the only certificate information we could gather from an `SSLSocket` was from the leaf certificate via the `getpeercert()` method. The complete certificate chain that was sent during the handshake wouldn't be available from Python. This meant that only the leaf certificate could be used in trust decisions from applications.

With these new APIs applications and libraries can make trust decisions with the entire cert chain. **Root CA pinning and using systems besides OpenSSL for trust decisions are now possible in Python! 🎉**

To use a separate API for verifying cert chains we can configure an `ssl.SSLContext` to not verify certificates during the handshake with `SSLContext.verify_mode = ssl.CERT_NONE` flag and instead use the `unverified_certificates()` method capture to forward all certificates to the separate API for verifying certs:

```python
import ssl

# Disable cert verification (enabled by default)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Handshake as normal, still set `server_hostname` for SNI
sock = ctx.wrap_socket(sock, server_hostname="example.com")
cert_chain = sock._sslobj.unverified_chain()

# Use a different API to verify certificates:
verify_cert_chain_api(cert_chain)
```

### Difference between `verified_chain()` and `unverified_chain()` methods

Despite similar names and return types, the `verified_chain()` and `unverified_chain()` methods have two distinct uses. The `verified_chain()` method uses OpenSSL's `SSL_get0_verified_chain` function. [The documentation of this function](https://manpages.debian.org/testing/libssl-doc/SSL_get0_verified_chain.3ssl.en.html) says that it returns "the **verified** certificate chain of the peer including the peer's end entity certificate". The unverified_chain() method uses the `SSL_get_peer_cert_chain()` OpenSSL function which returns a certificate chain that is **not verified**.

The difference between a verified and unverified chain is whether the chain is the minimal number of certificates between the target entity certificate and a trust anchor in the trust store. All certificates within a verified chain are valid, unexpired, and (as far as OpenSSL knows) not revoked. An unverified chain can include certificates that aren’t valid, are expired or revoked, or simply not necessary to create a chain of trust.

For example if the server provides 4 certificates during the TLS handshake (named L, A, B, and C) where C is in the trust store as a trust anchor and A and B are both intermediate certificates signed by C. The L certificate is the leaf certificate being used by the server and is signed by A. Here’s an ASCII-art diagram for the above situation:

```
                ┌───────┐   ┌───────┐
                │       │   │       │
                │       │   │       │
                │   A   ├───►   L+  │
    ┌───────┐   │       │   │       │
    │       ├───►       │   │       │
    │       │   └───────┘   └───────┘
    │   C*  │
    │       │   ┌───────┐
    │       ├───►       │     Legend
    └───────┘   │       │   ──────────
                │   B   │   ─► Signs
                │       │   +  Entity/leaf
                │       │   *  Trusted
                └───────┘
```

This means that B is not necessary to create a chain of trust for the handshake. In this case `verified_chain()` method would include L, A, and C and the `unverified_chain()` method would return L, A, B, and C.

### Why are OS trust stores better?

Why are OS trust stores superior to OpenSSL on platforms where these APIs are available? OS trust store APIs include many more features that are automatically handled in the background that make the experience better for both application developers and system operators.

Windows automatically downloads missing intermediate certificates when they’re detected and keeps the trust store up to date automatically via the Windows update process. This means that a new installation of Windows will still be able to make TLS handshakes without first manually downloading or updating certificates.

Windows and macOS both check certificate revocation lists (CRL) for certificates in a chain. If you’re using CRLs with OpenSSL you’ll have to implement the functionality yourself instead of getting it for free from the OS.

For full details on these APIs you can read the documentation on [Secure Channel](https://docs.microsoft.com/en-us/windows/win32/secauthn/secure-channel) and [CryptoAPI](https://docs.microsoft.com/en-us/windows/win32/seccrypto/cryptography-functions#certificate-trust-list-functions) for Windows and [Secure Transport](https://developer.apple.com/documentation/security/secure_transport) and [Security framework](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/trust?language=objc) for macOS.

## What’s next for trust stores in Python?

Python's `ssl` module is married to the OpenSSL API in multiple places. Even on Windows and macOS Python ships with its own version of OpenSSL for each platform to use with the `ssl` module. Because of this Python's trust store APIs are similarly OpenSSL-centric, allowing you to specify "[verify locations](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.load_verify_locations)" as a file, directory, or in-memory certificate data.

Non-Python native applications are unlikely to use this method, instead they defer to the operating system's trust store implementation to verify certificates, establish a TLS connection, or send an HTTP request over HTTPS.

### Prior art in PEP 543

[PEP 543](https://www.python.org/dev/peps/pep-0543) put forward a proposal for new TLS APIs for Python which are implementation agnostic and not tied to OpenSSL to open the door for alternate TLS implementations. The PEP contains a lot of discussion about trust stores and wanted to credit [Cory Benfield](https://github.com/Lukasa) and [all the authors and reviewers](https://www.python.org/dev/peps/pep-0543/#toc-entry-27) for their work on the PEP.

The [problems listed in the PEP](https://www.python.org/dev/peps/pep-0543/#problems) are mostly in the same state as they were in 2016 when the PEP was proposed. I recommend reading the PEP for historical context.

### The end of certifi

[Certifi](https://github.com/certifi/python-certifi) is a [repackaging of Mozilla’s CA bundle](https://hg.mozilla.org/releases/mozilla-beta/file/tip/security/nss/lib/ckfw/builtins/certdata.txt) meant to be a stopgap for the problem on Windows and macOS not having a single CA bundle to configure OpenSSL to use. Certificates are bundled into the certifi package and then a single API, `certifi.where()` will return the location on disk of the unbundled certifi certificates, typically somewhere within your `venv/lib/python/.../site-packages/...` directory.

This seems like a fine solution at first, but from the perspective of a system operator this is a nightmare. You now have tons of different CA bundles that are tough to track, usually per-application, and can easily get out of date. This is another big win when all applications use a single OS trust store instead of one trust store per application.

A small experimental package written by Python core developer [Christian Heimes](https://github.com/tiran) tries to solve this problem. The package [certifi-system-store](https://github.com/tiran/certifi-system-store) will rewrite the dist-info of the certifi package to point to the "actual" OS trust store instead of certifi's bundled trust store. However this solution is experimental, requires running a command after installation, and only works on Linux which is a platform that's already covered by not using certifi and using `ssl.create_default_context()` instead.

### The future is OS trust stores

The APIs mentioned above will likely stabilize and be available in a future Python version. My hope is before Python 3.10+ becomes pervasive there will be an effort to implement OS trust stores such that they can be used seamlessly by libraries and applications. We have many developers (myself included) that would be interested in helping make certificate verification better for everyone in our ecosystem.
