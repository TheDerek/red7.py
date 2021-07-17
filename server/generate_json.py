#!/usr/bin/env python

from thederek.red7.cards import COLOUR_MAPPINGS
import itertools
import json

colours = list(COLOUR_MAPPINGS.keys())
colours.reverse()
numbers = range(1, 8)
width = 375
height = 525

frames = []
size = {
    "w": width,
    "h": height
}

for colour_index, colour in enumerate(colours):
    for number_index, number in enumerate(numbers):
        filename = f"{colour}{number}"
        frames.append({
            "filename": filename,
            "frame": {
                "x": number_index * width,
                "y": colour_index * height,
                **size,
            },
            "spriteSourceSize": {"x": 0, "y": 0, **size},
            "sourceSize": size,
            "pivot": {"x": 0.5, "y": 0.5}
        })

dump = {"frames": frames}
print(json.dumps(dump))
