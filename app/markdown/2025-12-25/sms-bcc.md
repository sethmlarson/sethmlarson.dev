# Blind Carbon Copy (BCC) for SMS

Have you ever wanted the power of email [Blind Carbon Copy](https://en.wikipedia.org/wiki/Blind_carbon_copy) (BCC), but
for SMS? I've wanted this functionality myself for parties and organizing,
specifically without needing to use a
third-party service. This script automates the difficult parts
of drafting and sending a text message to many recipients with [SMS URLs](https://sethmlarson.dev/sms-urls) and QR codes.

Draft your message, choose your recipients,
and then scan-and-send all the QR codes until you're done.
Save your command for later to follow-up in different groups.

<!-- more -->

## Source code

Copy-and-paste the following source code into a file
named `sms-bcc`, make the file executable (`chmod a+x sms-bcc`)
and you're ready to start using the script. Requires Python
and the [`qrcode` package](https://pypi.org/project/qrcode) (`pip install qrcode`) to run.
This script is licensed MIT.

<blockquote>
<details>
<summary>Source code for <code>sms-bcc</code> script</summary>

```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "qrcode"
# ]
# ///
# License: MIT
# Copyright 2025, Seth Larson

import argparse
import pathlib
import re
import sys
import urllib.parse

from qrcode.console_scripts import main as qrcode_main

__version__ = "2025.12.26"


def sms_url(recipients: list[str], message: str, mobile_os: str | None = None) -> str:
    """
    Generate an SMS URL from a list of recipients and a message.
    """
    if len(recipients) > 1 and mobile_os is None:
        raise ValueError("Mobile OS required for multi-recipient messages")
    if not recipients:
        raise ValueError("Recipients required")
    message_encoded = urllib.parse.quote(message)
    if mobile_os is None or mobile_os == "android":
        return f"sms:{','.join(recipients)}?body={message_encoded}"
    else:  # mobile_os == "ios"
        return f"sms://open?addresses={','.join(recipients)}&body={message_encoded}"


def parse_contacts(contacts_data: str) -> dict[str, str]:
    """
    Parses a vCard file. Assumes that each contact
    has a full name and telephone number.
    """
    vcard_fn_re = re.compile(r"^FN:(.+)$", re.MULTILINE)
    vcard_tel_re = re.compile(r"^(?:item[0-9]\.)?TEL[^:]*:([ \.\(\)+0-9\-]+)$", re.MULTILINE)
    names_to_tel = {}
    for vcard in contacts_data.split("BEGIN:VCARD"):
        if not (
            (match_fn := vcard_fn_re.search(vcard))
            and (match_tel := vcard_tel_re.search(vcard))
        ):
            continue
        tel = re.sub(r"[^0-9]", "", match_tel.group(1))
        names_to_tel[match_fn.group(1)] = tel

    return names_to_tel


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Blind Carbon Copy (BCC) for SMS"
    )
    parser.add_argument(
        "--contacts",
        type=str,
        required=True,
        help="Path to contacts file in the vCard format",
    )
    parser.add_argument(
        "--recipients",
        type=str,
        nargs="+",
        required=False,
        help="List of recipients pulled from contacts",
    )
    parser.add_argument(
        "--always-recipients",
        type=str,
        nargs="+",
        required=False,
        help="List of recipients to include in every recipient group",
    )
    parser.add_argument(
        "--message",
        type=str,
        required=True,
        help="Message to send",
    )
    parser.add_argument(
        "--mobile-os",
        type=str,
        choices=["ios", "android"],
        required=False,
        default="ios",
        help="Mobile OS, only required for multi-recipient messages",
    )
    args = parser.parse_args(sys.argv[1:])

    contacts_data = pathlib.Path(args.contacts).read_text()
    names_to_tel = parse_contacts(contacts_data)

    message_data = pathlib.Path(args.message).read_text()
    list_of_recipients = [
        [r.strip() for r in recipients.split(",")] for recipients in args.recipients
    ]
    always_recipients = list(args.always_recipients or ())
    if (mobile_os := args.mobile_os) not in (None, "android", "ios"):
        raise ValueError("--mobile-os must be one of 'android' or 'ios'")

    def clear_terminal() -> None:
        print(chr(27) + "[2J")

    for recipients in list_of_recipients:
        recipients.extend(always_recipients)

        # Figure out which telephone numbers to include
        # and exclude. Can be numbers or names.
        recipient_tels = {}
        for recipient in recipients:
            # Last character is a number, probably a telephone number.
            if recipient[-1].isdigit():
                recipient_tels[recipient] = recipient
                continue
            for name, tel in names_to_tel.items():
                if recipient in name:
                    recipient_tels[name] = tel

        # Remove names filtered via '-Name'.
        for recipient in recipients:
            if recipient.startswith("-"):
                recipient_tels = {
                    name: tel
                    for name, tel in recipient_tels.items()
                    if recipient[1:] not in name
                }

        clear_terminal()
        qrcode_data = sms_url(
            sorted(set(recipient_tels.values())), message_data, mobile_os
        )
        qrcode_main(["--error-correction=L", qrcode_data])
        input(
            f"\n\nSending to: {', '.join(sorted(recipient_tels.keys()))}\nScan, send, and press enter to continue."
        )

    clear_terminal()
    print(f"Done sending {len(list_of_recipients)} messages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

</details>
</blockquote>

## How to use

Export your contacts from your phone to a vCard file (`.vcf`). For
iPhones this is done within the contacts app: long-press-and-hold “All Contacts”
and select “Export”. This will create a `.vcf` file that you can transfer
to your computer.

Now run the `sms-bcc` script with `--contacts` for the `.vcf` file,
draft a message in a file and pass with the `--message` option,
and choose your recipients by their name with the `--recipients` option.

```terminal
./sms-bcc \
  --contacts contacts.vcf \
  --recipients Alex,Bob Charlie \
  --message ./message.txt
```

This will draft the message to two groups: "You, Alex, and Bob"
and "You and Charlie". Note how spaces delimit groups of
recipients and commas (`,`) delimit recipient names within a group.

After running this script, a series of QR codes using the `sms://` URL scheme
will be generated one after another. Scan the QR code to load the message and
recipient into your phone, then you can optionally send the message or skip,
then press `Enter` to generate the next QR code.

The `--recipients` option uses a simple string-contains operation,
so I recommend having full names in your contacts to avoid excessive
duplicates. You can pass a name with a leading hyphen/minus (`-`)
character to exclude a name from the list of recipients.
The below invocation will match people named "Alex" without matching "Alexander":

```terminal
./sms-bcc --recipients Alex,-Alexander
```

If you have a spouse or partner that you want to include
in every recipient group, use the `--always-recipients` option:

```terminal
./sms-bcc \
  --contacts contacts.vcf \
  --recipients Bob Charlie,Dave \
  --always-recipients Alex \
  --message ./message.txt
```

This will draft the message for "You, Alex, and Bob"
and "You, Alex, Charlie, and Dave".

<center>
🎄 *Merry Christmas and happy organizing!* 🎄
</center>

## Changelog

* `2025.12.26`: Better handling for many different telephone number formats
  such as `(555) 555-555`. Added inline script metadata to header.
* `2025.12.25`: Initial release.