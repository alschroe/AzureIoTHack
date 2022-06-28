# Let's set up the Azure Machine Learning Service

We want to build a predictive model. The goal for now is to predict from the collected temperature and humidity data whether or not it is going to rain. In the end we want to display this information on our Raspberry Pi emulator.

![Showing the menu in the Azure portal with the + create button being on the very left](/images/architectureemu.png)

## Create the Azure Machine Learning workspace

We will create the workspace using a terminal on our local machine. Please open it.

1. Create a prefix for yourself consisting of four letters and in LOWERCASE. This should help us to solve any naming issues if you are working on the same subscription as other participants or service names need to be globally or regionally unique.
   <br>

   Using PowerShell:

   ```PowerShell
   $prefix = "<your prefix>"
   ```

   Using bash:

   ```bash
   prefix="<your prefix>"
   ```

1. Let's create a resource group so we can store all services we will provide today - which will have the same lifecycle.
   ```shell
   az group create --name $prefix'iotpirg' --location westeurope
   ```
1. Download the extension for az ml
   ```shell
   az extension add -n azure-cli-ml -y
   ```
1. Now we need to create the workspace:
   ```shell
   az ml workspace create -w $prefix'iotml' -g $prefix'iotpirg'
   ```

## Create a machine learning pipeline

This time we will use the Azure portal to use the Azure Machine Learning Studio for the next steps. Go to 'portal.azure.com'. You might need to switch to an incognito tab since it will make the handeling of you using different tenants easier. Make sure you are using the right subscription.

1. Navigate to your 'prefixiotpirg' resource group. You will see that a number of services were created. The AML workspace needs a keyvault to store its secrets, a storage for configuration, datasets and models, optionally Application Insights for monitoring and later on compute resources to run our training and model on.
1. Select the Azure Machine Learning workspace 'prefixiotml'. On the _Overview_ page you will see a blue _Launch studio_ button. Select it. It will forward you to a separate view for the Azure Machine Learning workspace. <br>
   ![Showing where AutoML can be found in the azure machine learning studio](/images/02studio.png) <br>
1. On the left side you will find the menue point _Automated ML_. Select it. We will work with the UI today but there are many options to make use of the Azure Machine Learning workspace.
   ![Showing where AutoML can be found in the azure machine learning studio](/images/01automl.png) <br>
1. Select _New Automated ML run_.
   ![Showing where AutoML can be found in the azure machine learning studio](/images/01newautoml.png) <br>
1. Start the process of creating a new dataset by selecting _Create dataset_ and from the dropdown _From web files_.
   ![Showing where AutoML can be found in the azure machine learning studio](/images/01webfiles.png) <br>
1. On the _Basic info_ tab, insert the _Web URL_ **https://raw.githubusercontent.com/alschroe/AzureIoTHack/main/data/weatherdata.csv** and _Name_ the dataset **weather**. It will contain three columns, _isRain_ - holding information whether it is raining or not (0 (yes), 1 (no)), _temperature_ - holding the temperature in Celsius and _humidity_ - holding the humidity.
   ![Showing where AutoML can be found in the azure machine learning studio](/images/01basicinfo.png) <br>
1. Leave everything as is on the next tabs until you can hit _Create_. Now select the Dataset _weather_ - you might need to refresh the dataset overview using the _Refresh_ button. After selecting hit _Next_.
1. You need to create an experiment and a compute resource on which your model will be trained. Under _Experiment name_ select _Create new_ and give your experiment the name **predictRain**. The _Target column_ should be **isRain (String)**.
   Under _Select Azure ML compute cluster_ hit the **+ New** link.
   Leave the virtual machine specifications as is, add some name and confirm.
   It will take some time to create the cluster. After that select it from the dropdown and hit _Next_.
   ![Showing where AutoML can be found in the azure machine learning studio](/images/01configrun.png) <br>
1. The _Classification_ task type should be pre-selected. Go on _View additional configuration settings_. Behind the category _Exit criterion_ you should make sure to set the _Training job time (hours)_ to **0.5**.
   ![](/images/01automltask.png)<br>
   ![Showing where AutoML can be found in the azure machine learning studio](/images/01taskconfig.png) <br>
1. Leave the next tabs unchanged and hit _Finish_ to start the training. This will take some time, so we will move on to the next step while the model is being trained.

Go to the [next steps](./02_emu_iothub.md).
