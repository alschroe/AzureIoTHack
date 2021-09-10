# Let's run the application

In the folder 'emulator_app' you will find the application we want to run on our Pi, so it sends us the temperature data we wish to collect. This is a node.js application and you need to set up your Pi so the application can be run there.

## Prepare your local machine
1. Download and install Node.js and npm using nvm on your local machine from [here](https://github.com/coreybutler/nvm-windows/releases/download/1.1.7/nvm-setup.zip). Reopen your terminal and nter node and npm to make sure everything is installed.
1. Since you have already cloned this repo, you just need to pull again, since there quite likely were changes since the last time you looked at it. Navigate to the root folder of the cloned repo named 'AzureIoTHack' and look up if it needs to be pulled again.
    ```shell
    git status
    git pull
    ```
1. Now 'cd' into the 'emulator_app' folder and install all packages for the application.
    ```shell
    cd ./emulator_app
    npm install
    ```

## Configure the application

1. We want do adapt the 'config.json' file. Open it in your favorite IDE, e.g. VS Code:
    ```shell
    code .
    ```

## Run the application

1. Now you are going to need the Azure IoT Hub connection string. Get it again from Azure using a shell that is connected to your subscription.
    Using PowerShell:
    ```PowerShell
    $connection = (az iot hub device-identity connection-string show --device-id myPi --hub-name $prefix'iotpihub' --output tsv)
    ```
    Using bash:
    ```bash
    connection=$(az iot hub device-identity connection-string show --device-id myPi --hub-name $prefix'iotpihub' --output tsv)
    ```
1. Now we give the connection string and run the application:
    Using PowerShell:
    ```PowerShell
    node index.js $connection
    ```
    Using bash:
    ```bash
    sudo node index.js $connection
    ```
