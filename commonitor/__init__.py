"""
ComMonitor: A small system tray utility that provides system notifications when COM port devices are added to or removed from the system.

Uses Qt (via PySide6) and windows_toasts.  Currently Windows-only.
"""

from .commonitor import *

__version__ = '0.1.1'
