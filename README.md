# Simple Backend

### Installation
* install [python 2.7.13](https://www.python.org/downloads/release/python-2713/) using the Windows installer
* open cmd.exe and type `pip install flask` to install flask

### Running
* set host and port at the end of file `shop.py`
  * if you want to access the server within your local network (e.g. WIFI) use port `0.0.0.0`
  * windows (probably) will ask you to allow the server to be accessible through Windows' Firewall, allow it
  * to look up the ip of your machine in the network, open `cmd.exe`, type `ipconfig` and look up the ipv4 address under the LAN connection you are using, it should start with `192.168.`
* open the folder with the source in windows explorer
* _right-click_ the open space of the folder while holding _shift_ and select _open terminal here_
* type `python shop.py` to start the server
* use any device with a browser in the same network to display the page, its address is `<host>:<port>` (Note: if you set the host to `0.0.0.0` in `shop.py` , you need to use the ip of your machine as host to access the page, not `0.0.0.0`)
