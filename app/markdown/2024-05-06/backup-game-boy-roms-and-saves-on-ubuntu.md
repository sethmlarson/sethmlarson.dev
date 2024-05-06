# Backup Game Boy ROMs and saves on Ubuntu

<div class="row">
<div class="col-6">
<p>I'm a big fan of retro video games,
specifically the Game Boy Color, Advance, and GameCube collections.
The <a href="https://brainbaking.com/post/2023/08/an-ode-to-game-boy-cartridges/">physicality of cartridges</a>, link cables, and accessories before the internet was widely
available for gaming has a special place in my heart.</p>

<p>With the <a href="https://www.theverge.com/24139004/apple-app-store-retro-game-emulators-ios-console-ports-storystream">recent changes to the App Store</a> to allow emulators
(and judging by the influx of issues opened on the <a href="https://github.com/rileytestut/Delta">Delta emulator GitHub repo</a>)
there is a growing interest in playing these games on mobile devices.</p>

<p>So if you're using Ubuntu like me, how can you backup your ROMs and saves?</p>

</div>
<div class="col-6">
<img src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_9158.jpg" style="max-width: 100%; border-radius: 1em;"/><br>
<center><small><i>Using GB Operator with my copy of Pokémon FireRed</i></small></center>
</div>
</div>

## What you'll need

To backup data from Game Boy cartridges I used the following software and hardware:

* Game Boy, GBC, or GBA cartridge
* [GB Operator](https://www.epilogue.co/product/gb-operator) from Epilogue ($50 USD + shipping)
* [Playback](https://www.epilogue.co/downloads) software from Epilogue
* Epilogue includes a USB-C to USB-A connector, so an adapter may be needed

There are other options for backing up Game Boy ROMs and saves, some of which are less
expensive than the GB Operator, but I went with the GB Operator because it explicitly
listed Linux support and from [watching reviews](https://www.youtube.com/watch?v=VMw4kNPUz-Y) appeared to provide a streamlined experience.

## Getting started with GB Operator and Playback

Download the [Playback AppImage](https://www.epilogue.co/downloads) for Linux and the CPU architecture you have.
Make the AppImage file executable with:

```commandline
$ chmod a+x ./Playback.AppImage
```

If you try to execute this file (`$ ./Playback.AppImage`) and receive this error:

```commandline
dlopen(): error loading libfuse.so.2

AppImages require FUSE to run. 
You might still be able to extract the contents of this AppImage 
if you run it with the --appimage-extract option. 
See https://github.com/AppImage/AppImageKit/wiki/FUSE 
for more information
```

You'll need to install FUSE on Ubuntu:

```commandline
$ sudo apt-get install libfuse2
```

After this you should be able to run Playback:

```commandline
$ ./Playback.AppImage
```

From here the application should launch, but even if you have your GB Operator plugged in there's
a chance it won't be detected. There's a good chance that your current user doesn't have access to the USB device.
Epilogue [provides some guides on how to enable access](https://support.epilogue.co/hc/en-us/articles/4403827118738-How-can-I-connect-my-Operator-device-on-Linux-under-a-non-root-user).

After following the above guide and logging in and out for the changes to take effect
your GB Operator should be detected. Connecting a cartridge and navigating to "Data" in the menus provides you with options to
"Backup Game" and "Backup Save".

Selecting these options might trigger a crash with the following error when starting the export process:

```
(Playback.AppImage:44475): Gtk-WARNING **: 15:05:20.886: Could not load a pixbuf from icon theme.
This may indicate that pixbuf loaders or the mime database could not be found.
**
Gtk:ERROR:../../../../gtk/gtkiconhelper.c:494:ensure_surface_for_gicon: assertion failed (error == NULL): Failed to load /usr/share/icons/Yaru/16x16/status/image-missing.png: Unrecognized image file format (gdk-pixbuf-error-quark, 3)
Bail out! Gtk:ERROR:../../../../gtk/gtkiconhelper.c:494:ensure_surface_for_gicon: assertion failed (error == NULL): Failed to load /usr/share/icons/Yaru/16x16/status/image-missing.png: Unrecognized image file format (gdk-pixbuf-error-quark, 3)
Aborted (core dumped)
```

The fix that worked for me [came from a Redditor](https://www.reddit.com/r/epilogue/comments/10au9sx/comment/j9jx7bu)
who talked with Epilogue support and received the following answer:

```
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-svg.so \
  ./Playback.AppImage
```

Running the AppImage with the `LD_PRELOAD` value set fixed my issue, I've since added this
shim to an alias, so I don't have to remember it. Hopefully in a future version of Playback
this won't be an issue.

From here backing up your ROMs and saves should work as expected. *Happy gaming!*
