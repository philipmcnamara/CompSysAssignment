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

The soundTest.py file is the main code file. It runnes connected to the storeFileFB.py which pushes the dats in json format out to Firebase.

The soundTest.py file also send the data out to thingspeak were I download it and build my PowerBi Dashboards with. This is the SoundMeterTrend.pbix file.I have added Images of the FireBase and Thingspeak channels I've been using. The Firebase data was a deadend as I hit a pay wall to use it fully, but the Thingspeak data was easily accessed and download in CSV format for analysis.

The pythonArray file stores 5 iterations of the collected info into and calculates the average dB lever over a 5 minute period. If the noise is too high the Pi will flash a "Too Loud" warning in red letters across it's face several times. This is positioned in the room in such a way that it is noticable. 

I have used this setup to monitor my childs work environemnt to ID the loudest times, this creats a better awareness of the environment as a way to monitor and reduce noice levels during the loudst time. 

