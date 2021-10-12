# Let's run the application

In the folder 'raspberrypi_app' you will find the application we want to run on our Pi, so it sends us the temperature data we wish to collect. This is a node.js application and you need to set up your Pi so the application can be run there.

## Prepare your Pi
1. Connect to your Pi, if you are not already connected to it via SSH, remote desktop or by attaching desktop, mouse and keyboard. If you are connected to it via the last two options, please open a terminal.
1. In the Bash navigate to root of this repo - **AzureIotHack** and pull any changes.
    ```bash
    git pull
    ```

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
    In the bash of your Pi paste the string:
    ```bash
    export DeviceConnectionString="<YOUR CONNECTION STRING>"
    ```
1. We need to install a package for our code to work on your Pi.
    ```bash
    pip3 install azure-iot-device
    ```
1. Now we can run the application. Make sure you are in the 'raspberry_app' folder and run the following:
    ```bash
    python3 temphumid.py 
    ```
    Temperature and humidity data are send to the Azure IoT Hub and displayed on the Sense Hat's LEDs.
1. The data from your Sense Hat is now sent to Azure. But we still need to connect it to our Machine Learning service.

Go to the [next steps](./04_pi_function.md)