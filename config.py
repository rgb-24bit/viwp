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
