# COM Port Monitor

![](https://github.com/joshburnett/COM-Port-Monitor/raw/main/example%20notification.png)

Ever find yourself plugging and unplugging devices into your computer and needing to
know their associated COM ports? I did, so I wrote COM Port Monitor.  All it does is keep track of COM ports that are
added or removed, and shows helpful system notifications to let you know about it.

To use this, you can install it via `pip install com-monitor` (you might want to create a virtual environment and
activate it first), then you run it from the command line simply via `commonitor` (no dash). To quit the app,
right-click it's icon in the system tray and select 'Exit' from the pop up menu.

Next up:

- Get installation via pipx working (not sure why it doesn't work at the moment)
- Support OSes other than Windows
- Build executables for supported platforms

Hope you find this helpful!

<a target="_blank" href="https://icons8.com/icon/QAmTCDyL5kmz/usb-disconnected">USB Disconnected</a> and
<a target="_blank" href="https://icons8.com/icon/gJXyOBQKhSlv/usb-connected">USB Connected</a> icons by
<a target="_blank" href="https://icons8.com">Icons8</a>