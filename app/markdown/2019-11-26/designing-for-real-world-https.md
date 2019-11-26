# Designing for Real-World HTTPS

Users care about security, privacy, and above all, for their HTTP client library to work.
When TLS or certificate issues get in the way of making requests to a web server
oftentimes users will insecurely configure their HTTP client.

And who can blame them when they don't have the documentation or tools to make proper
security decisions in a world full of legacy software and mis-configured servers?

This post discusses how to design an HTTP client for better security and user-experience.
There's a lot of additional / optional readings linked in this post. I encourage you if you
want to learn a whole lot more to take a look at those resources too.

## What is HTTPS?

HTTPS is defined in [RFC 2818](https://tools.ietf.org/html/rfc2818) as "HTTP over TLS".
If you're unsure what TLS is, you can read
[this explanation by Cloudflare](https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/).

## How do users typically solve TLS issues?

If you type "[requests certificate verify failed](https://www.google.com/search?q=requests+certificate+verify+failed)"
into Google the top result you'll receive is this [StackOverflow answer](https://stackoverflow.com/a/12864892)
which (among some good advice) mentions `verify=False` which disables certificate verification.

This will certainly allow your request to "succeed" but will also severely degrade the
security of the HTTPS requests being made.

The warnings against using `verify=False` within the StackOverflow answer may persuade some,
but searching ["`verify=False`" in Python code on GitHub](https://github.com/search?l=Python&q=%22verify%3DFalse%22&type=Code)
yields >150,000 results.

**Our goal as an interface designer is to keep verification on!**

## What issues do users experience?

Imagine you're trying to interact with an external service as a part of
your job via HTTP and of course, you want to use HTTPS because that's the proper thing to do!

The website's hostname is `tribunnews.com` which just so happens to
be at the time of this writing #41 most visited website in the world.
You'd expect them to have a proper TLS config, right?

When you make an HTTPS request to the website you receive this error:

```console
[SSL: UNSUPPORTED_PROTOCOL] unsupported protocol (_ssl.c:1108)
```

Now without using Google, can you figure out what this error means
and what you should do to fix it?

If you guessed that the server only supports TLSv1.0, you'd be right!
The client library you're using needs to be configured to use TLSv1.0
which is considered an insecure protocol to use nowadays.

After configuring your client properly (if you're able to!) you make
another request, this time receiving this:

```console
[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1108)
```

At this point unfortunately you're out of luck, because the website presents a certificate
with two `subjectAltName` entries:

- `*.maintenis.com`
- `maintenis.com`

... neither of which match our intended target website `tribunnews.com`.

When a certificate error occurs **we can't be certain that the web server we're talking to is
the one we intend to be talking to**, so now what? What would you do in this situation?

If you guessed using `www.tribunnews.com` (???) you'd be correct! Using the `www` sub-domain gets you the
website you want with all proper TLS configuration and certificates.

Browsers are smart and try `www` if the host is a privately-registrable domain name and the connection fails
for any reason, so the website works fine for browsers but doesn't work for our HTTP clients... **What a nightmare!**

Now try solving these problems under a time crunch and without a deep knowledge
of TLS and Public Key Infrastructure. You can now hopefully see why users disable
security features to mitigate TLS issues.

## More Examples of HTTPS Issues

Issues when using HTTPS can be categorized into two different groups,
TLS issues and certificate issues. TLS issues are usually to do
with the TLS protocol itself, things like not supporting the same TLS version,
having no ciphers shared between the client and server,
or sending incorrect data during the TLS handshake.

I've found that certificates issues tend to occur more frequently compared to
TLS protocol issues so I've focused on them below.

Here is the list of sources that I've looked through to find examples of these issues:

- [Stackoverflow 'python-requests' Tag](https://stackoverflow.com/questions/tagged/python-requests)
- [requests Issue Tracker](https://github.com/psf/requests/issues)
- [urllib3 Issue Tracker](https://github.com/urllib3/urllib3/issues)

I've also ran TLS handshakes on the top 10,000 domains in the Alexa 1 Million and
kept the results of all domains where the TLS handshake failed when configured
with [`certifi`](https://github.com/certifi/python-certifi) (a common choice for Python HTTP libraries
as a default CA certificate bundle) and with all TLS 1.2+ and all ciphers. 

All of these below issues can be found at least once in the top 10,000 domains.

### Certificate Doesn't Have a `subjectAltName`, only `commonName`

`commonName` was deprecated over 19 years ago in
[RFC 2818](https://tools.ietf.org/html/rfc2818#section-3.1). Here's the
exact language:

```
If a subjectAltName extension of type dNSName is 
present, that MUST be used as the identity. Otherwise,
the (most specific) Common Name field in the Subject
field of the certificate MUST be used. Although the
use of the Common Name is existing practice, it is
deprecated and Certification Authorities are encouraged
to use the dNSName instead.
```

Which unfortunately says that `commonName` must be used if there
are no `subjectAltName` `dNSName` entries. Meaning it's totally
valid for CAs to keep minting certificates with common names.

This means we probably need to keep supporting a way to verify
certificates via `commonName` for the time being.

Thankfully browsers and macOS are driving the world of standards
forward by removing support for common name.
[macOS dropped common name support completely in iOS 13 / macOS 10.15](https://support.apple.com/en-us/HT210176):

```
TLS server certificates must present the DNS name of
the server in the Subject Alternative Name extension
of the certificate. DNS names in the CommonName of a
certificate are no longer trusted.
```

Nothing like your website not working on Chrome, Firefox, macOS and iPhones
to make a business want to upgrade their certificate.

### Certificate is Self-Signed

This can be the case for a real web server, a certificate created for a
single peer-to-peer connection like two devices being manufactured together,
or most likely: a user-generated certificate for integration testing.

In this case, especially when the certificate is available to the
user and can be verified locally, [Certificate Pinning](https://www.owasp.org/index.php/Certificate_and_Public_Key_Pinning)
solves this problem! Certificate pinning is where you hard-code the signature
or fingerprint of the certificate you're expecting to be presented
in the handshake and if you receive a certificate with the same
fingerprint then the certificate is automatically trusted. 

Using certificate pinning is a form of
["Trust on First Use"](https://en.wikipedia.org/wiki/Trust_on_first_use)
which is nearly as secure as verifying a certificate using PKI and CA certs
except for the very first TLS handshake where you make the first "trust" decision yourself.

(**NOTE:** Certificate Signatures / Fingerprints are different from Certificate Thumbprints.
The former is used for cryptographic reasons, the second is for referencing only.)

Certificate pinning also works fairly well when the certificate
can't be verified locally, like when making a request to the Internet
because certificates that have short life-spans like LetsEncrypt are likely
to verify properly so unlikely to need certificate pinning.

The tough part about this feature is that error messages and documentation
don't usually recommend using the feature as an alternative to
disabling certificate verification. It's also non-trivial to calculate
the certificate fingerprint by hand.

Certificate pinning is currently supported by
[`urllib3`](https://urllib3.readthedocs.io/en/latest/reference/index.html#urllib3.connection.VerifiedHTTPSConnection.assert_fingerprint) and
[`aiohttp`](https://aiohttp.readthedocs.io/en/stable/client_reference.html#aiohttp.Fingerprint).
Requests doesn't provide a way to natively verify a certificate via a fingerprint.

Client libraries should use only `SHA256` or stronger because `MD5` is insecure and `SHA1` is on the edge of insecure.

Client libraries should also ensure users are aware of the pitfalls and dangers associated with
updating the certificate fingerprint or using certificate pinning with certs that are liable to change
frequently like certificates that are short-lived (~less than 6 months to expiry). 

### Certificate `subjectAltName` or `commonName` Doesn't Match Host

In this case the web server is presenting a certificate that we'd
be able to verify with our cert trust store but the fields for
verifying the hostname aren't the same as the host we're connecting to.

For this situation the most useful information for the user is
to display what the fields are on the certificate along with the
host that they're connecting to. Many libraries won't show the
certificates `subjectAltName` and `commonName` entries in the error.

I've seen this error come up where the service had a unicode hostname
encoded in the certificate with IDNA 2003 because it contained an emoji
(which is invalid in IDNA 2008), but urllib3 no longer supported IDNA 2003
due to security issues with URL parsing.

WHATWG-URL recommends falling back on IDNA 2003, but requires a lot of care
to mitigate all security issues related to using the encoding within URLs.

## Recommendations for HTTP Client Libraries

Above all, think about users when designing an interface to configure security.
An interface where it's easy to create secure configurations will result in
better security for every use-case.

Here's a list of elements I think result in such an interface:

### Provide a State-of-the-Art TLS Configuration by Default

90%+ users will be using these defaults so you want them to be the best they can reasonably be.

At the time of writing this means:

- TLSv1.2+ only ([Over 95% of websites support TLSv1.2+](https://www.ssllabs.com/ssl-pulse/))
- [AEAD Ciphers](https://en.wikipedia.org/wiki/Authenticated_encryption) (AES-GCM, CHACHA20)
- Key Exchanges that support [Forward Secrecy](https://scotthelme.co.uk/perfect-forward-secrecy/) (ECDHE, DHE)
- System Certificate Trust Store (This is still an open issue for Python, for now `certifi` is a crutch.)

Here's how to configure the above in Python via `ssl.SSLContext`:

```python
import ssl
import certifi

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
ctx.verify_mode = ssl.CERT_REQUIRED
ctx.load_verify_locations(certifi.where())
ctx.options |= (
    ssl.OP_NO_SSLv2 |
    ssl.OP_NO_SSLv3 |
    ssl.OP_NO_TLSv1 |
    ssl.OP_NO_TLSv1_1 |
    ssl.OP_NO_COMPRESSION
)
ctx.set_ciphers(":".join([
    "ECDHE+AESGCM",
    "ECDHE+CHACHA20",
    "DHE+AESGCM",
    "DHE+CHACHA20"
]))
```


### Don't Allow Users to Disable Certificate Verification

Especially for HSTS domains, where this is a requirement to be compliant
with [RFC 6797](https://tools.ietf.org/html/rfc6797).
Being able to turn off certificate verification results in insecure
software. Using cert pinning is a more secure alternative to disabling verification.

### Provide these Features for Configuring TLS

- Minimum and maximum supported version of TLS.
Recommend strongly that users don't set a maximum version
unless they're targeting one specific version on a single service.

- TLS ciphers should be added / removed depending on
the minimum and maximum TLS version. I don't think direct
access to configuring ciphers should be necessary but make
sure you cover all the common ciphers and key-exchanges.
Look at what Firefox uses as their default for an example.

- An interface to provide a pre-configured `SSLContext` is optional,
in my opinion if an interface wrapping TLS is good enough providing
an interface for `SSLContext` only allows for disabling security features.

- Ability to specify a non-default certificate bundle
or directory of certificates to verify against.
Unfortunately it's optimal to support both an
"additive" method and a "replace" method.

- **Additive** is useful when the rest of your trust store
  is still needed like in the case of a proxy certificate: you
  still want to use your actual trust store to verify
  external services.

- **Replace** is useful when you want to use a singular certificate
  for the requests you're making and don't want to accidentally
  trust a service outside that trust store.

I'd say that the 'additive' use-case is more common with typical
users but supporting both use-cases is important. I need to do
more thinking on this about what a proper interface would look like.

### Support Certificate Pinning as a means of verification

Provide documentation on how to use it, how to update the fingerprint,
and what using certificate pinning means for security.

### Recommend Solutions for Local Testing

For local testing recommend users use [`trustme`](https://github.com/python-trio/trustme)
or [`mkcert`](https://github.com/FiloSottile/mkcert) to generate real
certificates so that HTTPS and TLS function the same locally
as they would in the real world.  This removes the need for disabling verification
during testing or using pinning on a self-signed cert.

### Provide Better Error Messages and Documentation

Error messages should contain all information
they need to make proper security decisions. This includes information
from the certificate. This may require you to use `getpeercert(binary_form=True)`
and parse with a library like [`asn1crypto`](https://github.com/wbond/asn1crypto)
because Python doesn't give you nice parsed certificates unless cert
verification is enabled.

Document common TLS and certificate issues and the recommended
way for mitigating those issues. If possible, provide custom error
types for common issues along with pointers to official documentation
to prevent StackOverflow from recommending insecure configurations
to your users.

### Allow Configuring TLS via Environment Variables

Usually HTTP clients are buried a layer or more deep within an library
or tool being used and may sometimes not provide the means to configure
the HTTP client library properly. Allowing environment variables to
configure the library fixes this issue for users.

Did you have a scenario where the above doesn't work well or you want
to discuss this subject more? I'd love to hear about it, please let me know
by [tagging me Twitter](https://twitter.com/sethmlarson).
