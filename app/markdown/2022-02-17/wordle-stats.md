# Move or recover your Wordle stats and streaks

Have you ever wanted to play Wordle on another device but weren't able to transfer your statistics? Or worse, cleared your browser storage and lost your Wordle statistics on accident? 😱

Both my partner and I have lost our Wordle stats in the past and it can feel demotivating. That's why I built this tool which lets you import custom Wordle statistics for the current browser:

<style>
  .number-inputs {
    width: 8em;
    display: inline-block;
    margin-bottom: 0.3em;
  }
</style>
<center style="margin-top: 3em; margin-bottom: 3em;">
<blockquote style="max-width: 32em;">
 <form action="/api/wordle-stats" method="get" target="_blank">
   <label class="number-inputs" for="wins-1">Wins in 1</label>
  <input class="number-inputs" type="number" id="wins-1" name="wins-1" min="0" max="1000" value="0"><br>
    <label class="number-inputs" for="wins-2">Wins in 2</label>
  <input class="number-inputs" type="number" id="wins-2" name="wins-2" min="0" max="1000" value="0"><br>
    <label class="number-inputs" for="wins-3">Wins in 3</label>
  <input class="number-inputs" type="number" id="wins-3" name="wins-3" min="0" max="1000" value="0"><br>
    <label class="number-inputs" for="wins-4">Wins in 4</label>
  <input class="number-inputs" type="number" id="wins-4" name="wins-4" min="0" max="1000" value="0"><br>
    <label class="number-inputs" for="wins-5">Wins in 5</label>
  <input class="number-inputs" type="number" id="wins-5" name="wins-5" min="0" max="1000" value="0"><br>
  <label class="number-inputs" for="wins-6">Wins in 6</label>
  <input class="number-inputs" type="number" id="wins-6" name="wins-6" min="0" max="1000" value="0"><br>
  <label class="number-inputs" for="losses">Losses</label>
  <input class="number-inputs" type="number" id="losses" name="losses" min="0" max="1000" value="0"><br>
  <label class="number-inputs" for="current-streak">Current Streak</label>
  <input class="number-inputs" type="number" id="current-streak" name="current-streak" min="0" max="1000" value="0"><br>
  <label class="number-inputs" for="max-streak">Max Streak</label>
  <input class="number-inputs" type="number" id="max-streak" name="max-streak" min="0" max="1000" value="0"><br>
  <label class="number-inputs" for="games-played">Games Played</label>
  <input class="number-inputs" disabled type="number" id="games-played" name="games-played" min="0" max="1000" value="0"><br><br>
  <blockquote>
  <input type="checkbox" id="ack-checkbox" name="ack" value="ack" onclick="ackCheckbox(this)">
  <label for="ack">I acknowledge that using this tool will <strong>overwrite my Wordle statistics in the current browser</strong>.</label>
  </blockquote><br>
   <input disabled style="font-size: 1em;" id="import-stats" type="submit" value="Import statistics into Wordle">
</form>
</blockquote>
<script>
  function ackCheckbox(checkbox) {
    document.getElementById("import-stats").disabled = checkbox.checked ? false : true;
  }
  function recomputeGamesPlayed() {
    let gamesPlayed = 0;
    for (let i = 1; i <= 6; i++) {
      gamesPlayed += parseInt(document.getElementById("wins-" + i).value);
    }
    gamesPlayed += parseInt(document.getElementById("losses").value)
    document.getElementById("games-played").value = gamesPlayed.toString();
  }
  ackCheckbox(document.getElementById("ack-checkbox"));
  for (let i = 1; i <= 6; i++) {
    document.getElementById("wins-" + i).addEventListener("input", recomputeGamesPlayed);
  }
  document.getElementById("losses").addEventListener("input", recomputeGamesPlayed);
</script>
</center>

### How to use the tool?

Importing statistics only works if the current browser hasn't played Wordle before or if you clear your site data (see below).

- If you have existing statistics that you don't want to lose: **take a screenshot of them to be safe**.
- Open this webpage **on the device where you want to play Wordle** and do the following steps:
- Open up your settings and clear data for "nytimes.com". **Don't clear data for all websites**, only for "nytimes.com":
  - [How to clear data in Firefox](https://www.google.com/search?q=how+to+clear+website+data+firefox)
  - [How to clear data in Chrome](https://www.google.com/search?q=how+to+clear+website+data+chrome)
  - [How to clear data in Edge](https://www.google.com/search?q=how+to+clear+website+data+edge)
  - [How to clear data in Safari (macOS)](https://superuser.com/a/1534142)
  - [How to clear data in Safari (iOS)](https://browserhow.com/how-to-view-cache-and-clear-site-storage-in-safari-ios-ipados)
- Ensure that you have no tabs open for "nytimes.com", close any open tabs for "nytimes.com".
- Complete the form above by typing in the Wordle wins, losses, and streaks that you wish to import. "Games Played" is calculated automatically as the sum of wins and losses.
- Acknowledge that using this tool will overwrite your Wordle stats.
- Select "Import statistics into Wordle".
- This should open a page on the New York Times, check that your statistics have imported correctly.
- If your statistics didn't import correctly make sure **you've followed each step above** and have **filled out the form completely**, then try again.

### What if I lost my statistics and don't remember them?

Unfortunately they can't be recovered once lost, my recommendation is try remembering the number of wins in 1, 2, or 3 guesses and approximating your current streak and then keep playing. In the end, **Wordle is about having fun** and it'll keep being the same amazing game whether you have your old statistics or not.

### What if I got something wrong on my imported stats?

You can always clear your data and run the tool again with the correct information.

### What's stopping me from entering false information?

Nothing really, you're only cheating yourself :)

### How does this tool work?

This tool uses the same mechanism that the New York Times uses to import statistics from the previous Wordle website. I'm not sure when or if that mechanism will stop working, until then this form will work too!

The source code for this tool is [available on GitHub](https://github.com/sethmlarson/sethmlarson.dev/blob/master/app/app.py) and the import mechanism is fairly simple. It works by redirecting users to the URL `https://www.nytimes.com/games/wordle` with a preconstructed query string formatted like this:

```json
{
  "time": 0,
  "statistics": {
    "currentStreak": 0,
    "maxStreak": 0,
    "guesses": {
      "1": 0,
      "2": 0,
      "3": 0,
      "4": 0,
      "5": 0,
      "6": 0,
      "fails": 0
    },
    "gamesPlayed": 0,
    "gamesWon": 0,
    "averageGuesses": 0,
    "winPercentage": 0
  },
  "darkTheme": false,
  "colorBlindTheme": null
}
```

This structure is percent-encoded and appended to the URL like so: `?data={%22time%22:...}`.
