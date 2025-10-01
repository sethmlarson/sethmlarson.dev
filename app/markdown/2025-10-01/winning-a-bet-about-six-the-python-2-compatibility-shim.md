# Winning a bet about “six”, the Python 2 compatibility shim

Exactly five years ago today [Andrey Petrov](https://shazow.net) and I made a bet about whether
“[`six`](https://pypi.org/project/six)”, the compatibility shim for Python 2 and 3 APIs, would
still be in the top 20 daily downloads on PyPI. I said it would,
Andrey took the side against.

Well, today I can say that I've won the bet. When the bet
was placed, `six` was #2 in terms of daily downloads
and [today `six` is #14](https://pypistats.org/top).
Funnily enough, `six` was still exactly #14 back in 2023:

> “six is top 14 after 3 years, 2 years left,
> sounds like [Andrey] is winning”<br>
> -- [Quentin Pradet](https://quentin.pradet.me) (2023-07-09)

`six` itself isn't a library that many use on its own,
as [at least 96% of `six` downloads](https://pypistats.org/packages/six) come from Python 3 versions. Instead,
this library is installed because other libraries depend on the library.
Here are the top packages that still depend on `six`:

<table style="margin-left: auto;margin-right: auto;font-variant-numeric: tabular-nums;">
<thead>
<tr>
  <th>Package</th>
  <th>Downloads / Day</th>
  <th>Last Uploaded</th>
</tr>
</thead>
<tbody>
<tr>
  <td>python-dateutil</td>
  <td>22M</td>
  <td>2024-03-01</td>
</tr>
<tr>
  <td>yandexcloud</td>
  <td>6M</td>
  <td>2025-09-22</td>
</tr>
<tr>
  <td>azure-core</td>
  <td>4M</td>
  <td>2025-09-11</td>
</tr>
<tr>
  <td>jedi</td>
  <td>2M</td>
  <td>2024-11-11</td>
</tr>
<tr>
  <td>kubernetes</td>
  <td>2M</td>
  <td>2025-06-09</td>
</tr>
<tr>
  <td>rfc3339-validator</td>
  <td>2M</td>
  <td>2021-05-12</td>
</tr>
<tr>
  <td>google-pasta</td>
  <td>1M</td>
  <td>2020-03-13</td>
</tr>
<tr>
  <td>confluent-kafka</td>
  <td>1M</td>
  <td>2025-08-18</td>
</tr>
<tr>
  <td>oauth2client</td>
  <td>1M</td>
  <td>2018-09-07</td>
</tr>
<tr>
  <td>ecdsa</td>
  <td>1M</td>
  <td>2025-03-13</td>
</tr>
</tbody>
</table>

These packages were found by querying [my own dataset about PyPI](https://github.com/sethmlarson/pypi-data):

```sql
SELECT packages.name, packages.downloads
FROM packages JOIN deps ON packages.name = deps.package_name
WHERE deps.dep_name = 'six'
GROUP BY packages.name
ORDER BY packages.downloads DESC
LIMIT 10;
```

Notice how a single popular library, `python-dateutil`, keeping `six`
as a dependency was enough to carry me to victory.
Without `python-dateutil` I likely would have lost this bet.
I also wanted to note the "last uploaded" dates, as some of the libraries
aren't uploaded frequently, potentially explaining why they still depend on `six`.

> “surely in 10 years, six won't be a thing. right? RIGHT?”<br>
> -- Andrey Petrov (2020-10-01)

We'll see! ;) Thanks to [Benjamin Peterson](https://www.locrian.net/) for creating and maintaining `six`.