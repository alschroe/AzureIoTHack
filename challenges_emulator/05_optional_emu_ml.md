# Let's set up the Azure Machine Learning Service

We want to build a predictive model. The goal for now is to predict from the collected temperature and humidity data whether or not it is going to rain. Before we used Auto ML to do this for us, but let us get a little bit deeper into the details.


## Create the Azure Machine Learning workspace

There are again multiple options to do this, but we will go with the Azure CLI. So open a terminal on your local machine and create an Azure Machine Learning workspace.

1. This time we will use the Azure portal to create our service. Go to 'portal.azure.com'. You might need to switch to an incognito tab since it will make the handeling of you using different tenants easier. Make sure you are using the right subscription.
1. Navigate to your 'prefixiotpirg' resource group and select the '+ Create' butten in the menue.
   ![Showing the menue in the Azure portal with the + create button being on the very left](/images/02newresources.png)
1. Now search for **Machine Learning** or navigate via the _AI + Machine Learning_ category on the left to the service. Give it a name - you can go with your prefix here. The other needed resources will be created automatically. Leave the rest as is and hit _Create_.
1. Once the resource is created navigate to it. On the _Overview_ page you will find a button _Launch studio_. Press it. It will forward you to a separate view for the Azure Machine Learning workspace.

## Create a machine learning pipeline

1. On the left side you will find the menu point _Designer_. Select it. We will work with the UI today but there are many options to make use of the Azure Machine Learning workspace.
   </br>
   ![Showing where the designer can be found in the azure machine learning studio](/images/02designer.png)
1. Under _New pipeline_ select _Easy-to use prebuilt components_.
   Settings should show up in the new view. Here we need to create a compute resource on which our model can run. To create this resource click on **Create Azure ML compute instance**.
   ![Settings of new pipeline](/images/02compute.png)
   Give the compute instance a name and select the size **Standard_DS3_v2** - leave the rest as is and hit _Create_. It should take a minute or two to create the compute instance.
   ![View of Compute size](/images/02compute2.png)
   In the meantime, back in settings, we also want to rename our pipeline. Currently it should be named something like _Pipeline-Created-on-date_. Rename your pipeline to **Weather forecast**.

   Once the compute instance has finished being created, select it from the dropdown menu _Select Azure ML compute instance_.

   Don't forget to hit save.

1. Now let's assemble our pipeline. First we need data. We want to populate the model with as much data as possible, so we are going to work with a preexisting dataset. Beneath the assets list you will find **Sample datasets**. Find the **Weather Dataset** and drag it onto the empty canvas.
   ![Highlighting the Weather Dataset](/images/02dataset.png)
   When you select it on the canvas, a detailed window will pop up. In the _Outputs_ tab of this window you can get a preview of the data this dataset consists of.
1. As you can see there is a lot of information. We are for now only interested in certain columns. So we need to add another asset. This time you will find it under **Component** and then **Select Columns in Dataset**. Drag and drop it under the Weather Dataset on your canvas. Now the pipeline part of our pipeline needs to be created. Under the _Weather Dataset_ is a little circle that represents an endpoint - the same above and under the _Select Colums in Dataset_. Connect the bottom circle of the dataset with the upper one of the select function.
</br>
![How the connection looks like](/images/02pipeline.png)
1. Under the Details of **Select Columns in Dataset** press the **Edit column** link. In the showing popup select **By name**, as it is easier and then add **WeatherType** (we will use this to see wether it is rainy or not), **DryBulbCelsius** and **RelativeHumidity**. Press save and continue.
1. For the next step add the asset **Edit Metadata** also under **Component**. Connect it to the **Select Columns in Dataset** output and repeat the step before by opening the details and selecting the columns **WeatherType**, **DryBulbCelsius** and **RelativeHumidity**. We want to rename them in this step and therefore under _New column names_ enter the following manually:

   ```shell
   isRain,temperature,humidity
   ```

   It should look like this:

   ![How the Edit Metadata details should look like](/images/02metadata.png)

