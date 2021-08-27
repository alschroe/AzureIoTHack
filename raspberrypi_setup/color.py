# import the library of the Sense HAT
from sense_hat import SenseHat
from time import sleep

# variable that calls the library
sense = SenseHat()
# lower the brightness of the LEDs
sense.low_light = True

# variables that define what colors can be used using RGB values. Create more if you feel like it.
green = (0,255,0)
yellow = (255,255,0)
blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,0,212)
purple = (160,32,240)
orange = (255,165,0)
turquoise = (0,255,213)
brown = (102,51,0)
mgreen = (127,186,0)
myellow = (255,185,0)
mblue = (0,164,239)
mred = (242,80,34)

def microsoft():
    G = mgreen
    Y = myellow
    B = mblue
    R = mred
    logo = [
    R, R, R, R, G, G, G, G, 
    R, R, R, R, G, G, G, G,
    R, R, R, R, G, G, G, G, 
    R, R, R, R, G, G, G, G,
    B, B, B, B, Y, Y, Y, Y,
    B, B, B, B, Y, Y, Y, Y,
    B, B, B, B, Y, Y, Y, Y,
    B, B, B, B, Y, Y, Y, Y,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

while True:
  for event in sense.stick.get_events():
    # 
    if event.action == "pressed":      
      #
      if event.direction == "up":
        sense.show_letter("I")          # Up arrow shows the letter I
      elif event.direction == "right":
        sense.set_pixels([heart])       # Right arrow shows the heart
      elif event.direction == "down":
        sense.set_pixels([microsoft])   # Down arrow shows the Microsoft logo
      elif event.direction == "left": 
        sense.set_pixels([raspi_logo])  # Left arrow shows the Raspberry Pi logo
      elif event.direction == "middle":
        sense.clear()                   # Enter key clears the LEDs

      # Wait some time and than clear the LEDs
      sleep(1000)
      sense.clear()