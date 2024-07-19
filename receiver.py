import base64
import cv2 as cv
import numpy as np
import paho.mqtt.client as mqtt


MQTT_BROKER = '172.16.22.232' #'192.168.197.80'
MQTT_TOPIC = "esp0/img/"

frame = np.zeros((600, 800, 3), np.uint8)       # Height:240, Width:320 (QVGA)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_TOPIC)


# The callback for when a PUBLISH message is received from the server.

def on_message(client, userdata, msg):
	global frame
	img_bytes = msg.payload
	nparr = np.frombuffer(img_bytes, np.uint8)
	frame = cv.imdecode(nparr, cv.IMREAD_COLOR)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(MQTT_BROKER)


# Starting thread which will receive the frames
client.loop_start()

while True:
	cv.imshow("RECEIVED", frame)
		
	if cv.waitKey(1) & 0xFF == ord('q'):
		break
	
client.loop_stop()



# Stop the Thread

