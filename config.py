"""Flask config class."""
from os.path import dirname, abspath, join


class Config(object):
    """Set Flask base configuration"""
    SECRET_KEY = 'dfdQbTOExternjy5xmCNaA'

    # General Config
    DEBUG = False
    TESTING = False

    # Forms config
    WTF_CSRF_SECRET_KEY = 'dfdQbTOExternjy5xmCNaA'

class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    TESTING = True


class DevConfig(Config):
    DEBUG = True
