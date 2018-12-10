# mqtt subscribe start

import machine
from umqtt.simple import MQTTClient

CONFIG = {
	"broker": "192.168.1.7",
	"sensor_pin": 0, 
	"client_id": b"esp8266_" + ubinascii.hexlify(machine.unique_id()),
	"topic": b"esp8266",
}

def load_config():
	import ujson as json
	try:
		with open("/config.json") as f:
			config = json.loads(f.read())
	except (OSError, ValueError):
		print("Couldn't load /config.json")
		save_config()
	else:
		CONFIG.update(config)
	
	print("Loaded config from /config.json")

def save_config():
	import ujson as json
	try:
		with open("/config.json", "w") as f:
			f.write(json.dumps(CONFIG))
	except OSError:
		print("Couldn't save /config.json")

def sub_cb(topic, msg):
	print((topic, msg))

def subs():
	p2=machine.Pin(2,machine.Pin.OUT)
	client = MQTTClient(CONFIG['client_id'], CONFIG['broker'])
	client.set_callback(sub_cb)
	client.connect()
	print("Connected to {}".format(CONFIG['broker']))
	client.subscribe('{}/{}'.format(CONFIG['topic']))

 	while True:
		if True:
			client.wait_msg()
		else:
		# Non-blocking wait for message
			client.check_msg()
		# Then need to sleep to avoid 100% CPU usage (in a real
		# app other useful actions would be performed instead)
		
		p2.on() 
		time.sleep(1)
		p2.off()
		time.sleep(1) 

	client.disconnect()

def pubs():
	client = MQTTClient(CONFIG['client_id'], CONFIG['broker'])
	client.connect()
	print("Connected to {}".format(CONFIG['broker']))

	# Read Sensor Value
	#data = sensor_pin.read()
	#client.publish('{}/{}'.format(CONFIG['topic'], CONFIG['client_id']),bytes(str(data), 'utf-8'))
	#print('Sensor state: {}'.format(data))

# mqtt subscribe end	
	

def connect():
	import network
	sta_if = network.WLAN(network.STA_IF)

	if not sta_if.isconnected():
		print('connecting to network...')
		sta_if.active(True)
		sta_if.connect('AirtelNW', 'Password@01')

		while not sta_if.isconnected():
			pass

	print('network config:', sta_if.ifconfig())


def webrepl():
	import webrepl
	webrepl.start()

connect()
webrepl()

def dir()
	import os
	os.listdir()
	
def reboot()
	import machine
	machine.reset()

def no_debug():
	import esp
	# this can be run from the REPL as well
	esp.osdebug(None)

def disable_ap():
	import network
	ap = network.WLAN(network.AP_IF) # create access-point interface
	ap.active(False)



def enable_ap():
	import network
	ap = network.WLAN(network.AP_IF) # create access-point interface
	ap.active(True)         # activate the interface

def blink():
	import machine
	import time
	led = machine.Pin(2, machine.Pin.OUT)
