# Review of 2019 for urllib3

[urllib3](https://github.com/urllib3/urllib3) has had probably one of it's most eventful years in recent times,
especially with regards to sustainability of the project thanks to sponsors and grants.

I'm looking forward to 2020 and have many ideas for where the project is headed that I'll
be sharing in a future post. For now let's review what was accomplished in 2019:

## Grants and Sponsorships

urllib3 received **$23,580** USD throughout the year of 2019.
We're very grateful for our donators and sponsors, this year
would not have been as productive without you. Thank you!

Here's the breakdown on where that money came from:

- Grant from [CERT Governmental Luxembourg](https://www.govcert.lu) for **$10,944**
- Grant from [GitCoin Grants](https://gitcoin.co/grants/65/urllib3) for **$7,636** (1 DAI ~ $1)
- Sponsorship from [Tidelift](https://tidelift.com/lifter/search/pypi/urllib3) for **$5,000**

The breakdown above shows that most of our funding for this year came from grants.
Hopefully we can continue this into 2020 as the major accomplishments for the project
were completed as a result of dedicated developer(s) spending extended periods of time
working on features.

If you or your organization rely on urllib3 and would like to sponsor urllib3's development
send an email to `sethmichaellarson@gmail.com` and `andrey.petrov@shazow.net`. 

## Releases and Changes

urllib3 made 10 releases during 2019, up from only 3 releases during 2018.
The highlights of those releases include:

- Strict compliance to RFC 3986 for URL parsing.
  This functionality was implemented as a part of the two grants
  listed above and helped protect users from the new class of
  attacks related to URL parsers. See CVE-2019-9740, CVE-2019-9636, CVE-2019-10160.

- Added support for TLSv1.3 for OpenSSL 1.1.1+. This functionality was implemented
  as a part of the grant from GOVCERT LU. TLS 1.3 adds additional security and
  performance benefits for HTTPS connections.

- Added automatic downstream integration testing for Requests and Botocore
  and automated deploys to PyPI from CI. This means we can ship releases more frequently
  and also be more confident that the changes being made won't break the universe.
  Our CI was also augmented to be less flaky resulting in smoother merges for Pull Requests.
  This work was done as a part of both above grants.

- Added support for Brotli as a `Content-Encoding`. This means that if the requested website
  also supports Brotli your response bodies will be even smaller than gzip and save bandwidth.

- Added support for Python 3.8. Python 3.9 alphas have just started coming out and there are
  already issues on the horizon.

## Other Achievements

These achievements aren't related to library features but are still super-fun to celebrate!

- [We eclipsed 1 billion (1,000,000,000) total downloads on PyPI](https://twitter.com/sethmlarson/status/1182710786436882435),
  something that only ~10 projects have done. This number is unimaginably large and shows
  how essential a secure HTTP client library is to the Python ecosystem.

- [We receive a majority of our downloads from Python 3.X instead of Python 2.X](https://twitter.com/llanga/status/1204820198894772224)
  for the first time. About ~50% of all downloads still come from Python 2.7 but that number is very slowly decreasing
  over time.

- [We have a logo now](https://github.com/urllib3/urllib3) thanks to Ryan Feeley and Jess Shapiro! ♥
