# Communicate from the Azure IoT Hub to the Azure Machine Learing service

In this challenge, we are going to create an Azure Function, which is triggered every time the IoT Hub receives a message from your Pi emulator and forwards the needed content to the Azure Machine Learning Service. In return, it also receives the rain prediction to the sensor temperature and humidity data.

We will stay on your local machine to implement this.

## Deploy Machine Learning model

The automated Machine Learning model should have trained by now. In order to be able to use the trained Machine Learning model, we first need to deploy it. Therefore, please follow the next steps:

(Btw, If you have trained and deployed the Machine Learning model using the ML Designer, you can skip this step.)

1. Navigate back to the _Azure Machine Learning Studio_ (via the portal move to your AML service and from there to the studio).
1. Navigate to _Jobs_ and select your experiment _predictRain_.

   ![Showing where AutoML can be found in the azure machine learning studio](/images/04experiments.png) <br>

1. Under _Display name_ you should see the details of your run. Select the only run there is.
   ![Showing where AutoML can be found in the azure machine learning studio](/images/04model.png) <br>
1. Select the _Models_ tab. <br>
   ![Showing where AutoML can be found in the azure machine learning studio](/images/04modeltap.png) <br>
1. There select the **VotingEnsemble** - it should be the best ML Algorithm for the given data. (_Note_: The first algorithm in the list is the best one.)
1. Select **Deploy** so we can consume this ML model as an endpoint. Choose the **Deploy to web service** option:
   ![Showing where AutoML can be found in the azure machine learning studio](/images/01automlws.png) <br>
   There give it a name e.g. **mlendpoint** and for _Compute type_ select **Azure Container Instance**. Switch **Enable authentication** to on. After that hit **Deploy**.
   ![Showing where AutoML can be found in the azure machine learning studio](/images/04deploy1.png) <br>
   This will take a bit so let's move on to the next task.

## Create an Azure Function and an Azure Storage Account locally

Now, we will create the Azure Function, which is triggered every time the IoT Hub receives a message from your Pi emulator and forwards the needed content to the Azure Machine Learning Service.

Open a terminal on your local computer again and make sure your prefix is still stored in it.

1. We will start by creating our general-purpose storage account. This is needed to store the Azure function:
   ```shell
   az storage account create --name $prefix'awjstorage' --location westeurope --resource-group $prefix'iotpirg' --sku Standard_LRS
   ```
1. We need to create an Azure function at this point. We are going to keep using Python.
   ```shell
   az functionapp create --resource-group $prefix'iotpirg' --consumption-plan-location westeurope --runtime python --runtime-version 3.9 --functions-version 4 --name $prefix'iotfunction' --os-type linux --storage-account $prefix'awjstorage'
   ```

## Prepare the function locally

