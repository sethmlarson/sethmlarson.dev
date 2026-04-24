# More thoughts on Nintendo Switch 2 storage prices

Since my last post about Nintendo Switch 2
storage and prices three major things have happened
affecting Switch 2 game prices:

* Nintendo published a [new digital game pricing strategy](https://www.nintendo.com/us/whatsnew/about-nintendo-switch-2-game-pricing/)
  where digital first-party games would be priced $10 USD less than physical
  games. This puts the American game market in line with
  the rest of the world. We'll see below why this change makes sense.
* microSD Express cards have increased drastically in
  price. The Lexar 1TB microSDXC card cost [$200 USD in July 2025](https://sethmlarson.dev/nintendo-switch-2-physical-game-price-differences)
  and today is being sold for $335 USD from the same retailer. This
  means that “price-per-GB” has increased ~$0.13 for the highest
  capacity cards.
* Nintendo appears to be manufacturing Switch 2 game cartridges with
  [smaller than the typical 64GB capacity](https://www.youtube.com/watch?v=Wsf1jVeBVXU).
  <nobr>“[MIO: Memories in Orbit](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)”</nobr> released
  on a physical cartridge with a $30 price tag. This will hopefully
  mean fewer games being published to “[Game Key cards](https://en-americas-support.nintendo.com/app/answers/detail/a_id/68415/~/nintendo-switch%26nbsp%3B2-game-key-card-overview)”, especially smaller or indie games.

<!-- more -->

Nintendo Patent Watch [published some analysis](https://ninpatentswatch.wordpress.com/2026/04/22/game-card-memory-costs-and-suppliers/) about the new G4 Game Cards. Quoting the analysis: “Based on the pricing of several indie physicals for Switch 2, it suggests that the cost (to the publishers) of a 64GB card is around $15, and 16GB about $10”.

I [created a small Python script](https://gist.github.com/sethmlarson/6daf49f34ec11dbbbecfdef3fd1fcf08) which produces tables of data comparing physical and digital
prices comparing different microSD Express cards and their price-per-GB ratios across different Nintendo Switch 2 games.

## Mario Kart World

This is the game people think of for the Switch 2, and the $80 USD
price tag across both digital and physical provided some sticker
shock for many. I did not understand how the $60 USD standard across
all games hung on for as long as it did.

The table below
which includes both the price of the game and incremental price
of storage (depending on which storage device you purchase)
to compare the price between physical and digital.

|Edition|Storage|Total Price|Game Price|Storage Price|Game Size|
|-------|-------|----------:|---------:|------------:|--------:|
|Physical|Cartridge|$80.00|[$80.00](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|---|---|
|Digital|[Lexar 1TB (Costco)](https://www.costco.com/p/-/lexar-play-pro-1-tb-microsdxc-express-card/4000399472)|$83.87|[$80.00](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|$3.87 ([$0.18/GB](https://www.costco.com/p/-/lexar-play-pro-1-tb-microsdxc-express-card/4000399472))|[22 GB](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|
|Digital|[Lexar 512GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$86.45|[$80.00](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|$6.45 ([$0.29/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[22 GB](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|
|Digital|[Lexar 1TB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$87.20|[$80.00](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|$7.20 ([$0.33/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[22 GB](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|
|Digital|[Lexar 256GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$87.73|[$80.00](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|$7.73 ([$0.35/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[22 GB](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|
|Digital|[SanDisk 512GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$87.73|[$80.00](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|$7.73 ([$0.35/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[22 GB](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|
|Digital|[SanDisk 256GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$88.59|[$80.00](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|$8.59 ([$0.39/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[22 GB](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|
|Digital|[SanDisk 128GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$92.03|[$80.00](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|$12.03 ([$0.55/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[22 GB](https://www.nintendo.com/us/store/products/mario-kart-world-switch-2/)|

## Yoshi and the Mysterious Book

Now we look at the first game with the new pricing structure
in the USA: “Yoshi and the Mysterious Book”. The game is
priced at $70 USD physically and $60 USD digitally.
Compared to Mario Kart World where all digital editions
were *more* expensive than physical when storage costs
are factored in: almost all digital editions are cheaper
for Yoshi!

|Edition|Storage|Total Price|Game Price|Storage Price|Game Size|
|-------|-------|----------:|---------:|------------:|--------:|
|Physical|Cartridge|$70.00|[$70.00](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|---|---|
|Digital|[Lexar 1TB (Costco)](https://www.costco.com/p/-/lexar-play-pro-1-tb-microsdxc-express-card/4000399472)|$63.62|[$60.00](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|$3.62 ([$0.18/GB](https://www.costco.com/p/-/lexar-play-pro-1-tb-microsdxc-express-card/4000399472))|[20.6 GB](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|
|Digital|[Lexar 512GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$66.04|[$60.00](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|$6.04 ([$0.29/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[20.6 GB](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|
|Digital|[Lexar 1TB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$66.74|[$60.00](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|$6.74 ([$0.33/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[20.6 GB](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|
|Digital|[Lexar 256GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$67.24|[$60.00](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|$7.24 ([$0.35/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[20.6 GB](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|
|Digital|[SanDisk 512GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$67.24|[$60.00](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|$7.24 ([$0.35/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[20.6 GB](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|
|Digital|[SanDisk 256GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$68.05|[$60.00](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|$8.05 ([$0.39/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[20.6 GB](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|
|Digital|[SanDisk 128GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$71.27|[$60.00](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|$11.27 ([$0.55/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[20.6 GB](https://www.nintendo.com/us/store/products/yoshi-and-the-mysterious-book-switch-2/)|

## MIO: Memories in Orbit

MIO is the cheapest game to date that is published
on a non-“Game Key card” cartridge for the Switch 2
at $30 USD physically and $20 USD digitally. The game
being only 4GB means the digital edition is much cheaper
than the physical edition.

|Edition|Storage|Total Price|Game Price|Storage Price|Game Size|
|-------|-------|----------:|---------:|------------:|--------:|
|Physical|Cartridge|$30.00|[$30.00](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|---|---|
|Digital|[Lexar 1TB (Costco)](https://www.costco.com/p/-/lexar-play-pro-1-tb-microsdxc-express-card/4000399472)|$20.77|[$20.00](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|$0.77 ([$0.18/GB](https://www.costco.com/p/-/lexar-play-pro-1-tb-microsdxc-express-card/4000399472))|[4.4 GB](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|
|Digital|[Lexar 512GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$21.29|[$20.00](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|$1.29 ([$0.29/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[4.4 GB](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|
|Digital|[Lexar 1TB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$21.44|[$20.00](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|$1.44 ([$0.33/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[4.4 GB](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|
|Digital|[Lexar 256GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$21.55|[$20.00](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|$1.55 ([$0.35/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[4.4 GB](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|
|Digital|[SanDisk 512GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$21.55|[$20.00](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|$1.55 ([$0.35/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[4.4 GB](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|
|Digital|[SanDisk 256GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$21.72|[$20.00](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|$1.72 ([$0.39/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[4.4 GB](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|
|Digital|[SanDisk 128GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$22.41|[$20.00](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|$2.41 ([$0.55/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[4.4 GB](https://www.nintendo.com/us/store/products/mio-memories-in-orbit-switch-2/)|

## Final Fantasy VII Remake Intergrade

And finally, we look at FF7 Remake Intergrade, which
according to its Nintendo page is planned to be over 90GB
total. This massive game size makes the price to store
the game a significant percentage the total price of the game.

|Edition|Storage|Total Price|Game Price|Storage Price|Game Size|
|-------|-------|----------:|---------:|------------:|--------:|
|Digital|[Lexar 1TB (Costco)](https://www.costco.com/p/-/lexar-play-pro-1-tb-microsdxc-express-card/4000399472)|$55.89|[$40.00](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|$15.89 ([$0.18/GB](https://www.costco.com/p/-/lexar-play-pro-1-tb-microsdxc-express-card/4000399472))|[90.4 GB](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|
|Digital|[Lexar 512GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$66.48|[$40.00](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|$26.48 ([$0.29/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[90.4 GB](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|
|Digital|[Lexar 1TB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$69.57|[$40.00](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|$29.57 ([$0.33/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[90.4 GB](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|
|Digital|[Lexar 256GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/)|$71.78|[$40.00](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|$31.78 ([$0.35/GB](https://americas.lexar.com/product/lexar-play-pro-microsdxc-express-card/))|[90.4 GB](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|
|Digital|[SanDisk 512GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$71.78|[$40.00](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|$31.78 ([$0.35/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[90.4 GB](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|
|Digital|[SanDisk 256GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$75.31|[$40.00](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|$35.31 ([$0.39/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[90.4 GB](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|
|Digital|[SanDisk 128GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card)|$89.44|[$40.00](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|$49.44 ([$0.55/GB](https://www.sandisk.com/products/memory-cards/microsd-cards/sandisk-microsd-express-memory-card))|[90.4 GB](https://www.nintendo.com/us/store/products/final-fantasy-vii-remake-intergrade-switch-2/)|

It will be interesting seeing how specifically the availability of new cartridge types
will change whether companies use Game Key cards for their games. I suspect the pressure
to use Game Key cards will still be high as the cost of storage continues to increase
for companies and those costs cuts into margins.

None of these tables include the benefits and down-sides of each medium. Many digital
game buyers like not having to worry about lost or stolen games while in transit or
not having to physically store the boxes and cartridges. Many players may not need
to increase their Switch 2 storage if they only play a handful of games. And who knows,
maybe the price of storage will decrease in the future?

I hope this information helps you
make an informed choice when selecting digital or physical Nintendo Switch 2 games in the future.
Happy gaming!
