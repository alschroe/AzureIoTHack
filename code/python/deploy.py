# import required libraries
from azure.ai.ml import MLClient
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    OnlineDeployment,
    ManagedOnlineDeployment,
    Environment,
    BuildContext,
    CodeConfiguration
)
from azure.identity import DefaultAzureCredential

# enter details of your AzureML workspace
subscription_id = "921b1060-fc07-42c5-8bad-c255bbf99a42"
resource_group = "rgrg"
workspace = "mlws"

# get a handle to the workspace
ml_client = MLClient(
    DefaultAzureCredential(), subscription_id, resource_group, workspace
)

online_endpoint_name = "alex-endpoint21"

# create an online endpoint
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="this is the endpoint for our model",
    auth_mode="key",
)

poller = ml_client.begin_create_or_update(endpoint)

print(poller.result())

model = ml_client.models.get("redbrakeqrwl9fj3", "1")

# dockerbuild = BuildContext(dockerfile_path="../json/Dockerfile.json")

# #  Model(name="redbrakeqrwl9fj3", type="custom_model", version="1")
# env = Environment(build=dockerbuild)

# env_docker = Environment(
#     build=BuildContext(path="../json"),
#     name="environment7",
#     description="Environment created from a Docker context."
# )

# env_docker = Environment(
#     name="AzureML-AutoML",
#     version="129",
#     conda_file="../json/conda.yml"
# )

# poller = ml_client.environments.create_or_update(env_docker)
# blue_deployment = ManagedOnlineDeployment(
blue_deployment = ManagedOnlineDeployment(
    name="alex21",
    endpoint_name=online_endpoint_name,
    model=model,
    environment="azureml:AzureML-pytorch-1.10-ubuntu18.04-py38-cuda11-gpu:35",
    code_configuration=CodeConfiguration(
        code="./",
        scoring_script="score.py"),
    instance_type="Standard_DS2_v2",
    instance_count=3,
)

ml_client.begin_create_or_update(blue_deployment)