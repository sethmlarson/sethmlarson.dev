# Switching git back to GPG signing

Recently [GitHub announced support for SSH key signing of commits](https://github.blog/changelog/2022-08-23-ssh-commit-verification-now-supported/), which is awesome! I followed [the instructions](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key#telling-git-about-your-ssh-key) to configure my git for SSH signing
which was very straightforward. Went to create a commit to test the signing and
was met with this error:

```bash
$ git commit -m "..."

error: ssh-keygen -Y sign is needed for ssh signing (available in openssh version 8.2p1+)
error: unknown option -- Y?
usage: ssh-keygen [-q] [-b bits] [-t dsa | ecdsa | ed25519 | rsa]
                  [-N new_passphrase] [-C comment] [-f output_keyfile]
       ssh-keygen -p [-P old_passphrase] [-N new_passphrase] [-f keyfile]
       ssh-keygen -i [-m key_format] [-f input_keyfile]
```

Hmm, looks like I need OpenSSH version 8.2p1 or later. But I'm still on Ubuntu 18.04 LTS which is [fixed at 7.6 of OpenSSH](https://launchpad.net/ubuntu/+source/openssh). (Just another reason to upgrade...)

No problem, I'll switch back to PGP signing for now. Following the [same GitHub guide to switch to PGP](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key#telling-git-about-your-gpg-key-2):

```bash
$ gpg --list-secret-keys --keyid-format LONG
/home/sethmlarson/.gnupg/pubring.kbx
------------------------------------
sec   rsa4096/FFFFFFFFFFFFFFFF 2020-02-19 [SC]
      AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
uid                 [ultimate] Seth Michael Larson <sethmichaellarson@gmail.com>
ssb   rsa4096/FFFFFFFFFFFFFFFF 2022-02-18 [E]

# Grab the key ID listed after "sec" "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" which is in this case.
$ git config --global user.signingkey AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```

After following all the steps I still can't sign commits. What gives? I remember a step from the SSH key signing guide where I had to set `gpg.format` to `ssh`. Maybe something to do with that?

I try setting the `gpg.format` to `gpg` to see if that works:

```bash
# No error here, promising?
$ git config --global gpg.format gpg

$ git commit -m "..."
error: invalid value for 'gpg.format': 'gpg'
fatal: bad config variable 'gpg.format' in file '/home/sethmlarson/.gitconfig' at line 16
```

Hmm... maybe this is a [GPG/PGP mixup](http://www.differencebetween.net/technology/software-technology/difference-between-pgp-and-gpg/) situation?

```bash
$ git config --global gpg.format pgp

$ git commit -m "..."
error: invalid value for 'gpg.format': 'pgp'
fatal: bad config variable 'gpg.format' in file '/home/sethmlarson/.gitconfig' at line 16
```

Well that didn't work. After a few minutes of searching I figured out that the default value for `gpg.format` is `openpgp` not `gpg` or `pgp`:

```bash
$ git config --global gpg.format openpgp
$ git commit -m "..."

# Success! 🎉
```

When switching back to GPG this crucial step isn't listed in many guides because it's the default value and has been the only usable signing format for a long time. Hopefully guides like GitHub's will amend this step so users don't get lost while configuring their commit signing.
