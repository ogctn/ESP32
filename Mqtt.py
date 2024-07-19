# mqtt.py

from umqtt.simple import MQTTClient

CLIENT_NAME = 'esp0'
BROKER_ADDR = '172.16.22.232' #''

TOPIC = CLIENT_NAME.encode() + b'/img/'

class Mqtt:
    def __init__(self):
        self.obj = MQTTClient(CLIENT_NAME, BROKER_ADDR)
        self.obj.connect()
        self.CLIENT_NAME = CLIENT_NAME
        self.BROKER_ADDR = BROKER_ADDR
        self.LAST_STATUS = 0
    
    def publish(self, msg):
        try:
            self.obj.publish(TOPIC, msg)
            print("Message of len:", len(msg), " has been published.")
            self.LAST_STATUS = 1
        except:
            print("Message publishing error.")
            self.LAST_STATUS = 0
