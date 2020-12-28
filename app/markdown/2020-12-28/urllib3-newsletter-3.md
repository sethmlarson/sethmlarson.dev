# urllib3 Newsletter #3

Welcome to our third newsletter! If you'd like to join our
community you can [find us on Discord](https://discord.gg/CHEgCZN).

## GitHub Sponsors

[Starting in December the urllib3 organization is now on GitHub Sponsors!](https://github.com/sponsors/urllib3)

Big thank you to the generous individuals who started supporting us:

- [@Lukasa](https://github.com/Lukasa)
- [@cosmin](https://github.com/cosmin)
- [@jefftriplet](https://github.com/jefftriplet)
- [@tyrelsouza](https://github.com/tyrelsouza)
- [@mmchugh](https://github.com/mmchugh)
- [@filepreviews](https://github.com/filepreviews)
- [@adripwn](https://github.com/adripwn)

If you or your organization uses Python: consider sponsoring our team's effort to keep urllib3 maintained
and to ship urllib3 v2 in 2021, we really appreciate it!

In addition to GitHub Sponsors we also use [GitCoin Grants](https://gitcoin.co/grants/65/urllib3)
if you'd like to support us with cryptocurrency.

## Speaking at PyCascades 2021 about urllib3 v2

I'm very excited to announce that I will be [speaking about urllib3's upcoming breaking changes](https://2021.pycascades.com/talks/shipping-breaking-changes-as-the-most-downloaded-python-package/)
at [PyCascades 2021](https://2021.pycascades.com) happening on February 19th - 21st. More info on their site.

Specifically the talk will be about how our team plans on minimizing the impact of breaking changes
given how ubiquitous urllib3 is in the Python ecosystem and what these changes mean
for the future of urllib3.

Can't wait to see you all in the virtual audience!

## Removing code for v2

Tis the season of de-cluttering! Now that the main branch is devoted to v2 development
the urllib3 team has been removing legacy code like it's going out of style.

Since the last newsletter was released on November 13th of this year, we've removed the following:

- Removed Python 2 and 3.5 support
- Removed Google App Engine Standard support
- Removed vendored `six` dependency
- Removed deprecated commonName support
- Removed deprecated Retry options
- Removed deprecated `socket.error` (use `OSError` instead)
- Removed `strict` parameter
- Removed backported `socket.makefile()`
- Removed backported `hmac.compare_digest()`
- Removed backported `SSLContext`

and more! Adding up all the removed lines of code results in a reduction of ~3500 lines,
a massive amount! And there's likely still some more to come, stay tuned!

## HTTPS Proxy support for Botocore

Support for HTTPS proxies landed in urllib3 v1.26 thanks to our own [Jorge Lopez-Silva](https://github.com/jalopezsilva)
HTTPS proxy support [has been added to a botocore feature branch](https://github.com/boto/botocore/pull/2219)
thanks to Jorge as well!  There is no public release available with the support yet
but hopefully in the new year we'll see HTTPS proxies natively supported.
