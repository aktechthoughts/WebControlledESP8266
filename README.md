This project is Web controlled ESP8266. 

Technologies Used :
            HTML, CSS, Flask, Java Script, Jquery,  SocketIO, ESP8266, MicroPython, MQTT (Mosquitto), Raspberry Pi

ESP8266 is a device developed by espressif system, which is a programmable wifi device with full support to UDP/TCP/IP network. It can be programmed in native AT command or even the high level languages like MicroPython. Micropython can be flashed with the help of documentaion on micropython website (https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware).

The device has two main files boot.py and main.py. boot.py is executed when the device reboots, while main.py executes after the execution of boot.py. We can keep Micropython instructions to connect to wifi in boot.py and Main.py can be used to connect and handle MQTT requests.

While the device is fully capable of hosting any server (Web, Ftp etc) and it has 4 MB of flash storage. The storage is not enough so, I have hosted webserver and mosquitto  at a raspberry pi. The request to webserver is contolled using Flask framework.

