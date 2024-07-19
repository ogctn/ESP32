# boot.py

# This file is executed on every boot (including wake-boot from deepsleep
# exec(open('cam.py').read())


from net_connect import net_connect
from Mqtt import Mqtt
import camera
from EspCam import EspCam as Cam

def init():
    
    net = False
    while not (net):
            net = net_connect()

    mqtt = Mqtt()
    print("MQTT Status:", mqtt.LAST_STATUS == 1)
    mqtt.publish( b'Connected...' )
    print("MQTT Status:", mqtt.LAST_STATUS == 1)

    cam = Cam()
    
    return mqtt, cam

exec(open('main0.py').read())