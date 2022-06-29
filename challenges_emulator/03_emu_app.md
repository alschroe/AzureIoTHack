# Let's run the application

We are going to run our code on a simulated Raspberry Pi connected to a breadboard with an LED and a Sensor for humidity and temperature information. Since this is an emulator the data is created more or less randomly in a realistic range.

## Prepare your Emulator

1. You can find the **Raspberry Pi Azure IoT Online Simulator** under this [link](https://azure-samples.github.io/raspberry-pi-web-simulator/#getstarted). Open it.
1. The current code sends simulated humidity and temperature data to the Azure IoT Hub. To make it work, you will have to add the connection string to your IoT Hub.

## Run the application

1. First, you are going to need the Azure IoT Hub connection string.
   It might still be stored in the shell on your _local machine_. Copy it!
   ```shell
   echo $connection
   ```
   If it is not, get the connection string again:
   ```shell
   az iot hub device-identity connection-string show --device-id myPi --hub-name $prefix'iotpihub' --output tsv
   ```
1. Paste the connection string in line 15.
1. Now we can run the application. Press **Run** beneath your code.
   Temperature and humidity data are sent to the Azure IoT Hub and every time a message is sent the LED will light up.
1. Next, you need to alter some of the code so that the LED lights up depending on the sent temperature. It blinks once if the temperature is below 25° Celsius, twice if it is between 25 and 27° Celsius and three times if it is above 27° Celsius. Therefore, **from line 39 until 55** replace the function _sendMessage_ by pasting the following code:

   ```javascript
   function sendMessage() {
     if (!sendingMessage) {
       return;
     }

     getMessage(function (content, temperatureAlert) {
       var message = new Message(JSON.stringify(content));
       var temperature = content.temperature;
       message.properties.add("temperatureAlert", temperatureAlert.toString());
       client.sendEvent(message, function (err) {
         if (err) {
           console.error("Failed to send message to Azure IoT Hub");
         } else {
           console.log("Temperature: " + temperature + "° C");
           console.log("Message sent to Azure IoT Hub");
           // blink three times if temperature is above 27
           if (temperature >= 27) {
             blinkLEDthrice();
           }
           // blink two times if temperature is between 25 and 27
           else if (temperature < 27 && temperature > 25) {
             blinkLEDtwice();
           }
           // blink one time if temperature is below 25
           else if (temperature <= 25) {
             blinkLED();
           }
         }
       });
     });
   }
   ```

   Moreover, **from line 101 until 110** replace the function blinkLED with the following code:

   ```javascript
   function blinkLED() {
     // Light up LED for 250ms
     if (blinkLEDTimeout) {
       clearTimeout(blinkLEDTimeout);
     }
     wpi.digitalWrite(LEDPin, 1);
     blinkLEDTimeout = setTimeout(function () {
       wpi.digitalWrite(LEDPin, 0);
     }, 250);
   }

   function blinkLEDtwice() {
     blinkLED();
     setTimeout(blinkLED, 500);
   }

   function blinkLEDthrice() {
     blinkLEDtwice();
     setTimeout(blinkLED, 1000);
   }
   ```

   Lastly, delete the method **JSON.stringify** (without the brackets) on **line 27**, since we added it in the previous code snippet.

   Now you can see how the LEDs blink depending on the temperature.

1. The data from your emulator is now sent to Azure. But you still need to connect it to your Machine Learning service in order to draw predictions of potential rain from it.

## Check the IoT Hub

1. To see what is happening in the Azure IoT Hub navigate to the Azure portal. There, find your Azure IoT Hub. On the `Overview` site you will see the messages received:
   ![See the Overview site of the Azure IoT Hub](/images/03iothubinfo.png)
1. Let's open the Azure Cloud Shell:
   ![Image of the upper bar in the Azure portal with focus on the Cloud Shell icon](/images/00portalshell.png)
1. There enter the following to see the messages comming in:
   ```shell
   az extension add --name azure-iot
   ```
   ```shell
   az iot hub monitor-events --hub-name $prefix'iotpihub'
   ```
1. Press **Stop** on the emulator to save on messages.

Go to the [next steps](./04_emu_function.md)
