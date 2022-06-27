# Setup the Azure IoT hub

In this part you will seamlessly connect your Pi to the cloud by using Azure IoT Hub.

There are different ways to do this. You could use the Azure portal, the Cloud Shell or the Azure CLI for example.
The Azure portal is very helpful to get a feeling for the possibilities of Azure and offers you a great deal of visualization if it comes to topics like monitoring. But for cloud development you either want to deploy by using Infrastructure as Code (IaC) or go with the terminal. Since IaC is worth a whole workshop in and of itself, we will use the terminal. You can choose whether you prefer your local terminal or the Azure Cloud Shell. We set both up before.

## Create the Azure IoT hub
Open up the terminal of your local machine.
1. Add the azure-iot extension to your shell
    ```shell
    az extension add --name azure-iot
    ```
1. Now we create the IoT hub in the resource group we previously created. Make sure the prefix is still stored in your terminal otherwise store it again.
    ```shell
    az iot hub create --name $prefix'iotpihub' --resource-group $prefix'iotpirg' --location westeurope --sku S1
    ```
1. Let's register a new device:
    ```shell
    az iot hub device-identity create --device-id myPi --hub-name $prefix'iotpihub'
    ```
1. Get the primary connection string:
    Using PowerShell:
    ```PowerShell
    $connection = (az iot hub device-identity connection-string show --device-id myPi --hub-name $prefix'iotpihub' --output tsv)
    ```
    Using bash:
    ```bash
    connection=$(az iot hub device-identity connection-string show --device-id myPi --hub-name $prefix'iotpihub' --output tsv)
    ```
    You can have a look if it worked:
    ```shell
    echo $connection
    ```

Go to the [next steps](./03_pi_app.md)
