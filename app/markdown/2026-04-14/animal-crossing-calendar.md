# Add Animal Crossing events to your digital calendar

Animal Forest (“[Dōbutsu no Mori](https://nookipedia.com/wiki/Doubutsu_no_Mori)” or “どうぶつの森”) was released
in Japan for the Nintendo 64 on April 14th, 2001:
*exactly 25 years ago today!* To celebrate this beloved franchise I have 
created calendars for each of the “[first-generation](https://nookipedia.com/wiki/First_generation)”
Animal Crossing games that you can load
into calendar apps like Google Calendar or Apple Calendars
to see events from your town.

<!-- more -->

These calendars include holidays, special events, igloo and summer campers,
and more. Additionally, I've created a tool which can generate
importable calendars for the [birthdays](https://nookipedia.com/wiki/Birthday#In_Animal_Crossing) of villagers in your town
using data from future titles and [star signs from e-Reader cards](https://nookipedia.com/wiki/E-Reader_card#:~:text=Character%20Card,-The).

Select which game, region, and language you are interested in
and then scan the QR code or copy the URL and import the calendar
manually into your calendar application. Note that calendars are only available for a valid “game + region + language” combinations
such as: “Animal Forest e+ + <nobr>NTSC-J</nobr> + Japanese”.

<!-- rss -->

<blockquote>
<form>
<div class="row">
<div class="col-4">
<center><div id="qrcode"></div><br><div id="qrcodeLabel"></div></center>
</div>
<div class="col-3">
<label>Game</label><br>
<input type="radio" id="game-af" name="game" value="AF" checked/><label for="game-af">Animal Forest</label><br>
<input type="radio" id="game-af+" name="game" value="AF+"/><label for="game-af+">Animal Forest+</label><br>
<input type="radio" id="game-ac" name="game" value="AC"/><label for="game-ac">Animal Crossing</label><br>
<input type="radio" id="game-afe+" name="game" value="AFe+"/><label for="game-afe+">Animal Forest e+</label><br>
</div>
<div class="col-3">
<label>Region</label><br>
<input type="radio" name="region" id="region-ntsc-j" value="NTSC-J" checked/><label for="region-ntsc-j">Japan (NTSC-J)</label><br>
<input type="radio" name="region" id="region-ntsc" value="NTSC"/><label for="region-ntsc">America (NTSC)</label><br>
<input type="radio" name="region" id="region-pal" value="PAL"/><label for="region-pal">Europe (PAL)</label><br>
</div>
<div class="col-2">
<label>Language</label><br>
<input type="radio" name="language" id="language-jpn" value="JPN" checked/><label for="language-jpn">Japanese</label><br>
<input type="radio" name="language" id="language-eng" value="ENG"/><label for="language-eng">English</label><br>
<br>
</div>
</div>
</form>
</blockquote>

This project would not be possible without many contributions to
Animal Crossing game preservation such as [Nookipedia](https://nookipedia.com),
the [Animal Crossing decompilation project](https://github.com/ACreTeam/ac-decomp/), [Animal Crossing Megasheets](https://nookipedia.com/wiki/Community:ACGC_Spreadsheet),
and more. Thank you to everyone who contributes to these resources
and for cherishing an important game for many people, including myself.
The code to generate these calendars and birthdays is [available on
GitHub](https://github.com/sethmlarson/animal-crossing-calendar/), licensed MIT. Data is licensed according to their respective owners.
If you find issues, [please submit them on GitHub](https://github.com/sethmlarson/animal-crossing-calendar/issues/).

## Villager Birthdays

<blockquote>
<center>
<label for="villager">Villager:</label>
<select id="villager" style="border: 2px black solid; border-radius: 0;">
<option value="ACE">Ace</option>
<option value="ADMIRAL">Admiral</option>
<option value="AGENTS">Agent S</option>
<option value="AGNES">Agnes</option>
<option value="AIRU">アイル</option>
<option value="AL">Al</option>
<option value="ALFONSO">Alfonso</option>
<option value="ALICE">Alice</option>
<option value="ALLI">Alli</option>
<option value="AMELIA">Amelia</option>
<option value="ANABELLE">Anabelle</option>
<option value="ANAROGU">アナログ</option>
<option value="ANCHOVY">Anchovy</option>
<option value="ANGUS">Angus</option>
<option value="ANICOTTI">Anicotti</option>
<option value="ANKHA">Ankha</option>
<option value="ANNALISA">Annalisa</option>
<option value="ANNALISE">Annalise</option>
<option value="ANTONIO">Antonio</option>
<option value="APOLLO">Apollo</option>
<option value="APPLE">Apple</option>
<option value="ASTRID">Astrid</option>
<option value="AUDIE">Audie</option>
<option value="AURORA">Aurora</option>
<option value="AVA">Ava</option>
<option value="AVERY">Avery</option>
<option value="AXEL">Axel</option>
<option value="AZALEA">Azalea</option>
<option value="AZIZ">Aziz</option>
<option value="BAABARA">Baabara</option>
<option value="BAM">Bam</option>
<option value="BANGLE">Bangle</option>
<option value="BAROLD">Barold</option>
<option value="BAU">バウ</option>
<option value="BEA">Bea</option>
<option value="BEARDO">Beardo</option>
<option value="BEAU">Beau</option>
<option value="BECKY">Becky</option>
<option value="BELLA">Bella</option>
<option value="BELLE">Belle</option>
<option value="BENEDICT">Benedict</option>
<option value="BENJAMIN">Benjamin</option>
<option value="BERTHA">Bertha</option>
<option value="BESSIE">Bessie</option>
<option value="BETTINA">Bettina</option>
<option value="BETTY">Betty</option>
<option value="BIANCA">Bianca</option>
<option value="BIFF">Biff</option>
<option value="BIGTOP">Big Top</option>
<option value="BILL">Bill</option>
<option value="BILLY">Billy</option>
<option value="BISKIT">Biskit</option>
<option value="BITTY">Bitty</option>
<option value="BLAIRE">Blaire</option>
<option value="BLANCA">Blanca</option>
<option value="BLANCHE">Blanche</option>
<option value="BLATHERS">Blathers</option>
<option value="BLUEBEAR">Bluebear</option>
<option value="BOB">Bob</option>
<option value="BONBON">Bonbon</option>
<option value="BONES">Bones</option>
<option value="BOOKER">Booker</option>
<option value="BOOMER">Boomer</option>
<option value="BOONE">Boone</option>
<option value="BOOTS">Boots</option>
<option value="BORIS">Boris</option>
<option value="BOYD">Boyd</option>
<option value="BREE">Bree</option>
<option value="BREWSTER">Brewster</option>
<option value="BROCCOLO">Broccolo</option>
<option value="BROFFINA">Broffina</option>
<option value="BRUCE">Bruce</option>
<option value="BUBBLES">Bubbles</option>
<option value="BUCK">Buck</option>
<option value="BUD">Bud</option>
<option value="BUNNIE">Bunnie</option>
<option value="BUTCH">Butch</option>
<option value="BUZZ">Buzz</option>
<option value="CALLY">Cally</option>
<option value="CAMOFROG">Camofrog</option>
<option value="CANBERRA">Canberra</option>
<option value="CANDI">Candi</option>
<option value="CARMEN">Carmen</option>
<option value="CAROLINE">Caroline</option>
<option value="CARRIE">Carrie</option>
<option value="CASHMERE">Cashmere</option>
<option value="CECE">Cece</option>
<option value="CELESTE">Celeste</option>
<option value="CELIA">Celia</option>
<option value="CEPHALOBOT">Cephalobot</option>
<option value="CESAR">Cesar</option>
<option value="CHABWICK">Chabwick</option>
<option value="CHADDER">Chadder</option>
<option value="CHAI">Chai</option>
<option value="CHAMP">Champ</option>
<option value="CHARLISE">Charlise</option>
<option value="CHELSEA">Chelsea</option>
<option value="CHERI">Cheri</option>
<option value="CHERRY">Cherry</option>
<option value="CHESTER">Chester</option>
<option value="CHEVRE">Chevre</option>
<option value="CHICO">Chico</option>
<option value="CHIEF">Chief</option>
<option value="CHIP">Chip</option>
<option value="CHOPS">Chops</option>
<option value="CHOW">Chow</option>
<option value="CHRISSY">Chrissy</option>
<option value="CHUCK">Chuck</option>
<option value="CJ">C.J</option>
<option value="CLAUDE">Claude</option>
<option value="CLAUDIA">Claudia</option>
<option value="CLAY">Clay</option>
<option value="CLEO">Cleo</option>
<option value="CLYDE">Clyde</option>
<option value="COACH">Coach</option>
<option value="COBB">Cobb</option>
<option value="COCO">Coco</option>
<option value="COLE">Cole</option>
<option value="COLTON">Colton</option>
<option value="COOKIE">Cookie</option>
<option value="COPPER">Copper</option>
<option value="CORNIMER">Cornimer</option>
<option value="COUSTEAU">Cousteau</option>
<option value="CRANSTON">Cranston</option>
<option value="CROQUE">Croque</option>
<option value="CUBE">Cube</option>
<option value="CUPCAKE">Cupcake</option>
<option value="CURLOS">Curlos</option>
<option value="CURLY">Curly</option>
<option value="CURT">Curt</option>
<option value="CYD">Cyd</option>
<option value="CYRANO">Cyrano</option>
<option value="CYRUS">Cyrus</option>
<option value="DAISY">Daisy</option>
<option value="DAISYMAE">Daisy Mae</option>
<option value="DEENA">Deena</option>
<option value="DEIRDRE">Deirdre</option>
<option value="DEL">Del</option>
<option value="DELI">Deli</option>
<option value="DERWIN">Derwin</option>
<option value="DIANA">Diana</option>
<option value="DIGBY">Digby</option>
<option value="DIVA">Diva</option>
<option value="DIZZY">Dizzy</option>
<option value="DJKK">DJ KK</option>
<option value="DOBIE">Dobie</option>
<option value="DOC">Doc</option>
<option value="DOM">Dom</option>
<option value="DON">Don</option>
<option value="DORA">Dora</option>
<option value="DOTTY">Dotty</option>
<option value="DOZER">Dozer</option>
<option value="DRAGO">Drago</option>
<option value="DRAKE">Drake</option>
<option value="DRIFT">Drift</option>
<option value="ED">Ed</option>
<option value="EGBERT">Egbert</option>
<option value="ELINA">Elina</option>
<option value="ELISE">Elise</option>
<option value="ELLIE">Ellie</option>
<option value="ELMER">Elmer</option>
<option value="ELOISE">Eloise</option>
<option value="ELVIS">Elvis</option>
<option value="EMERALD">Emerald</option>
<option value="EPONA">Epona</option>
<option value="ERIK">Erik</option>
<option value="EUGENE">Eugene</option>
<option value="EUNICE">Eunice</option>
<option value="FAITH">Faith</option>
<option value="FANG">Fang</option>
<option value="FAUNA">Fauna</option>
<option value="FELICITY">Felicity</option>
<option value="FELYNE">Felyne</option>
<option value="FILBERT">Filbert</option>
<option value="FILLY">Filly</option>
<option value="FLASH">Flash</option>
<option value="FLICK">Flick</option>
<option value="FLIP">Flip</option>
<option value="FLO">Flo</option>
<option value="FLORA">Flora</option>
<option value="FLOSSIE">Flossie</option>
<option value="FLURRY">Flurry</option>
<option value="FRANCINE">Francine</option>
<option value="FRANK">Frank</option>
<option value="FRANKLIN">Franklin</option>
<option value="FRECKLES">Freckles</option>
<option value="FRETT">Frett</option>
<option value="FREYA">Freya</option>
<option value="FRIGA">Friga</option>
<option value="FRITA">Frita</option>
<option value="FROBERT">Frobert</option>
<option value="FUCHSIA">Fuchsia</option>
<option value="FURŪTĪ">フルーティー</option>
<option value="GABI">Gabi</option>
<option value="GALA">Gala</option>
<option value="GANON">Ganon</option>
<option value="GASTON">Gaston</option>
<option value="GAYLE">Gayle</option>
<option value="GEN">ゲン</option>
<option value="GENJI">Genji</option>
<option value="GIGI">Gigi</option>
<option value="GLADYS">Gladys</option>
<option value="GLORIA">Gloria</option>
<option value="GOLDIE">Goldie</option>
<option value="GONZO">Gonzo</option>
<option value="GOOSE">Goose</option>
<option value="GRACIE">Gracie</option>
<option value="GRAHAM">Graham</option>
<option value="GRAMS">Grams</option>
<option value="GRETA">Greta</option>
<option value="GRIZZLY">Grizzly</option>
<option value="GROUCHO">Groucho</option>
<option value="GRUFF">Gruff</option>
<option value="GULLIVARRR">Gullivarrr</option>
<option value="GULLIVER">Gulliver</option>
<option value="GWEN">Gwen</option>
<option value="HAMBO">Hambo</option>
<option value="HAMLET">Hamlet</option>
<option value="HAMPHREY">Hamphrey</option>
<option value="HANK">Hank</option>
<option value="HANS">Hans</option>
<option value="HARRIET">Harriet</option>
<option value="HARRY">Harry</option>
<option value="HARVEY">Harvey</option>
<option value="HAZEL">Hazel</option>
<option value="HECTOR">Hector</option>
<option value="HENRY">Henry</option>
<option value="HIPPEUX">Hippeux</option>
<option value="HOLDEN">Holden</option>
<option value="HOPKINS">Hopkins</option>
<option value="HOPPER">Hopper</option>
<option value="HORNSBY">Hornsby</option>
<option value="HUCK">Huck</option>
<option value="HUGGY">Huggy</option>
<option value="HUGH">Hugh</option>
<option value="IGGLY">Iggly</option>
<option value="IGGY">Iggy</option>
<option value="IKE">Ike</option>
<option value="INKWELL">Inkwell</option>
<option value="IONE">Ione</option>
<option value="ISABELLE">Isabelle</option>
<option value="JACK">Jack</option>
<option value="JACOB">Jacob</option>
<option value="JACQUES">Jacques</option>
<option value="JAMBETTE">Jambette</option>
<option value="JANE">Jane</option>
<option value="JAY">Jay</option>
<option value="JEREMIAH">Jeremiah</option>
<option value="JINGLE">Jingle</option>
<option value="JITTERS">Jitters</option>
<option value="JOAN">Joan</option>
<option value="JOEY">Joey</option>
<option value="JUDY">Judy</option>
<option value="JULIA">Julia</option>
<option value="JULIAN">Julian</option>
<option value="JUNE">June</option>
<option value="JŌ">ジョー</option>
<option value="JŪBĒ">ジュウベエ</option>
<option value="KABUKI">Kabuki</option>
<option value="KAPP'N">Kapp'n</option>
<option value="KATIE">Katie</option>
<option value="KATRINA">Katrina</option>
<option value="KATT">Katt</option>
<option value="KEATON">Keaton</option>
<option value="KEN">Ken</option>
<option value="KETCHUP">Ketchup</option>
<option value="KEVIN">Kevin</option>
<option value="KICKS">Kicks</option>
<option value="KIDCAT">Kid Cat</option>
<option value="KIDD">Kidd</option>
<option value="KIKI">Kiki</option>
<option value="KITT">Kitt</option>
<option value="KITTO">キット</option>
<option value="KITTY">Kitty</option>
<option value="KK">K.K</option>
<option value="KLAUS">Klaus</option>
<option value="KNOX">Knox</option>
<option value="KODY">Kody</option>
<option value="KOHARU">こはる</option>
<option value="KURARA">クララ</option>
<option value="KYAROTTO">キャロット</option>
<option value="KYLE">Kyle</option>
<option value="LABEL">Label</option>
<option value="LEIF">Leif</option>
<option value="LEIGH">Leigh</option>
<option value="LEILA">Leila</option>
<option value="LEILANI">Leilani</option>
<option value="LEONARDO">Leonardo</option>
<option value="LEOPOLD">Leopold</option>
<option value="LILY">Lily</option>
<option value="LIMBERG">Limberg</option>
<option value="LIONEL">Lionel</option>
<option value="LIZ">Liz</option>
<option value="LOBO">Lobo</option>
<option value="LOLLY">Lolly</option>
<option value="LOPEZ">Lopez</option>
<option value="LOUIE">Louie</option>
<option value="LUCHA">Lucha</option>
<option value="LUCKY">Lucky</option>
<option value="LUCY">Lucy</option>
<option value="LULU">Lulu</option>
<option value="LUNA">Luna</option>
<option value="LYLE">Lyle</option>
<option value="LYMAN">Lyman</option>
<option value="MABEL">Mabel</option>
<option value="MAC">Mac</option>
<option value="MADAMURŌZA">マダムローザ</option>
<option value="MADDIE">Maddie</option>
<option value="MAELLE">Maelle</option>
<option value="MAGGIE">Maggie</option>
<option value="MALLARY">Mallary</option>
<option value="MAPLE">Maple</option>
<option value="MARCEL">Marcel</option>
<option value="MARCIE">Marcie</option>
<option value="MARCY">Marcy</option>
<option value="MARGIE">Margie</option>
<option value="MARINA">Marina</option>
<option value="MARLO">Marlo</option>
<option value="MARSHAL">Marshal</option>
<option value="MARTY">Marty</option>
<option value="MASA">マサ</option>
<option value="MATHILDA">Mathilda</option>
<option value="MEDLI">Medli</option>
<option value="MEGAN">Megan</option>
<option value="MEGUMI">メグミ</option>
<option value="MELBA">Melba</option>
<option value="MERENGUE">Merengue</option>
<option value="MERRY">Merry</option>
<option value="MIDGE">Midge</option>
<option value="MINERU">Mineru</option>
<option value="MINT">Mint</option>
<option value="MIRA">Mira</option>
<option value="MIRANDA">Miranda</option>
<option value="MITZI">Mitzi</option>
<option value="MOE">Moe</option>
<option value="MOLLY">Molly</option>
<option value="MONIQUE">Monique</option>
<option value="MONTY">Monty</option>
<option value="MOOSE">Moose</option>
<option value="MOTT">Mott</option>
<option value="MUFFY">Muffy</option>
<option value="MURPHY">Murphy</option>
<option value="MYAU">ミャウ</option>
<option value="NAN">Nan</option>
<option value="NANA">Nana</option>
<option value="NAOMI">Naomi</option>
<option value="NAT">Nat</option>
<option value="NATE">Nate</option>
<option value="NIBBLES">Nibbles</option>
<option value="NIKO">Niko</option>
<option value="NINDORI">ニンドリ</option>
<option value="NORMA">Norma</option>
<option value="NOSEGAY">Nosegay</option>
<option value="O'HARE">O'Hare</option>
<option value="OCTAVIAN">Octavian</option>
<option value="OLAF">Olaf</option>
<option value="OLIVE">Olive</option>
<option value="OLIVIA">Olivia</option>
<option value="OPAL">Opal</option>
<option value="ORVILLE">Orville</option>
<option value="OTIS">Otis</option>
<option value="OXFORD">Oxford</option>
<option value="OZZIE">Ozzie</option>
<option value="PANCETTI">Pancetti</option>
<option value="PANGO">Pango</option>
<option value="PAOLO">Paolo</option>
<option value="PAPI">Papi</option>
<option value="PASCAL">Pascal</option>
<option value="PASHMINA">Pashmina</option>
<option value="PATE">Pate</option>
<option value="PATORISHIA">パトリシア</option>
<option value="PATTY">Patty</option>
<option value="PAULA">Paula</option>
<option value="PAVÉ">Pavé</option>
<option value="PEACHES">Peaches</option>
<option value="PEANUT">Peanut</option>
<option value="PECAN">Pecan</option>
<option value="PECK">Peck</option>
<option value="PEEWEE">Peewee</option>
<option value="PEGGY">Peggy</option>
<option value="PEKOE">Pekoe</option>
<option value="PELLY">Pelly</option>
<option value="PENELOPE">Penelope</option>
<option value="PENNY">Penny</option>
<option value="PETE">Pete</option>
<option value="PETRI">Petri</option>
<option value="PETUNIA">Petunia</option>
<option value="PHIL">Phil</option>
<option value="PHINEAS">Phineas</option>
<option value="PHOEBE">Phoebe</option>
<option value="PHYLLIS">Phyllis</option>
<option value="PIERCE">Pierce</option>
<option value="PIETRO">Pietro</option>
<option value="PIGLEG">Pigleg</option>
<option value="PINKY">Pinky</option>
<option value="PIPER">Piper</option>
<option value="PIPPY">Pippy</option>
<option value="PIĒRU">ピエール</option>
<option value="PLUCKY">Plucky</option>
<option value="POKO">ポコ</option>
<option value="POMPOM">Pompom</option>
<option value="PONCHO">Poncho</option>
<option value="POPPY">Poppy</option>
<option value="PORTER">Porter</option>
<option value="PORTIA">Portia</option>
<option value="PRINCE">Prince</option>
<option value="PUCK">Puck</option>
<option value="PUDDLES">Puddles</option>
<option value="PUDGE">Pudge</option>
<option value="PUNCHY">Punchy</option>
<option value="PURRL">Purrl</option>
<option value="QUEENIE">Queenie</option>
<option value="QUETZAL">Quetzal</option>
<option value="QUILLSON">Quillson</option>
<option value="QUINN">Quinn</option>
<option value="RADDLE">Raddle</option>
<option value="RASHER">Rasher</option>
<option value="RAYMOND">Raymond</option>
<option value="REDD">Redd</option>
<option value="REESE">Reese</option>
<option value="RENEIGH">Reneigh</option>
<option value="RENÉE">Renée</option>
<option value="RESETTI">Resetti</option>
<option value="REX">Rex</option>
<option value="RHODA">Rhoda</option>
<option value="RHONDA">Rhonda</option>
<option value="RIBBOT">Ribbot</option>
<option value="RICKY">Ricky</option>
<option value="RILLA">Rilla</option>
<option value="RIO">Rio</option>
<option value="RIZZO">Rizzo</option>
<option value="ROALD">Roald</option>
<option value="ROBIN">Robin</option>
<option value="ROCCO">Rocco</option>
<option value="ROCKET">Rocket</option>
<option value="ROD">Rod</option>
<option value="RODEO">Rodeo</option>
<option value="RODNEY">Rodney</option>
<option value="ROLF">Rolf</option>
<option value="ROLLO">Rollo</option>
<option value="ROONEY">Rooney</option>
<option value="RORY">Rory</option>
<option value="ROSCOE">Roscoe</option>
<option value="ROSIE">Rosie</option>
<option value="ROSWELL">Roswell</option>
<option value="ROVER">Rover</option>
<option value="ROWAN">Rowan</option>
<option value="RUBY">Ruby</option>
<option value="RUDY">Rudy</option>
<option value="RURU">ルル</option>
<option value="SABLE">Sable</option>
<option value="SAHARAH">Saharah</option>
<option value="SALLY">Sally</option>
<option value="SAMSON">Samson</option>
<option value="SANDY">Sandy</option>
<option value="SANĪ">サニー</option>
<option value="SASHA">Sasha</option>
<option value="SAVANNAH">Savannah</option>
<option value="SCOOT">Scoot</option>
<option value="SHARI">Shari</option>
<option value="SHELDON">Sheldon</option>
<option value="SHEP">Shep</option>
<option value="SHERB">Sherb</option>
<option value="SHINABIRU">シナビル</option>
<option value="SHINO">Shino</option>
<option value="SHOUKICHI">しょうきち</option>
<option value="SHRUNK">Shrunk</option>
<option value="SIMON">Simon</option>
<option value="SKYE">Skye</option>
<option value="SLY">Sly</option>
<option value="SNAKE">Snake</option>
<option value="SNOOTY">Snooty</option>
<option value="SOLEIL">Soleil</option>
<option value="SPARRO">Sparro</option>
<option value="SPIKE">Spike</option>
<option value="SPORK">Spork</option>
<option value="SPRINKLE">Sprinkle</option>
<option value="SPROCKET">Sprocket</option>
<option value="STATIC">Static</option>
<option value="STELLA">Stella</option>
<option value="STERLING">Sterling</option>
<option value="STINKY">Stinky</option>
<option value="STITCHES">Stitches</option>
<option value="STU">Stu</option>
<option value="SUEE">Sue E</option>
<option value="SVEN">Sven</option>
<option value="SYDNEY">Sydney</option>
<option value="SYLVANA">Sylvana</option>
<option value="SYLVIA">Sylvia</option>
<option value="TABBY">Tabby</option>
<option value="TAD">Tad</option>
<option value="TAMMI">Tammi</option>
<option value="TAMMY">Tammy</option>
<option value="TANGY">Tangy</option>
<option value="TANK">Tank</option>
<option value="TARŌ">タロウ</option>
<option value="TASHA">Tasha</option>
<option value="TBONE">T-Bone</option>
<option value="TEDDY">Teddy</option>
<option value="TEX">Tex</option>
<option value="TIA">Tia</option>
<option value="TIANSHENG">Tiansheng</option>
<option value="TIARA">Tiara</option>
<option value="TIFFANY">Tiffany</option>
<option value="TIMBRA">Timbra</option>
<option value="TIMMY">Timmy</option>
<option value="TIPPER">Tipper</option>
<option value="TOBY">Toby</option>
<option value="TOM">Tom</option>
<option value="TOMMY">Tommy</option>
<option value="TOMNOOK">Tom Nook</option>
<option value="TORTIMER">Tortimer</option>
<option value="TRUFFLES">Truffles</option>
<option value="TUCKER">Tucker</option>
<option value="TULIN">Tulin</option>
<option value="TUTU">Tutu</option>
<option value="TWIGGY">Twiggy</option>
<option value="TWIRP">Twirp</option>
<option value="TYBALT">Tybalt</option>
<option value="URSALA">Ursala</option>
<option value="VALISE">Valise</option>
<option value="VELMA">Velma</option>
<option value="VESTA">Vesta</option>
<option value="VIC">Vic</option>
<option value="VICHÉ">Viché</option>
<option value="VICTORIA">Victoria</option>
<option value="VIOLET">Violet</option>
<option value="VIVIAN">Vivian</option>
<option value="VLADIMIR">Vladimir</option>
<option value="WADE">Wade</option>
<option value="WALKER">Walker</option>
<option value="WALT">Walt</option>
<option value="WARDELL">Wardell</option>
<option value="WARTJR">Wart Jr</option>
<option value="WEBER">Weber</option>
<option value="WENDELL">Wendell</option>
<option value="WENDY">Wendy</option>
<option value="WERUDAN">ウェルダン</option>
<option value="WHITNEY">Whitney</option>
<option value="WILBUR">Wilbur</option>
<option value="WILLOW">Willow</option>
<option value="WINNIE">Winnie</option>
<option value="WISP">Wisp</option>
<option value="WLINK">W. Link</option>
<option value="WOLFGANG">Wolfgang</option>
<option value="WOOLIO">Woolio</option>
<option value="YODEL">Yodel</option>
<option value="YUKA">Yuka</option>
<option value="ZELL">Zell</option>
<option value="ZIPPER">Zipper</option>
<option value="ZOE">Zoe</option>
<option value="ZUCKER">Zucker</option>
<option value="ÉTOILE">Étoile</option>
</select><br>
<div id="qrcode2"></div><br><div id="qrcodeLabel2"></div>
</center>
</blockquote>

Villager birthdays were added in Animal Crossing Wild World,
so none of the first-generation Animal Crossing game supported villager
birthdays. There are 321 unique villagers across all first-generation
games. Of those 321 villagers, 258 villagers appear in future
games and can have their birthdays mapped from those games.

We have some information to go on for what the remaining
62 villagers' birthdays might be. Every villager from the
first generation has an e-Reader card that contains
information about the villager, including their star sign.
This star sign was used for a [single GBA e-Reader mini-game
about match-making](https://www.youtube.com/watch?v=UkyscChSQJM&t=339s), where the player would swipe two
e-Reader cards and be rewarded for compatible matches.

The 62 villagers without known birthdays are listed below, the vast majority
are exclusive to all first-generation games (32) or only Animal Forest e+ (24).
Below is a table with these villagers, and an "unofficial birthday" (*) column
that I've generated myself, methodology below the table:

<table>
<thead>
<tr>
  <th>Name</th>
  <th>Birthday *</th>
  <th>Star Sign</th>
  <th>Games</th>
</tr>
</thead>
<tbody>
<tr>
  <td><a href="https://nookipedia.com/wiki/Hector">Hector</a></td>
  <td>Mar 31</td>
  <td rowspan="6">Aries</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Rhoda">Rhoda</a></td>
  <td>Apr 19</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Woolio">Woolio</a></td>
  <td>Apr 14</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Gen">ゲン (Gen)</a></td>
  <td>Apr 10</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Poko">ポコ (Poko)</a></td>
  <td>Apr 5</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Megumi">メグミ (Megumi)</a></td>
  <td>Mar 24</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Bessie">Bessie</a></td>
  <td>May 11</td>
  <td rowspan="4">Taurus</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Chuck">Chuck</a></td>
  <td>May 1</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Oxford">Oxford</a></td>
  <td>Apr 21</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Petunia">Petunia</a></td>
  <td>Apr 26</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Betty">Betty</a></td>
  <td>May 28</td>
  <td rowspan="5">Gemini</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Cupcake">Cupcake</a></td>
  <td>Jun 12</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Flash">Flash</a></td>
  <td>Jun 20</td>
  
  <td>AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Kyarotto">キャロット (Kyarotto)</a></td>
  <td>Jun 7</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Tarō">タロウ (Tarō)</a></td>
  <td>May 30</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Belle">Belle</a></td>
  <td>Jun 22</td>
  <td rowspan="7">Cancer</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Elina">Elina</a></td>
  <td>Jul 6</td>
  
  <td>AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Emerald">Emerald</a></td>
  <td>Jul 16</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Marcy">Marcy</a></td>
  <td>Jun 25</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Penny">Penny</a></td>
  <td>Jul 10</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Shinabiru">シナビル (Shinabiru)</a></td>
  <td>Jul 18</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Jō">ジョー (Jō)</a></td>
  <td>Jun 23</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Pigleg">Pigleg</a></td>
  <td>Jul 29</td>
  <td rowspan="4">Leo</td>
  <td>AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Rollo">Rollo</a></td>
  <td>Aug 15</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Twirp">Twirp</a></td>
  <td>Aug 5</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Bau">バウ (Bau)</a></td>
  <td>Jul 23</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Hambo">Hambo</a></td>
  <td>Sep 2</td>
  <td rowspan="5">Virgo</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Liz">Liz</a></td>
  <td>Aug 23</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Quetzal">Quetzal</a></td>
  <td>Aug 25</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Patorishia">パトリシア (Patorishia)</a></td>
  <td>Sep 21</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Myau">ミャウ (Myau)</a></td>
  <td>Sep 13</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Flossie">Flossie</a></td>
  <td>Sep 29</td>
  <td rowspan="5">Libra</td>
  <td>AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Hank">Hank</a></td>
  <td>Sep 23</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Sue E">Sue E</a></td>
  <td>Oct 18</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Koharu">こはる (Koharu)</a></td>
  <td>Oct 2</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Kitto">キット (Kitto)</a></td>
  <td>Sep 27</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Tiara">Tiara</a></td>
  <td>Nov 11</td>
  <td rowspan="2">Scorpio</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Madamurōza">マダムローザ (Madamurōza)</a></td>
  <td>Nov 10</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Jane">Jane</a></td>
  <td>Dec 21</td>
  <td rowspan="9">Sagittarius</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Leigh">Leigh</a></td>
  <td>Dec 20</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Lulu">Lulu</a></td>
  <td>Dec 12</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Valise">Valise</a></td>
  <td>Nov 24</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Yodel">Yodel</a></td>
  <td>Dec 11</td>
  
  <td>AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Sanī">サニー (Sanī)</a></td>
  <td>Dec 15</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Jūbē">ジュウベエ (Jūbē)</a></td>
  <td>Dec 6</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Piēru">ピエール (Piēru)</a></td>
  <td>Nov 23</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Furūtī">フルーティー (Furūtī)</a></td>
  <td>Nov 27</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Chico">Chico</a></td>
  <td>Jan 4</td>
  <td rowspan="6">Capricorn</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Iggy">Iggy</a></td>
  <td>Dec 26</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Otis">Otis</a></td>
  <td>Jan 10</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Sven">Sven</a></td>
  <td>Dec 31</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Shoukichi">しょうきち (Shoukichi)</a></td>
  <td>Dec 22</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Airu">アイル (Airu)</a></td>
  <td>Jan 18</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Nosegay">Nosegay</a></td>
  <td>Feb 2</td>
  <td rowspan="3">Aquarius</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Anarogu">アナログ (Anarogu)</a></td>
  <td>Feb 12</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Werudan">ウェルダン (Werudan)</a></td>
  <td>Feb 14</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Aziz">Aziz</a></td>
  <td>Feb 29</td>
  <td rowspan="6">Pisces</td>
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Dozer">Dozer</a></td>
  <td>Mar 15</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Huggy">Huggy</a></td>
  <td>Mar 13</td>
  
  <td>AF, AF+, AC, AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Kurara">クララ (Kurara)</a></td>
  <td>Mar 19</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Masa">マサ (Masa)</a></td>
  <td>Feb 25</td>
  
  <td>AFe+</td>
</tr>
<tr>
  <td><a href="https://nookipedia.com/wiki/Ruru">ルル (Ruru)</a></td>
  <td>Mar 18</td>
  
  <td>AFe+</td>
</tr>
</tbody>
</table>

To assign birthdays for these villagers I gathered a list of dates
that did not yet have a villager with a birthday per star sign
and then randomly assigned birthdays to minimize "overlaps".
It turns out there's enough "slots" in each star sign to do this
without any overlaps, although Cancer is close with exactly 7
villagers without known birthdays and 7 open days:

|Star Sign|Villagers|Available|
|-|-|-|
|Aries|6|9|
|Taurus|4|13|
|Gemini|5|11|
|Cancer|7|7|
|Leo|4|10|
|Virgo|5|11|
|Libra|5|7|
|Scorpio|2|13|
|Sagittarius|9|10|
|Capricorn|6|9|
|Aquarius|3|8|
|Pisces|6|15|

If you're doing the math, you'll notice there's a single villager
unaccounted for. It turns out that there is **just one villager**
from Animal Forest e+ with a known birthday: [Nindori](https://nookipedia.com/wiki/Nindori). Nindori is special
because his birthday, September 14th, is [printed on his e-Reader card](https://nookipedia.com/wiki/Nindori#Card%20profiles:~:text=e%2DReader%20card,-Expand) as a "fun fact".
This date is special because it's the date the [Nintendo GameCube](https://nookipedia.com/wiki/Nintendo_GameCube) released
in Japan. Nindori's design is based on the Japanese-exclusive
spice-orange GameCube.

## How many years of Animal Crossing are left?

Animal Crossing for the GameCube is not an infinite game. After a certain year,
depending on which game you are playing, time will stop advancing. Once time freezes
every year will be the same as the previous year:

| Game             | Last Year |
|------------------|-----------|
| Animal Forest    | 2032      |
| Animal Forest+   | 2032      |
| Animal Crossing  | 2030      |
| Animal Forest e+ | 2030      |

This means that without mods, you only have 6 years left
before years stop advancing in all first-generation Animal Crossing games.

This was likely only done due to a single holiday: the [Harvest Moon Festival](https://nookipedia.com/wiki/Autumn_Moon) which corresponds
to the real-life holiday the “[Mid-Autumn Festival](https://en.wikipedia.org/wiki/Mid-Autumn_Festival)”.
This holiday follows the [Lunisolar calendar](https://en.wikipedia.org/wiki/Lunisolar_calendar)
instead of the Gregorian calendar. The dates for
the Harvest Moon were pre-calculated and stored as a lookup table
and the final "year" in each game corresponds to the last year in this
lookup table. The lookup tables were different for each game:

| Year  | Real | AF/AF+ | AC/AFe+ |
|-------|------|--------|---------|
| 2000  | 9/12 | 9/12   |         |
| 2001  | 10/1 | 10/1   |         |
| 2002  | 9/21 | 9/21   | 9/15    |
| 2003  | 9/11 | 9/11   | 9/10    |
| 2004  | 9/28 | 9/28   | 9/28    |
| 2005  | 9/18 | 9/18   | 9/18    |
| 2006  | 10/6 | 10/6   | 10/7    |
| 2007  | 9/25 | 9/25   | 9/26    |
| 2008  | 9/14 | 9/14   | 9/15    |
| 2009  | 10/3 | 10/3   | 10/4    |
| 2010  | 9/22 | 9/22   | 9/23    |
| 2011  | 9/12 | 9/12   | 9/12    |
| 2012  | 9/30 | 9/30   | 9/30    |
| 2013  | 9/19 | 9/19   | 9/19    |
| 2014  | 9/8  | 9/8    | 9/9     |
| 2015  | 9/27 | 9/27   | 9/28    |
| 2016  | 9/15 | 9/15   | 9/16    |
| 2017  | 10/4 | 10/4   | 10/5    |
| 2018  | 9/24 | 9/24   | 9/25    |
| 2019  | 9/13 | 9/13   | 9/14    |
| 2020  | 10/1 | 10/1   | 10/1    |
| 2021  | 9/21 | 9/21   | 9/20    |
| 2022  | 9/10 | 9/10   | 9/10    |
| 2023  | 9/29 | 9/29   | 9/29    |
| 2024  | 9/17 | 9/17   | 9/18    |
| 2025  | 10/6 | 10/6   | 10/7    |
| 2026  | 9/25 | 9/25   | 9/26    |
| 2027  | 9/15 | 9/15   | 9/15    |
| 2028  | 10/3 | 10/3   | 10/3    |
| 2029  | 9/22 | 9/22   | 9/22    |
| 2030  | 9/12 | 9/12   | 9/13    |
| 2031  | 10/1 | 10/1   |         |
| 2032  | 9/19 | 9/19   |         |

You'll notice that the dates for Animal Crossing
and Animal Forest e+ are sometimes not correct and the dates
for Animal Forest and Animal Forest+ are perfectly
aligned with the real dates for the harvest moon. Why they changed the
algorithm they were using to generates these dates
we'll likely never know.

If you're looking to play Animal Crossing beyond 2032, you are in luck! There is a mod for Animal Crossing
called “[Animal Crossing Deluxe](https://www.youtube.com/watch?v=YXmvaUAQSpM)” which extends the
last year in the game to 2099 and adds many quality of life features.

## Mushrooming Season

This event is one of the shortest per day,
running from 8:00 to 9:15AM as every 15 minutes
one of the mushrooms is found by a villager
and removed from the game.
The event doesn't have an official name in
Japanese, as the message board only references
the type of mushroom not 'Mushrooming Season'.
The name included in the calendars in Japanese
is an unofficial name.

## “Tom Nook’s Shop Hours”

Some events like the [Raffle](https://nookipedia.com/wiki/Raffle),
[Sale Day](https://nookipedia.com/wiki/Nook_Friday), or [Fukubukuro](https://nookipedia.com/wiki/Nook_Friday) occur at different times depending
on the current hours of Tom Nook’s shop. This value changes
depending on the tier of shop you have in your town. This
is something I didn't notice when I first played Animal Crossing:

| Shop         | Hours        |
|--------------|--------------|
| [Nook's Cranny](https://nookipedia.com/wiki/Nook%27s_Cranny) | 9am-10pm     |
| [Nook 'n' Go](https://nookipedia.com/wiki/Nook_%27n%27_Go)  | **7am-11pm** |
| [Nookway](https://nookipedia.com/wiki/Nookway)      | 9am-10pm     |
| [Nookingtons](https://nookipedia.com/wiki/Nookington%27s)  | 9am-10pm     |

Because Nook 'n' Go is open for three
additional hours compared to the other shop stages,
this means these events are available for longer, too.
To avoid giving incorrect information in the
calendars I simply put the event as being "9am-10pm".

## Town Day

There is a single holiday in Animal Crossing and Animal Forest e+
that has no defined date: "[Town Day](https://nookipedia.com/wiki/Hometown_Day)".
This holiday takes place on a random date in July (but not July 4th)
and is randomly determined during town generation.
For this reason, it is not included in the calendars for these games.

In Animal Forest+ this holiday occurs on
a fixed date: [February 11th](https://en.wikipedia.org/wiki/en:National_Foundation_Day_(Japan)).

## Tent Campers and “Summer Weekends”

[Tent Campers](https://nookipedia.com/wiki/Camping_Season) occur on “every summer weekend”
starting June 1st ...but sometimes also May 26th (if June 1st is a Saturday?).
This is also the only event that spans multiple days but can be broken
up by other holidays (like the Fireworks Show). I don't think my implementation
is correct, if anyone would like to fix it up then [submit a pull request](https://github.com/sethmlarson/animal-crossing-calendar/).

## Regional differences

To generate this section I created a calendar for
a single year (2026) for each game and then ran a textual
diff tool to find some smaller differences, here's what I found:

* Animal Crossing PAL has Labor Day on May 1st compared to
  Animal Crossing NTSC with Labor Day on September 1st.
* Animal Crossing PAL has Spring Cleaning Day on March 15th
  instead of May 1st.
* Animal Forest e+ has the same events as Animal Crossing except
  for a new event: [Tanabata](https://nookipedia.com/wiki/Starcrossed_Day) or “Star Festival Day”
  on July 7th.

## Physical Animal Crossing calendar

In addition to digital calendars, I have also procured a real-life calendar
for Animal Crossing for the year 2003. The calendar was distributed by Nintendo Power
in [Volume 164](https://archive.org/details/nintendo-power-issue-164-january-2003) as a promotional item. This calendar has holidays in-game
mixed with holidays in the United States of America and Canada.
The seasons are denoted by the backgrounds, ranging from snow in winter to dark green
grass for summer and leaves for autumn.

<div class="row">
<div class="col-6">
<center>
<img style="max-width: 100%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_4826_new.jpeg">
</center>
</div>
<div class="col-6">
<center>
<img style="max-width: 100%; border: 2px black solid;" src="https://storage.googleapis.com/sethmlarson-dev-static-assets/IMG_4828_new.jpeg">
</center>
</div>
</div>

Here are the complete list of events noted on the calendar:

<blockquote>
<details>
<summary>List of all events</summary>
<ul>
<li>New Year's Day</li>
<li>Martin Luther King Jr. Day (USA)</li>
<li>Groundhog Day</li>
<li>Valentine's Day</li>
<li>President's Day (USA)</li>
<li>St. Patrick's Day</li>
<li>Spring Sports Fair / Vernal Equinox</li>
<li>April Fool's Day</li>
<li>Cherry Blossom Festival</li>
<li>Daylight Savings Time Begins</li>
<li>Nature Day / Earth Day</li>
<li>Spring Cleaning</li>
<li>Mother's Day</li>
<li>Armed Forced Day (USA)</li>
<li>Victoria Day (Canada)</li>
<li>Memorial Day (USA)</li>
<li>Summer Fishing Tourney</li>
<li>Graduation Day</li>
<li>Flag Day (USA)</li>
<li>Father's Day</li>
<li>Summer Solstice</li>
<li>Quebec Day (Canada)</li>
<li>Canada Day (Canada)</li>
<li>Fireworks Show / Independence Day (USA)</li>
<li>Morning Aerobics</li>
<li>Meteor Shower</li>
<li>Founder's Day</li>
<li>Labor Day</li>
<li>Harvest Moon</li>
<li>Fall Sports Fair / Autumnal Equinox</li>
<li>Explorer's Day / Columbus Day (USA) / Thanksgiving (Canada)</li>
<li>Mushrooming Season</li>
<li>Daylight Savings Time Ends</li>
<li>Halloween</li>
<li>Fall Fishing Tourney</li>
<li>Mayor's Day / Election (USA)</li>
<li>Officer's Day / Veterans Day (USA) / Remembrance Day (Canada)</li>
<li>Harvest Festival / Thanksgiving (USA)</li>
<li>Sale Day</li>
<li>Snow Day</li>
<li>Winter Solstice</li>
<li>Toy Day</li>
<li>Jingle Comes to Town</li>
<li>New Year's Eve</li>
</ul>
</details>
</blockquote>

## Why are the iCalendar/ICS files so large?

Because at a minimum Apple calendars does not
support [the `RDATE` iCalendar feature](https://datatracker.ietf.org/doc/html/rfc5545#section-3.8.5.3).
Theis feature make it space-efficient to repeat an
event across multiple irregular dates. Unfortunately, it's not possible to
represent a set of dates in a Lunisolar calendar
within the Gregorian calendar using only `RRULE`, you
need to actually pre-calculate the dates.

It's likely that Android calendars also don't
support the entirety of the iCalendar RFCs, but I can't
verify this on my own. Therefore, I went with
the simplest approach that works on at least
Apple calendars: duplicate events completely and use
`RECURRENCE-ID`.

<script>
'use strict';function QRCode(r){var n,t,o,e,a=[],f=[],i=Math.max,u=Math.min,h=Math.abs,v=Math.ceil,c=/^[0-9]*$/,s=/^[A-Z0-9 $%*+.\/:-]*$/,l="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:",g=[[-1,7,10,15,20,26,18,20,24,30,18,20,24,26,30,22,24,28,30,28,28,28,28,30,30,26,28,30,30,30,30,30,30,30,30,30,30,30,30,30,30],[-1,10,16,26,18,24,16,18,22,22,26,30,22,22,24,24,28,28,26,26,26,26,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28],[-1,13,22,18,26,18,24,18,22,20,24,28,26,24,20,30,24,28,28,26,30,28,30,30,30,30,28,30,30,30,30,30,30,30,30,30,30,30,30,30,30],[-1,17,28,22,16,22,28,26,26,24,28,24,28,22,24,24,30,28,28,26,28,30,24,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]],d=[[-1,1,1,1,1,1,2,2,2,2,4,4,4,4,4,6,6,6,6,7,8,8,9,9,10,12,12,12,13,14,15,16,17,18,19,19,20,21,22,24,25],[-1,1,1,1,2,2,4,4,4,5,5,5,8,9,9,10,10,11,13,14,16,17,17,18,20,21,23,25,26,28,29,31,33,35,37,38,40,43,45,47,49],[-1,1,1,2,2,4,4,6,6,8,8,8,10,12,16,12,17,16,18,21,20,23,23,25,27,29,34,34,35,38,40,43,45,48,51,53,56,59,62,65,68],[-1,1,1,2,4,4,4,5,6,8,8,11,11,16,16,18,16,19,21,25,25,25,34,30,32,35,37,40,42,45,48,51,54,57,60,63,66,70,74,77,81]],m={L:[0,1],M:[1,0],Q:[2,3],H:[3,2]},p=function(r,n){for(var t=0,o=8;o--;)t=t<<1^285*(t>>>7)^(n>>>o&1)*r;return t},C=function(r,n){for(var t=[],o=r.length,e=o;e;)for(var a=r[o-e--]^t.shift(),f=n.length;f--;)t[f]^=p(n[f],a);return t},w=function(r){for(var n=[function(){return 0==(t+o)%2},function(){return 0==t%2},function(){return 0==o%3},function(){return 0==(t+o)%3},function(){return 0==((t/2|0)+(o/3|0))%2},function(){return 0==t*o%2+t*o%3},function(){return 0==(t*o%2+t*o%3)%2},function(){return 0==((t+o)%2+t*o%3)%2}][r],t=e;t--;)for(var o=e;o--;)f[t][o]||(a[t][o]^=n())},b=function(){for(var r=function(r,n){n[6]||(r+=e),n.shift(),n.push(r)},n=function(n,o,a){return n&&(r(o,a),o=0),r(o+=e,a),t(a)},t=function(r){var n=r[5],t=n>0&&r[4]==n&&r[3]==3*n&&r[2]==n&&r[1]==n;return(t&&r[6]>=4*n&&r[0]>=n?1:0)+(t&&r[0]>=4*n&&r[6]>=n?1:0)},o=0,f=e*e,i=0,u=e;u--;){for(var c=[0,0,0,0,0,0,0],s=[0,0,0,0,0,0,0],l=!1,g=!1,d=0,m=0,p=e;p--;){a[u][p]==l?5==++d?o+=3:d>5&&o++:(r(d,c),o+=40*t(c),d=1,l=a[u][p]),a[p][u]==g?5==++m?o+=3:m>5&&o++:(r(m,s),o+=40*t(s),m=1,g=a[p][u]);var C=a[u][p];C&&i++,p&&u&&C==a[u][p-1]&&C==a[u-1][p]&&C==a[u-1][p-1]&&(o+=3)}o+=40*n(l,d,c)+40*n(g,m,s)}return o+=10*(v(h(20*i-10*f)/f)-1)},A=function(r,n,t){for(;n--;)t.push(r>>>n&1)},M=function(r,n){return r.numBitsCharCount[(n+7)/17|0]},B=function(r,n){return 0!=(r>>>n&1)},x=function(r,n){for(var t=0,o=r.length;o--;){var e=r[o],a=M(e,n);if(1<<a<=e.numChars)return 1/0;t+=4+a+e.bitData.length}return t},D=function(r){if(r<1||r>40)throw"Version number out of range";var n=(16*r+128)*r+64;if(r>=2){var t=r/7|2;n-=(25*t-10)*t-55,r>=7&&(n-=36)}return n},I=function(r,n){for(var t=2;-2<=t;t--)for(var o=2;-2<=o;o--)E(r+o,n+t,1!=i(h(o),h(t)))},H=function(r,n){for(var t=4;-4<=t;t--)for(var o=4;-4<=o;o--){var a=i(h(o),h(t)),f=r+o,u=n+t;0<=f&&f<e&&0<=u&&u<e&&E(f,u,2!=a&&4!=a)}},$=function(r){for(var n=t[1]<<3|r,o=n,a=10;a--;)o=o<<1^1335*(o>>>9);var f=21522^(n<<10|o);if(f>>>15!=0)throw"Assertion error";for(a=0;a<=5;a++)E(8,a,B(f,a));E(8,7,B(f,6)),E(8,8,B(f,7)),E(7,8,B(f,8));for(a=9;a<15;a++)E(14-a,8,B(f,a));for(a=0;a<8;a++)E(e-1-a,8,B(f,a));for(a=8;a<15;a++)E(8,e-15+a,B(f,a));E(8,e-8,1)},O=function(){for(var r=e;r--;)E(6,r,0==r%2),E(r,6,0==r%2);for(var t=function(){var r=[];if(n>1)for(var t=2+(n/7|0),o=32==n?26:2*v((e-13)/(2*t-2));t--;)r[t]=t*o+6;return r}(),o=r=t.length;o--;)for(var a=r;a--;)0==a&&0==o||0==a&&o==r-1||a==r-1&&0==o||I(t[a],t[o]);H(3,3),H(e-4,3),H(3,e-4),$(0),function(){if(!(7>n)){for(var r=n,t=12;t--;)r=r<<1^7973*(r>>>11);var o=n<<12|r;if(t=18,o>>>18!=0)throw"Assertion error";for(;t--;){var a=e-11+t%3,f=t/3|0,i=B(o,t);E(a,f,i),E(f,a,i)}}}()},Q=function(r){if(r.length!=V(n,t))throw"Invalid argument";for(var o=d[t[0]][n],e=g[t[0]][n],a=D(n)/8|0,f=o-a%o,i=a/o|0,u=[],h=function(r){var n=1,t=[];t[r-1]=1;for(var o=0;o<r;o++){for(var e=0;e<r;e++)t[e]=p(t[e],n)^t[e+1];n=p(n,2)}return t}(e),v=0,c=0;v<o;v++){var s=r.slice(c,c+i-e+(v<f?0:1));c+=s.length;var l=C(s,h);v<f&&s.push(0),u.push(s.concat(l))}var m=[];for(v=0;v<u[0].length;v++)for(var w=0;w<u.length;w++)(v!=i-e||w>=f)&&m.push(u[w][v]);return m},S=function(r){for(var n=[],t=(r=encodeURI(r),0);t<r.length;t++)"%"!=r.charAt(t)?n.push(r.charCodeAt(t)):(n.push(parseInt(r.substr(t+1,2),16)),t+=2);return n},V=function(r,n){return(D(r)/8|0)-g[n[0]][r]*d[n[0]][r]},E=function(r,n,t){a[n][r]=t?1:0,f[n][r]=1},R=function(r){for(var n=[],t=0,o=r;t<o.length;t++){var e=o[t];A(e,8,n)}return{modeBits:4,numBitsCharCount:[8,16,16],numChars:r.length,bitData:n}},Z=function(r){if(!c.test(r))throw"String contains non-numeric characters";for(var n=[],t=0;t<r.length;){var o=u(r.length-t,3);A(parseInt(r.substr(t,o),10),3*o+1,n),t+=o}return{modeBits:1,numBitsCharCount:[10,12,14],numChars:r.length,bitData:n}},z=function(r){if(!s.test(r))throw"String contains unencodable characters in alphanumeric mode";var n,t=[];for(n=0;n+2<=r.length;n+=2){var o=45*l.indexOf(r.charAt(n));o+=l.indexOf(r.charAt(n+1)),A(o,11,t)}return n<r.length&&A(l.indexOf(r.charAt(n)),6,t),{modeBits:2,numBitsCharCount:[9,11,13],numChars:r.length,bitData:t}},L=function(r,n,t,o){var e=function(r){return""==r?[]:c.test(r)?[Z(r)]:s.test(r)?[z(r)]:[R(S(r))]}(r);return U(e,n,t,o)},N=function(r,i,u,h){t=i,o=h;for(var v=e=4*(n=r)+17;v--;)a[v]=[],f[v]=[];if(O(),function(r){for(var n=0,t=1,o=e-1,i=o;i>0;i-=2){6==i&&--i;for(var u=0>(t=-t)?o:0,h=0;h<e;++h){for(var v=i;v>i-2;--v)f[u][v]||(a[u][v]=B(r[n>>>3],7-(7&n)),++n);u+=t}}}(Q(u)),0>o){var c=1e9;for(v=8;v--;){w(v),$(v);var s=b();c>s&&(c=s,o=v),w(v)}}w(o),$(o),f=[]},U=function(r,n,t,o,e,a){if(void 0===e&&(e=1),void 0===a&&(a=40),void 0===o&&(o=-1),void 0===t&&(t=!0),!(1<=e&&e<=a&&a<=40)||o<-1||o>7)throw"Invalid value";for(var f=[],i=236,h=[],v=e;;){var c=x(r,v);if(c<=8*V(v,n))break;if(v>=a)throw"Data too long";v++}if(t)for(var s=(l=[m.H,m.Q,m.M]).length;s--;)c<=8*V(v,l[s])&&(n=l[s]);for(var l=0;l<r.length;l++){var g=r[l];A(g.modeBits,4,f),A(g.numChars,M(g,v),f);for(var d=0,p=g.bitData;d<p.length;d++)f.push(p[d])}if(f.length!=c)throw"Assertion error";var C=8*V(v,n);if(f.length>C)throw"Assertion error";if(A(0,u(4,C-f.length),f),A(0,(8-f.length%8)%8,f),f.length%8!=0)throw"Assertion error";for(;f.length<C;)A(i,8,f),i^=253;for(s=f.length;s--;)h[s>>>3]|=f[s]<<7-(7&s);return N(v,n,h,o)};return function(){function n(r){return/^#[0-9a-f]{3}(?:[0-9a-f]{3})?$/i.test(r)}function t(r,n){for(var t in r=document.createElementNS(s,r),n||{})r.setAttribute(t,n[t]);return r}var o,f,i,u,v,c,s="http://www.w3.org/2000/svg",l="",g="string"==typeof r?{msg:r}:r||{},d=g.pal||["#000"],p=h(g.dim)||256,C=[1,0,0,1,c=(c=h(g.pad))>-1?c:4,c],w=n(w=d[0])?w:"#000",b=n(b=d[1])?b:0,A=g.vrb?0:1;for(L(g.msg||"",m[g.ecl]||m.M,0==g.ecb?0:1,g.mtx),v=e+2*c,i=e;i--;)for(u=0,f=e;f--;)a[i][f]&&(A?(u++,a[i][f-1]||(l+="M"+f+","+i+"h"+u+"v1h-"+u+"v-1z",u=0)):l+="M"+f+","+i+"h1v1h-1v-1z");return o=t("svg",{viewBox:[0,0,v,v].join(" "),width:p,height:p,fill:w,"shape-rendering":"crispEdges",xmlns:s,version:"1.1"}),b&&o.appendChild(t("path",{fill:b,d:"M0,0V"+v+"H"+v+"V0H0Z"})),o.appendChild(t("path",{transform:"matrix("+C+")",d:l})),o}()}
function makeQrCode(data) {
  return new QRCode({
    msg: data,
    ecl: 'L',
    dim: 196,
  });
}
function computeCalendarQRCode() {
  var form = document.forms[0];
  var game = form.elements["game"].value;
  var region = form.elements["region"].value;
  var language = form.elements["language"].value;
  var filename = `CAL-${game}-${region}-${language}.ics`;
  var isValid = [
    'CAL-AF-NTSC-J-JPN.ics',
    'CAL-AF+-NTSC-J-JPN.ics',
    'CAL-AFe+-NTSC-J-JPN.ics',
    'CAL-AF-NTSC-J-ENG.ics',
    'CAL-AF+-NTSC-J-ENG.ics',
    'CAL-AFe+-NTSC-J-ENG.ics',
    'CAL-AC-NTSC-ENG.ics',
    'CAL-AC-PAL-ENG.ics',
  ].includes(filename);
  var url = `https://raw.githubusercontent.com/sethmlarson/animal-crossing-calendar/refs/heads/main/ics/${filename}`;
  var qrcodeLabel = `<a href="${url}">${filename}</a>`;
  if (!isValid) {
    qrcodeLabel = "INVALID GAME/REGION";
  };
  var qrcode = makeQrCode(url);
  qrcode.setAttribute('id', 'qrcode');
  document.getElementById("qrcode").replaceWith(qrcode);
  document.getElementById("qrcodeLabel").innerHTML = qrcodeLabel;
};
function computeBirthdayQRCode() {
  var villager = document.getElementById('villager').value;
  var filename = `BDAY-${villager}.ics`;
  var url = `https://raw.githubusercontent.com/sethmlarson/animal-crossing-calendar/refs/heads/main/ics/${filename}`;
  var qrcodeLabel2 = `<a href="${url}">${filename}</a>`;
  var qrcode2 = makeQrCode(url);
  qrcode2.setAttribute('id', 'qrcode2');
  document.getElementById("qrcode2").replaceWith(qrcode2);
  document.getElementById("qrcodeLabel2").innerHTML = qrcodeLabel2;
};
var formInputs = document.querySelectorAll("input[type=radio]");
formInputs.forEach(el => {el.addEventListener("change", function (e) {computeCalendarQRCode()})});
var selectInputs = document.querySelectorAll("select");
selectInputs.forEach(el => {el.addEventListener("change", function (e) {computeBirthdayQRCode()})});
computeCalendarQRCode();
computeBirthdayQRCode();
</script>