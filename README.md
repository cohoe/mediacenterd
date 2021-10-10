Media Center Daemon
===================

A media center automation API. Does Bluetooth stuff for now.

Setup
-----

1. Install the package. @TODO this is naughty
   ```
   sudo pip install git+https://github.com/cohoe/mediacenterd
   ```
2. Install the Systemd unit file.
   ```
   cp init_scripts/mediacenterd.service /etc/systemd/system/mediacenterd.service
   ```
3. Reload Systemd
   ```
   sudo systemctl daemon-reload
   ```
4. Start
   ```
   sudo systemctl enable mediacenterd
   sudo systemctl start mediacenterd
   ```
5. Host firewall may need opening.
   ```
   sudo firewall-cmd --add-port 5000/tcp
   sudo firewall-cmd --add-port 5000/tcp --permanent
   ```