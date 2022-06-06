import os
import platform
from json import dumps


class System():
    def __init__(
        self,
        arch:str,
        platform:str,
        version:str,
        release:str,
        cpus:int,
        home_dir:str,
        desktop_session:str,
        languaje:str,
        python_version:str,
    ) -> None:

        self.arch = arch
        self.platform = platform
        self.version = version
        self.release = release
        self.cpus = cpus
        self.home_dir = home_dir
        self.desktop_session = desktop_session
        self.languaje = languaje

        if python_version == '':
            self.python_version = 'Python not installed'
        self.python_version = python_version

    def get_object(self):
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


class Monitor():
    def __init__(self, system:System) -> None:
        self.system = system

    def show(self):
        print(self.system.get_object())



mysystem = System(
    platform.architecture(),
    platform.system(),
    platform.version(),
    platform.release(),
    os.cpu_count(),
    os.environ['HOME'],
    os.environ['DESKTOP_SESSION'],
    os.environ['LANG'],
    platform.python_version(),
)

monitor = Monitor(mysystem)

DUMPED = dumps(monitor.system.get_object(), indent = 2)
print(DUMPED)
