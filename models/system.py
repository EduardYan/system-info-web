"""
This module have the
model for create a system.
"""

class System():
    """
    Create a system object
    """

    def __init__(
        self,
        arch:str,
        platform:str,
        version:str,
        release:str,
        cpus:int,
        languaje:str,
        home_dir:str,
        desktop_session:str,
        date_and_time:str,
        python_version:str,
        node_version:str,
        win32_edition:tuple,
        win32_version:str,
        mac_ver:tuple,
    ) -> None:

        self.arch = arch
        self.platform = platform
        self.version = version
        self.release = release
        self.cpus = cpus
        self.languaje = languaje
        self.home_dir = home_dir
        self.desktop_session = desktop_session
        self.date_and_time = date_and_time

        # validating if python is installed
        if python_version == '' or python_version == None:
            self.python_version = 'Python not installed'
        else:
            self.python_version = python_version


        # validating if node is installed
        if node_version == '':
            self.node_version = 'Node not installed'
        else:
            self.node_version = node_version

        # properties only for windows systems
        self.win32_edition = win32_edition
        self.win32_version = win32_version

        # properties only for mac systems
        self.mac_ver = mac_ver

    def get_object(self) -> dict:
        # object to return
        OBJECT = {
            'arch': self.arch,
            'platform': self.platform,
            'version': self.version,
            'release': self.release,
            'cpus': self.cpus,
            'homeDir': self.home_dir,
            'desktop_session': self.desktop_session,
            'languaje': self.languaje,
            'pythonVersion': self.python_version,
        }
        return OBJECT
