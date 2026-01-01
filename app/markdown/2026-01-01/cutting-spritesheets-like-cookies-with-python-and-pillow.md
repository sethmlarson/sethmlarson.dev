# Cutting spritesheets like cookies with Python & Pillow 🍪

*Happy new year!* 🎉 For an upcoming project on the blog requiring [many video-game sprites](https://www.spriters-resource.com/)
I've created a small tool (“sugarcookie”) using the always-lovely Python image-processing
library [Pillow](https://python-pillow.github.io/).
This tool takes a spritesheet and a list of mask colors,
a minimum size, and then cuts the spritesheet into
its component sprites.

I'm sure this could be implemented more efficiently, or with a friendly
command line interface, but for more own purposes (~10 spritesheets) this
worked just fine. Feel free to use, share, and improve.
The script is [available as a GitHub gist](https://gist.github.com/sethmlarson/92dabc8420b0d2e2e6e8c688269fe5fd), but also included below.

<!-- more -->

<details>
<summary>Source code for <code>sugarcookie</code></summary>

```python
#!/usr/bin/env python
# /// script
# requires-python = ">=3.13"
# dependencies = [
#   "Pillow",
#   "tqdm"
# ]
# ///
# License: MIT
# Copyright 2025, Seth Larson

import os.path
import math
from PIL import Image
import tqdm

# Parameters
spritesheet = ""  # Path to spritesheet.
masks = {}  # Set of 3-tuples for RGB.
min_dim = 10  # Min and max dimensions in pixels.
max_dim = 260

img = Image.open(spritesheet)
if img.mode == "RGB":  # Ensure an alpha channel.
    alpha = Image.new("L", img.size, 255)
    img.putalpha(alpha)

output_prefix = os.path.splitext(os.path.basename(spritesheet))[0]
data = img.getdata()
visited = set()
shapes = set()
reroll_shapes = set()


def getpixel(x, y) -> tuple[int, int, int, int]:
    return data[x + (img.width * y)]


def make_2n(value: int) -> int:
    return 2 ** int(math.ceil(math.log2(value)))


with tqdm.tqdm(
    desc="Cutting cookies",
    total=int(img.width * img.height),
    unit="pixels",
) as t:
    for x in range(img.width):
        for y in range(img.height):
            xy = (x, y)
            if xy in visited:
                continue
            inshape = set()
            candidates = {(x, y)}

            def add_candidates(cx, cy):
                global candidates
                candidates |= {(cx - 1, cy), (cx + 1, cy), (cx, cy - 1), (cx, cy + 1)}

            while candidates:
                cx, cy = candidates.pop()
                if (
                    (cx, cy) in visited
                    or cx < 0
                    or cx >= img.width
                    or cy < 0
                    or cy >= img.height
                    or abs(cx - x) > max_dim
                    or abs(cy - y) > max_dim
                ):
                    continue
                visited.add((cx, cy))
                rgba = r, g, b, a = getpixel(cx, cy)
                if a == 0 or (r, g, b) in masks:
                    continue
                else:
                    inshape.add((cx, cy))
                    add_candidates(cx, cy)
            if inshape:
                shapes.add(tuple(inshape))
        t.update(img.height)

max_width = 0
max_height = 0
shapes_and_offsets = []
for shape in sorted(shapes):
    min_x = img.width + 2
    min_y = img.height + 2
    max_x = -1
    max_y = -1
    for x, y in shape:
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        min_x = min(x, min_x)
        min_y = min(y, min_y)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Too small! We have to reroll this
    # potentially into another shape.
    if width < min_dim or height < min_dim:
        reroll_shapes.add(shape)
        continue

    max_width = max(max_width, width)
    max_height = max(max_height, height)
    shapes_and_offsets.append((shape, (width, height), (min_x, min_y)))

# Make them powers of two!
max_width = make_2n(max_width)
max_height = make_2n(max_height)

sprite_number = 0
with tqdm.tqdm(
    desc="Baking cookies",
    total=len(shapes_and_offsets),
    unit="sprites"
) as t:
    for shape, (width, height), (offset_x, offset_y) in shapes_and_offsets:
        new_img = Image.new(mode="RGBA", size=(max_width, max_height))
        margin_x = (max_width - width) // 2
        margin_y = (max_height - height) // 2
        for rx in range(max_width):
            for ry in range(max_height):
                x = rx + offset_x
                y = ry + offset_y
                if (x, y) not in shape:
                    continue
                new_img.putpixel((rx + margin_x, ry + margin_y), getpixel(x, y))
        new_img.save(f"images/{output_prefix}-{sprite_number}.png")
        sprite_number += 1
        t.update(1)
```

</details>

When using the tool you may find yourself needing to add additional masking
across elements, such as the original spritesheet curator's name, in order
for the cutting process to work perfectly. This script also doesn't work
great for sprites which aren't contiguous across their bounding box.
There's an exercise left to the reader to implement `reroll_shapes`, a feature
I didn't end up needing for my own project. Let me know if you implement this
and send me a patch!