# Relative “Dependency Cooldowns” in pip v26.0 with crontab

> **WARNING:** Most of this blog post is
  a hack, everyone should probably just
  wait for relative dependency cooldowns to come
  to a future version of pip.

<!-- more -->

pip v26.0 [added support for the `--uploaded-prior-to` option](https://ichard26.github.io/blog/2026/01/whats-new-in-pip-26.0/#excluding-distributions-by-upload-time).
This new option enables implementing “[dependency cooldowns](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns)”, a technique
described by [William Woodruff](https://yossarian.net), that provides simple but effective
protections for the [relatively short attack-window time](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns#fn:filippo:~:text=Approx%2E%20Window%20of%20Opportunity)
of malware published to public software repositories. This brings the
reaction time to malware back within the realm of humans, who sometimes need to
execute manual triage processes to take down malware from PyPI.

<!-- more -->

So if you set `--uploaded-prior-to` to 7 days before this post
was published, February 25th, you'd do so like this:

```
python -m pip install \
  --uploaded-prior-to=2026-02-25 \
  urllib3
```

But this is only an absolute date, and we have to remember
to set the option on each call to `pip install`? That seems like
a lot of work!

Dependency cooldowns work best when the policy can be set in a
[global configuration file to a relative value](https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html)
like “7 days”.  The “window” of acceptable packages is then automatically updating over time
without needing to set a new absolute value constantly. “Set-and-forget”-style.

uv allows [setting a relative value](https://docs.astral.sh/uv/guides/scripts/#improving-reproducibility) via `--exclude-newer`,
but pip [doesn't support relative ranges yet](https://github.com/pypa/pip/issues/13674). I mostly use pip and still wanted to test this feature today, so I
created a little hack to update my user `pip.conf` configuration file
on a regular basis instead. Here's what my `pip.conf` file looks like:

```editorconfig
[install]
uploaded-prior-to = 2026-02-25
```

And below is the entire Python script doing the updating. Quick reminder that
I only tested this on my own system, your mileage
may vary, do not use in production.

```python
#!/usr/bin/python3
# License: MIT

import datetime
import sys
import os
import re

def main() -> int:
    # Parse the command line options.
    pip_conf = os.path.abspath(os.path.expanduser(sys.argv[1]))
    days = int(sys.argv[2])

    # Load the existing pip.conf file.
    try:
        with open(pip_conf, "r") as f:
            pip_conf_data = f.read()
    except FileNotFoundError:
        print(f"Could not find pip.conf file at: {pip_conf}")
        return 1

    # Update the existing uploaded-prior-to value.
    uploaded_prior_to_re = re.compile(
        r"^uploaded-prior-to\s*=\s*2[0-9]{3}-[0-9]{2}-[0-9]{2}$", re.MULTILINE
    )
    if not uploaded_prior_to_re.search(pip_conf_data):
        print("Could not find uploaded-prior-to option in pip.conf under [install]")
        return 1
    new_uploaded_prior_to = (
        datetime.date.today() - datetime.timedelta(days=days)
    ).strftime("%Y-%m-%d")
    pip_conf_data = uploaded_prior_to_re.sub(
        f"uploaded-prior-to = {new_uploaded_prior_to}", pip_conf_data
    )

    # Write the new uploaded-prior-to
    # value to pip.conf
    with open(pip_conf, "w") as f:
        f.write(pip_conf_data)
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

The script takes two parameters, your `pip.conf` file you want
to update (typically `~/.config/pip/pip.conf` on Linux) and
an integer number of days. I used 14 in my cron example below.

Simple right? I installed and `chmod u+X`-ed the script in my `/usr/local/bin` directory
and then added to my crontab using `crontab -u (USERNAME) -e`:

```
0 * * * * (/usr/local/bin/pip-dependency-cooldown /home/sethmlarson/.config/pip/pip.conf 14)  2>&1 | logger -t pip-dependency-cooldown
```

This pattern will run the script once per hour and update the value
of `uploaded-prior-to` to the new day. Now I only receive packages that
were published 14 or more days ago by default when running `pip install` without any other options.

Stay tuned for more about dependency cooldowns for Python installers
once pip supports relative values.
