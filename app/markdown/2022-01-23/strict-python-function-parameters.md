# Strict Python function parameters

**What do you think about when writing a new function in Python?** The function name, parameter names, optional/required parameters, and default arguments are all on the list. Here is a simple Python function that has all these covered:

```python
def process_data(data, encoding="ascii"):
   # Fancy data processing here!
```

However, there's one aspect many programmers have an opinion about but don't realize can be encoded into the function definition: **How should callers specify each argument to the function?** For the above function you'd likely document the following usages:

```python
process_data(b"input")

process_data(b"input", encoding="utf-8")
```

You don't need to specify `data=` for readers to infer what the first argument is likely to be. The parameter name is hinted by the function name: `process_data()`. On the other hand the `encoding` parameter isn't obvious if you only see the argument value. Given this I would recommend using a keyword argument for `encoding`.

The above decisions make sense to me having written lots of Python, but what about beginners to Python or the library? **Function parameters don't explain "how" to pass arguments.** Whether an argument is passed as a positional argument or keyword argument is *usually* up to the caller. Below are all the ways to specify the same parameters, but many are likely not what the author intended:

```python
# All positional parameters, tougher to
# infer the parameter for 'utf-8'.
process_data(b"input", "utf-8")

# Using `data` as keyword argument, but
# not as clean as "data" term is duplicated.
process_data(data=b"input")
process_data(data=b"input", encoding="utf-8")

# All keyword parameters but encoding
# and data are flip-flopped.
process_data(encoding="utf-8", data=b"input")
```

If the code is widespread enough you're almost guaranteed that [someone is using your code in a way you didn't intend](https://xkcd.com/1172). Let's see two Python features you can use to avoid this problem: 

## Keyword-only parameters

[PEP 3102](https://www.python.org/dev/peps/pep-3102) introduced this language feature in 2006 for Python 3.0 and later. Despite being in a ecosystem without Python 2 for two years I'm surprised how little I see this feature.

Defining a parameter as being "keyword-only" looks like this:

```python
def process_data(data, *, encoding="ascii"): ...
```

Notice the `*` between `data` and `encoding`? The asterisk means that **all parameters to the right in the function signature can't be passed as positional arguments**. These parameters are now "keyword-only".

Now that the `encoding` parameter is a keyword-only how does the list of potential usages change?

```python
# The way you want users to use the function:
process_data(b"input")
process_data(b"input", encoding="utf-8")

# Raises a TypeError:
process_data(b"input", "utf-8")

# What way can (and will) use the function:
process_data(data=b"input")
process_data(data=b"input", encoding="utf-8")
process_data(encoding="utf-8", data=b"input")
```

It's a small improvement but there's more we can do!

## Positional-only parameters

[PEP 570](https://www.python.org/dev/peps/pep-0570) introduced another feature for specifying how to pass arguments. This feature landed in Python 3.8 so you may not be able to use it in projects supporting Python 3.7 [until mid-2023](https://endoflife.date/python).

You can define "positional-only" argument in Python like so:

```python
def process_data(data, /, encoding="ascii"): ...
```

The `/` in the function signature means that all parameters to the left of the `/` are positional-only. Positional-only parameters can't be passed a keyword argument:

```python
# This will raise a TypeError:
process_data(data=b"input")
```

Many functions in the standard library don't follow the typical rules for parameters.  The example used in PEP 570 is the [`pow()` function](https://docs.python.org/3/library/functions.html#pow). When called with keyword arguments `pow()` will fail because the underlying C implementation only accepts positional arguments:

```python
# The `help()` output for `pow()` used
# the `/` character even before Python
# 3.8 implemented PEP 570:
>>> help(pow)
...
pow(x, y, z=None, /)
...

>>> pow(x=5, y=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pow() takes no keyword arguments
```

## Putting it all together

You can use both positional-only and keyword-only arguments together in the same function signature:

```python
def process_data(data, /, *, encoding="ascii"): ...
```

And now with `data` being positional-only and `encoding` keyword-only let's look at how our function can be used:

```python
# The way you want users to use the function:
process_data(b"input")
process_data(b"input", encoding="utf-8")

# Raises a TypeError:
process_data(b"input", "utf-8")
process_data(data=b"input")
process_data(data=b"input", encoding="utf-8")
process_data(encoding="utf-8", data=b"input")
```

**Success!!** 🎉 Your function now only allows specifying arguments as intended.

## Why use strict function signatures?

So why go through this extra bit of trouble? You could read the "motivation" sections of [PEP 3102](https://www.python.org/dev/peps/pep-3102/#rationale) and [PEP-570](https://www.python.org/dev/peps/pep-0570/#motivation) for some of the reasons why these features are useful. Below are a few reasons that I think are important from an API design perspective:

### Less to consider when your function changes

Here's a real-life example I had to handle with the [Elasticsearch Python client](https://github.com/elastic/elasticsearch-py). We have an API method called `get()` which fetches a document from Elasticsearch by its ID. The function signature was going to change in v8.0.0 due to the `doc_type` parameter being deprecated server-side in v7.0.0 and scheduled for removal in v8.0.0.

```python
# Function signature in v7.16.0
def get(index, id, doc_type=None, params=None, ...): ...

# Function signature in v8.0.0
def get(index, id, params=None, ...): ...
```

If the `doc_type` parameter were removed without mitigation, code using `get()` would change between v7.16 and v8.0.0:

```python
client.get("1", "2", "3")

# In 7.16.0 the above arguments will
# be assigned like so:

# {index=1, id=2, doc_type=3}

# In 8.0.0 (if not mitigated) the above
# arguments would be assigned like so:

# {index=1, id=2, params=3} (not good!)
```

We started emitting a `DeprecationWarning` whenever `doc_type` was used, but warnings are opt-in and can be missed. So in addition to deprecating parameters we decided to deprecate using positional arguments and require using only keyword arguments for all Elasticsearch API methods in v8.0.0. **Now parameters can be added and removed without considering the parameters' position in previous versions.**

This change also meant the API generator logic could be greatly simplified because the generator no longer needed to account for the order parameters were previously generated with.

**There's additional API freedoms when using positional-only arguments too.** Recall the `process_data()` function defined above:

```python
def process_data(data, /, *, encoding="utf-8"): ...
```

If you now wanted the `data` parameter to accept either a single `bytes` instance or a list of `bytes` instances you might want to rename the parameter to better represent the accepted types. **If `data` is a positional-only parameter then you can rename the parameter without breaking anyone**. Without being a positional-only argument you risk breaking users specifying `data` with a keyword argument:

```python
# You can rename 'data' -> 'data_or_list'
# without breaking anyone's code.
def process_data(data_or_list, /, *, encoding="utf-8"): ...
```

For more information there's an ["Empowering Library Authors" section in PEP 570](https://www.python.org/dev/peps/pep-0570/#id27) that details other cases.

### Consistency between documentation and usage

Ideally documentation will pick a single way of using each function and be consistent within itself. **Why not require users to use functions as they are documented?** If urllib3 was being written today the function signature for `request()` might look like this with `method` and `url` being positional-only and all other parameters being keyword-only:

```python
def request(method, url, /, *, headers=None, ...): ...
```

This function is found *everywhere*, even across other HTTP client libraries like Requests and aiohttp, so is likely to be understandable to users who have never used urllib3.

```python
# We're used to seeing this everywhere:
request("GET", "https://example.com", headers={...})

# These aren't as immediately recognizable:
request(method="GET", url="https://example.com")
request("GET", "https://example.com", {...})
```

By having a strict function signature we can ensure code written by users will look recognizable to future readers.
