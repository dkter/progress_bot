"""
progress_bot
(c) 2018 David Teresi

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

This Source Code Form is "Incompatible With Secondary Licenses", as
defined by the Mozilla Public License, v. 2.0.
"""

import math

import cairo


WIDTH, HEIGHT = 1080, 1080
ANGLE_TOP = 270 / 360 * math.pi * 2


def generate_image(percentage: int) -> cairo.ImageSurface:
    """
    Generate an image.
    """
    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    ctx = cairo.Context(img)

    # Background + outline rectangle
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0, 0, 0)
    ctx.fill()
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(142/255, 68/255, 173/255)
    ctx.set_line_width(50)
    ctx.stroke()

    # Circle to fill in
    ctx.arc(WIDTH / 2, HEIGHT / 2, 400, 0, math.pi * 2)
    ctx.set_source_rgb(189/255, 195/255, 199/255)
    ctx.set_line_width(50)
    ctx.stroke()

    # Progress
    # arc(cx, cy, r, angle1, angle2)
    # angles are measured in radians and 0 is 3 o'clock
    ctx.arc(WIDTH / 2, HEIGHT / 2, 400,
            ANGLE_TOP - percentage / 100 * (math.pi * 2),
            ANGLE_TOP)
    ctx.set_source_rgb(41/255, 128/255, 185/255)
    ctx.set_line_width(50)
    ctx.stroke()

    # Text
    text = f"{percentage}%"
    ctx.select_font_face("Lato",
                         cairo.FONT_SLANT_NORMAL,
                         cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(144.0)
    x_bearing, y_bearing, width, height, x_advance, y_advance = \
        ctx.text_extents(text)
    x = WIDTH / 2 - (width / 2 + x_bearing)
    y = HEIGHT / 2 - (height / 2 + y_bearing)
    ctx.move_to(x, y)
    ctx.show_text(text)

    return img
