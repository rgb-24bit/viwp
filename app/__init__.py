# -*- coding: utf-8 -*-

from flask import Flask
from flask_caching import Cache

from config import config


cache = Cache()


def create_app(config_name):
    """Create flask app instance.

    Args:
        config_name: Selected flask app configuration name.

    Returns:
        A flask app instance.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    cache.init_app(app)

    from .views import index as index_blueprint
    app.register_blueprint(index_blueprint)

    from .views import randstar as randstar_blueprint
    app.register_blueprint(randstar_blueprint, url_prefix='/randstar')

    from .views import plain as plain_blueprint
    app.register_blueprint(plain_blueprint, url_prefix='/plain')

    return app