1.  Now we start off locally. To work with Azure Funcitons locally we need to install the _Azure Functions Core Tools_. Follow [these instructions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v3%2Cwindows%2Ccsharp%2Cportal%2Cbash%2Ckeda#v2) to do so.
    Restart your terminal and enter this to make sure everything works:
    ```shell
    func --version
    ```
1.  Make sure you are up to date on the _AzureIoTHack_ git repo. While in the repo check:

    ```shell
    git pull
    ```

    We want to activate a virtual environment named .venv. We have already created all necessary parts, for you to create the Azure function. Therfore, change into the directory, where the Azure function files are stored.

    ```shell
    cd raspberrypi_function
    ```

    For Azure Functions we need to use Python Version 3.7, 3.8 or 3.9. Have a look whether you have the correct version installed. If not please do so.

    ```shell
    python --version
    ```

    If you have one or more versions installed you can set the version of the virtual environment you will create next by adding `-3.7`, `-3.8` or `-3.9` to the command.

    Using PowerShell:

    ```shell
    py -m venv .venv
    ```

    ```shell
    .venv/scripts/activate
    ```

    Using bash:

    ```bash
    python -m venv .venv
    ```

    ```bash
    source .venv/bin/activate
    ```

    ```bash
    sudo apt-get install python3-venv
    ```

1.  While we implemented the function for you, it still needs connection to your resources. We are starting by adding the _AzureWebJobsStorage_ and the IoT hub _ConnectionString_ values in the 'local.settings.json'. To do so open the function in the IDE of your choice. E.g. with VS Code:
    ```shell
    cd raspberrypi_function
    code .
    ```
    Get the needed values:
    ```shell
    # for AzureWebJobsStorage
    az storage account show-connection-string --name $prefix'awjstorage' --resource-group $prefix'iotpirg' --output tsv
    ```
    Paste the output 'DefaultEndpointProtocol=https;A...' as value for _AzureWebJobsStorage_ in the _local.settings.json_.
    ```shell
    # for ConnectionString
    az iot hub connection-string show -n $prefix'iotpihub' --default-eventhub --output tsv
    ```
    Paste the output 'Endpoint=sb://...' as value for _ConnectionString_ in the _local.settings.json_.
1.  Now navigate to the folder 'iothubtrigger' and there to `**__init__.py**`. There, the IoT hub connection string ('HostName=...') needs to be entered in line 15 behind _connectionstr_.
    Get the connection string like this:
    ```shell
    az iot hub connection-string show -n $prefix'iotpihub' --output tsv
    ```
1.  Finally, we will enter our Machine Learning model endpoint.
    Specifically we need to set the _url_ in line 17 and the _api_key_ in line 18.
    The az CLI extension for this is currently still experimental so we need to navigate back to the _Azure Machine Learning studio_.
    Under _Endpoints_ select the endpoint you previously deployed.
    ![Where to find the Endpoint](/images/01automlendoint.png) <br>
    On the _Consume_ tab of your endpoint you will find a **REST endpoint**. Paste its content to the _url_ in line 17 of `__init__.py`.
    Under _Authentication_ copy the **Primary key** and paste it to the _api_key_ in line 18 of `__init__.py`.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/04basics.png) <br>
    As you are already here go to the _Test_ tab and test your endpoint.
    Your function is now ready to run. If you are using VS Code hit **F5** to start the function. If not start the function from the _raspberrypi_function_ folder by entering:

```shell
func start
```

## Run the updated app on the Simulator

Go back to the simulator in your browser.

1. On **line 93** you see the function _receiveMessageCallback(msg)_ that is being called upon a received message. This is where we listen for the Cloud-2-Device Message we create in the Azure Function. It contains the prediction from the Azure ML Model. Replace the function with the following code:

   ```javascript
   function receiveMessageCallback(msg) {
     var message = msg.getData().toString("utf-8");
     if (message.includes("Yes")) {
       blinkLEDthrice();
       console.log("Receive message: " + "Rain predicted");
     } else {
       blinkLED();
       console.log("Receive message: " + "no Rain predicted");
     }
   }
   ```

   Temperature and humidity data are still being sent to the Azure IoT Hub and written into the console of the emulator.

   However, now your emulator also listens to the Azure IoT Hub, which forwards the result of your ML model. There, we again write the prediction into the console. If the prediction from temperature and humidity data is rain, the LED will light up three times and if no rain is predicted, the LED will light up once.

   In order to avoid too much blinking, comment out the function calls _blinkLEDthrice()_, _blinkLEDtwice()_, and _blinkLED()_ on lines 56, 60 and 64.

## Deploy the Azure function

1. Now we are going to run our function in Azure. Since this command takes the Python version of the current environment make sure to run it from within the .venv environment.
   ```shell
   func azure functionapp publish $prefix'iotfunction'
   ```
1. There is one thing missing. Our Connection String and the connection to the Azure Storage account currently reside in the `local.settings.json` file of the function project. This file will not be uploaded to Azure (see `.funcignore` for the files that will not be uploaded). We can set the needed keys in the Azure portal. So first navigate to the portal.
1. There find your Azure Function and from there the function `iothubtrigger` you just uploaded under `Function`.
   ![](/images/04iothubtrigger.png)
1. Here you can also see an overview of how often the function was triggered. For now we need to enter the keys that we did have in the `local.settings.json`. Navigate to `Function Keys`, select `+ New function key` and kopy all the key-value-pairs from your `local.settings.json`. The result should look like this:
   ![](/images/04functionkeys.png)

Now you should be able to start and stop the Pi Emulator and always get the prediction about whether or not it is going to rain, all running in the cloud. This is how your final project should look like:
![Showing the menu in the Azure portal with the + create button being on the very left](/images/architectureemu.png)

Go to the [next steps](./06_emu_github.md)
