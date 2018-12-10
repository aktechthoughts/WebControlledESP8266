import machine
import ubinascii
from umqtt.simple import MQTTClient



CONFIG = {
	"broker": "192.168.1.7",
	"sensor_pin": 0,
	"client_id": b"esp8266_" + ubinascii.hexlify(machine.unique_id()),
	"topic": b"esp8266",
}

adcValue = 0

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
	import ujson as json
	p2=machine.Pin(2,machine.Pin.OUT)
	print((topic, msg))
	data=(json.loads(json.dumps(msg)))
	data=data.replace('{','').replace('}','').replace('\"','')
	key=(data.split(':')[0]).replace(' ','')
	val=(data.split(':')[1]).replace(' ','')

	if key == 'sw2' and val == 'True':
		p2.off()
	if key == 'sw2' and val == 'False':
		p2.on()

def setup_pins():
	pass

def readADC():
	adc = machine.ADC(0)
	val = adc.read()
	return val


def subs():
	p2=machine.Pin(2,machine.Pin.OUT)
	client = MQTTClient(CONFIG['client_id'], CONFIG['broker'])
	client.set_callback(sub_cb)
	client.connect()
	print("Connected to {}".format(CONFIG['broker']))
	client.subscribe(CONFIG['topic'])

 	while True:
		if True:
			# Non-blocking wait for message
			client.wait_msg()
		else:
			client.check_msg()
		# Then need to sleep to avoid 100% CPU usage (in a real
		# app other useful actions would be performed instead)
		new_adcValue = readADC()
		if adcValue != new_adcValue :
			pubs(client,CONFIG['topic'],new_adcValue)
			adcValue = new_adcValue

	client.disconnect()

def pubs(cli,topic,msg):
	cli.publish(topic,bytes(str(msg), 'utf-8'))


def main():
	subs()

if __name__ == '__main__':
	load_config()
	setup_pins()
	main()

