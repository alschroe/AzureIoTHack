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
    If you cannot use 'pip' or 'pip3' on your Pi install it entering the following:
    ```bash
    sudo apt install python3-pip
    ```
1. Now we can run the application. Make sure you are in the 'raspberry_app' folder and run the following:
    ```bash
    python3 temphumid.py 
    ```
    Temperature and humidity data are send to the Azure IoT Hub and displayed on the Sense Hat's LEDs.
1. The data from your Sense Hat is now sent to Azure. But we still need to connect it to our Machine Learning service.

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
1. In the terminal of your Pi press ctrl + C to stop the device from sending the data to Azure.

Go to the [next steps](./04_pi_function.md)