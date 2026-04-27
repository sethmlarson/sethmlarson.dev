# pip v26.1 adds support for relative dependency cooldowns

<blockquote>
  <p>My work as the Security Developer-in-Residence at the <a href="https://www.python.org/psf-landing/">Python Software Foundation</a> is sponsored
  by <a href="https://alpha-omega.dev/">Alpha-Omega</a>. Thanks to Alpha-Omega for supporting
  security in the Python ecosystem.</p>
</blockquote>

<!-- more -->

I [published a blog post](https://sethmlarson.dev/pip-relative-dependency-cooling-with-crontab) two months ago about how to [hack relative dependency
cooldowns into pip v26.0](https://sethmlarson.dev/pip-relative-dependency-cooling-with-crontab) with crontab. Now with [pip v26.1 available](https://discuss.python.org/t/announcement-pip-26-1-release/107108), this hack is no longer required!
Time to upgrade my pip and delete that cron job...

Now in [pip v26.1](https://discuss.python.org/t/announcement-pip-26-1-release/107108) you can use `uploaded-prior-to` in your `~/.config/pip/pip.conf` file
or `--uploaded-prior-to=` as a CLI option with relative RFC 3339 duration values. pip supports
setting days using “`PND`” where `N` is the number of days.

<!-- more -->

For example, using the following as your `~/.config/pip/pip.conf` file
will only install packages that are at least 7 days old on the Python Package Index:

```ini
[install]
uploaded-prior-to = P7D
```

Because this setting is in your global pip config, it means that
you won't have to remember to set the option when invoking `pip install`.
Using a relative value also means you won't have to repeatedly
set new dates to receive new releases of the packages you use.

Using relative dependency cooldowns means that installing directly from a public
index such as the [Python Package Index](https://pypi.org) (PyPI) will benefit from [manual
malware reporting, triaging, and removal efforts](https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/). The vast majority of
malware and supply chain attacks published are detected and removed within
hours of being uploaded to the index. [Using relative dependency cooldowns](https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/#protecting-yourself-as-a-developer) means indexes have time to respond
to malicious software and keep you safe.

Reminder that dependency cooldowns should be paired with a vulnerability
upgrade strategy that prioritizes dependency releases with associated
vulnerabilities. You don't want to be waiting for days for a dependency
cooldown to clear if your service is vulnerable. Managing, reviewing,
upgrading, and deploying vulnerability patches should be a deliberate
task, not one that happens "on-accident" due to an upgrade-by-default
installation strategy.

Andrew Nesbitt has published a [comprehensive review of dependency cooldowns](https://nesbitt.io/2026/03/04/package-managers-need-to-cool-down.html)
across many different package managers. Thanks to William Woodruff who
[originally published this approach](https://blog.yossarian.net/2025/11/21/We-should-all-be-using-dependency-cooldowns).
