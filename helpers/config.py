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

    # open for load the json data
    with open(PATH_FILE, 'r') as f:
        OBJECT = load(f)

    return OBJECT


# object of configuration to use
OBJECT = get_config_object()
