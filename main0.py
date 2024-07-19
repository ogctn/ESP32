# main.py

from utime import sleep_ms
from time import sleep
from machine import Pin

def main():
    
    flash = Pin(4, mode=Pin.OUT)
    flash.on()
    sleep(1)
    flash.off()
    
    m, c = init()
    if not (m and c):
        Pin(33, Pin.OUT).off()
        sleep(1)
        Pin(33, Pin.OUT).on()
        Pin(33, Pin.OUT).off()
        sleep(1)
        Pin(33, Pin.OUT).on()
        return 0

    while True:
        m.publish( c.capture() )
        sleep_ms(3)

if __name__ == "__main__":
     main()
