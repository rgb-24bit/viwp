# -*- coding: utf-8 -*-

"""
Randomly show the repository of interest on github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2018 by rgb-24bit.
:license: MIT, see LICENSE for more details.
"""

import random

import requests

from flask import Blueprint, jsonify, render_template

from app import cache


randstar = Blueprint('randstar', __name__)


def make_starred_url(user, page=1):
    """Construct a github interface url that gets the star list."""
    # TODO The acquisition of the star list is done on the client side.
    url_format = 'https://api.github.com/users/{user}/starred' \
        + '?page={page}&per_page=100'
    return url_format.format(user=user, page=page)


@cache.cached(timeout=604800)  # Updated once a week
def get_user_starred(user):
    """Get the list of stars for the specified user."""
    # TODO clear empty list cache
    starred, page = [], 1
    while page > 0:
        response = requests.get(make_starred_url(user, page))

        # 403: Exceeded request limit
        # 404: User does not exist
        if response.status_code in (403, 404):
            return []

        # Up to 100 items at a time
        if len(response.json()) == 100:
            starred.extend(response.json())
            page += 1
        else:
            page = -1
    return starred


@randstar.route('/search/')
def randstar_search():
    return render_template('randstar/search.html')


@randstar.route('/user/<user>/')
def randstar_user(user):
    return render_template('randstar/user.html')


@randstar.route('/api/<user>')
def randstar_api_user(user):
    user_starred = get_user_starred(user)

    # random.choices() can't choose empty set
    if user_starred:
        return jsonify(random.choices(user_starred, k=8))
    return jsonify([])
