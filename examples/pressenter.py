##
# Press enter to light up the tree
##

from time import sleep
from gpiozero import LEDBoard
tree = LEDBoard(*range(2,28),pwm=True)

tree.off() # Turn all LED's off

while True:

  raw_input()
  print("button pressed")
  tree.on()
  sleep(.2)
  tree.off()
