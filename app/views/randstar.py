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
    url_format = 'https://api.github.com/users/{user}/starred' \
        + '?page={page}&per_page=100'
    return url_format.format(user=user, page=page)


@cache.cached(timeout=604800)  # Updated once a week
def get_user_starred(user):
    """Get the list of stars for the specified user."""
    starred, page = [], 1
    while page > 0:
        response = requests.get(make_starred_url(user, page))

        if response.status_code == 404:
            return []

        if response.json():
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
    return jsonify(random.choices(user_starred, k=6))
