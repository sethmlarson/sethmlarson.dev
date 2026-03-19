# Getting started with the GameSir “Pocket Taco” with iPhone and Delta emulator

GameSir shipped the pre-orders for the “[Pocket Taco](https://gamesir.com/products/gamesir-pocket-taco)”
mobile controller on March 15th and I received mine today.
This controller uses Bluetooth and a padded grip mechanism
to add physical buttons to the bottom half of your mobile
phone for use with mobile emulators like [Delta emulator](https://faq.deltaemulator.com/).

<!-- more -->

The guide, tutorials, FAQs, available from GameSir leave a bit to
be desired. Therefore, I'm documenting what I had to do to get the
controller working with my iPhone 13 Pro (iOS 26)
and using the Delta emulator.

## Pairing via Bluetooth

Download the GameSir app from the App Store and open the application.
If you allow the app access to Bluetooth, the app can automatically pair
your device when you turn it on.

Here was my first stumbling block: the included and online guides
reference multiple tutorials for entering pairing mode, depending on
your device. **For iPhone, you want the "AP Connection Tutorial"** (presumably
"AP" means "Apple"). So to pair for an iPhone hold the "Home"
button and the "A" button (right button in "ABYX") on the Pocket Taco
for three seconds. This will enter a pairing mode where the bottom 3
of 4 LEDs on the right side of the device will flash.

On your iPhone, you should see the device in the Bluetooth
pairing screen as "DUALSHOCK 4 Wireless Controller". If you see
'GameSir-Pocket' or something like this, it may not be in the right mode (?)

## Upgrading Pocket Taco firmware

Once your device is paired, you can do "over-the-air" (OTA) firmware
updates to the controller. When I received my controller there was a newer
firmware available. There is a button to do this in the GameSir app,
so might as well get the latest version.

## Using the Pocket Taco controller with Delta

Download and open the [Delta emulator app](https://faq.deltaemulator.com/) and open settings (gear in the top left).
With the Pocket Taco paired open the "Controllers" menu for "Player 1".

Note that the Pocket Taco turns off after a few seconds after closing the
mechanism holding the controller to your phone. To navigate all the menus
you'll want to either gently hold the Pocket Taco open with your other hand
or place it on the very edge of your phone to not overlap too much of the screen.

The Player 1 controller may be set to Keyboard. Set this to the "DUALSHOCK 4 Wireless Controller".
Select "Customize Control..." below this menu. By default, the controller might have the
"A" and "B" buttons switched, so select "A" in the menu and then press "A" on the Pocket Taco
controller to map the button correctly. Do the same for "B" and other buttons.

## Controller Skins

Now if you launch a game you might notice that the screen is cut-off,
as the on-screen controller is no longer being displayed. Go back into
"Settings" and scroll down to the emulator you want to use (Nintendo, Sega Genesis, Super Nintendo, etc).
In the Controller Skins menu for the emulator you want to use select the button in the top-right showing a crossed out
controller icon and select "Game Controller". This means you're configuring
the Controller Skin for when there is a game controller connected.

By default, this will be set to "No Controller Skin".
Select "No Controller Skin" under "Portrait" and then select the default Delta
emulator skin for that emulator. You'll need to do this for every emulator
you plan to use with Delta, as each has their own skin settings.

After this, you should be good to go with the Delta emulator and the Pocket Taco.
Happy gaming! 🌮