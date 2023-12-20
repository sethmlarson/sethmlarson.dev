# Querying every file in every release on the Python Package Index

<blockquote>
  <center>This critical role would not be possible without funding from the <a href="https://alpha-omega.dev">OpenSSF Alpha-Omega Project</a>. Massive thank-you to Alpha-Omega for investing in the security of the Python ecosystem!</center>
</blockquote>

<div class="row">
<div class="col-6 col-12-sm">
<p>Last week I <a href="https://fosstodon.org/@sethmlarson/111382964885780823">published a graphic</a> showing the use of memory safe and unsafe systems programming
languages in Python packages which garnered some interest from the community how I was
creating such a graphic.

<p>The graphic used file extension information which
isn't a perfect method for detecting other programming languages, but likely good enough for trends and identifying projects.</p>

<p>What is interesting about this graphic is it needs access to files within Python distributions like wheels and source distributions
on PyPI. This is something that's <strong>difficult to access without actually downloading the artifact</strong>. So how
can I query this information for every package since 2005?</p>

<p>I used the <a href="/security-developer-in-residence-weekly-report-16#finding-projects-with-vulnerable-libwebp">same dataset previously</a> to detect vulnerable WebP binaries bundled in Python packages.
Let's explore how to use this dataset to answer other questions!</p>
</div>
<div class="col-6 col-12-sm">
<iframe style="border-radius: 1em;" src="https://fosstodon.org/@sethmlarson/111382964885780823/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="100%" allowfullscreen="allowfullscreen"></iframe><script src="https://fosstodon.org/embed.js" async="async"></script>
</div>
</div>

