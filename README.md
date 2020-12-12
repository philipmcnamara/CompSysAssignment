# CompSysAssignment

Sound meter needs privileges to access usb and
the python-requests package should be installed
for the cloud push operation shown in the code.

This is done with:

python -m pip install requests

The USb on the Pi has to be set up, this is done with:

 sudo apt-get update
 sudo apt-get install python-pip
 sudo pip install pyusb
 sudo apt-get install python-usb python3-usb


SenseHat is Added for Visual Display

Import in with:

from sense_hat import SenseHat

The soundTest.py file is the main code file. It runnes connected to the storeFileFB.py which pushes the dats in json format out to Fiirebase.

The soundTest.py file also send the data out to thingspeak were I download it and biuld my PowerBi Dashboards with. This is the SoundMeterTrend.pbix file.

I have used this setup to monitor my childs work environemnt to ID the loudest times for attention to De-sensatice the area.

The Pi flashes messages if the volume gets too loud. 
