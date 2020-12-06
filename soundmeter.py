from sense_hat import SenseHat
import sys
import usb.core
import requests
import time
from urllib.request import urlopen
import  json

sense = SenseHat()
sense.clear()
green = (0, 255, 0)
red = (255,0,0)

dev = usb.core.find()

#streams="Philip  Sound Level Meter:i"
tokens="9YOJEJH3U0RDZ9LF"
baseURL='https://api.thingspeak.com/update?api_key=%s' % tokens

dev=usb.core.find(idVendor=0x16c0,idProduct=0x5dc)

assert dev is not None

print (dev)

print (hex(dev.idVendor)+','+hex(dev.idProduct))

def writeData(dB):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s' % (dB))
    conn.close()

while True:
    ret = dev.ctrl_transfer(0xC0,4,0,0,200)
    dB = round((ret[0]+((ret[1]&3)*256))*0.1+30,2)
    writeData(dB)
    time.sleep(10)
    msg="{'dB':'"+str(dB)+"'}"
    print (msg)
    if dB >=60.5:
     sense.show_message("Too Loud", text_colour = red)
    else:
     sense.show_message("Fine!", text_colour = green)


