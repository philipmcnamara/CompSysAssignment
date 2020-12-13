from sense_hat import SenseHat
import time


sense = SenseHat()
sense.clear()
green = (0, 255, 0)
red = (255,0,0)

#Array to use
lastFive = [0,0,0,0,0]


def avgVol (avg):
 time.sleep(1)
 if avg >=60.5:
  sense.show_message("Too Loud....Too Loud...Too Loud", text_colour = red)
  print("Avg Volume" + str(avg))
  q = 0
 else:
   sense.show_message(str(avg), text_colour = green)
   print("...")
   q = 0
