from sense_hat import SenseHat
import sys
import usb.core
import requests
import time
from urllib.request import urlopen
import  json
import mysql.connector
from mysql.connector import Error
import datetime
import storeFileFB

datetime_object = datetime.datetime.now()

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='soundMeterData',
                                       user='root',
                                       password='root')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()

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
    currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    time.sleep(10)
    msg="{'dB':'"+str(dB)+"'}"
    print (msg)
    storeFileFB.push_db(dB, currentTime)
    if dB >=60.5:
     sense.show_message("Too Loud", text_colour = red)
    else:
     sense.show_message("Fine!", text_colour = green)


def insert_reading(datetime_object, reading):
    query = "INSERT INTO mainData(datetime_object,reading) " \
            "VALUES(%s,%s)"
    args = (datetime_object, reading)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

