# Easily create co-authored commits with GitHub handles

You can [add co-authors to a GitHub commit](https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors) using the `Co-authored-by`
field in the git commit message. But what if your co-author doesn't have a
public email address listed on GitHub?

No problem, you can use this handy
script to automatically discover a users' display name and per-account
"noreply" email address that'll mark their account as a co-author
without a public email address.

<!-- more -->

```bash
#!/bin/bash
login="$@"
read id display_name < <(echo $(curl -s "https://api.github.com/users/$login" | jq -r '.id, .name'))
echo "Co-authored-by: $display_name <$id+$login@users.noreply.github.com>"
```

I've added this script to my `PATH` in a file named `coauthoredby`, so I can call the script like so:

```terminaloutput
$ coauthoredby sethmlarson
Co-authored-by: Seth Michael Larson <18519037+sethmlarson@users.noreply.github.com>
```

And this can be used auto-magically with multi line git commits,
so if I'm trying to credit [Quentin Pradet](https://github.com/pquentin) as a coauthor I'd do this:

```terminaloutput
$ git commit -m "Fixing bugs as usual
>
> $(coauthoredby pquentin)"
```

Resulting in this git commit message:

```terminaloutput
$ git log

Author: Seth Michael Larson <sethmichaellarson@gmail.com>
Date:   Fri Oct 24 11:07:55 2025 -0500

    Fixing bugs as usual
    
    Co-authored-by: Quentin Pradet <42327+pquentin@users.noreply.github.com>
```