from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml import automl, Input
from azure.ai.ml.entities import AmlCompute
from azure.ai.ml.entities import Data



# Set up your workspace
credential = DefaultAzureCredential()
ml_client = None
try:
    ml_client = MLClient.from_config(credential)
except Exception as ex:
    print(ex)
    # Enter details of your AzureML workspace
    subscription_id = "921b1060-fc07-42c5-8bad-c255bbf99a42"
    resource_group = "rgrg"
    workspace = "mlws"
    ml_client = MLClient(credential, subscription_id, resource_group, workspace)

#Create MLTable for training data from your local directory
my_training_data_input = Input(
    type=AssetTypes.MLTABLE, path="../../data"
)

# Specify aml compute
cpu_compute_target = "cpu-cluster"

try:
    ml_client.compute.get(cpu_compute_target)
except Exception:
    print("Creating a new cpu compute target...")
    compute = AmlCompute(
        name=cpu_compute_target, size="STANDARD_D2_V2", min_instances=0, max_instances=4
    )
    ml_client.compute.begin_create_or_update(compute).result()

# Create Dataset
# my_path = "https://raw.githubusercontent.com/alschroe/AzureIoTHack/main/data/weatherdata.csv"

# my_data = Data(
#     path=my_path,
#     type=AssetTypes.URI_FOLDER,
#     description="rain(binary), temp(float), humidity(integer)",
#     name="weather_data5",
#     version='v2'
# )

#  ml_client.data.create_or_update(my_data)

# note that the below is a code snippet -- you might have to modify the variable values to run it successfully
classification_job = automl.classification(
    compute="cpu-cluster",
    experiment_name="experiment22",
    training_data=my_training_data_input,
    target_column_name="isRain",
    primary_metric="accuracy",
    n_cross_validations=5,
    enable_model_explainability=True
)

# Limits are all optional

classification_job.set_limits(
    timeout_minutes=15, 
    trial_timeout_minutes=15, 
    max_trials=4,
    enable_early_termination=True,
)

# Training properties are optional
classification_job.set_training(
    blocked_training_algorithms=["LogisticRegression"], 
    enable_onnx_compatible_models=True
)

# Submit the AutoML job
returned_job = ml_client.jobs.create_or_update(
    classification_job
)  # submit the job to the backend

print(f"Created job: {returned_job}")

# Get a URL for the status of the job
returned_job.services["Studio"].endpoint