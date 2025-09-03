# SMS URLs

Did you know there is a URL scheme for sending
an “SMS” or text message, similar to `mailto:`? SMS URLs
are defined in [RFC 5724](https://www.rfc-editor.org/rfc/rfc5724.html) and are formatted like so:

`sms:<recipient(s)>?body=<body>`

<!-- more -->

Here's a bunch of test links with different scenarios
you can try on your mobile phone:

* [`sms:`](sms:) 

* [`sms:+15551234567`](sms:+15551234567) 

* [`sms:+15551234567?body=`](sms:+15551234567?body=) 

* [`sms:+15551234567?body=Hello%20world!`](sms:+15551234567?body=Hello%20world!) 

Annoyingly, it appears that as of today Apple
doesn't implement RFC 5724 correctly for multiple recipients.
The first URL won't work on iPhones, but will work on Android.
Only the second URL will work on iPhones (and there's not much
[public explanation](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/SMSLinks/SMSLinks.html) as to [why that might be](https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/SMSLinks/SMSLinks.html)).

* [`sms:+15551230001,+15551230002,...?body=Hello%20world!`](sms:+15551230001,+15551230002,+15551230003,+15551230004?body=Hello%20world!)
* [`sms://open?addresses=+15551230001,+15551230002,...&body=Hello%20world!`](sms://open?addresses=+15551230001,+15551230002,+15551230003,+15551230004&body=Hello%20world!)

I used this discovery to create a [small client-side application](https://sethmlarson.dev/draft-sms-and-imessage-from-any-computer-keyboard) for drafting
long SMS and iMessage messages on your computer to be loaded into your phone via QR code.
