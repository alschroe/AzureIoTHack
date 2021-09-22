# Setup the Azure IoT hub

In this part you will seamlessly connect your Pi to the cloud by using Azure IoT Hub.

There are different ways to do this. You could use the Azure portal, the Cloud Shell or the Azure CLI for example.
The Azure portal is very helpful to get a feeling for the possibilities of Azure and offers you a great deal of visualization if it comes to topics like monitoring. But for cloud development you either want to deploy by using Infrastructure as Code (IaC) or go with the terminal. Since IaC is worth a whole workshop in and of itself, we will use the terminal. You can choose whether you prefer your local terminal or the Azure Cloud Shell. We set both up before.

## Create the Azure IoT hub

1. Add the azure-iot extension to your shell
    ```shell
    az extension add --upgrade --name azure-iot
    ```
1. Create a prefix for yourself consisting of four letters. This should help us to solve any naming issues if you are working on the same subscription as other participants or service names need to be globally or regionally unique.
    Using PowerShell:
    ```PowerShell
    $prefix = "<YOUR PREFIX HERE>"
    ```
    Using bash:
    ```bash
    prefix="<YOUR PREFIX HERE>"
    ```
1. Let's create another resource group so we can store all services we will provide today, and which will have the same lifecycle.
    ```shell
    az group create --name $prefix'iotpirg' --location westeurope
    ```
1. Now we create the IoT hub:
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

