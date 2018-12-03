# -*- coding: utf-8 -*-

from flask import Flask

from config import config


def create_app(config_name):
    """Create flask app instance.

    Args:
        config_name: Selected flask app configuration name.

    Returns:
        A flask app instance.
    """
    app = Flask(__name__,
                static_folder="../web/static", template_folder="../web")
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    return app
