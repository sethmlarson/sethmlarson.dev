# Lockdown Mode for Apple devices 

Back in September 2023 the [libwebp vulnerability](https://www.cve.org/CVERecord?id=CVE-2023-4863) (also known as BLASTPASS)
was being actively exploited to target a journalist's mobile device.
After reading the [report from Citizen Lab](https://citizenlab.ca/2023/09/blastpass-nso-group-iphone-zero-click-zero-day-exploit-captured-in-the-wild)
I learned about an iOS feature called "[Lockdown Mode](https://support.apple.com/en-ca/105120)" for Apple devices.

I've been running Lockdown Mode [for almost a year now](https://twitter.com/sethmlarson/status/1700186723638997344), and at the time I promised a write-up of my experience with the feature,
so here it is!

## How does Lockdown Mode keep your phone more secure?

Lockdown Mode prevents some methods of sending or injecting data into your phone
without your active engagement (such as preloading data, injecting data into unsecured connections, etc).
Data that's processed by your phone automatically, such as images, can exploit flaws in image format parser
in order to escape and begin executing code.

BLASTPASS exploited memory safety issues in the libwebp library
which processes WebP images. The malicious WebP image was delivered to the target's device via a [PassKit attachment](https://developer.apple.com/documentation/walletpasses/building_a_pass)
which can be sent in a text message.

## What does Lockdown Mode disable?

Here's the full list of disabled or degraded features when Lockdown Mode is enabled, quoted from [Apple's docs](https://support.apple.com/en-ca/105120) on the feature:

* Most message attachment types are blocked. Some features such as links and link previews are unavailable.
* Certain complex web technologies are blocked. (ie JavaScript JIT)
* FaceTime calls from unknown contacts are blocked. SharePlay and Live Photos are unavailable.
* Photo location information is excluded. Shared Albums are removed and disabled.
* Wi-Fi must be secure for device to connect to a network. 2G cellular support is disabled.
* Mobile Device Management and Configuration Profiles are disabled.

## What are the impacts?

The biggest impacts for day-to-day usage is two-fold: Message Links and Search.

With Lockdown Mode enabled, links will not highlight like they typically do,
and they won't show the fancy preloaded image that gives you a preview of the content on the other side of a click.

Not having links and link previews in messages is a real inconvenience. The fastest work-around to extract a link
in the middle of a text message is to either copy the whole message into your own message box and then
copy the URL or to screenshot the message and use [Live Text](https://support.apple.com/en-us/120004) to copy-and-paste directly from your screenshot.

If you're able to persuade your partner to send links in a separate message, that also speeds up the copy-and-paste process by copying the whole message.
Persuading your partner is left as an exercise to the reader :)

The other major impact is not being able to search through my messages.
This feature is super helpful when you're trying to recall something from years ago, but not something you're using every day usually.
This feature being disabled has never been such a problem that I've had a memorable negative outcome, but it definitely is frustrating when you know the answer is *somewhere* in your messages.

The only other time Lockdown Mode has introduced friction is during Trina and I's wedding.
The wedding party was sharing pictures and videos via a Shared Album which aren't available
when Lockdown Mode is enabled. Fortunately, I could disable Lockdown Mode for a short time after the wedding
was over, copy all the photos that I wanted, and then re-enable Lockdown Mode to work-around this.

Beyond this, some image formats don't load in any context (likely WebP?) and I haven't noticed any slowdown from not having a JavaScript JIT. 

## Would I recommend Lockdown Mode?

For most people: no. If you have a decent reason to expect you'd be the target of a cyberattack, then you should definitely consider it.

There is a non-zero amount of extra friction to using your phone, but as someone who's trying to actively
reduce my phone usage anyway it wasn't a big issue over the year that I've had it enabled.

## Bonus tip: Quick one-time disabling of biometric authentication

Privacy gated by biometrics (ie, "Face ID" or fingerprint scanners) [doesn't have the same legal protections as a password](https://arstechnica.com/tech-policy/2024/04/cops-can-force-suspect-to-unlock-phone-with-thumbprint-us-court-rules/).
Biometrics are quite convenient, especially if you've configured a relatively short amount of time that your phone
will lock itself after a lack of use.

So how can one have the benefits of biometrics while maintaining the ability to disable biometrics if needed?

By holding down the volume up and side button on your iPhone you'll bring up the screen
that offers to shut down your phone or enter "SOS mode". If you select cancel on this screen your phone
will become locked again but will **require non-biometric authentication for the next phone unlock**.

Give it a try on your phone, so you understand what to do ahead of time.

Because this process is fast (takes less than a second of holding the two buttons) it's great to have in
your back pocket in case you need it. It's also useful for one-time activities when you're separated from your
device such as crossing a security checkpoint.
