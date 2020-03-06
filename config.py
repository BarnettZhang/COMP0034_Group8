"""Flask config class."""
from os.path import dirname, abspath, join


class Config(object):
    """Set Flask base configuration"""
    # CSRF_ENABLED = True
    # Secret key was randomly created using a Python console and enter 'import secrets' and then 'secrets.token_urlsafe(16)'
    SECRET_KEY = 'dfdQbTOExternjy5xmCNaA'

    # General Config
    DEBUG = False
    TESTING = False

    # Forms config
    # Generated using the same method as the SECRET_KEY
    WTF_CSRF_SECRET_KEY = 'f7Z-JN0ftel5Sp_TywHuxA'

    # Database config
    CWD = dirname(abspath(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(CWD, 'cscourses.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    # The following are fictitious details for a MySQL server database! Included to illustrate the syntax.
    DB_SERVER = '192.168.19.32'
    SQLALCHEMY_DATABASE_URI = 'mysql://user@{}/foo'.format(DB_SERVER)
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevConfig(Config):
    DEBUG = True
