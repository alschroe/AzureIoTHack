# Let's set up the Azure Machine Learning Service

We want to build a predictive model. The goal for now is to predict from the collected temperature and humidity data whether or not it is going to rain.

## Create the Azure Machine Learning workspace
We will create the workspace using a terminal on our local machine. Please open it.
1. Create a prefix for yourself consisting of four letters. This should help us to solve any naming issues if you are working on the same subscription as other participants or service names need to be globally or regionally unique.
    Using PowerShell:
    ```PowerShell
    $prefix = "<YOUR PREFIX HERE>"
    ```
    Using bash:
    ```bash
    prefix="<YOUR PREFIX HERE>"
    ```
1. Let's create a resource group so we can store all services we will provide today - which will have the same lifecycle.
    ```shell
    az group create --name $prefix'iotpirg' --location westeurope
    ```
1. Now we need to create the workspace:
    ```shell
    az ml workspace create -w $prefix'iotml' -g $prefix'iotpirg'
    ```

There are again multiple options to do this, but we will go with the Azure portal.
1. This time we will use the Azure portal to create our service. Go to 'portal.azure.com'. You might need to switch to an incognito tab since it will make the handeling of you using different tenants easier. Make sure you are using the right subscription.
1. Navigate to your 'prefixiotpirg' resource group and select the '+ Create' butten in the menue.
    ![Showing the menue in the Azure portal with the + create button being on the very left](/images/02newresources.png)
1. Now search for **Machine Learning** or navigate via the *AI + Machine Learning* category on the left to the service. Give it a name - you can go with your prefix here. The other needed resources will be created automatically. Leave the rest as is and hit *Create*.
1. Once the resource is created navigate to it. On the *Overview* page you will find a button *Launch studio*. Press it. It will forward you to a separate view for the Azure Machine Learning workspace.

## Create a machine learning pipeline
This time we will use the Azure portal to use the Azure Machine Learning Studio for the next steps. Go to 'portal.azure.com'. You might need to switch to an incognito tab since it will make the handeling of you using different tenants easier. Make sure you are using the right subscription. 
1. Navigate to your 'prefixiotpirg' resource group. You will see that a number of services were created. The AML workspace needs a keyvault to store its secrets, a storage for configuration, datasets and models, optnionally Application Insights for monitoring and later on compute resources to run our training and model on.
1. Select the Azure Machine Learning workspace 'prefixiotml'. On the *Overview* page you will see a blue *Launch studio* button. Select it. It will forward you to a separate view for the Azure Machine Learning workspace. 
    ![Showing where AutoML can be found in the azure machine learning studio](/images/02studio.png)
1. On the left side you will find the menue point *Automated ML*. Select it. We will work with the UI today but there are many options to make use of the Azure Machine Learning workspace.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/01automl.png)
1. Select *New Automated ML run*.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/01newautoml.png)
1. Start the process of creating a new dataset by selecting *Create dataset* and from the dropdown *From web files*.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/01webfiles.png)
1. On the *Basic info* tab, insert the *Web URL* **https://azuresynapseml.blob.core.windows.net/weather/data.dataset.parquet** and *Name* the dataset **weather**. It will contain three columns, *isRain* - holding information whether it is raining or not (Yes, NO), *temperature* - holding the temperature in Celsius and *humidity* - holding well the humindity.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/01basicinfo.png)
1. Leave everything as is on the next tabs until you can hit *Create*. Now select the Dataset *weather* - you might need to refresh the dataset overview using the *Refresh* button. After selecting hit *Next*.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/01automl.png)
1. You need to create an experiment and a compute resource on which your model will be trained. Under *Experiment name* select *Create new* and give your experiment the name **predictRain**. The *Target column* should be **isRain (String)**. 
    Under *Select compute cluster* hit the **Create a new compute** link.
    Leave the virtual machine specifications as is and confirm.
    Move on to the next tab.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/01automl.png)
1. The *Classification* task type should be pre-selected. Go on *View additional configuration settings*. Behind the category *Exit criterion* you should make sure to set the *Training job time (hours)* to **0.5**.
    ![Showing where AutoML can be found in the azure machine learning studio](/images/01automl.png)
1. Hit *Finish* and the training will start. This will take some time, so we will move on to the next step while the model is being trained.
