import os

from dotenv import load_dotenv
from pathlib import Path  # python3 only

# base directory
basedir = os.path.abspath(os.path.dirname(__file__))


env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config(object):
    """ database configuration class
    :arg
        object(dict)

    """
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv('secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
    # import pdb; pdb.set_trace()


class ProductionConfig(Config):
    """ Configuration for production environment"""
    DEBUG = False


class StagingConfig(Config):
    """ Configuration for devlopment environment"""
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    """
    Configuration for development environment
    """
    DEBUG = True
    DEVELOPMENT = True


class TestConfig(Config):
    """ Configuration for testing environment"""
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'test': TestConfig,
    'production': ProductionConfig
}