None of this article would be possible without the work of [Tom Forbes](https://tomforb.es) to create
and continually update this dataset. Thanks Tom for all your work and for helping
me get started.

## Why is this data useful?

I'm also doing work on a few different projects regarding Python packaging metadata, namely
[PEP 639](https://peps.python.org/pep-0639/) and "Tracking bundled projects in Python distributions". Having this dataset available
gives me a bunch of contextual information for those projects as well as being able to
track adoption of new packaging metadata.

There was also a bit of emphasis about memory-safe programming languages in the recent [US Government
RFI](https://www.regulations.gov/document/ONCD-2023-0002-0001), and I was the author for the section regarding memory safety. I wanted to explore the Python package ecosystems' current usage of memory safe languages
like Rust and Go compared to C, C++, and Fortran. From the above graphic it seems there's
some interest in using memory-safe languages which is nice to see.

The need to be able to query this dataset for multiple projects meant it probably made
a bit of sense to create a small utility that can be reused, including by others (yay open source!) I
[created a small Gist](https://gist.github.com/sethmlarson/852341a9b7899eda7d22d8c362c0a095) that includes this utility. It's not optimized (actually quite slow if you
don't use threads when downloading of files).

## Downloading the file metadata dataset

> ⚠️ **WARNING: PLEASE READ!** ⚠️
>
> A word of warning before we start blindly downloading all the things, **these datasets are all very large**, like
> 30+ GB just for the high-level metadata in Parquet files. Make sure you have enough storage space before 
> copying and pasting any commands you see in this blog post. I don't want to hear that anyone's filled up
> their hard-drive without knowing. **You have been warned!** 🐉

With that out of the way, let's get started ourselves! The entire dataset is available under the [pypi-data GitHub organization](https://github.com/pypi-data)
with varying levels of detail all the way from high-level metadata and filenames to actual file contents.

There are many datasets available on [py-code.org/datasets](https://py-code.org/datasets). The Clickhouse dataset isn't completely up-to-date
but as a way to experiment with the dataset it can be an easy place to play around and get started. We want the complete
up-to-date dataset though, so we need to download things locally. We want the "[Metadata on every file uploaded to PyPI](https://py-code.org/datasets#metadata)"
dataset.

To download the dataset there's a series of `curl` commands:

```shell
$ curl -L --remote-name-all $(curl -L "https://github.com/pypi-data/data/raw/main/links/dataset.txt")
```

Two curls in one (at least there's no `... | sudo sh` involved...) let's examine the innermost curl first
and use a local copy instead of fetching from the network:

```shell
$ curl -L "https://github.com/pypi-data/data/raw/main/links/dataset.txt" > dataset.txt
$ cat dataset.txt

https://github.com/pypi-data/data/releases/download/2023-11-12-03-06/index-0.parquet
https://github.com/pypi-data/data/releases/download/2023-11-12-03-06/index-1.parquet
https://github.com/pypi-data/data/releases/download/2023-11-12-03-06/index-10.parquet
https://github.com/pypi-data/data/releases/download/2023-11-12-03-06/index-11.parquet
https://github.com/pypi-data/data/releases/download/2023-11-12-03-06/index-12.parquet
https://github.com/pypi-data/data/releases/download/2023-11-12-03-06/index-13.parquet
https://github.com/pypi-data/data/releases/download/2023-11-12-03-06/index-14.parquet
...
```

It's a list of URLs that all look legit, let's download those (this will take some time):

```shell
$ curl -L --remote-name-all $(cat dataset.txt)
$ ls
index-0.parquet   index-12.parquet  index-1.parquet  index-4.parquet  index-7.parquet
index-10.parquet  index-13.parquet  index-2.parquet  index-5.parquet  index-8.parquet
index-11.parquet  index-14.parquet  index-3.parquet  index-6.parquet  index-9.parquet
```

## Querying the dataset

In order to take full advantage of this dataset we can query the top-level Parquet metadata and subsequently download the underlying individual files only when
necessary. I've created a [small helper as I mentioned earlier](https://gist.github.com/sethmlarson/852341a9b7899eda7d22d8c362c0a095) (`pycodeorg` module below) to assist with these examples.

The dataset uses Parquet as a data storage format which is columnar and can be [queried using DuckDB](https://duckdb.org/). This is the first project I've used DuckDB with and
from first impressions it seems like a lovely piece of software. Before we start creating our query I like to see what the dataset fields and types are so lets run a `DESCRIBE`:

```sql
DESCRIBE SELECT * FROM '*.parquet';

┌─────────────────┬─────────────┬─────────┐
│   column_name   │ column_type │  null   │
│     varchar     │   varchar   │ varchar │
├─────────────────┼─────────────┼─────────┤
│ project_name    │ VARCHAR     │ YES     │
│ project_version │ VARCHAR     │ YES     │
│ project_release │ VARCHAR     │ YES     │
│ uploaded_on     │ TIMESTAMP   │ YES     │
│ path            │ VARCHAR     │ YES     │
│ archive_path    │ VARCHAR     │ YES     │
│ size            │ UBIGINT     │ YES     │
│ hash            │ BLOB        │ YES     │
│ skip_reason     │ VARCHAR     │ YES     │
│ lines           │ UBIGINT     │ YES     │
│ repository      │ UINTEGER    │ YES     │
├─────────────────┴─────────────┴─────────┤
│ 11 rows                       6 columns │
└─────────────────────────────────────────┘
```

Now that we know the form of the dataset we can make our first query. Let's create a query for projects per file extension and split that by month.
That query would look something like this:

```sql
SELECT (
  -- We're bucketing our data by month and extension --
  datetrunc('month', uploaded_on) AS month,
  regexp_extract(path, '\.([a-z0-9]+)$', 1) AS ext,

  -- DuckDB has native list/object manipulation, pretty cool! --
  LIST(DISTINCT project_name) AS projects
)
FROM '*.parquet'
WHERE (
  -- Our regex for matching files for languages we care about --
  regexp_matches(path, '\.(asm|c|cc|cpp|cxx|h|hpp|rs|[Ff][0-9]{0-2}(?:or)?|go)$')

  -- Filter out test files and whole virtual environments --
  -- embedded in Python distributions. --
  AND NOT regexp_matches(path, '(^|/)test(|s|ing)')
  AND NOT contains(path, '/site-packages/')
)
GROUP BY month, ext
ORDER BY month DESC;
```

With this query and some data massaging we can create this graphic and see how Rust is driving the majority
of memory-safe programming language use in binary Python distributions:

<div>
<center>
<img src="https://cdn.fosstodon.org/media_attachments/files/111/410/225/101/983/840/original/71a542db21ab6e7d.png" style="max-width: 100%; height: auto;" alt="Graph of different languages in Python packages over time. Initially was almost all C/C++, now Rust is gaining." title="Graph of different languages in Python packages over time. Initially was almost all C/C++, now Rust is gaining."/>
</center>
</div>

## Accessing file data

Previously it was very difficult to learn about the adoption of new packaging metadata standards
and fields due to the prohibitively large bandwidth, storage, and CPU cost that came with downloading an entire
swath of PyPI and unpack their contents only to examine a small `METADATA` or `WHEEL` file. However, with this dataset
we can write a simple query and fetch only the files we need to get the answers to the above questions:

```sql
SELECT repository, project_name, path
FROM '*.parquet'
WHERE (
  -- We only want distributions uploaded in --
  -- October 2023 for a recent snapshot. --
  datetrunc('month', uploaded_on) = DATE '2023-10-01'

  -- We want .dist-info/WHEEL files from wheels --
  AND regexp_matches(path, '\.dist-info/WHEEL$')

  -- And files shouldn't be skipped since we can't call --
  -- `get_file()` on these, like if they're empty or binaries. --
  -- Pretty unlikely! --
  AND skip_reason == ''
);
```

substitute this query in for the `QUERY` variable below:

```python
import re
import pycodeorg

QUERY = ...

# Find all 'WHEEL' metadata files in wheels:
for repo, project, path in pycodeorg.query(QUERY):

    # Fetch the file data from the dataset
    data = pycodeorg.get_data(repo, project, path)
    
    # Then parse the 'Generator' field and aggregate
    if match := re.search(rb"\nGenerator:\s*([\w]+)", data):
        builder = match.group(1).decode()
        ...
```

This query allows me to provide this data, which to my knowledge isn't available yet
and from this we can answer questions like which wheel builder is most common (which are `bdist_wheel` by a wide margin, then `poetry` and `hatch`)
and which packaging metadata fields are in use. I'm excited to see what other insights folks are able to gather
from using this dataset!

## Other items

* The [Request for Information (RFI) response](https://www.regulations.gov/document/ONCD-2023-0002-0001) for the Python Software Foundation has been submitted. Hope that our submission will be available on regulations.gov soon.
  We'll write a blog post on the PSF blog sharing the response once its available.
* [PyPI's security audit blog post](https://blog.pypi.org/posts/2023-11-14-1-pypi-completes-first-security-audit/) and [corresponding post by Trail of Bits](https://blog.trailofbits.com/2023/11/14/our-audit-of-pypi/) have been published. I didn't work directly on this project but it's so exciting to see the results of this work
  be shared.
* Pushed the blog post announcing the "Becoming a CVE Numbering Authority as an Open Source project"
  into final draft, now working with OpenSSF marketing to schedule the post for the blog.
* Received a [shoutout from Carol Willing](https://twitter.com/tiangolo/status/1723335223750861152) during her keynote at PyCon Sweden. Thanks, Carol!

That's all for this week! 👋 If you're interested in more you can read [next week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-19) or [last week's report](https://sethmlarson.dev/security-developer-in-residence-weekly-report-17).
