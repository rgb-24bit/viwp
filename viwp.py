# -*- coding: utf-8 -*-

import os

from app import create_app, cache


app = create_app('default')


@app.shell_context_processor
def make_shell_context():
    return dict(cache=cache)


if __name__ == '__main__':
    app.run()
