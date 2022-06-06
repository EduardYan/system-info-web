"""
This module have the
model for create a monitor.
"""

from .system import System

class Monitor():
    """
    Create a monitor object
    """

    def __init__(self, system:System) -> None:
        self.system = system

    def show(self):
        """
        Show the system object
        """
        print(self.system.get_object())
