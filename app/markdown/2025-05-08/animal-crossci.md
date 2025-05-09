# A(nimal Cros)SCII

What is the character encoding for Animal Crossing?
[This page](https://nookipedia.com/wiki/Secret_code/Generator) details all the characters that are allowed for player
names, town names, and passwords in Animal Crossing for the GameCube. A much larger
character set was used for writing mail and communication.

Each character was internally represented as a value between `0x00` and `0xFF`
which is the same size as ASCII, thus me naming this encoding “Animal CrosSCII”.
The characters between `0xD5` and `0xDE` are only used in the EU version. `0xDF` to `0xFF` are unused.

The names of the characters (and descriptions when ambiguous) were sourced from the [Animal Crossing decompilation project](https://github.com/ACreTeam/ac-decomp/blob/da0c91fd94282e5fa8999a2f5ace5304f2d95288/include/m_font.h#L14).
I've mapped each character to the best of my ability back to Unicode
and collected them in a table below:

<table style="width: 610px; font-variant-numeric: tabular-nums">
<thead>
<tr>
  <th>Name</th>
  <th>Hex</th>
  <th>Character</th>
  <th>Unicode</th>
</tr>
</thead>
<tbody>
<tr><td><code>INVERT_EXCLAMATION</code></td><td><code>0x00</code></td><td>︎¡</td><td>U+00A1</td></tr>
<tr><td><code>INVERT_QUESTIONMARK</code></td><td><code>0x01</code></td><td>︎¿</td><td>U+00BF</td></tr>
<tr><td><code>DIAERESIS_A</code></td><td><code>0x02</code></td><td>︎Ä</td><td>U+00C4</td></tr>
<tr><td><code>GRAVE_A</code></td><td><code>0x03</code></td><td>︎À</td><td>U+00C0</td></tr>
<tr><td><code>ACUTE_A</code></td><td><code>0x04</code></td><td>︎Á</td><td>U+00C1</td></tr>
<tr><td><code>CIRCUMFLEX_A</code></td><td><code>0x05</code></td><td>︎Â</td><td>U+00C2</td></tr>
<tr><td><code>TILDE_A</code></td><td><code>0x06</code></td><td>︎Ã</td><td>U+00C3</td></tr>
<tr><td><code>ANGSTROM_A</code></td><td><code>0x07</code></td><td>︎Ȧ</td><td>U+0226</td></tr>
<tr><td><code>CEDILLA</code></td><td><code>0x08</code></td><td>︎Ç</td><td>U+00C7</td></tr>
<tr><td><code>GRAVE_E</code></td><td><code>0x09</code></td><td>︎È</td><td>U+00C8</td></tr>
<tr><td><code>ACUTE_E</code></td><td><code>0x0A</code></td><td>︎É</td><td>U+00C9</td></tr>
<tr><td><code>CIRCUMFLEX_E</code></td><td><code>0x0B</code></td><td>︎Ê</td><td>U+00CA</td></tr>
<tr><td><code>DIARESIS_E</code></td><td><code>0x0C</code></td><td>︎Ë</td><td>U+00CB</td></tr>
<tr><td><code>GRAVE_I</code></td><td><code>0x0D</code></td><td>︎Ì</td><td>U+00CC</td></tr>
<tr><td><code>ACUTE_I</code></td><td><code>0x0E</code></td><td>︎Í</td><td>U+00CD</td></tr>
<tr><td><code>CIRCUMFLEX_I</code></td><td><code>0x0F</code></td><td>︎Î</td><td>U+00CE</td></tr>
<tr><td><code>DIARESIS_I</code></td><td><code>0x10</code></td><td>︎Ï</td><td>U+00CF</td></tr>
<tr><td><code>ETH</code></td><td><code>0x11</code></td><td>︎Đ</td><td>U+0110</td></tr>
<tr><td><code>TILDE_N</code></td><td><code>0x12</code></td><td>︎Ñ</td><td>U+00D1</td></tr>
<tr><td><code>GRAVE_O</code></td><td><code>0x13</code></td><td>︎Ò</td><td>U+00D2</td></tr>
<tr><td><code>ACUTE_O</code></td><td><code>0x14</code></td><td>︎Ó</td><td>U+00D3</td></tr>
<tr><td><code>CIRCUMFLEX_O</code></td><td><code>0x15</code></td><td>︎Ô</td><td>U+00D4</td></tr>
<tr><td><code>TILDE_O</code></td><td><code>0x16</code></td><td>︎Õ</td><td>U+00D5</td></tr>
<tr><td><code>DIARESIS_O</code></td><td><code>0x17</code></td><td>︎Ö</td><td>U+00D6</td></tr>
<tr><td><code>OE</code></td><td><code>0x18</code></td><td>︎Ø</td><td>U+00D8</td></tr>
<tr><td><code>GRAVE_U</code></td><td><code>0x19</code></td><td>︎Ù</td><td>U+00D9</td></tr>
<tr><td><code>ACUTE_U</code></td><td><code>0x1A</code></td><td>︎Ú</td><td>U+00DA</td></tr>
<tr><td><code>CIRCUMFLEX_U</code></td><td><code>0x1B</code></td><td>︎Û</td><td>U+00DB</td></tr>
<tr><td><code>DIARESIS_U</code></td><td><code>0x1C</code></td><td>︎Ü</td><td>U+00DC</td></tr>
<tr><td><code>LOWER_BETA</code></td><td><code>0x1D</code></td><td>︎β</td><td>U+03B2</td></tr>
<tr><td><code>THORN</code></td><td><code>0x1E</code></td><td>︎?</td><td>U+003F</td></tr>
<tr><td><code>GRAVE_a</code></td><td><code>0x1F</code></td><td>︎à</td><td>U+00E0</td></tr>
<tr><td><code>SPACE</code></td><td><code>0x20</code></td><td>︎ </td><td>U+0020</td></tr>
<tr><td><code>EXCLAMATION</code></td><td><code>0x21</code></td><td>︎!</td><td>U+0021</td></tr>
<tr><td><code>QUOTATION</code></td><td><code>0x22</code></td><td>︎&quot;</td><td>U+0022</td></tr>
<tr><td><code>ACUTE_a</code></td><td><code>0x23</code></td><td>︎á</td><td>U+00E1</td></tr>
<tr><td><code>CIRCUMFLEX_a</code></td><td><code>0x24</code></td><td>︎â</td><td>U+00E2</td></tr>
<tr><td><code>PERCENT</code></td><td><code>0x25</code></td><td>︎%</td><td>U+0025</td></tr>
<tr><td><code>AMPERSAND</code></td><td><code>0x26</code></td><td>︎&amp;</td><td>U+0026</td></tr>
<tr><td><code>APOSTROPHE</code></td><td><code>0x27</code></td><td>︎&#x27;</td><td>U+0027</td></tr>
<tr><td><code>OPEN_PARENTHESIS</code></td><td><code>0x28</code></td><td>︎(</td><td>U+0028</td></tr>
<tr><td><code>CLOSE_PARENTHESIS</code></td><td><code>0x29</code></td><td>︎)</td><td>U+0029</td></tr>
<tr><td><code>TILDE</code></td><td><code>0x2A</code></td><td>︎~</td><td>U+007E</td></tr>
<tr><td><code>SYMBOL_HEART</code></td><td><code>0x2B</code></td><td>︎♥</td><td>U+2665</td></tr>
<tr><td><code>COMMA</code></td><td><code>0x2C</code></td><td>︎,</td><td>U+002C</td></tr>
<tr><td><code>DASH</code></td><td><code>0x2D</code></td><td>︎-</td><td>U+002D</td></tr>
<tr><td><code>PERIOD</code></td><td><code>0x2E</code></td><td>︎.</td><td>U+002E</td></tr>
<tr><td><code>SYMBOL_MUSIC_NOTE</code></td><td><code>0x2F</code></td><td>︎𝅘𝅥𝅮</td><td>U+1D160</td></tr>
<tr><td><code>ZERO</code></td><td><code>0x30</code></td><td>︎0</td><td>U+0030</td></tr>
<tr><td><code>ONE</code></td><td><code>0x31</code></td><td>︎1</td><td>U+0031</td></tr>
<tr><td><code>TWO</code></td><td><code>0x32</code></td><td>︎2</td><td>U+0032</td></tr>
<tr><td><code>THREE</code></td><td><code>0x33</code></td><td>︎3</td><td>U+0033</td></tr>
<tr><td><code>FOUR</code></td><td><code>0x34</code></td><td>︎4</td><td>U+0034</td></tr>
<tr><td><code>FIVE</code></td><td><code>0x35</code></td><td>︎5</td><td>U+0035</td></tr>
<tr><td><code>SIX</code></td><td><code>0x36</code></td><td>︎6</td><td>U+0036</td></tr>
<tr><td><code>SEVEN</code></td><td><code>0x37</code></td><td>︎7</td><td>U+0037</td></tr>
<tr><td><code>EIGHT</code></td><td><code>0x38</code></td><td>︎8</td><td>U+0038</td></tr>
<tr><td><code>NINE</code></td><td><code>0x39</code></td><td>︎9</td><td>U+0039</td></tr>
<tr><td><code>COLON</code></td><td><code>0x3A</code></td><td>︎:</td><td>U+003A</td></tr>
<tr><td><code>SYMBOL_DROPLET</code></td><td><code>0x3B</code></td><td>︎🌢</td><td>U+1F322</td></tr>
<tr><td><code>LESS_THAN</code></td><td><code>0x3C</code></td><td>︎&lt;</td><td>U+003C</td></tr>
<tr><td><code>EQUALS</code></td><td><code>0x3D</code></td><td>︎=</td><td>U+003D</td></tr>
<tr><td><code>GREATER_THAN</code></td><td><code>0x3E</code></td><td>︎&gt;</td><td>U+003E</td></tr>
<tr><td><code>QUESTIONMARK</code></td><td><code>0x3F</code></td><td>︎?</td><td>U+003F</td></tr>
<tr><td><code>AT_SIGN</code></td><td><code>0x40</code></td><td>︎@</td><td>U+0040</td></tr>
<tr><td><code>A</code></td><td><code>0x41</code></td><td>︎A</td><td>U+0041</td></tr>
<tr><td><code>B</code></td><td><code>0x42</code></td><td>︎B</td><td>U+0042</td></tr>
<tr><td><code>C</code></td><td><code>0x43</code></td><td>︎C</td><td>U+0043</td></tr>
<tr><td><code>D</code></td><td><code>0x44</code></td><td>︎D</td><td>U+0044</td></tr>
<tr><td><code>E</code></td><td><code>0x45</code></td><td>︎E</td><td>U+0045</td></tr>
<tr><td><code>F</code></td><td><code>0x46</code></td><td>︎F</td><td>U+0046</td></tr>
<tr><td><code>G</code></td><td><code>0x47</code></td><td>︎G</td><td>U+0047</td></tr>
<tr><td><code>H</code></td><td><code>0x48</code></td><td>︎H</td><td>U+0048</td></tr>
<tr><td><code>I</code></td><td><code>0x49</code></td><td>︎I</td><td>U+0049</td></tr>
<tr><td><code>J</code></td><td><code>0x4A</code></td><td>︎J</td><td>U+004A</td></tr>
<tr><td><code>K</code></td><td><code>0x4B</code></td><td>︎K</td><td>U+004B</td></tr>
<tr><td><code>L</code></td><td><code>0x4C</code></td><td>︎L</td><td>U+004C</td></tr>
<tr><td><code>M</code></td><td><code>0x4D</code></td><td>︎M</td><td>U+004D</td></tr>
<tr><td><code>N</code></td><td><code>0x4E</code></td><td>︎N</td><td>U+004E</td></tr>
<tr><td><code>O</code></td><td><code>0x4F</code></td><td>︎O</td><td>U+004F</td></tr>
<tr><td><code>P</code></td><td><code>0x50</code></td><td>︎P</td><td>U+0050</td></tr>
<tr><td><code>Q</code></td><td><code>0x51</code></td><td>︎Q</td><td>U+0051</td></tr>
<tr><td><code>R</code></td><td><code>0x52</code></td><td>︎R</td><td>U+0052</td></tr>
<tr><td><code>S</code></td><td><code>0x53</code></td><td>︎S</td><td>U+0053</td></tr>
<tr><td><code>T</code></td><td><code>0x54</code></td><td>︎T</td><td>U+0054</td></tr>
<tr><td><code>U</code></td><td><code>0x55</code></td><td>︎U</td><td>U+0055</td></tr>
<tr><td><code>V</code></td><td><code>0x56</code></td><td>︎V</td><td>U+0056</td></tr>
<tr><td><code>W</code></td><td><code>0x57</code></td><td>︎W</td><td>U+0057</td></tr>
<tr><td><code>X</code></td><td><code>0x58</code></td><td>︎X</td><td>U+0058</td></tr>
<tr><td><code>Y</code></td><td><code>0x59</code></td><td>︎Y</td><td>U+0059</td></tr>
<tr><td><code>Z</code></td><td><code>0x5A</code></td><td>︎Z</td><td>U+005A</td></tr>
<tr><td><code>TILDE_a</code></td><td><code>0x5B</code></td><td>︎ã</td><td>U+00E3</td></tr>
<tr><td><code>SYMBOL_ANNOYED</code></td><td><code>0x5C</code></td><td>︎💢</td><td>U+1F4A2</td></tr>
<tr><td><code>DIARESIS_a</code></td><td><code>0x5D</code></td><td>︎ä</td><td>U+00E4</td></tr>
<tr><td><code>ANGSTROM_a</code></td><td><code>0x5E</code></td><td>︎ȧ</td><td>U+0227</td></tr>
<tr><td><code>UNDERSCORE</code></td><td><code>0x5F</code></td><td>︎_</td><td>U+005F</td></tr>
<tr><td><code>LOWER_CEDILLA</code></td><td><code>0x60</code></td><td>︎ç</td><td>U+00E7</td></tr>
<tr><td><code>a</code></td><td><code>0x61</code></td><td>︎a</td><td>U+0061</td></tr>
<tr><td><code>b</code></td><td><code>0x62</code></td><td>︎b</td><td>U+0062</td></tr>
<tr><td><code>c</code></td><td><code>0x63</code></td><td>︎c</td><td>U+0063</td></tr>
<tr><td><code>d</code></td><td><code>0x64</code></td><td>︎d</td><td>U+0064</td></tr>
<tr><td><code>e</code></td><td><code>0x65</code></td><td>︎e</td><td>U+0065</td></tr>
<tr><td><code>f</code></td><td><code>0x66</code></td><td>︎f</td><td>U+0066</td></tr>
<tr><td><code>g</code></td><td><code>0x67</code></td><td>︎g</td><td>U+0067</td></tr>
<tr><td><code>h</code></td><td><code>0x68</code></td><td>︎h</td><td>U+0068</td></tr>
<tr><td><code>i</code></td><td><code>0x69</code></td><td>︎i</td><td>U+0069</td></tr>
<tr><td><code>j</code></td><td><code>0x6A</code></td><td>︎j</td><td>U+006A</td></tr>
<tr><td><code>k</code></td><td><code>0x6B</code></td><td>︎k</td><td>U+006B</td></tr>
<tr><td><code>l</code></td><td><code>0x6C</code></td><td>︎l</td><td>U+006C</td></tr>
<tr><td><code>m</code></td><td><code>0x6D</code></td><td>︎m</td><td>U+006D</td></tr>
<tr><td><code>n</code></td><td><code>0x6E</code></td><td>︎n</td><td>U+006E</td></tr>
<tr><td><code>o</code></td><td><code>0x6F</code></td><td>︎o</td><td>U+006F</td></tr>
<tr><td><code>p</code></td><td><code>0x70</code></td><td>︎p</td><td>U+0070</td></tr>
<tr><td><code>q</code></td><td><code>0x71</code></td><td>︎q</td><td>U+0071</td></tr>
<tr><td><code>r</code></td><td><code>0x72</code></td><td>︎r</td><td>U+0072</td></tr>
<tr><td><code>s</code></td><td><code>0x73</code></td><td>︎s</td><td>U+0073</td></tr>
<tr><td><code>t</code></td><td><code>0x74</code></td><td>︎t</td><td>U+0074</td></tr>
<tr><td><code>u</code></td><td><code>0x75</code></td><td>︎u</td><td>U+0075</td></tr>
<tr><td><code>v</code></td><td><code>0x76</code></td><td>︎v</td><td>U+0076</td></tr>
<tr><td><code>w</code></td><td><code>0x77</code></td><td>︎w</td><td>U+0077</td></tr>
<tr><td><code>x</code></td><td><code>0x78</code></td><td>︎x</td><td>U+0078</td></tr>
<tr><td><code>y</code></td><td><code>0x79</code></td><td>︎y</td><td>U+0079</td></tr>
<tr><td><code>z</code></td><td><code>0x7A</code></td><td>︎z</td><td>U+007A</td></tr>
<tr><td><code>GRAVE_e</code></td><td><code>0x7B</code></td><td>︎è</td><td>U+00E8</td></tr>
<tr><td><code>ACUTE_e</code></td><td><code>0x7C</code></td><td>︎é</td><td>U+00E9</td></tr>
<tr><td><code>CIRCUMFLEX_e</code></td><td><code>0x7D</code></td><td>︎ê</td><td>U+00EA</td></tr>
<tr><td><code>DIARESIS_e</code></td><td><code>0x7E</code></td><td>︎ë</td><td>U+00EB</td></tr>
<tr><td><code>CONTROL_CODE</code></td><td><code>0x7F</code></td><td></td><td>???</td></tr>
<tr><td><code>MESSAGE_TAG</code></td><td><code>0x80</code></td><td></td><td>???</td></tr>
<tr><td><code>GRAVE_i</code></td><td><code>0x81</code></td><td>︎ì</td><td>U+00EC</td></tr>
<tr><td><code>ACUTE_i</code></td><td><code>0x82</code></td><td>︎í</td><td>U+00ED</td></tr>
<tr><td><code>CIRCUMFLEX_i</code></td><td><code>0x83</code></td><td>︎î</td><td>U+00EE</td></tr>
<tr><td><code>DIARESIS_i</code></td><td><code>0x84</code></td><td>︎ï</td><td>U+00EF</td></tr>
<tr><td><code>INTERPUNCT</code></td><td><code>0x85</code></td><td>︎·</td><td>U+00B7</td></tr>
<tr><td><code>LOWER_ETH</code></td><td><code>0x86</code></td><td>︎?</td><td>U+003F</td></tr>
<tr><td><code>TILDE_n</code></td><td><code>0x87</code></td><td>︎ñ</td><td>U+00F1</td></tr>
<tr><td><code>GRAVE_o</code></td><td><code>0x88</code></td><td>︎ò</td><td>U+00F2</td></tr>
<tr><td><code>ACUTE_o</code></td><td><code>0x89</code></td><td>︎ó</td><td>U+00F3</td></tr>
<tr><td><code>CIRCUMFLEX_o</code></td><td><code>0x8A</code></td><td>︎ô</td><td>U+00F4</td></tr>
<tr><td><code>TILDE_o</code></td><td><code>0x8B</code></td><td>︎õ</td><td>U+00F5</td></tr>
<tr><td><code>DIARESIS_o</code></td><td><code>0x8C</code></td><td>︎ö</td><td>U+00F6</td></tr>
<tr><td><code>oe</code></td><td><code>0x8D</code></td><td>︎ø</td><td>U+00F8</td></tr>
<tr><td><code>GRAVE_u</code></td><td><code>0x8E</code></td><td>︎ù</td><td>U+00F9</td></tr>
<tr><td><code>ACUTE_u</code></td><td><code>0x8F</code></td><td>︎ú</td><td>U+00FA</td></tr>
<tr><td><code>HYPHEN</code></td><td><code>0x90</code></td><td>︎-</td><td>U+002D</td></tr>
<tr><td><code>CIRCUMFLEX_u</code></td><td><code>0x91</code></td><td>︎û</td><td>U+00FB</td></tr>
<tr><td><code>DIARESIS_u</code></td><td><code>0x92</code></td><td>︎ü</td><td>U+00FC</td></tr>
<tr><td><code>ACUTE_y</code></td><td><code>0x93</code></td><td>︎ý</td><td>U+00FD</td></tr>
<tr><td><code>DIARESIS_y</code></td><td><code>0x94</code></td><td>︎ÿ</td><td>U+00FF</td></tr>
<tr><td><code>LOWER_THORN</code></td><td><code>0x95</code></td><td>︎þ</td><td>U+00FE</td></tr>
<tr><td><code>ACUTE_Y</code></td><td><code>0x96</code></td><td>︎Ý</td><td>U+00DD</td></tr>
<tr><td><code>BROKEN_BAR</code></td><td><code>0x97</code></td><td>︎\|</td><td>U+007C</td></tr>
<tr><td><code>SILCROW</code></td><td><code>0x98</code></td><td>︎§</td><td>U+00A7</td></tr>
<tr><td><code>FEMININE_ORDINAL</code></td><td><code>0x99</code></td><td>︎ª</td><td>U+00AA</td></tr>
<tr><td><code>MASCULINE_ORDINAL</code></td><td><code>0x9A</code></td><td>︎º</td><td>U+00BA</td></tr>
<tr><td><code>DOUBLE_VERTICAL_BAR</code></td><td><code>0x9B</code></td><td>︎∥</td><td>U+2225</td></tr>
<tr><td><code>LATIN_MU</code></td><td><code>0x9C</code></td><td>︎ᵧ</td><td>U+1D67</td></tr>
<tr><td><code>SUPERSCRIPT_THREE</code></td><td><code>0x9D</code></td><td>︎³</td><td>U+00B3</td></tr>
<tr><td><code>SUPERSCRIPT_TWO</code></td><td><code>0x9E</code></td><td>︎²</td><td>U+00B2</td></tr>
<tr><td><code>SUPRESCRIPT_ONE</code></td><td><code>0x9F</code></td><td>︎¹</td><td>U+00B9</td></tr>
<tr><td><code>MACRON_SYMBOL</code></td><td><code>0xA0</code></td><td>︎¯</td><td>U+00AF</td></tr>
<tr><td><code>LOGICAL_NEGATION</code></td><td><code>0xA1</code></td><td>︎¬</td><td>U+00AC</td></tr>
<tr><td><code>ASH</code></td><td><code>0xA2</code></td><td>︎Æ</td><td>U+00C6</td></tr>
<tr><td><code>LOWER_ASH</code></td><td><code>0xA3</code></td><td>︎æ</td><td>U+00E6</td></tr>
<tr><td><code>INVERT_QUOTATION</code></td><td><code>0xA4</code></td><td>︎„</td><td>U+201E</td></tr>
<tr><td><code>GUILLEMET_OPEN</code></td><td><code>0xA5</code></td><td>︎»</td><td>U+00BB</td></tr>
<tr><td><code>GUILLEMET_CLOSE</code></td><td><code>0xA6</code></td><td>︎«</td><td>U+00AB</td></tr>
<tr><td><code>SYMBOL_SUN</code></td><td><code>0xA7</code></td><td>︎☀</td><td>U+2600</td></tr>
<tr><td><code>SYMBOL_CLOUD</code></td><td><code>0xA8</code></td><td>︎☁</td><td>U+2601</td></tr>
<tr><td><code>SYMBOL_UMBRELLA</code></td><td><code>0xA9</code></td><td>︎☂</td><td>U+2602</td></tr>
<tr><td><code>SYMBOL_WIND</code></td><td><code>0xAA</code></td><td>︎꩜</td><td>U+AA5C</td></tr>
<tr><td><code>SYMBOL_SNOWMAN</code></td><td><code>0xAB</code></td><td>︎☃</td><td>U+2603</td></tr>
<tr><td><code>LINES_CONVERGE_RIGHT</code></td><td><code>0xAC</code></td><td>︎⚞</td><td>U+269E</td></tr>
<tr><td><code>LINES_CONVERGE_LEFT</code></td><td><code>0xAD</code></td><td>︎⚟</td><td>U+269F</td></tr>
<tr><td><code>FORWARD_SLASH</code></td><td><code>0xAE</code></td><td>︎/</td><td>U+002F</td></tr>
<tr><td><code>INFINITY</code></td><td><code>0xAF</code></td><td>︎∞</td><td>U+221E</td></tr>
<tr><td><code>CIRCLE</code></td><td><code>0xB0</code></td><td>︎⭕</td><td>U+2B55</td></tr>
<tr><td><code>CROSS</code></td><td><code>0xB1</code></td><td>︎❌</td><td>U+274C</td></tr>
<tr><td><code>SQUARE</code></td><td><code>0xB2</code></td><td>︎☐</td><td>U+2610</td></tr>
<tr><td><code>TRIANGLE</code></td><td><code>0xB3</code></td><td>︎△</td><td>U+25B3</td></tr>
<tr><td><code>PLUS</code></td><td><code>0xB4</code></td><td>︎+</td><td>U+002B</td></tr>
<tr><td><code>SYMBOL_LIGTNING</code></td><td><code>0xB5</code></td><td>︎⚡</td><td>U+26A1</td></tr>
<tr><td><code>MARS_SYMBOL</code></td><td><code>0xB6</code></td><td>︎♂</td><td>U+2642</td></tr>
<tr><td><code>VENUS_SYMBOL</code></td><td><code>0xB7</code></td><td>︎♀</td><td>U+2640</td></tr>
<tr><td><code>SYMBOL_FLOWER</code></td><td><code>0xB8</code></td><td>︎⚘</td><td>U+2698</td></tr>
<tr><td><code>SYMBOL_STAR</code></td><td><code>0xB9</code></td><td>︎★</td><td>U+2605</td></tr>
<tr><td><code>SYMBOL_SKULL</code></td><td><code>0xBA</code></td><td>︎☠</td><td>U+2620</td></tr>
<tr><td><code>SYMBOL_SURPRISE</code></td><td><code>0xBB</code></td><td>︎😯</td><td>U+1F62F</td></tr>
<tr><td><code>SYMBOL_HAPPY</code></td><td><code>0xBC</code></td><td>︎😄</td><td>U+1F604</td></tr>
<tr><td><code>SYMBOL_SAD</code></td><td><code>0xBD</code></td><td>︎😞</td><td>U+1F61E</td></tr>
<tr><td><code>SYMBOL_ANGRY</code></td><td><code>0xBE</code></td><td>︎😠</td><td>U+1F620</td></tr>
<tr><td><code>SYMBOL_SMILE</code></td><td><code>0xBF</code></td><td>︎😃</td><td>U+1F603</td></tr>
<tr><td><code>DIMENSION_SIGN</code></td><td><code>0xC0</code></td><td>︎×</td><td>U+00D7</td></tr>
<tr><td><code>OBELUS_SIGN</code></td><td><code>0xC1</code></td><td>︎÷</td><td>U+00F7</td></tr>
<tr><td><code>SYMBOL_HAMMER</code></td><td><code>0xC2</code></td><td>︎🔨</td><td>U+1F528</td></tr>
<tr><td><code>SYMBOL_RIBBON</code></td><td><code>0xC3</code></td><td>︎🎀</td><td>U+1F380</td></tr>
<tr><td><code>SYMBOL_MAIL</code></td><td><code>0xC4</code></td><td>︎✉</td><td>U+2709</td></tr>
<tr><td><code>SYMBOL_MONEY</code></td><td><code>0xC5</code></td><td>︎💰</td><td>U+1F4B0</td></tr>
<tr><td><code>SYMBOL_PAW</code></td><td><code>0xC6</code></td><td>︎🐾</td><td>U+1F43E</td></tr>
<tr><td><code>SYMBOL_SQUIRREL</code></td><td><code>0xC7</code></td><td>︎🐶</td><td>U+1F436</td></tr>
<tr><td><code>SYMBOL_CAT</code></td><td><code>0xC8</code></td><td>︎🐱</td><td>U+1F431</td></tr>
<tr><td><code>SYMBOL_RABBIT</code></td><td><code>0xC9</code></td><td>︎🐰</td><td>U+1F430</td></tr>
<tr><td><code>SYMBOL_OCTOPUS</code></td><td><code>0xCA</code></td><td>︎🐦</td><td>U+1F426</td></tr>
<tr><td><code>SYMBOL_COW</code></td><td><code>0xCB</code></td><td>︎🐮</td><td>U+1F42E</td></tr>
<tr><td><code>SYMBOL_PIG</code></td><td><code>0xCC</code></td><td>︎🐷</td><td>U+1F437</td></tr>
<tr><td><code>NEW_LINE</code></td><td><code>0xCD</code></td><td>︎␤</td><td>U+2424</td></tr>
<tr><td><code>SYMBOL_FISH</code></td><td><code>0xCE</code></td><td>︎🐟</td><td>U+1F41F</td></tr>
<tr><td><code>SYMBOL_BUG</code></td><td><code>0xCF</code></td><td>︎🪲</td><td>U+1FAB2</td></tr>
<tr><td><code>SEMICOLON</code></td><td><code>0xD0</code></td><td>︎;</td><td>U+003B</td></tr>
<tr><td><code>HASHTAG</code></td><td><code>0xD1</code></td><td>︎#</td><td>U+0023</td></tr>
<tr><td><code>SPACE_2</code></td><td><code>0xD2</code></td><td></td><td>???</td></tr>
<tr><td><code>SPACE_3</code></td><td><code>0xD3</code></td><td></td><td>???</td></tr>
<tr><td><code>SYMBOL_KEY</code></td><td><code>0xD4</code></td><td>︎🔑</td><td>U+1F511</td></tr>
<tr><td><code>LEFT_QUOTATION</code></td><td><code>0xD5</code></td><td>︎“</td><td>U+201C</td></tr>
<tr><td><code>RIGHT_QUOTATION</code></td><td><code>0xD6</code></td><td>︎”</td><td>U+201D</td></tr>
<tr><td><code>LEFT_APOSTROPHE</code></td><td><code>0xD7</code></td><td>︎‘</td><td>U+2018</td></tr>
<tr><td><code>RIGHT_APOSTROPHE</code></td><td><code>0xD8</code></td><td>︎’</td><td>U+2019</td></tr>
<tr><td><code>ETHEL</code></td><td><code>0xD9</code></td><td>︎Œ</td><td>U+0152</td></tr>
<tr><td><code>LOWER_ETHEL</code></td><td><code>0xDA</code></td><td>︎œ</td><td>U+0153</td></tr>
<tr><td><code>ORDINAL_e</code></td><td><code>0xDB</code></td><td>︎ᵉ</td><td>U+1D49</td></tr>
<tr><td><code>ORDINAL_er</code></td><td><code>0xDC</code></td><td></td><td>???</td></tr>
<tr><td><code>ORDINAL_re</code></td><td><code>0xDD</code></td><td></td><td>???</td></tr>
<tr><td><code>BACKSLASH</code></td><td><code>0xDE</code></td><td>︎\</td><td>U+005C</td></tr>
</tbody>
</table>

And here's the Unicode characters laid out into a “square”:

```
︎¡︎¿︎Ä︎À︎Á︎Â︎Ã︎Ȧ︎Ç︎È︎É︎Ê︎Ë︎Ì︎Í︎Î︎
︎Ï︎Đ︎Ñ︎Ò︎Ó︎Ô︎Õ︎Ö︎Ø︎Ù︎Ú︎Û︎Ü︎β︎?︎à︎
︎ ︎!︎"︎á︎â︎%︎&︎'︎(︎)︎~︎♥︎,︎-︎.︎𝅘𝅥𝅮︎
︎0︎1︎2︎3︎4︎5︎6︎7︎8︎9︎:︎🌢︎<︎=︎>︎?︎
︎@︎A︎B︎C︎D︎E︎F︎G︎H︎I︎J︎K︎L︎M︎N︎O︎
︎P︎Q︎R︎S︎T︎U︎V︎W︎X︎Y︎Z︎ã︎💢︎ä︎ȧ︎_︎
︎ç︎a︎b︎c︎d︎e︎f︎g︎h︎i︎j︎k︎l︎m︎n︎o︎
︎p︎q︎r︎s︎t︎u︎v︎w︎x︎y︎z︎è︎é︎ê︎ë︎ ︎
︎ ︎ì︎í︎î︎ï︎·︎?︎ñ︎ò︎ó︎ô︎õ︎ö︎ø︎ù︎ú︎
︎-︎û︎ü︎ý︎ÿ︎þ︎Ý︎|︎§︎ª︎º︎∥︎ᵧ︎³︎²︎¹︎
︎¯︎¬︎Æ︎æ︎„︎»︎«︎☀︎☁︎☂︎꩜︎☃︎⚞︎⚟︎/︎∞︎
︎⭕︎❌︎☐︎△︎+︎⚡︎♂︎♀︎⚘︎★︎☠︎😯︎😄︎😞︎😠︎😃︎
︎×︎÷︎🔨︎🎀︎✉︎💰︎🐾︎🐶︎🐱︎🐰︎🐦︎🐮︎🐷︎␤︎🐟︎🪲︎
︎;︎#︎ ︎ ︎🔑︎“︎”︎‘︎’︎Œ︎œ︎ᵉ︎ ︎ ︎\
```

I wasn't able to find Unicode equivalents to some of the characters
and a few others (marked with `???` in the table). If you're able to find Unicode characters for
the missing ones please send me an email or pull request. 
*Time to brush up on [Animalese](https://nookipedia.com/wiki/Animalese)!*
