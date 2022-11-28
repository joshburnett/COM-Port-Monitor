"""
ComMonitor: A small system tray utility that provides system notifications when COM port devices are added to or removed from the system.

Uses Qt (via PySide6) and windows_toasts.  Currently Windows-only.
"""

import sys

from windows_toasts import WindowsToaster, ToastImageAndText2
from serial.tools.list_ports import comports

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtCore import QTimer


__version__ = '0.1.0'


class ComMonitor(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        menu = QMenu(parent)
        exit_action = menu.addAction("Exit")

        self.setContextMenu(menu)
        exit_action.triggered.connect(QApplication.quit)

        self.ports = set(comports())
        self.wintoaster = WindowsToaster('COM Monitor')

        self.timer = QTimer(parent=self)
        self.timer.timeout.connect(self.check_com_ports)
        self.timer.start(1000)  # check every second

    def check_com_ports(self):
        new_ports = set(comports())

        # Check for removed devices
        for port in self.ports - new_ports:
            print(f'{port.device} disconnected')
            toast = ToastImageAndText2()
            toast.SetHeadline(port.device)
            toast.SetFirstLine('Device disconnected')
            toast.SetImage("icons8-usb-disconnected-96.png")
            self.wintoaster.show_toast(toast)

        # Check for added devices
        for port in new_ports - self.ports:
            print(f'{port.device} connected')
            toast = ToastImageAndText2()
            toast.SetHeadline(port.device)
            toast.SetFirstLine('Device connected')
            toast.SetImage("icons8-usb-connected-96.png")
            self.wintoaster.show_toast(toast)

        self.ports = new_ports


def main():
    app = QApplication(sys.argv)

    w = QWidget()
    tray_icon = ComMonitor(QIcon('system-monitor.png'), w)
    tray_icon.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
