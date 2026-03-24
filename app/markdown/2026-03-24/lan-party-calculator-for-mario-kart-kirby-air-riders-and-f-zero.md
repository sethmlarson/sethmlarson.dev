# LAN Party Calculator (Mario Kart, Kirby Air Riders, F-Zero)

Nintendo has multiple popular racing franchises,
including [Mario Kart](https://en.wikipedia.org/wiki/Mario_Kart),
[Kirby Air Ride](https://en.wikipedia.org/wiki/Kirby_Air_Ride), and [F-Zero](https://en.wikipedia.org/wiki/F-Zero). Each of these
franchises spans multiple titles and consoles and
have ways to play with *more than one console*
in a single shared “game lobby”. This feature makes these games interesting
for [LAN parties](https://en.wikipedia.org/wiki/LAN_party), where you have
many players, consoles, and games in one area.

What does it mean to be the **most “LAN-party-able” Nintendo racing game**?
There are three metrics I found
interesting for this question: **most-players**, **price-per-player**, and **“real-estate”-per-player** (aka: TVs/consoles).
There is a different “best” game according to each of these metrics. I've compiled
the data and created a small calculator to compare:

<!-- more -->

<p>
<blockquote>
<form>
<label for='game'>Game</label><br>
<select onchange="updateTable()" style="max-width: 100%; border: 2px black solid; border-radius: 0;" id="game" name="game">
<option value='any'>(Any)</option>
<optgroup label='SNES'>
<option value='FZ'>F-Zero (FZ)</option>
<option value='SMK'>Super Mario Kart (SMK)</option>
</optgroup>
<optgroup label='N64'>
<option value='MK64'>Mario Kart 64 (MK64)</option>
</optgroup>
<optgroup label='GBA'>
<option value='FZGL'>F-Zero: GP Legend (FZGL)</option>
<option value='FZMV'>F-Zero: Maximum Velocity (FZMV)</option>
<option value='MKSS'>Mario Kart: Super Circuit (MKSS)</option>
</optgroup>
<optgroup label='GameCube'>
<option value='FZGX'>F-Zero GX (FZGX)</option>
<option value='KAR'>Kirby Air Ride (KAR)</option>
<option value='MKDD'>Mario Kart: Double Dash!! (MKDD)</option>
</optgroup>
<optgroup label='Wii'>
<option value='MKWII'>Mario Kart Wii (MKWII)</option>
</optgroup>
<optgroup label='DS'>
<option value='MKDS'>Mario Kart DS (MKDS)</option>
</optgroup>
<optgroup label='3DS/2DS'>
<option value='MK7'>Mario Kart 7 (MK7)</option>
</optgroup>
<optgroup label='Wii U'>
<option value='MK8'>Mario Kart 8 (MK8)</option>
</optgroup>
<optgroup label='Switch'>
<option value='FZ99'>F-Zero 99 (FZ99)</option>
<option value='MK8D'>Mario Kart 8 Deluxe (MK8D)</option>
</optgroup>
<optgroup label='Switch 2'>
<option value='KARS'>Kirby Air Riders (KARS)</option>
<option value='MKWRD'>Mario Kart World (MKWRD)</option>
</optgroup>
</select>
<br>
<label for="players">Players</label><br>
<select onchange="updateTable()" style="max-width: 100%; border: 2px black solid; border-radius: 0;" id="players" name="players">
<option value='any'>(Any)</option>
<option value='1'>1</option>
<option value='2'>2</option>
<option value='3'>3</option>
<option value='4'>4</option>
<option value='5'>5</option>
<option value='6'>6</option>
<option value='7'>7</option>
<option value='8'>8</option>
<option value='9'>9</option>
<option value='10'>10</option>
<option value='11'>11</option>
<option value='12'>12</option>
<option value='13'>13</option>
<option value='14'>14</option>
<option value='15'>15</option>
<option value='16'>16</option>
<option value='17'>17</option>
<option value='18'>18</option>
<option value='19'>19</option>
<option value='20'>20</option>
<option value='21'>21</option>
<option value='22'>22</option>
<option value='23'>23</option>
<option value='24'>24</option>
</select>
<label for="mode">Mode</label>
<select onchange="updateTable()" style="max-width: 100%; border: 2px black solid; border-radius: 0;" id="mode" name="mode">
<option value='any'>(Any)</option>
<option value='LOCAL'>Local</option>
<option value='LAN'>LAN</option>
<option value='ONLINE'>Online</option>
<option value='SHARE'>Share</option>
</select>
</form>
<br>
<table id='results'>
<thead><th>Game</th><th>Mode</th><th>#P</th><th>Price</th><th>Consoles</th><th>Games</th><th>Cables</th><th>Adapters</th><th>TVs</th></thead>
<tbody></tbody>
</table>
</blockquote>
</p>
<script>
var GameData = [
  ['SMK', 'LOCAL', '1', 163, 1, 1, 0, 0, 1, '#84fa80'],
  ['SMK', 'LOCAL', '2', 180, 1, 1, 0, 0, 1, '#85f980'],
  ['FZ', 'LOCAL', '1', 147, 1, 1, 0, 0, 1, '#83fb80'],
  ['FZ', 'LOCAL', '2', 164, 1, 1, 0, 0, 1, '#84fa80'],
  ['MK64', 'LOCAL', '1', 133, 1, 1, 0, 0, 1, '#82fc80'],
  ['MK64', 'LOCAL', '2', 149, 1, 1, 0, 0, 1, '#83fb80'],
  ['MK64', 'LOCAL', '3', 165, 1, 1, 0, 0, 1, '#84fa80'],
  ['MK64', 'LOCAL', '4', 181, 1, 1, 0, 0, 1, '#85f980'],
  ['MKSS', 'LOCAL', '1', 90, 1, 1, 0, 0, 0, '#80ff80'],
  ['MKSS', 'LAN', '2', 204, 2, 2, 1, 0, 0, '#86f880'],
  ['MKSS', 'LAN', '3', 318, 3, 3, 2, 0, 0, '#8ef080'],
  ['MKSS', 'LAN', '4', 432, 4, 4, 3, 0, 0, '#96e880'],
  ['MKSS', 'SHARE', '2', 187, 2, 1, 1, 0, 0, '#85f980'],
  ['MKSS', 'SHARE', '3', 284, 3, 1, 2, 0, 0, '#8cf280'],
  ['MKSS', 'SHARE', '4', 381, 4, 1, 3, 0, 0, '#92ec80'],
  ['FZMV', 'LOCAL', '1', 93, 1, 1, 0, 0, 0, '#80ff80'],
  ['FZMV', 'LAN', '2', 210, 2, 2, 1, 0, 0, '#87f780'],
  ['FZMV', 'LAN', '3', 327, 3, 3, 2, 0, 0, '#8fef80'],
  ['FZMV', 'LAN', '4', 444, 4, 4, 3, 0, 0, '#96e880'],
  ['FZMV', 'SHARE', '2', 190, 2, 1, 1, 0, 0, '#86f880'],
  ['FZMV', 'SHARE', '3', 287, 3, 1, 2, 0, 0, '#8cf280'],
  ['FZMV', 'SHARE', '4', 384, 4, 1, 3, 0, 0, '#92ec80'],
  ['FZGL', 'LOCAL', '1', 103, 1, 1, 0, 0, 0, '#80fe80'],
  ['FZGL', 'LAN', '2', 230, 2, 2, 1, 0, 0, '#88f680'],
  ['FZGL', 'LAN', '3', 357, 3, 3, 2, 0, 0, '#91ed80'],
  ['FZGL', 'LAN', '4', 484, 4, 4, 3, 0, 0, '#99e580'],
  ['FZGL', 'SHARE', '2', 200, 2, 1, 1, 0, 0, '#86f880'],
  ['FZGL', 'SHARE', '3', 297, 3, 1, 2, 0, 0, '#8df180'],
  ['FZGL', 'SHARE', '4', 394, 4, 1, 3, 0, 0, '#93eb80'],
  ['MKDD', 'LOCAL', '1', 179, 1, 1, 0, 0, 1, '#85f980'],
  ['MKDD', 'LOCAL', '2', 207, 1, 1, 0, 0, 1, '#87f780'],
  ['MKDD', 'LOCAL', '3', 235, 1, 1, 0, 0, 1, '#89f580'],
  ['MKDD', 'LOCAL', '4', 263, 1, 1, 0, 0, 1, '#8af480'],
  ['MKDD', 'LAN', '2', 418, 2, 2, 2, 2, 2, '#95e980'],
  ['MKDD', 'LAN', '3', 446, 2, 2, 2, 2, 2, '#97e780'],
  ['MKDD', 'LAN', '4', 474, 2, 2, 2, 2, 2, '#98e680'],
  ['MKDD', 'LAN', '5', 502, 2, 2, 2, 2, 2, '#9ae480'],
  ['MKDD', 'LAN', '6', 530, 2, 2, 2, 2, 2, '#9ce280'],
  ['MKDD', 'LAN', '7', 558, 2, 2, 2, 2, 2, '#9ee080'],
  ['MKDD', 'LAN', '8', 586, 2, 2, 2, 2, 2, '#a0de80'],
  ['MKDD', 'LAN', '9', 795, 3, 3, 3, 3, 3, '#aed080'],
  ['MKDD', 'LAN', '10', 823, 3, 3, 3, 3, 3, '#b0ce80'],
  ['MKDD', 'LAN', '11', 851, 3, 3, 3, 3, 3, '#b2cc80'],
  ['MKDD', 'LAN', '12', 879, 3, 3, 3, 3, 3, '#b4ca80'],
  ['MKDD', 'LAN', '13', 1088, 4, 4, 4, 4, 4, '#c2bc80'],
  ['MKDD', 'LAN', '14', 1116, 4, 4, 4, 4, 4, '#c3bb80'],
  ['MKDD', 'LAN', '15', 1144, 4, 4, 4, 4, 4, '#c5b980'],
  ['MKDD', 'LAN', '16', 1172, 4, 4, 4, 4, 4, '#c7b780'],
  ['KAR', 'LOCAL', '1', 190, 1, 1, 0, 0, 1, '#86f880'],
  ['KAR', 'LOCAL', '2', 218, 1, 1, 0, 0, 1, '#87f780'],
  ['KAR', 'LOCAL', '3', 246, 1, 1, 0, 0, 1, '#89f580'],
  ['KAR', 'LOCAL', '4', 274, 1, 1, 0, 0, 1, '#8bf380'],
  ['KAR', 'LAN', '2', 440, 2, 2, 2, 2, 2, '#96e880'],
  ['KAR', 'LAN', '3', 468, 2, 2, 2, 2, 2, '#98e680'],
  ['KAR', 'LAN', '4', 496, 2, 2, 2, 2, 2, '#9ae480'],
  ['FZGX', 'LOCAL', '1', 180, 1, 1, 0, 0, 1, '#85f980'],
  ['FZGX', 'LOCAL', '2', 208, 1, 1, 0, 0, 1, '#87f780'],
  ['FZGX', 'LOCAL', '3', 236, 1, 1, 0, 0, 1, '#89f580'],
  ['FZGX', 'LOCAL', '4', 264, 1, 1, 0, 0, 1, '#8af480'],
  ['MKDS', 'LOCAL', '1', 77, 1, 1, 0, 0, 0, '#80ff80'],
  ['MKDS', 'LAN', '2', 154, 2, 2, 0, 0, 0, '#83fb80'],
  ['MKDS', 'LAN', '3', 231, 3, 3, 0, 0, 0, '#88f680'],
  ['MKDS', 'LAN', '4', 308, 4, 4, 0, 0, 0, '#8df180'],
  ['MKDS', 'LAN', '5', 385, 5, 5, 0, 0, 0, '#93eb80'],
  ['MKDS', 'LAN', '6', 462, 6, 6, 0, 0, 0, '#98e680'],
  ['MKDS', 'LAN', '7', 539, 7, 7, 0, 0, 0, '#9de180'],
  ['MKDS', 'LAN', '8', 616, 8, 8, 0, 0, 0, '#a2dc80'],
  ['MKDS', 'ONLINE', '2', 154, 2, 2, 0, 0, 0, '#83fb80'],
  ['MKDS', 'ONLINE', '3', 231, 3, 3, 0, 0, 0, '#88f680'],
  ['MKDS', 'ONLINE', '4', 308, 4, 4, 0, 0, 0, '#8df180'],
  ['MKDS', 'SHARE', '2', 137, 2, 1, 0, 0, 0, '#82fc80'],
  ['MKDS', 'SHARE', '3', 197, 3, 1, 0, 0, 0, '#86f880'],
  ['MKDS', 'SHARE', '4', 257, 4, 1, 0, 0, 0, '#8af480'],
  ['MKDS', 'SHARE', '5', 317, 5, 1, 0, 0, 0, '#8ef080'],
  ['MKDS', 'SHARE', '6', 377, 6, 1, 0, 0, 0, '#92ec80'],
  ['MKDS', 'SHARE', '7', 437, 7, 1, 0, 0, 0, '#96e880'],
  ['MKDS', 'SHARE', '8', 497, 8, 1, 0, 0, 0, '#9ae480'],
  ['MKWII', 'LOCAL', '1', 95, 1, 1, 0, 0, 1, '#80ff80'],
  ['MKWII', 'LOCAL', '2', 108, 1, 1, 0, 0, 1, '#80fe80'],
  ['MKWII', 'LOCAL', '3', 121, 1, 1, 0, 0, 1, '#81fd80'],
  ['MKWII', 'LOCAL', '4', 134, 1, 1, 0, 0, 1, '#82fc80'],
  ['MKWII', 'ONLINE', '2', 190, 2, 2, 0, 0, 2, '#86f880'],
  ['MKWII', 'ONLINE', '3', 203, 2, 2, 0, 0, 2, '#86f880'],
  ['MKWII', 'ONLINE', '4', 216, 2, 2, 0, 0, 2, '#87f780'],
  ['MKWII', 'ONLINE', '5', 311, 3, 3, 0, 0, 3, '#8ef080'],
  ['MKWII', 'ONLINE', '6', 324, 3, 3, 0, 0, 3, '#8ef080'],
  ['MKWII', 'ONLINE', '7', 419, 4, 4, 0, 0, 4, '#95e980'],
  ['MKWII', 'ONLINE', '8', 432, 4, 4, 0, 0, 4, '#96e880'],
  ['MKWII', 'ONLINE', '9', 527, 5, 5, 0, 0, 5, '#9ce280'],
  ['MKWII', 'ONLINE', '10', 540, 5, 5, 0, 0, 5, '#9de180'],
  ['MKWII', 'ONLINE', '11', 635, 6, 6, 0, 0, 6, '#a3db80'],
  ['MKWII', 'ONLINE', '12', 648, 6, 6, 0, 0, 6, '#a4da80'],
  ['MK7', 'LOCAL', '1', 108, 1, 1, 0, 0, 0, '#80fe80'],
  ['MK7', 'LAN', '2', 216, 2, 2, 0, 0, 0, '#87f780'],
  ['MK7', 'LAN', '3', 324, 3, 3, 0, 0, 0, '#8ef080'],
  ['MK7', 'LAN', '4', 432, 4, 4, 0, 0, 0, '#96e880'],
  ['MK7', 'LAN', '5', 540, 5, 5, 0, 0, 0, '#9de180'],
  ['MK7', 'LAN', '6', 648, 6, 6, 0, 0, 0, '#a4da80'],
  ['MK7', 'LAN', '7', 756, 7, 7, 0, 0, 0, '#abd380'],
  ['MK7', 'LAN', '8', 864, 8, 8, 0, 0, 0, '#b3cb80'],
  ['MK7', 'ONLINE', '2', 216, 2, 2, 0, 0, 0, '#87f780'],
  ['MK7', 'ONLINE', '3', 324, 3, 3, 0, 0, 0, '#8ef080'],
  ['MK7', 'ONLINE', '4', 432, 4, 4, 0, 0, 0, '#96e880'],
  ['MK7', 'SHARE', '2', 202, 2, 1, 0, 0, 0, '#86f880'],
  ['MK7', 'SHARE', '3', 296, 3, 1, 0, 0, 0, '#8df180'],
  ['MK7', 'SHARE', '4', 390, 4, 1, 0, 0, 0, '#93eb80'],
  ['MK7', 'SHARE', '5', 484, 5, 1, 0, 0, 0, '#99e580'],
  ['MK7', 'SHARE', '6', 578, 6, 1, 0, 0, 0, '#9fdf80'],
  ['MK7', 'SHARE', '7', 672, 7, 1, 0, 0, 0, '#a6d880'],
  ['MK7', 'SHARE', '8', 766, 8, 1, 0, 0, 0, '#acd280'],
  ['MK8', 'LOCAL', '1', 139, 1, 1, 0, 0, 1, '#82fc80'],
  ['MK8', 'LOCAL', '2', 169, 1, 1, 0, 0, 1, '#84fa80'],
  ['MK8', 'LOCAL', '3', 199, 1, 1, 0, 0, 1, '#86f880'],
  ['MK8', 'LOCAL', '4', 229, 1, 1, 0, 0, 1, '#88f680'],
  ['MK8', 'ONLINE', '2', 278, 2, 2, 0, 0, 2, '#8bf380'],
  ['MK8', 'ONLINE', '3', 308, 2, 2, 0, 0, 2, '#8df180'],
  ['MK8', 'ONLINE', '4', 338, 2, 2, 0, 0, 2, '#8fef80'],
  ['MK8', 'ONLINE', '5', 477, 3, 3, 0, 0, 3, '#99e580'],
  ['MK8', 'ONLINE', '6', 507, 3, 3, 0, 0, 3, '#9be380'],
  ['MK8', 'ONLINE', '7', 646, 4, 4, 0, 0, 4, '#a4da80'],
  ['MK8', 'ONLINE', '8', 676, 4, 4, 0, 0, 4, '#a6d880'],
  ['MK8D', 'LOCAL', '1', 170, 1, 1, 0, 0, 0, '#84fa80'],
  ['MK8D', 'LOCAL', '2', 170, 1, 1, 0, 0, 0, '#84fa80'],
  ['MK8D', 'LOCAL', '3', 206, 1, 1, 0, 0, 0, '#87f780'],
  ['MK8D', 'LOCAL', '4', 242, 1, 1, 0, 0, 0, '#89f580'],
  ['MK8D', 'LAN', '2', 390, 2, 2, 2, 2, 0, '#93eb80'],
  ['MK8D', 'LAN', '3', 390, 2, 2, 2, 2, 0, '#93eb80'],
  ['MK8D', 'LAN', '4', 390, 2, 2, 2, 2, 0, '#93eb80'],
  ['MK8D', 'LAN', '5', 585, 3, 3, 3, 3, 0, '#a0de80'],
  ['MK8D', 'LAN', '6', 585, 3, 3, 3, 3, 0, '#a0de80'],
  ['MK8D', 'LAN', '7', 780, 4, 4, 4, 4, 0, '#add180'],
  ['MK8D', 'LAN', '8', 780, 4, 4, 4, 4, 0, '#add180'],
  ['MK8D', 'LAN', '9', 975, 5, 5, 5, 5, 0, '#bac480'],
  ['MK8D', 'LAN', '10', 975, 5, 5, 5, 5, 0, '#bac480'],
  ['MK8D', 'LAN', '11', 1170, 6, 6, 6, 6, 0, '#c7b780'],
  ['MK8D', 'LAN', '12', 1170, 6, 6, 6, 6, 0, '#c7b780'],
  ['MK8D', 'ONLINE', '2', 340, 2, 2, 0, 0, 0, '#90ee80'],
  ['MK8D', 'ONLINE', '3', 340, 2, 2, 0, 0, 0, '#90ee80'],
  ['MK8D', 'ONLINE', '4', 340, 2, 2, 0, 0, 0, '#90ee80'],
  ['MK8D', 'ONLINE', '5', 510, 3, 3, 0, 0, 0, '#9be380'],
  ['MK8D', 'ONLINE', '6', 510, 3, 3, 0, 0, 0, '#9be380'],
  ['MK8D', 'ONLINE', '7', 680, 4, 4, 0, 0, 0, '#a6d880'],
  ['MK8D', 'ONLINE', '8', 680, 4, 4, 0, 0, 0, '#a6d880'],
  ['FZ99', 'LOCAL', '1', 135, 1, 1, 0, 0, 0, '#82fc80'],
  ['FZ99', 'ONLINE', '2', 270, 2, 2, 0, 0, 0, '#8bf380'],
  ['FZ99', 'ONLINE', '3', 405, 3, 3, 0, 0, 0, '#94ea80'],
  ['FZ99', 'ONLINE', '4', 540, 4, 4, 0, 0, 0, '#9de180'],
  ['FZ99', 'ONLINE', '5', 675, 5, 5, 0, 0, 0, '#a6d880'],
  ['FZ99', 'ONLINE', '6', 810, 6, 6, 0, 0, 0, '#afcf80'],
  ['FZ99', 'ONLINE', '7', 945, 7, 7, 0, 0, 0, '#b8c680'],
  ['FZ99', 'ONLINE', '8', 1080, 8, 8, 0, 0, 0, '#c1bd80'],
  ['FZ99', 'ONLINE', '9', 1215, 9, 9, 0, 0, 0, '#cab480'],
  ['FZ99', 'ONLINE', '10', 1350, 10, 10, 0, 0, 0, '#d3ab80'],
  ['FZ99', 'ONLINE', '11', 1485, 11, 11, 0, 0, 0, '#dca280'],
  ['FZ99', 'ONLINE', '12', 1620, 12, 12, 0, 0, 0, '#e59980'],
  ['FZ99', 'ONLINE', '13', 1755, 13, 13, 0, 0, 0, '#ee9080'],
  ['FZ99', 'ONLINE', '14', 1890, 14, 14, 0, 0, 0, '#f78780'],
  ['FZ99', 'ONLINE', '15', 2025, 15, 15, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '16', 2160, 16, 16, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '17', 2295, 17, 17, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '18', 2430, 18, 18, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '19', 2565, 19, 19, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '20', 2700, 20, 20, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '21', 2835, 21, 21, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '22', 2970, 22, 22, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '23', 3105, 23, 23, 0, 0, 0, '#ff8080'],
  ['FZ99', 'ONLINE', '24', 3240, 24, 24, 0, 0, 0, '#ff8080'],
  ['MKWRD', 'LOCAL', '1', 453, 1, 1, 0, 0, 0, '#97e780'],
  ['MKWRD', 'LOCAL', '2', 453, 1, 1, 0, 0, 0, '#97e780'],
  ['MKWRD', 'LOCAL', '3', 489, 1, 1, 0, 0, 0, '#9ae480'],
  ['MKWRD', 'LOCAL', '4', 525, 1, 1, 0, 0, 0, '#9ce280'],
  ['MKWRD', 'LAN', '2', 956, 2, 2, 2, 2, 0, '#b9c580'],
  ['MKWRD', 'LAN', '2', 916, 2, 2, 2, 0, 2, '#b6c880'],
  ['MKWRD', 'LAN', '3', 956, 2, 2, 2, 2, 0, '#b9c580'],
  ['MKWRD', 'LAN', '3', 916, 2, 2, 2, 0, 2, '#b6c880'],
  ['MKWRD', 'LAN', '4', 956, 2, 2, 2, 2, 0, '#b9c580'],
  ['MKWRD', 'LAN', '4', 916, 2, 2, 2, 0, 2, '#b6c880'],
  ['MKWRD', 'LAN', '5', 1434, 3, 3, 3, 3, 0, '#d9a580'],
  ['MKWRD', 'LAN', '5', 1374, 3, 3, 3, 0, 3, '#d5a980'],
  ['MKWRD', 'LAN', '6', 1434, 3, 3, 3, 3, 0, '#d9a580'],
  ['MKWRD', 'LAN', '6', 1374, 3, 3, 3, 0, 3, '#d5a980'],
  ['MKWRD', 'LAN', '7', 1912, 4, 4, 4, 4, 0, '#f98580'],
  ['MKWRD', 'LAN', '7', 1832, 4, 4, 4, 0, 4, '#f38b80'],
  ['MKWRD', 'LAN', '8', 1912, 4, 4, 4, 4, 0, '#f98580'],
  ['MKWRD', 'LAN', '8', 1832, 4, 4, 4, 0, 4, '#f38b80'],
  ['MKWRD', 'LAN', '9', 2390, 5, 5, 5, 5, 0, '#ff8080'],
  ['MKWRD', 'LAN', '9', 2290, 5, 5, 5, 0, 5, '#ff8080'],
  ['MKWRD', 'LAN', '10', 2390, 5, 5, 5, 5, 0, '#ff8080'],
  ['MKWRD', 'LAN', '10', 2290, 5, 5, 5, 0, 5, '#ff8080'],
  ['MKWRD', 'LAN', '11', 2868, 6, 6, 6, 6, 0, '#ff8080'],
  ['MKWRD', 'LAN', '11', 2748, 6, 6, 6, 0, 6, '#ff8080'],
  ['MKWRD', 'LAN', '12', 2868, 6, 6, 6, 6, 0, '#ff8080'],
  ['MKWRD', 'LAN', '12', 2748, 6, 6, 6, 0, 6, '#ff8080'],
  ['MKWRD', 'LAN', '13', 3346, 7, 7, 7, 7, 0, '#ff8080'],
  ['MKWRD', 'LAN', '13', 3206, 7, 7, 7, 0, 7, '#ff8080'],
  ['MKWRD', 'LAN', '14', 3346, 7, 7, 7, 7, 0, '#ff8080'],
  ['MKWRD', 'LAN', '14', 3206, 7, 7, 7, 0, 7, '#ff8080'],
  ['MKWRD', 'LAN', '15', 3824, 8, 8, 8, 8, 0, '#ff8080'],
  ['MKWRD', 'LAN', '15', 3664, 8, 8, 8, 0, 8, '#ff8080'],
  ['MKWRD', 'LAN', '16', 3824, 8, 8, 8, 8, 0, '#ff8080'],
  ['MKWRD', 'LAN', '16', 3664, 8, 8, 8, 0, 8, '#ff8080'],
  ['MKWRD', 'LAN', '17', 4302, 9, 9, 9, 9, 0, '#ff8080'],
  ['MKWRD', 'LAN', '17', 4122, 9, 9, 9, 0, 9, '#ff8080'],
  ['MKWRD', 'LAN', '18', 4302, 9, 9, 9, 9, 0, '#ff8080'],
  ['MKWRD', 'LAN', '18', 4122, 9, 9, 9, 0, 9, '#ff8080'],
  ['MKWRD', 'LAN', '19', 4780, 10, 10, 10, 10, 0, '#ff8080'],
  ['MKWRD', 'LAN', '19', 4580, 10, 10, 10, 0, 10, '#ff8080'],
  ['MKWRD', 'LAN', '20', 4780, 10, 10, 10, 10, 0, '#ff8080'],
  ['MKWRD', 'LAN', '20', 4580, 10, 10, 10, 0, 10, '#ff8080'],
  ['MKWRD', 'LAN', '21', 5258, 11, 11, 11, 11, 0, '#ff8080'],
  ['MKWRD', 'LAN', '21', 5038, 11, 11, 11, 0, 11, '#ff8080'],
  ['MKWRD', 'LAN', '22', 5258, 11, 11, 11, 11, 0, '#ff8080'],
  ['MKWRD', 'LAN', '22', 5038, 11, 11, 11, 0, 11, '#ff8080'],
  ['MKWRD', 'LAN', '23', 5736, 12, 12, 12, 12, 0, '#ff8080'],
  ['MKWRD', 'LAN', '23', 5496, 12, 12, 12, 0, 12, '#ff8080'],
  ['MKWRD', 'LAN', '24', 5736, 12, 12, 12, 12, 0, '#ff8080'],
  ['MKWRD', 'LAN', '24', 5496, 12, 12, 12, 0, 12, '#ff8080'],
  ['MKWRD', 'ONLINE', '2', 906, 2, 2, 0, 0, 0, '#b5c980'],
  ['MKWRD', 'ONLINE', '3', 906, 2, 2, 0, 0, 0, '#b5c980'],
  ['MKWRD', 'ONLINE', '4', 906, 2, 2, 0, 0, 0, '#b5c980'],
  ['MKWRD', 'ONLINE', '5', 1359, 3, 3, 0, 0, 0, '#d4aa80'],
  ['MKWRD', 'ONLINE', '6', 1359, 3, 3, 0, 0, 0, '#d4aa80'],
  ['MKWRD', 'ONLINE', '7', 1812, 4, 4, 0, 0, 0, '#f28c80'],
  ['MKWRD', 'ONLINE', '8', 1812, 4, 4, 0, 0, 0, '#f28c80'],
  ['MKWRD', 'ONLINE', '9', 2265, 5, 5, 0, 0, 0, '#ff8080'],
  ['MKWRD', 'ONLINE', '10', 2265, 5, 5, 0, 0, 0, '#ff8080'],
  ['MKWRD', 'ONLINE', '11', 2718, 6, 6, 0, 0, 0, '#ff8080'],
  ['MKWRD', 'ONLINE', '12', 2718, 6, 6, 0, 0, 0, '#ff8080'],
  ['MKWRD', 'ONLINE', '13', 3171, 7, 7, 0, 0, 0, '#ff8080'],
  ['MKWRD', 'ONLINE', '14', 3171, 7, 7, 0, 0, 0, '#ff8080'],
  ['MKWRD', 'ONLINE', '15', 3624, 8, 8, 0, 0, 0, '#ff8080'],
  ['MKWRD', 'ONLINE', '16', 3624, 8, 8, 0, 0, 0, '#ff8080'],
  ['KARS', 'LOCAL', '1', 445, 1, 1, 0, 0, 0, '#97e780'],
  ['KARS', 'LOCAL', '2', 445, 1, 1, 0, 0, 0, '#97e780'],
  ['KARS', 'LOCAL', '3', 481, 1, 1, 0, 0, 0, '#99e580'],
  ['KARS', 'LOCAL', '4', 517, 1, 1, 0, 0, 0, '#9be380'],
  ['KARS', 'LAN', '2', 940, 2, 2, 2, 2, 0, '#b8c680'],
  ['KARS', 'LAN', '2', 900, 2, 2, 2, 0, 2, '#b5c980'],
  ['KARS', 'LAN', '3', 1410, 3, 3, 3, 3, 0, '#d7a780'],
  ['KARS', 'LAN', '3', 1350, 3, 3, 3, 0, 3, '#d3ab80'],
  ['KARS', 'LAN', '4', 1880, 4, 4, 4, 4, 0, '#f68880'],
  ['KARS', 'LAN', '4', 1800, 4, 4, 4, 0, 4, '#f18d80'],
  ['KARS', 'LAN', '5', 2350, 5, 5, 5, 5, 0, '#ff8080'],
  ['KARS', 'LAN', '5', 2250, 5, 5, 5, 0, 5, '#ff8080'],
  ['KARS', 'LAN', '6', 2820, 6, 6, 6, 6, 0, '#ff8080'],
  ['KARS', 'LAN', '6', 2700, 6, 6, 6, 0, 6, '#ff8080'],
  ['KARS', 'LAN', '7', 3290, 7, 7, 7, 7, 0, '#ff8080'],
  ['KARS', 'LAN', '7', 3150, 7, 7, 7, 0, 7, '#ff8080'],
  ['KARS', 'LAN', '8', 3760, 8, 8, 8, 8, 0, '#ff8080'],
  ['KARS', 'LAN', '8', 3600, 8, 8, 8, 0, 8, '#ff8080'],
  ['KARS', 'LAN', '9', 4230, 9, 9, 9, 9, 0, '#ff8080'],
  ['KARS', 'LAN', '9', 4050, 9, 9, 9, 0, 9, '#ff8080'],
  ['KARS', 'LAN', '10', 4700, 10, 10, 10, 10, 0, '#ff8080'],
  ['KARS', 'LAN', '10', 4500, 10, 10, 10, 0, 10, '#ff8080'],
  ['KARS', 'LAN', '11', 5170, 11, 11, 11, 11, 0, '#ff8080'],
  ['KARS', 'LAN', '11', 4950, 11, 11, 11, 0, 11, '#ff8080'],
  ['KARS', 'LAN', '12', 5640, 12, 12, 12, 12, 0, '#ff8080'],
  ['KARS', 'LAN', '12', 5400, 12, 12, 12, 0, 12, '#ff8080'],
  ['KARS', 'LAN', '13', 6110, 13, 13, 13, 13, 0, '#ff8080'],
  ['KARS', 'LAN', '13', 5850, 13, 13, 13, 0, 13, '#ff8080'],
  ['KARS', 'LAN', '14', 6580, 14, 14, 14, 14, 0, '#ff8080'],
  ['KARS', 'LAN', '14', 6300, 14, 14, 14, 0, 14, '#ff8080'],
  ['KARS', 'LAN', '15', 7050, 15, 15, 15, 15, 0, '#ff8080'],
  ['KARS', 'LAN', '15', 6750, 15, 15, 15, 0, 15, '#ff8080'],
  ['KARS', 'LAN', '16', 7520, 16, 16, 16, 16, 0, '#ff8080'],
  ['KARS', 'LAN', '16', 7200, 16, 16, 16, 0, 16, '#ff8080'],
  ['KARS', 'ONLINE', '2', 890, 2, 2, 0, 0, 0, '#b4ca80'],
  ['KARS', 'ONLINE', '3', 890, 2, 2, 0, 0, 0, '#b4ca80'],
  ['KARS', 'ONLINE', '4', 890, 2, 2, 0, 0, 0, '#b4ca80'],
  ['KARS', 'ONLINE', '5', 1335, 3, 3, 0, 0, 0, '#d2ac80'],
  ['KARS', 'ONLINE', '6', 1335, 3, 3, 0, 0, 0, '#d2ac80'],
  ['KARS', 'ONLINE', '7', 1780, 4, 4, 0, 0, 0, '#f08e80'],
  ['KARS', 'ONLINE', '8', 1780, 4, 4, 0, 0, 0, '#f08e80'],
  ['KARS', 'SHARE', '2', 580, 2, 1, 0, 0, 0, '#a0de80'],
  ['KARS', 'SHARE', '3', 715, 3, 1, 0, 0, 0, '#a9d580'],
  ['KARS', 'SHARE', '4', 850, 4, 1, 0, 0, 0, '#b2cc80'],
];
function updateTable() {
  var game = document.getElementById("game").value;
  var players = document.getElementById("players").value;
  var mode = document.getElementById("mode").value;
  var rows = [];
  GameData.forEach(function(item) {
    if (game !== 'any' && game !== item[0]) {
      return;
    }
    if (players !== 'any' && players !== item[2]) {
      return;
    }
    if (mode !== 'any' && mode !== item[1]) {
      return;
    }
    rows.push(item);
  });
  rows = rows.sort(function (a, b) { return parseInt(a[3]) - parseInt(b[3]) }).slice(0, 10);

  var tbody = document.querySelector("#results tbody");
  var newTbody = document.createElement("tbody");
  rows.forEach(function(element) {
    var newRow = newTbody.insertRow();
    element.forEach(function(cell, index) {
        if (index === 9) {return}
        var html = cell.toString();
        var cell = newRow.insertCell()
        if (index === 3) {
          html = '$' + html;
          cell.style["background-color"] = element[9];
        }
        cell.innerHTML = html;
    });
  });
  tbody.parentNode.replaceChild(newTbody, tbody);
}
updateTable();
</script>

<ul>
<li>Price includes consoles, controllers, games, cables, adapters. Prices sourced from <a href="https://pricecharting.com">Pricecharting</a> and <a href="https://www.microcenter.com/">Microcenter</a> (no affiliation) for March 2026.
TVs and <nobr>Mountain Dew™</nobr> not included in price.</li>
<li>“Cables” means Link Cables for the GBA or Ethernet for the GameCube, Switch, and Switch 2.</li>
<li>“Adapters” means ETH2GC for the GameCube, “USB-A to Ethernet” adapters for docked Switch 1, or “USB-C to Ethernet” for undocked Switch 1 and Switch 2.</li>
</ul>

## Which games are the winners?

* **Best price per player**: Mario Kart DS using DS Download Play. With this method
  you can buy a single copy of Mario Kart DS and play concurrently with up to 8
  players. **With 8 players would cost $62 per player**.
* **Best real-estate per player**: Mario Kart: Double Dash!! in LAN mode.
  This is somehow the only game in the list that **supports 4 players per
  console** in LAN mode, all future games only support 1 or 2 players per console in LAN mode.
  This means fewer TVs and consoles per player and helps alleviate
  slightly higher prices these days for GameCube gear.
* **Most players**: F-Zero 99 hands down wins most players with **up to 99
  per lobby**. Mario Kart World also supports up to 24 concurrent players
  in LAN mode, but needing to use 12 Switch 2's compared to F-Zero
  being a Switch 1 title means a much higher price.

## Why did you build this?

This post was inspired by hosting a LAN party
with friends for my birthday. Researching and verifying the limits for each game
and console took a lot of work, so I hope this can save *someone*
some time wrangling all these numbers in the future.
After all this research, the games I chose for the LAN party are
“[Mario Kart: Double Dash](https://en.wikipedia.org/wiki/Mario_Kart:_Double_Dash)” on the GameCube, “[Mario Kart 8 Deluxe](https://en.wikipedia.org/wiki/Mario_Kart_8)” and
“[F-Zero 99](https://en.wikipedia.org/wiki/F-Zero_99)” on the Nintendo Switch, and “[Mario Kart World](https://en.wikipedia.org/wiki/Mario_Kart_World)” on the Nintendo Switch 2.

The data and the [script I used to generate this calculator](https://gist.github.com/sethmlarson/8ab1b0c7524ac2c642d56cd56c1bbb72)
is [all open source](https://gist.github.com/sethmlarson/8ab1b0c7524ac2c642d56cd56c1bbb72). If there are mistakes or improvements,
[please submit a patch](mailto:sethmichaellarson@gmail.com). Please note that I don't own a
DS, 3DS, or Wii U so the numbers there are more likely to be incorrect.
The rest of this blog post will be about the specifics for each
console and game.

## What features does each game support?

Each game supports one of four multiplayer modes: Local, LAN, Online, and Share.
Availability depends on both the console and the game.

<table><thead><th>Game</th><th>Console</th><th>Year</th><th>Local</th><th>LAN</th><th>Online</th><th>Share</th></thead>
<tr><td>Super Mario Kart</td><td>SNES</td><td>1992</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>F-Zero</td><td>SNES</td><td>1990</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>Mario Kart 64</td><td>N64</td><td>1996</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>Mario Kart: Super Circuit</td><td>GBA</td><td>2001</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES (1)</td></tr>
<tr><td>F-Zero: Maximum Velocity</td><td>GBA</td><td>2003</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES (1)</td></tr>
<tr><td>F-Zero: GP Legend</td><td>GBA</td><td>2003</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES (1)</td></tr>
<tr><td>Mario Kart: Double Dash!!</td><td>GameCube</td><td>2003</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>Kirby Air Ride</td><td>GameCube</td><td>2003</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>F-Zero GX</td><td>GameCube</td><td>2003</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>Mario Kart DS</td><td>DS</td><td>2005</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES (2)</td></tr>
<tr><td>Mario Kart Wii</td><td>Wii</td><td>2008</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>Mario Kart 7</td><td>3DS/2DS</td><td>2011</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES (2)</td></tr>
<tr><td>Mario Kart 8</td><td>Wii U</td><td>2014</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>Mario Kart 8 Deluxe</td><td>Switch</td><td>2017</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>F-Zero 99</td><td>Switch</td><td>2023</td><td style="background-color: #ff8080">NO</td><td style="background-color: #ff8080">NO</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>Mario Kart World</td><td>Switch 2</td><td>2025</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #ff8080">NO</td></tr>
<tr><td>Kirby Air Riders</td><td>Switch 2</td><td>2025</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES</td><td style="background-color: #80ff80">YES (3)</td></tr>
</table>

* (1): via GBA Single-Pak Link Mode
* (2): via DS Download Play
* (3): via Nintendo Switch GameShare

## Pricing

Here is a table with costs from March 2026 for each
game, console, and accessory:

<table><thead><th></th><th>Game</th><th></th><th>Console</th><th>Controller</th><th>Cable</th><th>Adapter</th></thead>
<tr><td>F-Zero</td><td><a href='https://www.pricecharting.com/game/super-nintendo/f-zero'>$18</a></td><td rowspan="2">SNES</td><td rowspan="2"><a href='https://www.pricecharting.com/game/super-nintendo/super-nintendo-system'>$129</a></td><td rowspan="2"><a href='https://www.pricecharting.com/game/super-nintendo/super-nintendo-controller'>$17</a></td><td rowspan="2"></td><td rowspan="2"></td></tr>
<tr><td>Super Mario Kart</td><td><a href='https://www.pricecharting.com/game/super-nintendo/super-mario-kart'>$34</a></td></tr>
<tr><td>Mario Kart 64</td><td><a href='https://www.pricecharting.com/game/nintendo-64/mario-kart-64'>$46</a></td><td>N64</td><td><a href='https://www.pricecharting.com/game/nintendo-64/nintendo-64-system'>$87</a></td><td><a href='https://www.pricecharting.com/game/nintendo-64/gray-controller'>$16</a></td><td></td><td></td></tr>
<tr><td>Mario Kart: Super Circuit</td><td><a href='https://www.pricecharting.com/game/gameboy-advance/mario-kart-super-circuit'>$17</a></td><td rowspan="3">GBA</td><td rowspan="3"><a href='https://www.pricecharting.com/game/gameboy-advance/indigo-gameboy-advance-system'>$73</a></td><td rowspan="3"></td><td rowspan="3"><a href='https://www.pricecharting.com/game/gameboy-advance/gameboy-advance-game-link-cable'>$24</a></td><td rowspan="3"></td></tr>
<tr><td>F-Zero: GP Legend</td><td><a href='https://www.pricecharting.com/game/gameboy-advance/f-zero-gp-legend'>$30</a></td></tr>
<tr><td>F-Zero: Maximum Velocity</td><td><a href='https://www.pricecharting.com/game/gameboy-advance/f-zero-maximum-velocity'>$20</a></td></tr>
<tr><td>F-Zero GX</td><td><a href='https://www.pricecharting.com/game/gamecube/f-zero-gx'>$61</a></td><td rowspan="3">GameCube</td><td rowspan="3"><a href='https://www.pricecharting.com/game/gamecube/indigo-gamecube-system'>$119</a></td><td rowspan="3"><a href='https://www.pricecharting.com/game/gamecube/indigo-controller'>$28</a></td><td rowspan="3">$5</td><td rowspan="3"><a href='https://www.pricecharting.com/game/gamecube/gamecube-broadband-adapter'>$25</a></td></tr>
<tr><td>Kirby Air Ride</td><td><a href='https://www.pricecharting.com/game/gamecube/kirby-air-ride'>$71</a></td></tr>
<tr><td>Mario Kart: Double Dash!!</td><td><a href='https://www.pricecharting.com/game/gamecube/mario-kart-double-dash'>$60</a></td></tr>
<tr><td>Mario Kart DS</td><td><a href='https://www.pricecharting.com/game/nintendo-ds/mario-kart-ds'>$17</a></td><td>DS</td><td><a href='https://www.pricecharting.com/game/nintendo-ds/black-nintendo-ds-lite'>$60</a></td><td></td><td></td><td></td></tr>
<tr><td>Mario Kart Wii</td><td><a href='https://www.pricecharting.com/game/wii/mario-kart-wii'>$35</a></td><td>Wii</td><td><a href='https://www.pricecharting.com/game/wii/white-nintendo-wii-system'>$60</a></td><td><a href='https://www.pricecharting.com/game/wii/white-wii-remote'>$13</a></td><td></td><td></td></tr>
<tr><td>Mario Kart 7</td><td><a href='https://www.pricecharting.com/game/nintendo-3ds/mario-kart-7'>$14</a></td><td>3DS/2DS</td><td><a href='https://www.pricecharting.com/game/nintendo-3ds/nintendo-2ds-crimson-red'>$94</a></td><td></td><td></td><td></td></tr>
<tr><td>Mario Kart 8</td><td><a href='https://www.pricecharting.com/game/wii-u/mario-kart-8'>$10</a></td><td>Wii U</td><td><a href='https://www.pricecharting.com/game/wii-u/wii-u-console-basic-white-8gb'>$129</a></td><td><a href='https://www.pricecharting.com/game/wii-u/wii-u-pro-controller-white'>$30</a></td><td></td><td></td></tr>
<tr><td>Mario Kart 8 Deluxe</td><td><a href='https://www.pricecharting.com/game/nintendo-switch/mario-kart-8-deluxe'>$35</a></td><td rowspan="2">Switch</td><td rowspan="2"><a href='https://www.pricecharting.com/game/nintendo-switch/nintendo-switch-with-blue-and-red-joy-con'>$135</a></td><td rowspan="2"><a href='https://www.pricecharting.com/game/nintendo-switch/joy-con-neon-red-&-neon-blue'>$36</a></td><td rowspan="2">$5</td><td rowspan="2"></td></tr>
<tr><td>F-Zero 99</td><td>$0</td></tr>
<tr><td>Kirby Air Riders</td><td><a href='https://www.pricecharting.com/game/nintendo-switch-2/kirby-air-riders'>$50</a></td><td rowspan="2">Switch 2</td><td rowspan="2"><a href='https://www.pricecharting.com/game/nintendo-switch-2/nintendo-switch-2-console'>$395</a></td><td rowspan="2"><a href='https://www.pricecharting.com/game/nintendo-switch/joy-con-neon-red-&-neon-blue'>$36</a></td><td rowspan="2">$5</td><td rowspan="2">$20</td></tr>
<tr><td>Mario Kart World</td><td><a href='https://www.pricecharting.com/game/nintendo-switch-2/mario-kart-world'>$58</a></td></tr>
</table>

### Game Boy Advance

The Game Boy Advance (GBA) had multiple features that made the console
perfect for multi-console multiplayer. These features being the new
GBA Link Cables, allowing more than two consoles to connect, and the
Single-Pak Link Play that all the GBA titles on this list support.

[GBA Link Cables](https://en.wikipedia.org/wiki/Game_Link_Cable#Third_generation) have three terminals per cable, a larger grey plug,
a smaller blue plug, and a smaller blue socket in the middle of the cable.
The grey and blue plugs both fit into a GBA console, but the larger grey plug
does not fit into the small blue socket on the cable. To connect four players,
two players connect like normal, and then player three connects their blue plug
into the blue socket between the existing connected consoles.
In the end, this means you only need N-1 cables for N consoles and that
a single player (player 1) ends up with a blue plug in their console.

The second feature “[Single-Pak Link Play](https://www.mygamer.com/gba-single-pak-linking-games/)” allowed a single player to own
a cartridge and to share the game with other connected consoles if the
game supports the mode. This mode is also sometimes called “Multiboot”
or “Joyboot”. Because the game ROM data itself is transferred to the
other consoles, this often made for load-times during startup and
meant all content wasn't playable by all players. For example, in
Mario Kart: Super Circuit only a subset of maps and characters were
available in Single-Pay Link Play mode.

### GameCube

The GameCube was Nintendo’s [first internet-enabled console](https://en.wikipedia.org/wiki/GameCube_online_functionality),
even if only 8 titles supported the feature. Only [three titles supported
LAN play](https://en.wikipedia.org/wiki/GameCube_online_functionality#LAN_games),
that being Kirby Air Ride, Mario Kart: Double Dash!!, and 1080° Avalanche.

The GameCube Broadband Adapter is [legendarily expensive](https://www.pricecharting.com/game/gamecube/gamecube-broadband-adapter) now due to how
few games supported the feature at all. Nowadays, it's advised to
modify your GameCube with a method to [boot into Swiss](https://www.gc-forever.com/wiki/index.php?title=Swiss)
and using Swiss’s “[Emulate Broadband Adapter](https://retrorgb.com/bba-emulation-demonstrated-in-swiss.html)” feature with an
ETH2GC adapter. These adapters are cheap, even if you don't assemble
them yourself. There are a few variants, [ETH2GC Sidecar](https://github.com/webhdx/ETH2GC),
[ETH2GC Lite](https://github.com/webhdx/ETH2GC?tab=readme-ov-file#-eth2gc-lite),
and [ETH2GC Card Slot](https://github.com/silverstee1/ETH2GC-Card-Slot-Adapter).
I am currently running a ETH2GC Sidecar and ETH2GC Card Slot and both
work together with Mario Kart: Double Dash!! and Kirby Air Ride.

### DS, Wii, Wii U, 3DS

The DS supported a feature called [DS Download Play](https://en.wikipedia.org/wiki/Nintendo_DS#Download_Play), which similar to
Single-Pak Link play for the GBA, allowed a playing single game cartridge
with up to 8 consoles. The 3DS also supported this feature.

Beyond this I didn't have a lot to say about these consoles, as they aren't my interest.
If you have more to say, maybe write your own blog post and [send it to me](mailto:sethmichaellarson@gmail.com)
after!

### Nintendo Switch

The first-generation Switch is a quirky console being both portable and dockable.
Because the console  itself has a screen on it, this means you can play games
without a TV. However, to access “LAN” modes in Mario Kart 8 Deluxe you need to be
physically linked via Ethernet.

Problem is... the original Switch doesn't have
an Ethernet port. And depending on whether you're playing docked or undocked:
you'll need a different adapter!
If you're playing undocked, using the Switch screen as your “TV” you'll
need to buy a USB-C to Ethernet adapter. If you're playing docked you'll
need to buy a USB-A to Ethernet adapter, as the dock itself doesn't have
a USB-C port except for power delivery. Switch OLED docks do have an Ethernet port,
so if you have one of those models then you won't need an adapter in docked mode.


**Test your adapters before your LAN party, as not every adapter
will be accepted by the Switch!**

Both the first-generation Switch and Switch 2 also come with two controllers
(“Joycons”) per console, meaning you'll have to buy fewer controllers to
reach high player counts.

### Nintendo Switch 2

The Switch 2 is similar to the Switch 1, being both portable and dockable.
Nintendo included an Ethernet port on the Switch 2 dock,
and also USB-A and USB-C ports, too. So if you're playing without
a TV, you'll still need a USB-C to Ethernet adapter for your Switch 2.

The Switch 2 adds support for a new mode: Game Share. This mode is similar to
DS Download Play and Single-Pak Link in terms of functionality but in terms of
implementation: it's local game streaming! Even cooler, this feature means that
first-generation Switch consoles can “play” some Switch 2 games like Kirby Air
Riders without sacrificing any features.

### Mario Kart: Double Dash!!

The game supports up to 16 players, however you can
only have 8 total karts per race. Double Dash allows two players
to share a single kart, with one player driving and other throwing
items. LAN mode also doesn't allow selecting which character
or kart you are, you are assigned which kart you
will be driving.

### Kirby Air Ride

Despite supporting LAN mode and having 8 Kirby colors,
you are only allowed to have 4 players maximum within
City Trial or Air Ride modes. So, the LAN mode only
allows having fewer people sharing a TV. 

### F-Zero GX

I saw a reference online to a Nintendo-hosted online leaderboard via passwords
or ghosts for Time Attack, but wasn't able to find an
actual source that this happened. If you have a reference or video,
[please send it my way](mailto:sethmichaellarson@gmail.com)!
Otherwise, I may be mis-remembering something else that I read in the past.

### F-Zero 99

First F-Zero game in over 20 years (sorry F-Zero fans, us Kirby Air Ride fans know how
you feel). Allows up to 99 players in a private lobby. Game is free, but
you need a Switch or Switch 2 console per player. There isn't any local
or LAN multiplayer, so once Nintendo Switch Online is sunsetted this
game won't be playable with multiplayer.

### Mario Kart 8 Deluxe, Mario Kart World

In both Mario Kart 8 Deluxe and Mario Kart World the LAN play mode
is hidden behind holding L+R and pressing the left joystick down
on the "Wireless Play" option.

### Kirby Air Riders

There is very little information online about Kirby Air Riders LAN multiplayer mode.
The [official Nintendo documentation](https://en-americas-support.nintendo.com/app/answers/detail/a_id/68636/~/how-to-start-a-multiplayer-game-%28kirby-air-riders%29#:~:text=LAN%20Play,-%28local) doesn't describe the allowed number of players per console. If anyone
has more definitive data, [please reach out](mailto:sethmichaellarson@gmail.com). Nintendo Switch GameShare allows playing online with four players with only one cartridge.
Nintendo Switch GameShare for Kirby Air Riders is also compatible with Nintendo Switch consoles.

Note that on launch Kirby Air Riders was very disappointing with online play
only allowing one player per console. An update [added support](https://www.nintendo.com/au/news-and-articles/new-multiplayer-features-have-arrived-in-kirby-air-riders/)
for more than one player per console for wireless play. LAN mode
still requires 1 console per player.

## Local Multiplayer

Multiple players play the game on a single console
with different controllers.

<table><thead><th>Game</th><th>1</th><th>2</th><th>3</th><th>4</th></thead>
<tr><td rowspan='1'>Super Mario Kart</td><td style='background-color: #94ea80'>$163</td><td style='background-color: #99e580'>$180</td><td></td><td></td></tr>
<tr><td rowspan='1'>F-Zero</td><td style='background-color: #8fef80'>$147</td><td style='background-color: #94ea80'>$164</td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart 64</td><td style='background-color: #8bf380'>$133</td><td style='background-color: #8fef80'>$149</td><td style='background-color: #94ea80'>$165</td><td style='background-color: #99e580'>$181</td></tr>
<tr><td rowspan='1'>Mario Kart: Double Dash!!</td><td style='background-color: #98e680'>$179</td><td style='background-color: #a1dd80'>$207</td><td style='background-color: #a9d580'>$235</td><td style='background-color: #b1cd80'>$263</td></tr>
<tr><td rowspan='1'>Kirby Air Ride</td><td style='background-color: #9ce280'>$190</td><td style='background-color: #a4da80'>$218</td><td style='background-color: #acd280'>$246</td><td style='background-color: #b4ca80'>$274</td></tr>
<tr><td rowspan='1'>F-Zero GX</td><td style='background-color: #99e580'>$180</td><td style='background-color: #a1dd80'>$208</td><td style='background-color: #a9d580'>$236</td><td style='background-color: #b1cd80'>$264</td></tr>
<tr><td rowspan='1'>Mario Kart Wii</td><td style='background-color: #80ff80'>$95</td><td style='background-color: #83fb80'>$108</td><td style='background-color: #87f780'>$121</td><td style='background-color: #8bf380'>$134</td></tr>
<tr><td rowspan='1'>Mario Kart 8</td><td style='background-color: #8cf280'>$139</td><td style='background-color: #95e980'>$169</td><td style='background-color: #9ee080'>$199</td><td style='background-color: #a7d780'>$229</td></tr>
<tr><td rowspan='1'>Mario Kart 8 Deluxe</td><td style='background-color: #96e880'>$170</td><td style='background-color: #96e880'>$170</td><td style='background-color: #a0de80'>$206</td><td style='background-color: #abd380'>$242</td></tr>
<tr><td rowspan='1'>Mario Kart World</td><td style='background-color: #e99580'>$453</td><td style='background-color: #e99580'>$453</td><td style='background-color: #f48a80'>$489</td><td style='background-color: #ff8080'>$525</td></tr>
<tr><td rowspan='1'>Kirby Air Riders</td><td style='background-color: #e79780'>$445</td><td style='background-color: #e79780'>$445</td><td style='background-color: #f28c80'>$481</td><td style='background-color: #fc8280'>$517</td></tr>
</table>

## LAN Multiplayer

Consoles directly communicate to each other
through wired, short-range wireless, or “local” internet connections, such as ethernet
running to an internet switch/router or
are directly wired together through ethernet
or console-specific link cable. What distinguishes
this mode from “Wireless” is that this mode will
continue to work even after Nintendo servers
have been discontinued.

<table><thead><th>Game</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th><th>21</th><th>22</th><th>23</th><th>24</th></thead>
<tr><td rowspan='1'>Mario Kart: Super Circuit</td><td style='background-color: #83fb80'>$204</td><td style='background-color: #8bf380'>$318</td><td style='background-color: #93eb80'>$432</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>F-Zero: Maximum Velocity</td><td style='background-color: #83fb80'>$210</td><td style='background-color: #8bf380'>$327</td><td style='background-color: #93eb80'>$444</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>F-Zero: GP Legend</td><td style='background-color: #85f980'>$230</td><td style='background-color: #8df180'>$357</td><td style='background-color: #96e880'>$484</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart: Double Dash!!</td><td style='background-color: #92ec80'>$418</td><td style='background-color: #94ea80'>$446</td><td style='background-color: #96e880'>$474</td><td style='background-color: #97e780'>$502</td><td style='background-color: #99e580'>$530</td><td style='background-color: #9be380'>$558</td><td style='background-color: #9de180'>$586</td><td style='background-color: #acd280'>$795</td><td style='background-color: #aed080'>$823</td><td style='background-color: #afcf80'>$851</td><td style='background-color: #b1cd80'>$879</td><td style='background-color: #c0be80'>$1088</td><td style='background-color: #c2bc80'>$1116</td><td style='background-color: #c4ba80'>$1144</td><td style='background-color: #c6b880'>$1172</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Kirby Air Ride</td><td style='background-color: #93eb80'>$440</td><td style='background-color: #95e980'>$468</td><td style='background-color: #97e780'>$496</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart DS</td><td style='background-color: #80ff80'>$154</td><td style='background-color: #85f980'>$231</td><td style='background-color: #8af480'>$308</td><td style='background-color: #8fef80'>$385</td><td style='background-color: #95e980'>$462</td><td style='background-color: #9ae480'>$539</td><td style='background-color: #9fdf80'>$616</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart 7</td><td style='background-color: #84fa80'>$216</td><td style='background-color: #8bf380'>$324</td><td style='background-color: #93eb80'>$432</td><td style='background-color: #9ae480'>$540</td><td style='background-color: #a1dd80'>$648</td><td style='background-color: #a9d580'>$756</td><td style='background-color: #b0ce80'>$864</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart 8 Deluxe</td><td style='background-color: #90ee80'>$390</td><td style='background-color: #90ee80'>$390</td><td style='background-color: #90ee80'>$390</td><td style='background-color: #9de180'>$585</td><td style='background-color: #9de180'>$585</td><td style='background-color: #abd380'>$780</td><td style='background-color: #abd380'>$780</td><td style='background-color: #b8c680'>$975</td><td style='background-color: #b8c680'>$975</td><td style='background-color: #c5b980'>$1170</td><td style='background-color: #c5b980'>$1170</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart World</td><td style='background-color: #b7c780'>$956</td><td style='background-color: #b7c780'>$956</td><td style='background-color: #b7c780'>$956</td><td style='background-color: #d8a680'>$1434</td><td style='background-color: #d8a680'>$1434</td><td style='background-color: #f88680'>$1912</td><td style='background-color: #f88680'>$1912</td><td style='background-color: #ff8080'>$2390</td><td style='background-color: #ff8080'>$2390</td><td style='background-color: #ff8080'>$2868</td><td style='background-color: #ff8080'>$2868</td><td style='background-color: #ff8080'>$3346</td><td style='background-color: #ff8080'>$3346</td><td style='background-color: #ff8080'>$3824</td><td style='background-color: #ff8080'>$3824</td><td style='background-color: #ff8080'>$4302</td><td style='background-color: #ff8080'>$4302</td><td style='background-color: #ff8080'>$4780</td><td style='background-color: #ff8080'>$4780</td><td style='background-color: #ff8080'>$5258</td><td style='background-color: #ff8080'>$5258</td><td style='background-color: #ff8080'>$5736</td><td style='background-color: #ff8080'>$5736</td></tr>
<tr><td rowspan='1'>Kirby Air Riders</td><td style='background-color: #b6c880'>$940</td><td style='background-color: #d6a880'>$1410</td><td style='background-color: #f68880'>$1880</td><td style='background-color: #ff8080'>$2350</td><td style='background-color: #ff8080'>$2820</td><td style='background-color: #ff8080'>$3290</td><td style='background-color: #ff8080'>$3760</td><td style='background-color: #ff8080'>$4230</td><td style='background-color: #ff8080'>$4700</td><td style='background-color: #ff8080'>$5170</td><td style='background-color: #ff8080'>$5640</td><td style='background-color: #ff8080'>$6110</td><td style='background-color: #ff8080'>$6580</td><td style='background-color: #ff8080'>$7050</td><td style='background-color: #ff8080'>$7520</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</table>

## Online Multiplayer

Multiplayer where you can play against your friends
or other players without needing to be on the
same local network. This uses
either Wi-Fi or Ethernet but connected to the global internet.
This mode relies on a central service so once discontinued will
either not be possible or will require modifications to your console,
such as wiimmfi for the Nintendo Wii.

<table><thead><th>Game</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th><th>21</th><th>22</th><th>23</th><th>24</th></thead>
<tr><td rowspan='1'>Mario Kart DS</td><td style='background-color: #80ff80'>$154</td><td style='background-color: #85f980'>$231</td><td style='background-color: #8af480'>$308</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart Wii</td><td style='background-color: #82fc80'>$190</td><td style='background-color: #83fb80'>$203</td><td style='background-color: #84fa80'>$216</td><td style='background-color: #8af480'>$311</td><td style='background-color: #8bf380'>$324</td><td style='background-color: #92ec80'>$419</td><td style='background-color: #93eb80'>$432</td><td style='background-color: #99e580'>$527</td><td style='background-color: #9ae480'>$540</td><td style='background-color: #a1dd80'>$635</td><td style='background-color: #a1dd80'>$648</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart 7</td><td style='background-color: #84fa80'>$216</td><td style='background-color: #8bf380'>$324</td><td style='background-color: #93eb80'>$432</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart 8</td><td style='background-color: #88f680'>$278</td><td style='background-color: #8af480'>$308</td><td style='background-color: #8cf280'>$338</td><td style='background-color: #96e880'>$477</td><td style='background-color: #98e680'>$507</td><td style='background-color: #a1dd80'>$646</td><td style='background-color: #a3db80'>$676</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart 8 Deluxe</td><td style='background-color: #8cf280'>$340</td><td style='background-color: #8cf280'>$340</td><td style='background-color: #8cf280'>$340</td><td style='background-color: #98e680'>$510</td><td style='background-color: #98e680'>$510</td><td style='background-color: #a4da80'>$680</td><td style='background-color: #a4da80'>$680</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>F-Zero 99</td><td style='background-color: #87f780'>$270</td><td style='background-color: #91ed80'>$405</td><td style='background-color: #9ae480'>$540</td><td style='background-color: #a3db80'>$675</td><td style='background-color: #add180'>$810</td><td style='background-color: #b6c880'>$945</td><td style='background-color: #bfbf80'>$1080</td><td style='background-color: #c8b680'>$1215</td><td style='background-color: #d2ac80'>$1350</td><td style='background-color: #dba380'>$1485</td><td style='background-color: #e49a80'>$1620</td><td style='background-color: #ee9080'>$1755</td><td style='background-color: #f78780'>$1890</td><td style='background-color: #ff8080'>$2025</td><td style='background-color: #ff8080'>$2160</td><td style='background-color: #ff8080'>$2295</td><td style='background-color: #ff8080'>$2430</td><td style='background-color: #ff8080'>$2565</td><td style='background-color: #ff8080'>$2700</td><td style='background-color: #ff8080'>$2835</td><td style='background-color: #ff8080'>$2970</td><td style='background-color: #ff8080'>$3105</td><td style='background-color: #ff8080'>$3240</td></tr>
<tr><td rowspan='1'>Mario Kart World</td><td style='background-color: #b3cb80'>$906</td><td style='background-color: #b3cb80'>$906</td><td style='background-color: #b3cb80'>$906</td><td style='background-color: #d2ac80'>$1359</td><td style='background-color: #d2ac80'>$1359</td><td style='background-color: #f28c80'>$1812</td><td style='background-color: #f28c80'>$1812</td><td style='background-color: #ff8080'>$2265</td><td style='background-color: #ff8080'>$2265</td><td style='background-color: #ff8080'>$2718</td><td style='background-color: #ff8080'>$2718</td><td style='background-color: #ff8080'>$3171</td><td style='background-color: #ff8080'>$3171</td><td style='background-color: #ff8080'>$3624</td><td style='background-color: #ff8080'>$3624</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Kirby Air Riders</td><td style='background-color: #b2cc80'>$890</td><td style='background-color: #b2cc80'>$890</td><td style='background-color: #b2cc80'>$890</td><td style='background-color: #d1ad80'>$1335</td><td style='background-color: #d1ad80'>$1335</td><td style='background-color: #ef8f80'>$1780</td><td style='background-color: #ef8f80'>$1780</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</table>

Mario Kart Wii, Mario Kart DS have mods you can apply to play online
in private servers. Mario Kart: Double Dash!! and Kirby Air Ride
also have mods that allow wireless play which wasn't possible
when the games were first released.

## Share Multiplayer (Single-Pak Link, DS Download Play, Game Share)

This multiplayer mode allows playing with local players
that own a console, but not the game. This usually results in
a degraded experience for players that don't own the game, such
as a reduced number of playable characters, karts, or racetracks.
Nintendo Switch “GameShare” uses game streaming between consoles.

<table><thead><th>Game</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th></thead>
<tr><td rowspan='1'>Mario Kart: Super Circuit</td><td style='background-color: #84fa80'>$187</td><td style='background-color: #8cf280'>$284</td><td style='background-color: #94ea80'>$381</td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>F-Zero: Maximum Velocity</td><td style='background-color: #84fa80'>$190</td><td style='background-color: #8cf280'>$287</td><td style='background-color: #95e980'>$384</td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>F-Zero: GP Legend</td><td style='background-color: #85f980'>$200</td><td style='background-color: #8df180'>$297</td><td style='background-color: #95e980'>$394</td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart DS</td><td style='background-color: #80ff80'>$137</td><td style='background-color: #85f980'>$197</td><td style='background-color: #8af480'>$257</td><td style='background-color: #8fef80'>$317</td><td style='background-color: #94ea80'>$377</td><td style='background-color: #99e580'>$437</td><td style='background-color: #9ee080'>$497</td></tr>
<tr><td rowspan='1'>Mario Kart 7</td><td style='background-color: #85f980'>$202</td><td style='background-color: #8df180'>$296</td><td style='background-color: #95e980'>$390</td><td style='background-color: #9de180'>$484</td><td style='background-color: #a5d980'>$578</td><td style='background-color: #add180'>$672</td><td style='background-color: #b5c980'>$766</td></tr>
<tr><td rowspan='1'>Kirby Air Riders</td><td style='background-color: #bbc380'>$840</td><td style='background-color: #dda180'>$1235</td><td style='background-color: #ff8080'>$1630</td><td></td><td></td><td></td><td></td></tr>
</table>

## All Multiplayers

Here is a table comparing all multiplayer modes and their costs:

<table><thead><th>Game</th><th>Mode</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th><th>14</th><th>15</th><th>16</th><th>17</th><th>18</th><th>19</th><th>20</th><th>21</th><th>22</th><th>23</th><th>24</th></thead>
<tr><td rowspan='1'>Super Mario Kart</td><td>LOCAL</td><td style='background-color: #85f980'>$163</td><td style='background-color: #86f880'>$180</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>F-Zero</td><td>LOCAL</td><td style='background-color: #84fa80'>$147</td><td style='background-color: #85f980'>$164</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>Mario Kart 64</td><td>LOCAL</td><td style='background-color: #83fb80'>$133</td><td style='background-color: #84fa80'>$149</td><td style='background-color: #85f980'>$165</td><td style='background-color: #86f880'>$181</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='3'>Mario Kart: Super Circuit</td><td>LOCAL</td><td style='background-color: #80fe80'>$90</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #80fe80'>$90</td><td style='background-color: #88f680'>$204</td><td style='background-color: #8fef80'>$318</td><td style='background-color: #97e780'>$432</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>SHARE</td><td style='background-color: #80fe80'>$90</td><td style='background-color: #87f780'>$187</td><td style='background-color: #8df180'>$284</td><td style='background-color: #94ea80'>$381</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='3'>F-Zero: Maximum Velocity</td><td>LOCAL</td><td style='background-color: #81fd80'>$93</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #81fd80'>$93</td><td style='background-color: #88f680'>$210</td><td style='background-color: #90ee80'>$327</td><td style='background-color: #98e680'>$444</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>SHARE</td><td style='background-color: #81fd80'>$93</td><td style='background-color: #87f780'>$190</td><td style='background-color: #8df180'>$287</td><td style='background-color: #94ea80'>$384</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='3'>F-Zero: GP Legend</td><td>LOCAL</td><td style='background-color: #81fd80'>$103</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #81fd80'>$103</td><td style='background-color: #8af480'>$230</td><td style='background-color: #92ec80'>$357</td><td style='background-color: #9ae480'>$484</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>SHARE</td><td style='background-color: #81fd80'>$103</td><td style='background-color: #88f680'>$200</td><td style='background-color: #8ef080'>$297</td><td style='background-color: #94ea80'>$394</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='2'>Mario Kart: Double Dash!!</td><td>LOCAL</td><td style='background-color: #86f880'>$179</td><td style='background-color: #88f680'>$207</td><td style='background-color: #8af480'>$235</td><td style='background-color: #8cf280'>$263</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #86f880'>$179</td><td style='background-color: #96e880'>$418</td><td style='background-color: #98e680'>$446</td><td style='background-color: #9ae480'>$474</td><td style='background-color: #9ce280'>$502</td><td style='background-color: #9de180'>$530</td><td style='background-color: #9fdf80'>$558</td><td style='background-color: #a1dd80'>$586</td><td style='background-color: #afcf80'>$795</td><td style='background-color: #b1cd80'>$823</td><td style='background-color: #b3cb80'>$851</td><td style='background-color: #b4ca80'>$879</td><td style='background-color: #c2bc80'>$1088</td><td style='background-color: #c4ba80'>$1116</td><td style='background-color: #c6b880'>$1144</td><td style='background-color: #c8b680'>$1172</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='2'>Kirby Air Ride</td><td>LOCAL</td><td style='background-color: #87f780'>$190</td><td style='background-color: #89f580'>$218</td><td style='background-color: #8bf380'>$246</td><td style='background-color: #8df180'>$274</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #87f780'>$190</td><td style='background-color: #97e780'>$440</td><td style='background-color: #99e580'>$468</td><td style='background-color: #9be380'>$496</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='1'>F-Zero GX</td><td>LOCAL</td><td style='background-color: #86f880'>$180</td><td style='background-color: #88f680'>$208</td><td style='background-color: #8af480'>$236</td><td style='background-color: #8cf280'>$264</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='4'>Mario Kart DS</td><td>LOCAL</td><td style='background-color: #80ff80'>$77</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #80ff80'>$77</td><td style='background-color: #85f980'>$154</td><td style='background-color: #8af480'>$231</td><td style='background-color: #8fef80'>$308</td><td style='background-color: #94ea80'>$385</td><td style='background-color: #99e580'>$462</td><td style='background-color: #9ee080'>$539</td><td style='background-color: #a3db80'>$616</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>ONLINE</td><td style='background-color: #80ff80'>$77</td><td style='background-color: #85f980'>$154</td><td style='background-color: #8af480'>$231</td><td style='background-color: #8fef80'>$308</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>SHARE</td><td style='background-color: #80ff80'>$77</td><td style='background-color: #83fb80'>$137</td><td style='background-color: #87f780'>$197</td><td style='background-color: #8bf380'>$257</td><td style='background-color: #8fef80'>$317</td><td style='background-color: #93eb80'>$377</td><td style='background-color: #97e780'>$437</td><td style='background-color: #9be380'>$497</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='2'>Mario Kart Wii</td><td>LOCAL</td><td style='background-color: #81fd80'>$95</td><td style='background-color: #82fc80'>$108</td><td style='background-color: #82fc80'>$121</td><td style='background-color: #83fb80'>$134</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>ONLINE</td><td style='background-color: #81fd80'>$95</td><td style='background-color: #87f780'>$190</td><td style='background-color: #88f680'>$203</td><td style='background-color: #89f580'>$216</td><td style='background-color: #8fef80'>$311</td><td style='background-color: #90ee80'>$324</td><td style='background-color: #96e880'>$419</td><td style='background-color: #97e780'>$432</td><td style='background-color: #9de180'>$527</td><td style='background-color: #9ee080'>$540</td><td style='background-color: #a4da80'>$635</td><td style='background-color: #a5d980'>$648</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='4'>Mario Kart 7</td><td>LOCAL</td><td style='background-color: #82fc80'>$108</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #82fc80'>$108</td><td style='background-color: #89f580'>$216</td><td style='background-color: #90ee80'>$324</td><td style='background-color: #97e780'>$432</td><td style='background-color: #9ee080'>$540</td><td style='background-color: #a5d980'>$648</td><td style='background-color: #acd280'>$756</td><td style='background-color: #b3cb80'>$864</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>ONLINE</td><td style='background-color: #82fc80'>$108</td><td style='background-color: #89f580'>$216</td><td style='background-color: #90ee80'>$324</td><td style='background-color: #97e780'>$432</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>SHARE</td><td style='background-color: #82fc80'>$108</td><td style='background-color: #88f680'>$202</td><td style='background-color: #8ef080'>$296</td><td style='background-color: #94ea80'>$390</td><td style='background-color: #9ae480'>$484</td><td style='background-color: #a1dd80'>$578</td><td style='background-color: #a7d780'>$672</td><td style='background-color: #add180'>$766</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='2'>Mario Kart 8</td><td>LOCAL</td><td style='background-color: #84fa80'>$139</td><td style='background-color: #86f880'>$169</td><td style='background-color: #88f680'>$199</td><td style='background-color: #8af480'>$229</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>ONLINE</td><td style='background-color: #84fa80'>$139</td><td style='background-color: #8df180'>$278</td><td style='background-color: #8fef80'>$308</td><td style='background-color: #91ed80'>$338</td><td style='background-color: #9ae480'>$477</td><td style='background-color: #9ce280'>$507</td><td style='background-color: #a5d980'>$646</td><td style='background-color: #a7d780'>$676</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='3'>Mario Kart 8 Deluxe</td><td>LOCAL</td><td style='background-color: #86f880'>$170</td><td style='background-color: #86f880'>$170</td><td style='background-color: #88f680'>$206</td><td style='background-color: #8af480'>$242</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #86f880'>$170</td><td style='background-color: #94ea80'>$390</td><td style='background-color: #94ea80'>$390</td><td style='background-color: #94ea80'>$390</td><td style='background-color: #a1dd80'>$585</td><td style='background-color: #a1dd80'>$585</td><td style='background-color: #aed080'>$780</td><td style='background-color: #aed080'>$780</td><td style='background-color: #bbc380'>$975</td><td style='background-color: #bbc380'>$975</td><td style='background-color: #c8b680'>$1170</td><td style='background-color: #c8b680'>$1170</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>ONLINE</td><td style='background-color: #86f880'>$170</td><td style='background-color: #91ed80'>$340</td><td style='background-color: #91ed80'>$340</td><td style='background-color: #91ed80'>$340</td><td style='background-color: #9ce280'>$510</td><td style='background-color: #9ce280'>$510</td><td style='background-color: #a7d780'>$680</td><td style='background-color: #a7d780'>$680</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='2'>F-Zero 99</td><td>LOCAL</td><td style='background-color: #83fb80'>$135</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>ONLINE</td><td style='background-color: #83fb80'>$135</td><td style='background-color: #8cf280'>$270</td><td style='background-color: #95e980'>$405</td><td style='background-color: #9ee080'>$540</td><td style='background-color: #a7d780'>$675</td><td style='background-color: #b0ce80'>$810</td><td style='background-color: #b9c580'>$945</td><td style='background-color: #c2bc80'>$1080</td><td style='background-color: #cbb380'>$1215</td><td style='background-color: #d4aa80'>$1350</td><td style='background-color: #dca280'>$1485</td><td style='background-color: #e59980'>$1620</td><td style='background-color: #ee9080'>$1755</td><td style='background-color: #f78780'>$1890</td><td style='background-color: #ff8080'>$2025</td><td style='background-color: #ff8080'>$2160</td><td style='background-color: #ff8080'>$2295</td><td style='background-color: #ff8080'>$2430</td><td style='background-color: #ff8080'>$2565</td><td style='background-color: #ff8080'>$2700</td><td style='background-color: #ff8080'>$2835</td><td style='background-color: #ff8080'>$2970</td><td style='background-color: #ff8080'>$3105</td><td style='background-color: #ff8080'>$3240</td></tr>
<tr><td rowspan='3'>Mario Kart World</td><td>LOCAL</td><td style='background-color: #98e680'>$453</td><td style='background-color: #98e680'>$453</td><td style='background-color: #9be380'>$489</td><td style='background-color: #9de180'>$525</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #98e680'>$453</td><td style='background-color: #bac480'>$956</td><td style='background-color: #bac480'>$956</td><td style='background-color: #bac480'>$956</td><td style='background-color: #d9a580'>$1434</td><td style='background-color: #d9a580'>$1434</td><td style='background-color: #f98580'>$1912</td><td style='background-color: #f98580'>$1912</td><td style='background-color: #ff8080'>$2390</td><td style='background-color: #ff8080'>$2390</td><td style='background-color: #ff8080'>$2868</td><td style='background-color: #ff8080'>$2868</td><td style='background-color: #ff8080'>$3346</td><td style='background-color: #ff8080'>$3346</td><td style='background-color: #ff8080'>$3824</td><td style='background-color: #ff8080'>$3824</td><td style='background-color: #ff8080'>$4302</td><td style='background-color: #ff8080'>$4302</td><td style='background-color: #ff8080'>$4780</td><td style='background-color: #ff8080'>$4780</td><td style='background-color: #ff8080'>$5258</td><td style='background-color: #ff8080'>$5258</td><td style='background-color: #ff8080'>$5736</td><td style='background-color: #ff8080'>$5736</td></tr>
<tr><td>ONLINE</td><td style='background-color: #98e680'>$453</td><td style='background-color: #b6c880'>$906</td><td style='background-color: #b6c880'>$906</td><td style='background-color: #b6c880'>$906</td><td style='background-color: #d4aa80'>$1359</td><td style='background-color: #d4aa80'>$1359</td><td style='background-color: #f28c80'>$1812</td><td style='background-color: #f28c80'>$1812</td><td style='background-color: #ff8080'>$2265</td><td style='background-color: #ff8080'>$2265</td><td style='background-color: #ff8080'>$2718</td><td style='background-color: #ff8080'>$2718</td><td style='background-color: #ff8080'>$3171</td><td style='background-color: #ff8080'>$3171</td><td style='background-color: #ff8080'>$3624</td><td style='background-color: #ff8080'>$3624</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td rowspan='4'>Kirby Air Riders</td><td>LOCAL</td><td style='background-color: #98e680'>$445</td><td style='background-color: #98e680'>$445</td><td style='background-color: #9ae480'>$481</td><td style='background-color: #9de180'>$517</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>LAN</td><td style='background-color: #98e680'>$445</td><td style='background-color: #b8c680'>$940</td><td style='background-color: #d8a680'>$1410</td><td style='background-color: #f78780'>$1880</td><td style='background-color: #ff8080'>$2350</td><td style='background-color: #ff8080'>$2820</td><td style='background-color: #ff8080'>$3290</td><td style='background-color: #ff8080'>$3760</td><td style='background-color: #ff8080'>$4230</td><td style='background-color: #ff8080'>$4700</td><td style='background-color: #ff8080'>$5170</td><td style='background-color: #ff8080'>$5640</td><td style='background-color: #ff8080'>$6110</td><td style='background-color: #ff8080'>$6580</td><td style='background-color: #ff8080'>$7050</td><td style='background-color: #ff8080'>$7520</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>ONLINE</td><td style='background-color: #98e680'>$445</td><td style='background-color: #b5c980'>$890</td><td style='background-color: #b5c980'>$890</td><td style='background-color: #b5c980'>$890</td><td style='background-color: #d3ab80'>$1335</td><td style='background-color: #d3ab80'>$1335</td><td style='background-color: #f08e80'>$1780</td><td style='background-color: #f08e80'>$1780</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
<tr><td>SHARE</td><td style='background-color: #98e680'>$445</td><td style='background-color: #b2cc80'>$840</td><td style='background-color: #ccb280'>$1235</td><td style='background-color: #e69880'>$1630</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
</table>