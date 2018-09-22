import unittest

import datetime
import math

import cairo

import img
import util


class TestUtil(unittest.TestCase):
    """Test class for the util module."""
    SCHOOL_START = datetime.date(2018, 9, 4)
    SCHOOL_END = datetime.date(2019, 6, 25)

    def test_percentage_from_date(self):
        self.assertEqual(util.percentage_from_date(self.SCHOOL_START,
                                                   self.SCHOOL_START,
                                                   self.SCHOOL_END), 0.0)
        self.assertEqual(util.percentage_from_date(self.SCHOOL_END,
                                                   self.SCHOOL_START,
                                                   self.SCHOOL_END), 100.0)
        middle_date = datetime.date.fromordinal(
            (self.SCHOOL_START.toordinal() + self.SCHOOL_END.toordinal()) // 2)
        self.assertEqual(util.percentage_from_date(middle_date,
                                                   self.SCHOOL_START,
                                                   self.SCHOOL_END), 50.0)

    def test_date_from_percentage(self):
        self.assertEqual(util.date_from_percentage(0.0,
                                                   self.SCHOOL_START,
                                                   self.SCHOOL_END),
                         self.SCHOOL_START)
        self.assertEqual(util.date_from_percentage(100.0,
                                                   self.SCHOOL_START,
                                                   self.SCHOOL_END),
                         self.SCHOOL_END)
        middle_date = datetime.date.fromordinal(
            (self.SCHOOL_START.toordinal() + self.SCHOOL_END.toordinal()) // 2)
        self.assertEqual(util.date_from_percentage(50.0,
                                                   self.SCHOOL_START,
                                                   self.SCHOOL_END),
                         middle_date)


class TestImg(unittest.TestCase):
    """Test class for the img module."""
    #base_img = Image.new("RGB", (1080, 1080))

    def generate_test_image(self):
        # construct image objects to test
        with cairo.ImageSurface(cairo.FORMAT_ARGB32,
                                img.WIDTH, img.HEIGHT) as img1:
            ctx = cairo.Context(img1)

            # background
            ctx.rectangle(0, 0, img.WIDTH, img.HEIGHT)
            ctx.set_source_rgb(0, 0, 0)
            ctx.fill()

            # border rectangle
            ctx.rectangle(0, 0, img.WIDTH, img.HEIGHT)
            ctx.set_source_rgb(142/255, 68/255, 173/255)
            ctx.set_line_width(50)
            ctx.stroke()

            # full grey circle
            ctx.arc(img.WIDTH / 2, img.HEIGHT / 2, 400, 0, math.pi * 2)
            ctx.set_source_rgb(189/255, 195/255, 199/255)
            ctx.set_line_width(50)
            ctx.stroke()

            # progress
            ctx.arc(img.WIDTH / 2, img.HEIGHT / 2, 400,
                    img.ANGLE_TOP - 65 / 100 * (math.pi * 2),
                    img.ANGLE_TOP)
            ctx.set_source_rgb(41/255, 128/255, 185/255)
            ctx.set_line_width(50)
            ctx.stroke()

            # text
            text = "65%"
            ctx.select_font_face("Lato",
                                 cairo.FONT_SLANT_NORMAL,
                                 cairo.FONT_WEIGHT_NORMAL)
            ctx.set_font_size(144.0)
            x_bearing, y_bearing, width, height, x_advance, y_advance = \
                ctx.text_extents(text)
            x = img.WIDTH / 2 - (width / 2 + x_bearing)
            y = img.HEIGHT / 2 - (height / 2 + y_bearing)
            ctx.move_to(x, y)
            ctx.show_text(text)

            with open("img1.png", "wb") as fobj:
                img1.write_to_png(fobj)

    def test_generate_image(self):
        img1 = img.generate_image(0)
        with open("img1.png", "wb") as fobj:
            img1.write_to_png(fobj)

        img2 = img.generate_image(65)
        with open("img2.png", "wb") as fobj:
            img2.write_to_png(fobj)

        img3 = img.generate_image(100)
        with open("img3.png", "wb") as fobj:
            img3.write_to_png(fobj)


if __name__ == '__main__':
    unittest.main()
