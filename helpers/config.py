"""
Utils functions to use for
the configuration.
"""

from json import load


def get_config_object() -> dict:
    """
    Return a dictionary with
    the configuration in the file
    './conf.json'
    """

    PATH_FILE = './conf.json'

    with open(PATH_FILE, 'r') as f:
        OBJECT = load(f)

    return OBJECT


# object of configuration to use
OBJECT = get_config_object()
