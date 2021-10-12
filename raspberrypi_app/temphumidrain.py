import time
import os

# Using the Python Device SDK for IoT Hub:
# https://github.com/Azure/azure-iot-sdk-python
from azure.iot.device import IoTHubDeviceClient, Message
from six.moves import input
from sense_hat import SenseHat

# The device connection string to authenticate the device with your IoT hub.
# The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
devicecs = os.getenv("DeviceConnectionString")

# Define the JSON message to send to IoT Hub.
msgtxt = '{{"Temperature": {temperature}, "Humidity": {humidity}}}'

# The client object is used to interact with your Azure IoT hub.
client = IoTHubDeviceClient.create_from_connection_string(devicecs, websockets=True)

# variable that calls the library
sense = SenseHat()

# clear the LED grid of any text or colour
sense.clear()

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
W = (102,51,0)          # brown

sun = [
    N, N, N, N, N, N, N, N,
    N, N, N, O, O, N, N, N,
    N, N, O, O, O, O, N, N,
    N, O, O, O, O, O, O, N,
    N, O, O, O, O, O, O, N,
    N, N, O, O, O, O, N, N,
    N, N, N, O, O, N, N, N,
    N, N, N, N, N, N, N, N,
]

umbrella = [
    N, N, N, B, N, N, N, N,
    N, N, B, B, B, N, N, N,
    N, B, B, B, B, B, N, N,
    B, B, B, B, B, B, B, N,
    N, N, N, B, N, N, N, N,
    N, N, N, B, N, N, N, N,
    N, N, N, B, N, N, N, N,
    N, N, N, B, B, N, N, N,
]

def iothubTemperatureHumidity():
    try:
        global client
        global temp
        print ( "IoT Hub device sending messages from sense-hat, press Ctrl-C to exit" )
        sense = SenseHat()
        while True:
            time.sleep(0.1)
            temperature =  sense.get_temperature()
            # pressure = sense.get_pressure()
            humidity = sense.get_humidity()
            temp = int(temperature)
            if temperature and humidity:
                msgtxtformatted = msgtxt.format(temperature=temperature, humidity=humidity)
                message = Message(msgtxtformatted)
                # Send the message.
                print( "Sending message: {}".format(message) )
                client.send_message(message)
                client.on_message_received = message_handler
                time.sleep(10)        

    except KeyboardInterrupt:
        print ( "Stopped sending data to the IoT Hub" )
        client.shutdown()
        sense.clear()

def message_handler(message):
    msg1 = message.data
    msg2 = msg1.decode('utf8')
    print(msg2)
    if temp >= 33:
        sense.show_message(str(temp),scroll_speed=0.2,text_colour=R)
        if "NO" in msg2:
            sense.set_pixels(sun)
        elif "Yes" in msg2:
            sense.set_pixels(umbrella)
    elif temp < 33 and temp > 26:
        sense.show_message(str(temp),scroll_speed=0.2,text_colour=Y)
        if "NO" in msg2:
            sense.set_pixels(sun)
        elif "Yes" in msg2:
            sense.set_pixels(umbrella)
    elif temp <= 26 and temp > 23:
        sense.show_message(str(temp),scroll_speed=0.2,text_colour=G)
        if "NO" in msg2:
            sense.set_pixels(sun)
        elif "Yes" in msg2:
            sense.set_pixels(umbrella)
    elif temp <= 23 and temp > 18:
        sense.show_message(str(temp),scroll_speed=0.2,text_colour=T)
        if "NO" in msg2:
            sense.set_pixels(sun)
        elif "Yes" in msg2:
            sense.set_pixels(umbrella)
    elif temp <= 18:
        sense.show_message(str(temp),scroll_speed=0.2,text_colour=B)
        if "NO" in msg2:
            sense.set_pixels(sun)
        elif "Yes" in msg2:
            sense.set_pixels(umbrella)


if __name__ == '__main__':
    print ( "Press Ctrl-C to exit" )
    iothubTemperatureHumidity()

