"""Flask config class."""

from os.path import dirname, abspath, join

CWD = dirname(abspath(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(CWD, 'cscourses.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'dfdQbTOExternjy5xmCNaA'


class ProdConfig(Config):
    # The following are fictitious details for a MySQL server database! Included to illustrate the syntax.
    DB_SERVER = '192.168.19.32'
    SQLALCHEMY_DATABASE_URI = 'mysql://user@{}/foo'.format(DB_SERVER)
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    #  In memory database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    #  To allow forms to be submitted from the tests without the CSRF token
    WTF_CSRF_ENABLED = False


class DevConfig(Config):
    DEBUG = True


app_config = {
    'development': DevConfig,
    'production': ProdConfig,
    'testing': TestConfig
}
