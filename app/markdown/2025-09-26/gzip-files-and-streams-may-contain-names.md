# GZipped files and streams may contain names

It's just another day, you're sending a bunch of
files to a friend. For no particular reason you
decide to name the archive with your controversial movie opinions:

```shell
$ tar -cf i-did-not-care-for-the-godfather.tar *.txt
$ gzip i-did-not-care-for-the-godfather.tar
```

<!-- more -->

Realizing you'd be sharing this file with others, you decide
to rename the file.

```shell
$ mv i-did-not-care-for-the-godfather.tar.gz \
     i-love-the-godfather.tar.gz
```

That's better! Now your secret is safe. You share the tarball with your colleague
who notes your "good taste" in movies and proceeds to extract the archive.

```shell
$ gunzip --name i-love-the-godfather.tar.gz 

i-love-the-godfather.tar.gz:	 100.0% --
replaced with i-did-not-care-for-the-godfather.tar
```

Uh oh, your secret is out! The decompressed `.tar` file was named `i-did-not-care-for-the-godfather.tar`
instead of `i-love-the-godfather.tar` like we intended. *How could this happen?*

It turns out that GZip streams have fields for information about the original file
including the [filename](https://www.rfc-editor.org/rfc/rfc1952.html#:~:text=%20(if%20FLG.FNAME%20set)), modified timestamp, and comments.
This means GZip streams can leak secret information if it's contained within the file metadata.
Luckily `tar` when using `$ tar -czf` (which is the typical workflow) instead of the `gzip` and `gunzip` commands
doesn't preserve the original filename in the GZip stream.

If you do have to use `gzip`, **use the `--no-name` option to strip this information
from the GZip stream.** Use a hex editor to check a GZip compressed file if you are unsure.

