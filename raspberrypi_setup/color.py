# import the library of the Sense HAT
from sense_hat import SenseHat
from time import sleep

# variable that calls the library
sense = SenseHat()
# lower the brightness of the LEDs
sense.low_light = True

# variables that define what colors can be used using RGB values. Create more if you feel like it.
G = (0,255,0)           # green
Y = (255,255,0)         # yellow
B = (0,0,255)           # blue
R = (255,0,0)           # red
W = (255,255,255)       # white
N = (0,0,0)             # nothing
P = (255,0,212)         # pink
L = (160,32,240)        # purple
O = (255,165,0)         # orange
T = (0,255,213)         # turquoise
B = (102,51,0)          # brown
mg = (127,186,0)        # microsoft green
my = (255,185,0)        # microsoft yellow
mb = (0,164,239)        # microsoft blue
mr = (242,80,34)        # microsoft red

microsoft = [
mr, mr, mr, mr, mg, mg, mg, mg, 
mr, mr, mr, mr, mg, mg, mg, mg,
mr, mr, mr, mr, mg, mg, mg, mg, 
mr, mr, mr, mr, mg, mg, mg, mg,
mb, mb, mb, mb, my, my, my, my,
mb, mb, mb, mb, my, my, my, my,
mb, mb, mb, mb, my, my, my, my,
mb, mb, mb, mb, my, my, my, my
]

heart = [
N, N, N, N, N, N, N, N,
N, P, P, N, P, P, N, N,
P, P, P, P, P, P, P, N,
P, P, P, P, P, P, P, N,
N, P, P, P, P, P, N, N,
N, N, P, P, P, N, N, N,
N, N, N, P, N, N, N, N,
N, N, N, N, N, N, N, N
]

raspi = [
N, G, G, N, N, G, G, N, 
N, N, G, G, G, G, N, N,
N, N, R, R, R, R, N, N, 
N, R, R, R, R, R, R, N,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
N, R, R, R, R, R, R, N,
N, N, R, R, R, R, N, N
]

print('up is for I, right is for heart, down is for microsoft and left is for the raspberry - in the middle you clear the LEDs')

while True:
    #
    for event in sense.stick.get_events():
        # 
        if event.action == "pressed":      
            #
            if event.direction == "up":
                sense.show_letter("I")          # Up arrow shows the letter I
            elif event.direction == "right":
                sense.set_pixels(heart)         # Right arrow shows the heart
            elif event.direction == "down":
                sense.set_pixels(microsoft)     # Down arrow shows the Microsoft logo
            elif event.direction == "left": 
                sense.set_pixels(raspi)         # Left arrow shows the Raspberry Pi logo
            elif event.direction == "middle":
                sense.clear()                   # Enter key clears the LEDs

    # Wait some time and than clear the LEDs
    sleep(10)
    sense.clear()