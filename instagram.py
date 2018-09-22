"""
progress_bot
(c) 2018 David Teresi

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

This Source Code Form is "Incompatible With Secondary Licenses", as
defined by the Mozilla Public License, v. 2.0.
"""

import datetime
import json
from typing import List

from InstagramAPI import InstagramAPI

import img
import util
from credentials import username, password

api = InstagramAPI(username, password)
api.login()

percentages_done: List[int] = []
percentages_to_do = (3, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 69,
                     70, 75, 80, 85, 90, 95, 96, 97, 98, 99, 100)


def run_bot(start, end):
    """Get percentage and upload a photo."""
    global percentages_done
    with open("percentages_done.json", "r") as fobj:
        percentages_done = json.load(fobj)

    print("Calculating percentage")
    percentage = int(util.percentage_from_date(
        datetime.date.today(), start, end))
    print(percentage, percentages_done)

    if percentage in percentages_to_do and percentage not in percentages_done:
        print("Generating image")
        image = img.generate_image(percentage)
        with open("tempimage.png", "wb") as fobj:
            image.write_to_png(fobj)

        print("Converting to JPG")
        im = Image.open("tempimage.png")
        rgb_im = im.convert('RGB')
        rgb_im.save('tempimage.jpg')

        print("Uploading to Instagram")
        api.uploadPhoto("tempimage.jpg", caption="")
        percentages_done.append(percentage)
        with open("percentages_done.json", "w") as fobj:
            json.dump(percentages_done, fobj)


if __name__ == "__main__":
    SCHOOL_START = datetime.date(2018, 9, 4)
    SCHOOL_END = datetime.date(2019, 6, 25)
    run_bot(SCHOOL_START, SCHOOL_END)
