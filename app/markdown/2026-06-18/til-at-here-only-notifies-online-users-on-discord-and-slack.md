# TIL “@here” only notifies online users on Discord and Slack

I'm in a few Discord servers of friends and we get together in-person
regularly. Whenever I was the one organizing an event
I would attempt to ping everyone details in the Discord using `@here`.

After the initial ping I would usually follow-up with
folks over text, which is fine and expected part of organizing.
More often than not, invitees would be *way more responsive* over text than over Discord. I created an [SMS BCC
tool](https://sethmlarson.dev/sms-bcc) because of how effective texting is for organizing events.

Turns out that `@here` is [*functionally different*](https://superuser.com/questions/1212953/how-do-everyone-and-here-work-whats-the-difference-between-them) from `@everyone` or `@channel` on Slack and Discord.
<!-- more -->
`@here` only sends notifications to users that are *currently online* 🟢, not offline ⚫
or “away” 🟡. This makes `@here` useful for when you’re trying to play
an online multiplayer game or chat synchronously... but not for planning
a hang-out in advance. So none of my usually-offline friends on Discord
would get my initial notification, only the follow-ups. I’ll be using
`@channel` for this purpose from now on.

I learned this from a friend and *three people* including me were not aware
of this distinction, so I figure I have to share this on the blog. Maybe
this will help you increase the turn-out for the next event you host
for Discord friends. What other Discord or Slack hacks am I probably unaware of?
Send them to me via email or on social media.

*Happy organizing!* 
