import time
import os
import threading
import json

# Using the Python Device SDK for IoT Hub:
# https://github.com/Azure/azure-iot-sdk-python
from azure.iot.device import IoTHubDeviceClient, Message
from six.moves import input
from sense_hat import SenseHat

# The device connection string to authenticate the device with your IoT hub.
# The connection string for a device should never be stored in code. For the sake of simplicity we're using an environment variable here.
connection_str = os.getenv("iothubDeviceConnectionString")

# Define the JSON message to send to IoT Hub.
msgtxt = '{{"Temperature": {temperature}, "Humidity": {humidity}}}'

# The client object is used to interact with your Azure IoT hub.
client = IoTHubDeviceClient.create_from_connection_string(connection_str)

# connect to the client
client.connect()

# variable that calls the library
sense = SenseHat()
# clear the LED grid of any text or colour
sense.clear()

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
B1 = (204,229,255) 
B2 = (153,204,255) 
B3 = (102,178,255) 
B4 = (51,153,255) 
B5 = (0,128,255) 

#def iothubClientInit():
    # The client object is used to interact with your Azure IoT hub.
    # client = IoTHubDeviceClient.create_from_connection_string(connstr)
    # return client

def iothubTemperatureHumidity():
    try:
        global client
        print ( "IoT Hub device sending messages from sense-hat, press Ctrl-C to exit" )
        sense = SenseHat()
        while True:
            time.sleep(0.1)
            temperature =  sense.get_temperature()
            # pressure = sense.get_pressure()
            humidity = sense.get_humidity()
            if temperature and humidity:
              msgtxtformatted = msgtxt.format(temperature=temperature, humidity=humidity)
              message = Message(msgtxtformatted)
              # Send the message.
              print( "Sending message: {}".format(message) )
              client.send_message(message)
              print ( "Message successfully sent" )
              time.sleep(1)
              return message
            

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

# define behavior for receiving a message
def message_handler(message):
    print("message data raw " + message.data)
    json_object = json.loads(message.data)
    print("message data json " + json_object)
    temp = json_object["Temperature"]
    humidity = json_object["Humidity"]
    if temp > 31:
        if humidity > 81:
            sense.show_message(temp,text_colour=[R],back_colour=[B4])
        elif humidity < 80 and humidity > 61:
            sense.show_message(temp,text_colour=[R],back_colour=[B3])
        elif humidity < 60 and humidity > 41:
            sense.show_message(temp,text_colour=[R],back_colour=[B2])
        elif humidity < 40 and humidity > 21:
            sense.show_message(temp,text_colour=[R],back_colour=[B1])
        elif humidity < 20:
            sense.show_message(temp,text_colour=[R],back_colour=[W])
    elif temp < 30 and temp > 24:
        if humidity > 81:
            sense.show_message(temp,text_colour=[G],back_colour=[B4])
        elif humidity < 80 and humidity > 61:
            sense.show_message(temp,text_colour=[G],back_colour=[B3])
        elif humidity < 60 and humidity > 41:
            sense.show_message(temp,text_colour=[G],back_colour=[B2])
        elif humidity < 40 and humidity > 21:
            sense.show_message(temp,text_colour=[G],back_colour=[B1])
        elif humidity < 20:
            sense.show_message(temp,text_colour=[G],back_colour=[W])
    elif temp < 23 and temp > 0:
        if humidity > 81:
            sense.show_message(temp,text_colour=[B],back_colour=[B4])
        elif humidity < 80 and humidity > 61:
            sense.show_message(temp,text_colour=[B],back_colour=[B3])
        elif humidity < 60 and humidity > 41:
            sense.show_message(temp,text_colour=[B],back_colour=[B2])
        elif humidity < 40 and humidity > 21:
            sense.show_message(temp,text_colour=[B],back_colour=[B1])
        elif humidity < 20:
            sense.show_message(temp,text_colour=[B],back_colour=[W])


# set the message handler on the client
# client.on_message_received = message_handler

messageresponse = client.on_message_received

message_handler(messageresponse)

if __name__ == '__main__':
    print ( "Press Ctrl-C to exit" )
    iothubTemperatureHumidity()

# shut down the client
client.shutdown()