1. Let's clean the missing data.
   Select **Clean Missing Data** and connect the asset to **Edit Metadata**. In Details you will now have to enter the names manually, since currently the columns do not exist, as we have not yet run the pipeline. So enter one after the other:

   ```shell
   isRain
   temperature
   humidity
   ```

   Make also sure that you select **Remove entire row** under _Cleaning mode_, since we are just deleting data that is not complete.
   ![How the Clean Missing Data details should look like](/images/02clean.png)

   If you would like to understand more why we are cleaning missing data, we can recommend reading up on data for machine learning [here](https://docs.microsoft.com/en-us/learn/modules/introduction-to-data-for-machine-learning/).

1. Now the fun part. We can add our own scripts (python or R) to the pipeline. We will go with python.
   Drag and drop **Execute Python Script** from the **Component** section onto the canvas.

   What we want to do is to rename the values of the column _isRain_. Currently it is quite cryptic and we just need the binary information whether it is raining or not. Connect the _Cleaned dataset_ output from _Clean Missing Data_ to the _Dataset1: DataFrameDirectory_ input from _Execute Python Script_. In the details you will see the current Python script. Replace it with the following code:

   ```python
   import numpy as np

   def azureml_main(dataframe1 = None):

       # RA, SN etc. denote rain
       dataframe1['isRain']=np.where((dataframe1.isRain=='RA'),'Yes',dataframe1.isRain)
       dataframe1['isRain']=np.where((dataframe1.isRain=='SN'),'Yes',dataframe1.isRain)
       dataframe1['isRain']=np.where((dataframe1.isRain=='DZ'),'Yes',dataframe1.isRain)
       dataframe1['isRain']=np.where((dataframe1.isRain=='PL'),'Yes',dataframe1.isRain)
       dataframe1['isRain']=np.where((dataframe1.isRain!='Yes'),'No',dataframe1.isRain)

       return dataframe1,
   ```

   As you know, Python works with indentation - so make sure it looks like above.

1. For supervised Machine Learning, we need to split our dataset into a training and testing dataset. Therefore, add the **Split Data** to the canvas and connect the **Result dataset** output to the _Split Data_ input.

   Set _Fraction of rows in the first output dataset_ to **0.9**:
   ![How the Split Data details should look like](/images/02split.png)

1. We are going to train a regression model on the isRain column.

   Select **Train Model** and connect the **Results dataset1** output of _Split Data_ to the **Dataset** input of _Train Model_.
   Set _Label column_ to **isRain**:
   ![How the Train Model details should look like](/images/02train.png)

1. We will create a two-class logistic regression model to build our prediction.

   Add **Two-Class Logistic Regression** and connect the **Untrained model** output of the _Two-Class Logistic Regression_ to the **Untrained model** input of _Train Model_.
   Select **ParameterRange** under _create trainer mode_:
   ![How the Two-Class Logistic Regression details should look like](/images/02regression.png)

1. Now we score predictions for a trained regression model.

   Add **Score Model** and connect the **Trained Model** output of _Train Model_ to the **Trained Model** input of _Score Model_. And the the **Results dataset2** output of _Split Data_ to the **Dataset** input of _Score Model_.

1. Finally we want to evaluate the results of our regression model with standard metrics.

   Add **Evaluate Model** and connect the **Scored dataset** output of _Score Model_ to the **Scored dataset** input of _Evaluate Model_.
   The final pipeline should look like this:

   ![How the entire pipeline should look like](/images/02all.png)

1. Now hit **Submit** in the upper left corner and create a new experiment. This will start your pipeline. You have logs, outputs and much more for each step, if you select the assets. Feel free to take a closer look specifically at the output of the _Evaluate Model_ asset.
1. After the run, you can create a _Real time inference pipeline_. This way the trained model is stored as a dataset, training modules are therefore removed and the trained model is added back into the pipeline. Additionally, Web service input and output modules are added. They show where we will enter and return our data.
   ![Screenshot of where to create inference pipeline](/images/02inferencepipeline.png)

   ![How the real time inference pipeline should look like](/images/02rtip.png)

   You can click _Show lineage_ to refer back to the training pipeline.

1. Hit **Submit** on the _Real time inference pipeline_.
1. After this job has run through, select **Deploy** to create an endpoint we can consume and under _Compute type_ select **Azure Container Instance**.
   (Note: If you are working in a customer project Azure Kubernetes Service gives you much more options to manage a complex environment.) Then hit **Deploy**.
   ![How the endpoint settings should look like](/images/02endpoint.png)

   Let's move on, since this will take some time.

   Go to the [next steps](./02_emu_iothub.md)
