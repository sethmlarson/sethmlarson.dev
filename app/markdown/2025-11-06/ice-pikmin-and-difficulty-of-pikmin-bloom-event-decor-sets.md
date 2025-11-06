# Ice Pikmin and difficulty of Pikmin Bloom event decor sets

I play Pikmin Bloom regularly with a group of friends. The game
can be best described as “Pokémon Go, but walking”. One of
the main goals of the game is to collect “[decor Pikmin](https://www.pikminwiki.com/Decor_Pikmin)” which can
come from the environment, landmarks, and businesses that you walk by.
Recently there's been a change to the game that makes completing sets
of decor Pikmin **significantly more difficult**, this post
explores the new difficulty increase.

<!-- more -->

Every month there are [special decor Pikmin](https://www.pikminwiki.com/Special_Decor_Pikmin) which are earned by completing
challenges like walking, growing Pikmin, or planting flowers. The type of Pikmin
you receive is randomized between the available types, and you can only complete
the set by collecting one of [each available Pikmin type](https://www.pikminwiki.com/Pikmin_family). You can only
receive these special decors during the specific month, after the month is
over you have to wait a calendar year before you can continue collecting seedlings.

Just a few days ago there were 7 Pikmin types corresponding to the
first three mainline Pikmin games: Red, Yellow, Blue, White, Purple, Rock, and Wing Pikmin.
With the most recent update another Pikmin type has been added: [Ice Pikmin from Pikmin 4](https://pikminbloom.com/en/news/nov25-icepikmin-welcome).
This means that going forward there will be 8 Pikmin types per event decor set
instead of only 7.

**So, what does that mean for the difficulty of the game?**
I could probably do some math here, but it'd be much easier to simulate how
many event Pikmin you'd need to receive before completing the set depending
on if there are 7 or 8 total Pikmin types.

Running this [Python simulation script](https://gist.github.com/sethmlarson/e0ec72671b2362d9da4090121750179e) creates the below table which shows the difference in [cumulative
probability](https://en.wikipedia.org/wiki/Cumulative_distribution_function) for completing a decor set after receiving a number of Pikmin seedlings. For example,
if you have grown 10 seedlings you'd have a **10.5% chance** of completing the decor set
**before Ice Pikmin** and only a **2.8% chance** of completing the decor set **after Ice Pikmin**.

<table>
<thead>
<tr>
  <th># Seedlings</th>
  <th>Before</th>
  <th>After</th>
  <th>Diff</th>
</tr>
</thead>
<tbody><tr><td>7</td><td style="background-color: #fdfefd">0.6%</td><td style="background-color: #fdfefd">0.0%</td><td style="background-color: #fff9f9">-0.6%</td></tr>
<tr><td>8</td><td style="background-color: #f8fff8">2.4%</td><td style="background-color: #f8fff8">0.3%</td><td style="background-color: #ffecec">-2.2%</td></tr>
<tr><td>9</td><td style="background-color: #f0fff0">5.8%</td><td style="background-color: #f0fff0">1.1%</td><td style="background-color: #ffd7d7">-4.7%</td></tr>
<tr><td>10</td><td style="background-color: #e4fee4">10.5%</td><td style="background-color: #e4fee4">2.8%</td><td style="background-color: #ffbdbd">-7.7%</td></tr>
<tr><td>11</td><td style="background-color: #d5ffd5">16.3%</td><td style="background-color: #d5ffd5">5.6%</td><td style="background-color: #ffa4a4">-10.7%</td></tr>
<tr><td>12</td><td style="background-color: #c4ffc4">22.8%</td><td style="background-color: #c4ffc4">9.4%</td><td style="background-color: #ff8c8c">-13.5%</td></tr>
<tr><td>13</td><td style="background-color: #b3ffb3">29.7%</td><td style="background-color: #b3ffb3">13.9%</td><td style="background-color: #ff7878">-15.8%</td></tr>
<tr><td>14</td><td style="background-color: #a1ffa1">36.6%</td><td style="background-color: #a1ffa1">19.2%</td><td style="background-color: #ff6a6a">-17.4%</td></tr>
<tr><td>15</td><td style="background-color: #90ff90">43.3%</td><td style="background-color: #90ff90">24.9%</td><td style="background-color: #ff6161">-18.5%</td></tr>
<tr><td>16</td><td style="background-color: #80ff80">49.7%</td><td style="background-color: #80ff80">30.7%</td><td style="background-color: #ff5d5d">-19.0%</td></tr>
<tr><td>17</td><td style="background-color: #71ff71">55.7%</td><td style="background-color: #71ff71">36.5%</td><td style="background-color: #ff5c5c">-19.1%</td></tr>
<tr><td>18</td><td style="background-color: #63ff63">61.1%</td><td style="background-color: #63ff63">42.3%</td><td style="background-color: #ff5f5f">-18.8%</td></tr>
<tr><td>19</td><td style="background-color: #56ff56">66.0%</td><td style="background-color: #56ff56">47.9%</td><td style="background-color: #ff6464">-18.1%</td></tr>
<tr><td>20</td><td style="background-color: #4bff4b">70.4%</td><td style="background-color: #4bff4b">53.1%</td><td style="background-color: #ff6b6b">-17.3%</td></tr>
<tr><td>21</td><td style="background-color: #41ff41">74.3%</td><td style="background-color: #41ff41">57.9%</td><td style="background-color: #ff7373">-16.4%</td></tr>
<tr><td>22</td><td style="background-color: #38ff38">77.7%</td><td style="background-color: #38ff38">62.4%</td><td style="background-color: #ff7c7c">-15.3%</td></tr>
<tr><td>23</td><td style="background-color: #31ff31">80.7%</td><td style="background-color: #31ff31">66.5%</td><td style="background-color: #ff8686">-14.2%</td></tr>
<tr><td>24</td><td style="background-color: #2aff2a">83.3%</td><td style="background-color: #2aff2a">70.3%</td><td style="background-color: #fe8f8f">-13.1%</td></tr>
<tr><td>25</td><td style="background-color: #24ff24">85.6%</td><td style="background-color: #24ff24">73.6%</td><td style="background-color: #ff9999">-12.0%</td></tr>
<tr><td>26</td><td style="background-color: #1fff1f">87.6%</td><td style="background-color: #1fff1f">76.7%</td><td style="background-color: #ffa1a1">-10.9%</td></tr>
<tr><td>27</td><td style="background-color: #1bff1b">89.3%</td><td style="background-color: #1bff1b">79.4%</td><td style="background-color: #ffaaaa">-9.9%</td></tr>
<tr><td>28</td><td style="background-color: #17ff17">90.8%</td><td style="background-color: #17ff17">81.8%</td><td style="background-color: #ffb2b2">-9.0%</td></tr>
<tr><td>29</td><td style="background-color: #14ff14">92.1%</td><td style="background-color: #14ff14">84.0%</td><td style="background-color: #ffbaba">-8.1%</td></tr>
<tr><td>30</td><td style="background-color: #11ff11">93.2%</td><td style="background-color: #11ff11">85.9%</td><td style="background-color: #ffc1c1">-7.3%</td></tr>
<tr><td>31</td><td style="background-color: #0eff0e">94.2%</td><td style="background-color: #0eff0e">87.6%</td><td style="background-color: #ffc7c7">-6.5%</td></tr>
<tr><td>32</td><td style="background-color: #0cff0c">95.0%</td><td style="background-color: #0cff0c">89.1%</td><td style="background-color: #ffcdcd">-5.9%</td></tr>
<tr><td>33</td><td style="background-color: #0aff0a">95.7%</td><td style="background-color: #0aff0a">90.4%</td><td style="background-color: #ffd2d2">-5.3%</td></tr>
<tr><td>34</td><td style="background-color: #09ff09">96.3%</td><td style="background-color: #09ff09">91.6%</td><td style="background-color: #ffd7d7">-4.7%</td></tr>
<tr><td>35</td><td style="background-color: #08ff08">96.8%</td><td style="background-color: #08ff08">92.6%</td><td style="background-color: #ffdbdb">-4.2%</td></tr>
<tr><td>36</td><td style="background-color: #06ff06">97.3%</td><td style="background-color: #06ff06">93.6%</td><td style="background-color: #ffdfdf">-3.7%</td></tr>
<tr><td>37</td><td style="background-color: #05ff05">97.7%</td><td style="background-color: #05ff05">94.4%</td><td style="background-color: #ffe2e2">-3.3%</td></tr>
<tr><td>38</td><td style="background-color: #05ff05">98.0%</td><td style="background-color: #05ff05">95.1%</td><td style="background-color: #ffe5e5">-2.9%</td></tr>
<tr><td>39</td><td style="background-color: #04ff04">98.3%</td><td style="background-color: #04ff04">95.7%</td><td style="background-color: #fee8e8">-2.6%</td></tr>
<tr><td>40</td><td style="background-color: #03ff03">98.5%</td><td style="background-color: #03ff03">96.2%</td><td style="background-color: #feebeb">-2.3%</td></tr>
<tr><td>41</td><td style="background-color: #03ff03">98.7%</td><td style="background-color: #03ff03">96.7%</td><td style="background-color: #ffeded">-2.1%</td></tr>
<tr><td>42</td><td style="background-color: #02ff02">98.9%</td><td style="background-color: #02ff02">97.1%</td><td style="background-color: #ffefef">-1.8%</td></tr>
<tr><td>43</td><td style="background-color: #02ff02">99.1%</td><td style="background-color: #02ff02">97.5%</td><td style="background-color: #fff1f1">-1.6%</td></tr>
<tr><td>44</td><td style="background-color: #02ff02">99.2%</td><td style="background-color: #02ff02">97.8%</td><td style="background-color: #fff2f2">-1.4%</td></tr>
<tr><td>45</td><td style="background-color: #01ff01">99.3%</td><td style="background-color: #01ff01">98.0%</td><td style="background-color: #fff4f4">-1.3%</td></tr>
<tr><td>46</td><td style="background-color: #01ff01">99.4%</td><td style="background-color: #01ff01">98.3%</td><td style="background-color: #fff5f5">-1.1%</td></tr>
<tr><td>47</td><td style="background-color: #01ff01">99.5%</td><td style="background-color: #01ff01">98.5%</td><td style="background-color: #fff6f6">-1.0%</td></tr>
<tr><td>48</td><td style="background-color: #01ff01">99.6%</td><td style="background-color: #01ff01">98.7%</td><td style="background-color: #fff7f7">-0.9%</td></tr>
<tr><td>49</td><td style="background-color: #00ff00">99.6%</td><td style="background-color: #00ff00">98.9%</td><td style="background-color: #fff8f8">-0.8%</td></tr>
<tr><td>50</td><td style="background-color: #00ff00">99.7%</td><td style="background-color: #00ff00">99.0%</td><td style="background-color: #fff9f9">-0.7%</td></tr></tbody>
</table>

For mid-range numbers of Pikmin seedlings (13-22)
you'll be at **least 15% less likely** to have completed the Pikmin decor set
for that number of seedlings. To have a 95% chance of completing a decor set
you'd need to gather 32 seedlings prior to Ice Pikmin, with Ice Pikmin you'd
need to collect 38 seedlings.

I don't know how many event Pikmin seedlings I receive in a typical month,
I'll be watching that number and see if I'm able to complete the set. Good luck out there, Pikmin players! 😬
