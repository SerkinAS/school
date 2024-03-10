import os

from .settings import DevConfig, ProductConfig


config_schema = {
    'DEV': DevConfig,
    'PROD': ProductConfig
}

config = config_schema[os.environ['ENV']]()
