"""
Utils functions to
use for get information
about of the system.
"""


import os
import platform
import datetime
import re
import subprocess
from models.system import System
from models.monitor import Monitor


# getting the current date and time
datetime_current = datetime.datetime.now()
datetime_current = datetime_current.strftime('%d/%m/%Y %H:%M:%S')

# in case node not is installed or get a error
try:
    # getting node version
    node_version = subprocess.run(['node','--version'], check = True, stdout=subprocess.PIPE).stdout.decode()
    # removing "v" letter
    node_version = re.search(r'\d\d.\d.\d', node_version).group(0)
except:
    node_version = ''



# in case some key of the environ dictionary is error
try:
    USER_SYSTEM = System(
        platform.architecture(),
        platform.system(),
        platform.version(),
        platform.release(),
        os.cpu_count(),
        os.environ['LANG'],
        os.environ['HOME'],
        os.environ['DESKTOP_SESSION'],
        datetime_current,
        platform.python_version(),
        node_version,
        platform.win32_edition(),
        platform.win32_ver(),
        platform.mac_ver(),
    )
except KeyError:
    USER_SYSTEM = System(
        platform.architecture(),
        platform.system(),
        platform.version(),
        platform.release(),
        os.cpu_count(),
        os.environ['LANG'],
        os.environ['HOME'],
        os.environ['DESKTOP_SESSION_WM'],
        datetime_current,
        platform.python_version(),
        node_version,
        platform.win32_edition(),
        platform.win32_ver(),
        platform.mac_ver(),
    )


def get_monitor() -> Monitor:
    """
    Return the monitor object
    to use.
    """

    monitor = Monitor(USER_SYSTEM)
    return monitor
