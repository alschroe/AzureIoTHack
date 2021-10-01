# Let's set up the Azure Machine Learning Service

We want to build a predictive model. The goal for now is to predict from the collected temperature and humidity data whether or not it is going to rain.

## Create the Azure Machine Learning workspace

There are again multiple options to do this, but we will go with the Azure CLI. So open a terminal on your local machine and create an Azure Machine Learning workspace.
1. This time we will use the Azure portal to create our service. Go to 'portal.azure.com'. You might need to switch to an incognito tab since it will make the handeling of you using different tenants easier. Make sure you are using the right subscription.
1. Navigate to your 'prefixiotpirg' resource group and select the '+ Create' butten in the menue.
![Showing the menue in the Azure portal with the + create button being on the very left](/images/02newresources.png)
1. Now search for **Machine Learning** or navigate via the *AI + Machine Learning* category on the left to the service. Give it a name - you can go with your prefix here. The other needed resources will be created automatically. Leave the rest as is and hit *Create*.
1. Once the resource is created navigate to it. On the *Overview* page you will find a button *Launch studio*. Press it. It will forward you to a separate view for the Azure Machine Learning workspace.

## Create a machine learning pipeline
1. On the left side you will find the menue point *Designer*. Select it. We will work with the UI today but there are many options to make use of the Azure Machine Learning workspace.
![Showing where the designer can be found in the azure machine learning studio](/images/02designer.png)
1. Under *New pipeline* select *Easy-to use prebuild components*.
    Settings should show up in the new view. Here we need to create a compute resource on which our model can run. To create this resource click on **Create Azure ML compute instance**. 
    ![Settings of new pipeline](/images/02compute.png)
    Give the compute instance a name and select the size **Standard_DS3_v2** - leave the rest as is and hit *Create*. 
    ![View of Compute size](/images/02compute2.png)
    Back in settings we also want to rename our pipeline. Currently it should be named something like *Pipeline-Created-on-date*. Rename your pipeline to **Weather forcast**.
1. Now let's assamble our pipeline. First we need data. We want to populate the model with as much data as possible, so we are going to work with a preexisting dataset. Beneath the assets list you will find **Sample datasets**. Find the **Weather Dataset** and drag it onto the empty canvas.
![Highlighting the Weather Dataset](/images/02dataset.png)
    When you select it on the canvas, a detailed window will pop up. In the *Outputs* tab of this window you can get a preview of the data this dataset consists of.
1. As you can see there is a lot of information. We are for now only interested certain columns. So we need to add another asset. This time you will find it under **Data trasformation** and than **Select Columns in Dataset**. Drop it under the Weather Dataset on your canvas. Now the pipeline part of our pipeline needs to be created. Under the *Weather Dataset* is a little circle that represents an endpoint - the same above and under the *Select Colums in Dataset*. Connect the bottom circle of the dataset with the upper one of the select function.
![How the connection looks like](/images/02pipeline.png)
1. Under the Details of **Select Columns in Dataset** press the **Edit column** link. In the showing popup select **By name**, as it is easier and than add **WeatherType** (we will use this to see weather it is rainy or not), **DryBulbCelsius** and **RelativeHumidity**. Press save and continue.
1. For the next step add the asset **Edit Metadata** also under the *Data transformation* category. Connet it to the **Select Columns in Dataset** output and repeat the step before by opening the details and slecting the columns **WeatherType**, **DryBulbCelsius** and **RelativeHumidity**. We want to rename them in this step and therefore under *New column names* enter the following manually:
    ```shell
    isRain, temperature, humidity
    ```
    It should look like this:
    ![How the Edit Metadata details should look like](/images/02metadata.png)
1. Let's clean the missing data. 
    Category --> *Data transformaiton*
    Asset --> **Clean Missing Data**
    Connect the asset to **Edit Metadata**. In Details you will now have to enter the names manially, since currently the columns do not exist, as we have not yet run the pipeline. So enter one after the other:
    ```shell
    isRain
    temperature
    humidity
    ```
    Make also sure that you select **Remove entire row** under *Cleaning mode*, since we are just deleting data that is not complete.
    ![How the Clean Missing Data details should look like](/images/02clean.png)
