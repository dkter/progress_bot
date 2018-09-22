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


def percentage_from_date(date: datetime.date,
                         start: datetime.date,
                         end: datetime.date) -> float:
    """
    Turn a date into a percentage in the timeline from
    `start` to `end`.
    """
    max_date = end.toordinal() - start.toordinal()
    days_past_start = date.toordinal() - start.toordinal()
    percentage = days_past_start / max_date * 100
    return percentage


def date_from_percentage(percentage: float,
                         start: datetime.date,
                         end: datetime.date) -> datetime.date:
    """
    Turn a percentage into a date in the timeline from
    `start` to `end`.
    """
    max_date = end.toordinal() - start.toordinal()
    days_past_start = percentage * max_date / 100
    date = int(days_past_start + start.toordinal())
    return datetime.date.fromordinal(date)
