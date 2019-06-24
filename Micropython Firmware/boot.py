try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)
import time
import gc
gc.collect()

ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(13, Pin.OUT)
motor = Pin(10, Pin.OUT)
valveA = Pin(14, Pin.OUT)
valveB = Pin(12, Pin.OUT)

led.value(0)
motor.value(0)
valveA.value(0)
valveB.value(0)
time.sleep(1)
led.value(0)
motor.value(1)
valveA.value(1)
valveB.value(1)