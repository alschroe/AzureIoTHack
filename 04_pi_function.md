# Communicate from the Azure IoT Hub to the Azure Machine Learing service

We created an Azure Function for you. It is triggered every time the Iot hub recreives a message from your Pi and forwards the needed content to the Azure Machine Learning service. In return it also receives the rain prediction to the sensor temperature and humidity data.

We will stay on your local machine to implement this.

## Deploy Machine Learning model
The automated Machine Learning model should have trained by now. 
1. Navigate back to the *Azure Machine Leanrning Studio* (via the portal move to your AML service and from there to the studio).
1. Navigate to *Experiments* and select your experiment *predictRain*.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/04experiments.png)
1. Under *Display name* you should see the details of your run. Select the only run there is.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/04model.png)
1. Select the *Models* tab.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/04modeltap.png)
1. There select the **VotingEnsemble** - it should be the best ML Algorithm for the given data.
1. Select **Deploy** so we can consume this ML model as an endpoint. 
    ![Showing where AutoML can be found in the azure machine learning studio](/images/04deploy.png)
    There give it a name e.g. **mlendpoint** and for *Compute type* select **Azure Container Instance**. After that hit **Deploy**. 
    ![Showing where AutoML can be found in the azure machine learning studio](/images/04deploy2.png)
This will take a bit so let's move on to the next task.


## Create an Azure Function and an Azure Storage Account
Open a terminal again and make sure your prefix is still stored in it.
1. We will start by creating our general-purpose storage account.
    ```shell
    az storage account create --name $prefix'awjstorage' --location westeurope --resource-group $prefix'iotpirg' --sku Standard_LRS
    ```
1. We need to create an Azure function at this point. We are going to keep using Python.
    ```shell
    az functionapp create --resource-group $prefix'iotpirg' --consumption-plan-location westeurope --runtime python --runtime-version 3.8 --functions-version 3 --name $prefix'iotfunction' --os-type linux
    ```

## Prepare locally
1. Now we start off locally. To work with Azure Funcitons locally we need to install the *Azure Functions Core Tools*. Follow [these instructions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v3%2Cwindows%2Ccsharp%2Cportal%2Cbash%2Ckeda#v2) to do so.
    Restart your terminal and enter this to make sure everything works:
    ```shell
    func --version
    ```
1. Make sure you are uo to date on the *AzureIoTHack* git repo. While in the repo check:
    ```shell
    git pull
    ```
    We want to activate a virtual environment named .venv.
    ```shell
    cd raspberrypi_function
    ```
    Using PowerShell:
        ```PowerShell
        py -m venv .venv
        ```
        ```PowerShell
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
1. While we implemented the function for you, it still needs connection to your resources. We are starting by adding the *AzureWebJobsStorage* and the IoT hub *ConnectionString* values in the 'local.settings.json'. To do so open the function in the IDE of your choice. E.g. with VS Code:
    ```shell
    cd raspberrypi_function
    code .
    ```
    Get the needed values:
    ```shell
    # for AzureWebJobsStorage
    az storage account show-connection-string --name $prefix'awjstorage' --resource-group $prefix'iotpirg' --output tsv
    ```
    Paste the output 'DefaultEndpointProtocol=https;A...' as value for *AzureWebJobsStorage* in the *local.settings.json*.
    ```shell
    # for ConnectionString
    az iot hub connection-string show -n $prefix'iotpihub' --default-eventhub --output tsv
    ```
    Paste the output 'Endpoint=sb://...' as value for *ConnectionString* in the *local.settings.json*.
1. Now navigate to the folder 'iothubtrigger' ane there to '__init__.py'. There we will enter our Machine Learning model endpoint.
    Specifically we need to set the *url* in line 14 and the *api_key* in line 15.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/04basics.png)
    The az CLI extension for this is currently still experimental so we need to navigate back to the *Azure Machine Learning studio*.
    Under *Endpoints* select the endpoint you previously deployed.
    On the *Consume* tab of your endpoint you will find a **REST endpoint**. Paste it's content to the *url* in line 14 of '__init__.py'.
    Beneath under *Authentication* copy the **Primary key** and paste it to the *api_key* in line 14 of '__init__.py'.
    As you are already here fo to the *Test* tab and test your endpoint.
Your function is now ready to run.If you are using VS Code hit **F5** to start the function. If not start the function from the *raspberrypi_function* folder by entering:
```shell
func start
```

## Deploy the Azure funciton
1. Now we are going to run our function in Azure.
    ```shell
    func azure functionapp publish $prefix'iotfunction'
    ```
    To watch what is happening after the function is published:
    ```shell
    func azure functionapp logstream $prefix'iotfunction' --browser
    ```


