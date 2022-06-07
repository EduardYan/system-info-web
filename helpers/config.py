"""
Utils functions to use for
the configuration.
"""

from json import load
from os import getcwd


def get_config_object() -> dict:
    """
    Return a dictionary with
    the configuration in the file
    './conf.json'
    """

    CURRENT_DIR = getcwd()
    PATH_FILE = CURRENT_DIR + '/conf.json'

    # in case the config file not is found
    try:
        # open for load the json data
        with open(PATH_FILE, 'r') as f:
            OBJECT = load(f)

        return OBJECT
    except FileNotFoundError:
        # return a port for default and debug not restarning
        return {
            'PORT': 5000,
            'DEBUG': 1
        }


# object of configuration to use
OBJECT = get_config_object()
