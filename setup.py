from cx_Freeze import setup, Executable

setup(
    name = 'Get System Info',
    options = {
        'build_exe': {
            'packages': ['flask'],
             'include_files': ['/home/dan/workspace/web-system-monitor/conf.json', '/home/dan/Descargas/logo.ico'],
        }
    },
    version = '1.0',
    description = 'A web application for get info about the system',
    executables = [
        Executable(
            '/home/dan/workspace/web-system-monitor/index.py',
            icon = '/home/dan/Descargas/logo.ico',
            shortcut_name = 'System Info',
            shortcut_dir = 'DesktopFolder',
            base = 'Win32GUI',
        ),
    ]
)
