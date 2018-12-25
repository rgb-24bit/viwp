# -*- coding: utf-8 -*-

import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Base config class."""
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Development config class."""
    DEBUG = True

    # flask-caching configuration
    # https://flask-caching.readthedocs.io/en/latest/#rediscache
    # https://flask-caching.readthedocs.io/en/latest/#configuring-flask-caching
    CACHE_TYPE = 'redis'
    CACHE_KEY_PREFIX = 'viwp/'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    # CACHE_REDIS_PASSWORD = ''
    CACHE_REDIS_DB = 1

class TestingConfig(Config):
    """Test config class."""
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


if __name__ == '__main__':
    pass
