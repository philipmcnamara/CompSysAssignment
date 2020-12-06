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
