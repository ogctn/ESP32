# net_connect.py

import config
import network
import utime
import ntptime

import urequests

def net_connect():
    sta_if = network.WLAN(network.STA_IF)
    start = utime.time()
    timed_out = False

    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        try:
            sta_if.connect(config.WIFI_SSID, config.WIFI_PWD)
            while not sta_if.isconnected() and not timed_out:        
                if utime.time() - start >= 20:
                    timed_out = True
                    print("Timed out")
                else: pass
        except:
            print("WIFI AP NOT FOUND!")
            return False

    if sta_if.isconnected():
        print('connected to network')
        ntptime.settime()
        print('local time has been synchronized')
        print('network config:', sta_if.ifconfig())
        response = urequests.get("http://clients3.google.com/generate_204")
        if response.status_code == 204 : print("online")
        else: print("offline")
        return True
    else: 
        print('could not connect')
        return False

