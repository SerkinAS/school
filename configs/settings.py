import os


class DefaultConfig:
  ENV: str = 'DEV'
  SECRET_KEY: str = os.environ['SECRET_KEY']
  SQLALCHEMY_DATABASE_URI: str = os.environ['DATABASE_URL']
  SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevConfig(DefaultConfig):
    DEBUG: bool = True


class ProductConfig(DefaultConfig):
    DEBUG: bool = False
