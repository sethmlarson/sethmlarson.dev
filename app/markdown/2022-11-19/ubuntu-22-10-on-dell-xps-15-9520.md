# Ubuntu 22.10 on Dell XPS 15 9520

I recently purchased a new laptop after spending a few months without one. This purchase has been a long time coming
as I was waiting for Black Friday deals to start in the US to save some money.

I received many recommendations about the XPS 15 9500 series, thanks all. I set my sights on the [XPS 15 9520](https://www.dell.com/en-us/shop/dell-laptops/xps-15-laptop/spd/xps-15-9520-laptop/xn9520fmgjs) that seemed to have specs that will last the full 8 years I'm hoping to get out of this purchase. These were the specs I chose:

- 12th Gen i9-12900HK (14 cores, 5.0GHz Turbo)
- GeForce RTX 3050Ti
- 2x16GB DDR5 RAM
- 2TB SSD, OLED screen

After a few days of use I absolutely love the machine and am so happy to get back into open source after an extended break. I recorded my "speed run" to setup my machine to be ready for open source contributions below so others can recreate it:

## Install all the packages

```bash
sudo apt-get install build-essential git openssh-client gnome-tweaks \
  libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
  llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev \
  liblzma-dev gedit
```

## Fix right clicks on a trackpad

Right clicks didn't work out of the box which can be a frustrating experience. I've been
through this before though, the `gnome-tweaks` package has a setting to fix this.

- Open the "Tweaks" program through activities
- Select "Keyboard & Mouse"
- Under "Mouse Click Emulation" select "Area"

## Get access to password manager, SSH and GPG keys

I previously saved my SSH public and private key and GPG key into my password manager under secure notes.
Time to retrieve those values and get access to my passwords so I can login to my accounts.

- Open Firefox
- Install the Bitlocker extension
- Login to Bitlocker
- Download the `id_rsa`, `id_rsa.pub`, and `gpg.key` files from secure notes

```bash
# Put your keys here:
gedit ~/.ssh/id_rsa
gedit ~/.ssh/id_rsa.pub

# Apply the proper permissions (u+rw)
chmod -R 600 ~/.ssh/id_rsa*

# Import my GPG key after exporting from other machine:
# gpg --export-secret-key ${id} > gpg.key
gpg --import gpg.key
```

## Configure git

```bash
git config --global user.name "Seth Michael Larson"
git config --global user.email "sethmichaellarson@gmail.com"

# Telling git about my GPG key
gpg --list-secret-keys --keyid-format=long
# /home/sethmlarson/.gnupg/pubring.kbx
# ------------------------------------
# sec   rsa4096/022EB89790807303 ...
# id is '022EB89790807303' from above output

git config --global user.signingkey 022EB89790807303

# Telling git to always sign commits
git config --global commit.gpgsign true
```

## Install Python

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
cd ~/.pyenv && src/configure && make -C src

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

At this point I closed and restarted a terminal instance to get pyenv on the path.

```bash
pyenv install 3.11.0
pyenv global 3.11.0
```

## Install PyCharm community edition

```bash
sudo snap install pycharm-community --classic
```

From here I'm ready to work on open source projects, happy hacking!

