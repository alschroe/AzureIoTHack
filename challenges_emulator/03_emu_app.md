# Let's run the application

We are going to run our code on a simulated Raspberry Pi connected to a breadboard with an LED and a Sensor for humidity and temperature information. Since this is an emulator the data is created more or less randomly in a realistic range.

## Prepare your Emulator
1. You can find the **Raspberry Pi Azure IoT Online Simulator** under this [link](https://azure-samples.github.io/raspberry-pi-web-simulator/#getstarted). Open it
1. The current code sends simulated humidity and temperature data to the Azure IoT Hub. To make it work 

## Run the application
1. Now you are going to need the Azure IoT Hub connection string.
    It might still be stored in the shell on your *local machine*. Copy it!
    ```shell
    echo $connection
    ```
    If it is not get the connection string again:
    ```shell
    az iot hub device-identity connection-string show --device-id myPi --hub-name $prefix'iotpihub' --output tsv
    ```
1. Paste the connection string in line 15.
1. Now we can run the application. Press **Run** beneath your code.
    Temperature and humidity data are send to the Azure IoT Hub and every time a message is sent the LED will light up.
1. The data from your Emulator is now sent to Azure. But you still need to connect it to your Machine Learning service.

## Check the IoT Hub
1. To see what is happening in the Azure IoT Hub navigate to the Azure portal. There find your Azure IoT Hub. On the `Overview` site you will see the messages received.
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
1. Press on **Stop** in the emulator to save on messages.

Go to the [next steps](./04_emu_function.md)