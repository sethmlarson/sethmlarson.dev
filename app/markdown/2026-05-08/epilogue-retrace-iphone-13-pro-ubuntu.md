# Using Epilogue Retrace app with iPhone 13 Pro and Ubuntu

When [Epilogue announced the Retrace app](https://www.epilogue.co/software/retrace) for iOS and Android
I was over the moon excited. In theory this meant I could
archive ROMs from the GB Operator directly to my iPhone
where I play the games with the [Delta emulator](/getting-started-with-gamesir-pocket-taco-iphone-delta-emulator).
This meant I wouldn't need to ferry ROMs between the GB
Operator to my laptop to my phone. Unfortunately
I ran into two hurdles with my plan, if you
were able to get Retrace to work with a pre-USB-C
iPhone let me know.

<!-- more -->

## Upgrading the GB Operator firmware

First I saw that the Retrace app required a new firmware
version for the GB Operator (`v10.0.10`), so I set
out to [update the GB Operator firmware](https://www.epilogue.co/support/hardware/firmware-updates).
The documentation says to use Playback, so I went to update
Playback. Previously Playback was distributed as an AppImage
but [newer versions use Flatpak](https://www.epilogue.co/software/playback). So... I had to figure out
[how to install a Flatpak on Ubuntu](https://flatpak.org/setup/Ubuntu).

I did that, had the new Playback app on Ubuntu and... the firmware
update notification never prompted in the app. I contacted support
and learned that apparently the Linux versions of Playback don't
support updating the firmware... So I needed a Windows computer.
My wife's laptop is Windows, so I was able to update the firmware
using her computer instead of my Ubuntu laptop.

## Trying Retrace with an iPhone 13 Pro

GB Operator uses USB-C for power delivery and data transfer
and comes with a high-quality USB-C cord. This is perfect
for my laptop which only has USB-C ports.

Unfortunately, I would be using Retrace on an iPhone 13 Pro.
The iPhone 13 Pro came before Apple was legally required to use USB-C
on their phones in Europe, so the phone has a lightning port.
I purchased a [Lightning to USB-C
adapter cord](https://www.apple.com/shop/product/muq93am/a/usb-c-to-lightning-cable-1-m) from the Apple Store.

But... that doesn't work with the GB Operator. It doesn't deliver power
to the device. I was able to try with my wife's iPhone 15 Pro (which has USB-C)
and power delivery worked like normal, the GB Operator turned on as usual.
That's unfortunate.

In summary: if you want to use Epilogue Retrace you need
a phone that supports USB-C and upgrading the GB Operator
firmware requires either macOS or Windows... I guess
I'll be using Playback on Ubuntu for the next five years
now that I've just replaced my iPhone 13 Pro battery 😢