1. Now the fun part. We can add our own scripts (python or R) to the pipeline. We will go with python.
    Category --> **Python Language**
    Asset --> **Execute Python Script**
    What we want to do is to rename the values of the column *isRain*. Currently it is quire crypric and we just need the binary information whether it is raining or not. Connect the *Cleaned dataset* output from *Clean Missing Data* to the *Dataset1: DataFrameDirectory* input from *Execute Python Script*. In the details you will see the current Python script. Replace it with the following code:
    ```python
    import pandas as pd
    import numpy as np

    def azureml_main(dataframe1 = None):

        dataframe1['isRain']=np.where((dataframe1.isRain=='RA'),'Yes',dataframe1.isRain)
        dataframe1['isRain']=np.where((dataframe1.isRain=='SN'),'Yes',dataframe1.isRain)
        dataframe1['isRain']=np.where((dataframe1.isRain=='DZ'),'Yes',dataframe1.isRain)
        dataframe1['isRain']=np.where((dataframe1.isRain=='PL'),'Yes',dataframe1.isRain)
        dataframe1['isRain']=np.where((dataframe1.isRain!='Yes'),'NO',dataframe1.isRain)

        return dataframe1,
    ```
    As you know Python works with indentation - so make sure it looks like above.
1. For supervised Machine Learning we need to split our dataset.
    Category --> **Data Transformation**
    Asset --> **Split Data**
    Connect the **Result dataset** output to the *Split Data* input.
    Set *Fraction of rows in the first output dataset* to **0.9**:
    ![How the Split Data details should look like](/images/02split.png)
1. We are going to train a regression model on the isRain column.
    Category --> **Model Training**
    Asset --> **Train Model**
    Connect the **Results dataset1** output of *Split Data* to the **Dataset** input of *Train Model*.
    Set *Label column* to **isRain**:
    ![How the Train Model details should look like](/images/02train.png)
1. We will create a two-class logistic regression model to build our prediction.
    Category --> **Machine Learning Algorithms**
    Asset --> **Two-Class Logistic Regression**
    Connect the **Untrained model** output of the *Two-Class Logistic Regression* to the **Untrained model** input of *Train Model*.
    Select **ParameterRange** under *create trainer mode*:
    ![How the Two-Class Logistic Regression details should look like](/images/02regression.png)
1. Now we score predictions for a trained regression model.
    Category --> **Model Scoring & Evaluation**
    Asset --> **Score Model**
    Connect the **Trained Model** output of *Train Model* to the **Trained Model** input of *Score Model*. And the the **Results dataset2** output of *Split Data* to the **Dataset** input of *Score Model*.
1. Finally we want to evaluate the results of our regression model with standard metrics. 
    Category --> **Model Scoring & Evaluation**
    Asset --> **Evaluate Model**
    Connect the **Scored dataset** output of *Score Model* to the **Scored dataset** input of *Evaluate Model*.
    The final pipeline should look like this:
    ![How the entire pipeline should look like](/images/02all.png)
1. Now hit **Submit** in the upper right corner and create a new experiment. This will start your pipeline. You have logs, outputs and much more for each step, if you select the assets. Feel free to take a closer look specifically at the output of the *Evaluate Model* asset.
1. After the run the Azure ML service has created a *Real time inference pipeline* for you. The trained model is now stored as a Dataset, training modules are therefore removed and the trained model is added back into the pipeline. Additionally Web service input and output modules are added. They show where we will enter and return our data.
    ![How the real time inference pipeline should look like](/images/02rtip.png)
    You can switch between the trainingpipeline and the real time inference pipeline:
    ![How the real time inference pipeline should look like](/images/02rtip2.png)
1. Hit **Submit** the *Real time inference pipeline*.
1. After this submit has run through, select **Deploy** to create an endpoint we can consume and under *Compute type* select **Azure Container Instance**. If you are working in a customer project Azure Kubernetes Service gives you much more options to manage a complex environment. Hit **Deploy**.
    ![How the endpoint settings should look like](/images/endpoint.png)
Let's move on, since this will take some time.

## Consume Endpoint


