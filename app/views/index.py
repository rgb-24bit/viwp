# -*- coding: utf-8 -*-

"""
View of index page and error page
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2018 by rgb-24bit.
:license: MIT, see LICENSE for more details.
"""

from flask import Blueprint, render_template


index = Blueprint('index', __name__)


@index.route('/')
@index.route('/index/')
def viwp_index_page():
    return render_template('index/index.html')


@index.app_errorhandler(404)
def page_not_found(e):
    return render_template('index/404.html'), 404


@index.app_errorhandler(500)
def internal_server_error(e):
    return render_template('index/500.html'), 500
