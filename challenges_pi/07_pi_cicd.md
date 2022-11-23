# Use GitHub for your DevOps automation

When it comes to Cloud there are a lot of concepts around Continous Delivery and Continous Integration.
The fundamental idea around this concept is that we will apply an agile process to our solutions. We will continously fix, update and add from within a project team.
Today we will use GitHub and Bizeps/Terraform to do so.

Let's dive into the DevOps world. You can also work as a Team on this part since you can invite other to jointly work on a repo.

## Using projects

We want to use GitHub as our DevOps tool. So let's treat it like a real software development project and create some **user stories**. A user story is an informal, natural language description of a feature that we want to implement.

1. Navigate to the **Projects** within your GitHub organization. There select **New project**.
    ![](/images/07createproject.png)

1. In the **Select Template** window select **Boards** and hit **Create**.
    ![](/images/07board.png)

1. Rename the Project from 'untitled project' to something more specific and create your first **Todo** items. Name them as seen below.
    1. `Create Issues from Draft items`
    1. `Enable GitHub Actions to create resources in Azure`
    1. `Enable Terraform to create resources in Azure`
    1. `Edit the unique naming within GitHub Actions`
    1. `Edit the unique naming within Terraform`
    1. `Push the changes to GitHub`
    1. `Adapt the application running on the device`
    ![](/images/07additem.png)

1. As you can see currently they are all drafts. Draft items exist only in your project and are a quick way to build an overview while not going into detail right away. We want to turn them into issues and add some more information. Make sure **Issues** are activated on your repo. If you cannot see a Tab labled issues, navigate to `Settings > General`. When you scroll down you will find *Features*. There set the check next to **Issues**.
    Issues are used to track todos but also bugs, feature requests and more.
    ![](/images/07enableissues.png)

1. Now navigate back to your first work item in your projects board. Select it and add some details. Assign the task to someone and convert the Draft into an Issue. Make sure to select the **AzureIotHack** repository.
    ![](/images/07convertissue.png)

    **Hint**: If you want to work jointly you can assign tasks to your teammembers.

1. Close the item and on the board move the *Create Issues from Draft items* to **In Progress**.
    ![](/images/07doneitem.png)

1. Take some time to familiarize yourself with the options GitHub Projects offer you and turn all work items into Issues.

1. After that you can drag the *Create Issues from Draft items* to **Done**. Select it and **Close Issue**. This way you will also see less Issues within your Repo.
    ![](/images/07closeissue.png)

1. Move the *Enable GitHub Actions to create resources in Azure* to **In Progress**.

## Enable Azure for GitHub Actions

