# -*- coding: utf-8 -*-

"""
Display a view of the content in plain text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2019 by rgb-24bit.
:license: MIT, see LICENSE for more details.
"""

import calendar
import datetime

from flask import Blueprint, render_template


plain = Blueprint('plain', __name__)


class Timep(object):
    """Plain text display of time progress."""
    def __init__(self):
        self.now = datetime.datetime.now()

    def _build_progress_bar(self, title, curr, total, width=50):
        """The construction progress bar is similar to the following form:

        Year: [>>>>>>>>>>>>>>>>>>>>>>>>>----------------]60.00%
        """

        curr_width = curr * width // total

        bar = '{title:5}: [{curr}{remain}]{percent:.2f}%'.format(
            title = title,
            curr = '>' * curr_width,
            remain = '-' * (width - curr_width),
            percent = curr * 100 / total
        )

        return bar

    def for_year(self):
        if calendar.isleap(self.now.year):
            total = 366
        else:
            total = 365
        curr = self.now.timetuple().tm_yday
        return self._build_progress_bar('Year', curr, total)

    def for_month(self):
        total = calendar.monthrange(self.now.year, self.now.month)[1]
        return self._build_progress_bar('Month', self.now.day, total)

    def for_week(self):
        curr = self.now.weekday() * 24 + self.now.hour
        return self._build_progress_bar('Week', curr, 24 * 7)

    def for_day(self):
        curr = self.now.hour * 60 + self.now.minute
        return self._build_progress_bar('Day', curr, 24 * 60)


@plain.route('/')
def plain_main_page():
    return render_template('plain/plain.html')


@plain.route('/timep/<opt>')
def plain_timep_opt(opt):
    timep = Timep()

    timep_map = {
        'year': timep.for_year(),
        'month': timep.for_month(),
        'week': timep.for_week(),
        'day': timep.for_day()
    }

    if opt in timep_map:
        result = timep_map[opt]
    elif opt == 'all':
        result = '\n'.join(timep_map.values())
    else:
        result = 'Use like: curl /plain/timep/<all, year, month, week, day>'

    return result
