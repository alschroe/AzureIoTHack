from typing import List
import logging
import urllib.request
import json
import os
import ssl
import azure.functions as func
from azure.iot.hub import IoTHubRegistryManager

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

connectionstr = os.getenv("DeviceConnectionString") # Replace this with the Primary Connection String for your IoT device myPi
device = 'myPi'
url = 'http://3738065f-cbbe-4e7c-a075-c715eb7b79c8.westeurope.azurecontainer.io/score' # Replace this with the endpoint for the Azure ML web service
api_key = 'KPCchFMubf7H74TP8hGAsWFCNx2tbdyV' # Replace this with the API key for the Azure ML web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

def sendData(temp, humid):
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

    # Request data goes here
    data = {
        "Inputs": {
            "data":
            [
                {
                    'Temperature': temp,
                    'Humidity': humid
                }
            ]
        },
        "GlobalParameters":{
            "method": "predict"
        }
    }

    body = str.encode(json.dumps(data))

    req = urllib.request.Request(url, body, headers)

    print("send data")

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        registry_manager = IoTHubRegistryManager(connectionstr)
        registry_manager.send_c2d_message(device, result)
        print(result)
        

    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))


def main(events: List[func.EventHubEvent]):
    for event in events:
        logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))
        print("printer in 62", event.get_body().decode('utf-8'))
        weather = json.loads(event.get_body().decode('utf-8'))
        temp=weather['temperature']
        humid=weather['humidity']
        sendData(temp, humid)

