from typing import List
import logging
import urllib.request
import json
import os
import ssl
import azure.functions as func

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

url = '<YOUR REST ENDPOINT>'
api_key = '<YOUR REST ENDPOINTS KEY>' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

def sendData():
    allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

    # Request data goes here
    data = {
        "data":
        [
            {
                ' temperature': temp,
                ' humidity': humid,
            },
        ],
    }

    body = str.encode(json.dumps(data))

    req = urllib.request.Request(url, body, headers)

    print("send data")

    try:
        response = urllib.request.urlopen(req)

        result = response.read()
        print(result)
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))


def main(events: List[func.EventHubEvent]):
    global temp
    global humid
    for event in events:
        logging.info('Python EventHub trigger processed an event: %s',
                        event.get_body().decode('utf-8'))
        print(event.get_body().decode('utf-8'))
        weather = json.loads(event.get_body().decode('utf-8'))
        temp=weather['Temperature']
        humid=weather['Humidity']
        sendData()