We need to allow our GitHub Actions to create resources within Azure. To do so there is a concept called [**service principal**](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals#service-principal-object) in [Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis).
There are two options you can either create the service principal yourself or it was created for you previously.

<details>
    <summary>If service principal details were provided to you</summary>
    

Your details should look something like this: `{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`
    
1. Within your GitHub repo navigate to `Settings > Actions > Secrets`. There add a repository secret. Name it `AZURE_CREDENTIALS` and add the value mentioned above `{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`.

    ![](/images/07actionsecrets.png)

</details>


<details>
    <summary>If you need to create a service principal</summary>
    

1. From your local terminal enter the following
    ```shell
    az ad sp create-for-rbac --name "<NAME>-github-actions-sp" --sdk-auth --role contributor --scopes /subscriptions/<SUBSCRIPTION_ID>
    ```

1. Store the following part of the output that will be returned in your terminal to an editor: `{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`

1. Within your GitHub repo navigate to `Settings > Secrets`. There add a repository secret. Name it `AZURE_CREDENTIALS` and add the value mentioned above 
`{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`.

</details>

1. Move the *Enable GitHub Actions to create resources in Azure* to **Done** and **Close the Issue**.

1. Move the *Enable Terraform to create resources in Azure* to **In Progress**.

## Enable Azure for Terraform

Infrastructure as Code s the managing and provisioning of infrastructure through code instead of through manual processes. And this is what we want to do.
[Terraform](https://www.terraform.io/) by HashiCorp is just one of the options to go with when it comes to Azure. There is a predefined GitHub Action we can use later on, but to enable this Terraform to create resources within Azure we need to add some more secrets.

1. Navigate to `Settings > Actions > Secrets` again and create the following secrets that you can derive from the previously used service principal:
    1. `AZURE_CLIENT_ID`
    1. `AZURE_CLIENT_SECRET`
    1. `AZURE_SUBSCRIPTION_ID`
    1. `AZURE_TENANT_ID`

1. While unrelated to enabling GitHub Actions we will create two more secrets to enable the ML model usage. As before the `local.settings.json` will not be uploaded. But we do not want to place the endpoint and the key of our Azure ML model as plain text into our function or our workflow. Mainly because we will push the code into our repo where it will be visible for everyone. So create two more secrets and fill them with the url of your deployed model and it's key:
    1. `AZURE_ML_MODEL_URL` = `http://...`
    1. `AZURE_ML_MODEL_KEY` = `...`

1. The final list of secrets should look like this:
    ![](/images/07reposecrets.png)

1. Move the *Enable Terraform to create resources in Azure* to **Done** and **Close the Issue**.

1. Move the *Edit the unique naming within GitHub Actions* to **In Progress**. This time also note down the number of your item. It should be **#4**.

## Adapt the GitHub Actions locally

1. We want to add some more changes to our repo. We have already done some so let's first push the current state by typing in your local terminal from the directory of your repo (`/AzureIotHack`):
    ```shell
    git add *
    ```
    ```shell
    git commit -m "first commit"
    ```
    ```shell
    git push
    ```

1. Now that the remote repo is up to date let's create a new branch for the changes we will make:
    ```shell
    git checkout -b actions
    ```

1. In the IDE of your choice navigate to the `.github/workflows` folder of this repo. You should see two yaml files.

1. In the `functions.yml` replace <YOUR PREFIX> with a prefix of your choice. It can be the same as the one you startet off with. You should have to replace it twice.

1. Push the changes by entering the following in your terminal within the correct directory. If the issue/item you are working on is not **#4** adapt the commit message:
    ```shell
    git add *
    ```
    ```shell
    git commit -m "Closes #4"
    ```
    ```shell
    git push --set-upstream origin actions
    ```

1. Within GitHub navigate to **Pull requests**. Select **Compare & pull request**. Now you can review the changes and hit **Create pull request**.

1. Navigate to **Issues** to see that issue #4 has been closed. Also look in **Projects** to see that the workitem has been moved to **Done** for you.

1. Move the *Edit the unique naming within Terraform* and *Push the changes to GitHub* to **In Progress**. These should be **#5** and **#6**.

## Adapt the Azure Function locally

1. As before you still need to change the configuration of the binding. The binding represents how the function is being triggered. This configuration can be found in `/raspberrypy_function/iothubtrigger/function.json`. Adapt your prefix to the current one if you have chosen a different one than you used in the previous challenges.

## Adapt the Terraform locally

1. Let's first create a new branch for this task:
    ```shell
    git checkout -b terraform
    ```
1. Find the `variables.tf` in your repo.

1. In line 9 change `<YOUR PREFIX>` to the value you chose in the last step. Make sure it is the same.

1. Push the changes by entering the following.. If the issues/items you are working on are not **#5** & **#6** adapt the commit message:
    ```shell
    git add *
    ```
    ```shell
    git commit -m "Closes #5, closes #6"
    ```
    ```shell
    git push --set-upstream origin terraform
    ```

1. Repeat the steps from above to merge the new changes to the **main** branch. The changes in the `variables.tf` file will have triggered the GitHub Action. The first one will create all Azure resources and the second one will adapt them and deploy the Azure functions code. To see this more in detail navigate to the **Actions** tab and later on have a look at the Azure Portal.
    ![](/images/07pullreq.png)

1. Move the *Adapt the application running on the device* to **In Progress**.

## Prepare your Pi

One last step needs to be done. Currently the Pi sends and listens to the old IoTHub, but we did create a new one automatically. Therefore we need to get the new Connection String to the new Device in the IoT Hub.

1. In your local terminal enter the following. Adapt `<YOUR PREFIX>` to whatever value you gave it in the yaml and the terraform file before:
    ```shell
    az iot hub device-identity connection-string show --device-id myPi --hub-name <YOUR PREFIX>iot-prod-iothub --output tsv
    ```

1. Navigate back to your Pi and replace the old connection string with the new one in your Bash by entering the following:
    ```bash
    export DeviceConnectionString="<YOUR NEW CONNECTION STRING>"
    ```

1. Now we can run the application again. Make sure you are in the 'raspberry_app' folder and run the following:
    ```bash
    python3 temphumidrain.py 
    ```

Go to the [next steps](./08_pi_missing.md)