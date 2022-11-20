# Use GitHub for your DevOps automation

When it comes to Cloud there are a lot of concepts around Continous Delivery and Continous Integration.
The fundamental idea around this concept is that we will apply an agile process to our solutions. We will continously fix, update and add from within a project team.
Today we will use GitHub and Bizeps/Terraform to do so.

Let's dive into the DevOps world. You can also work as a Team on this part since you can invite other to jointly work on a repo.

## Get your repo ready

We will need to set everything up so you have an own version of this repo within GitHub.

1. Since you already cloned the repo to your local machine let's push it to your own GitHub organization. To do so first create a new organization within your GitHub. Navigate to 'github.com'. Make sure you are logged in with your user. 
    1. There create an [organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch).
    1. Make sure you are in right directory on your local terminal '../AzureIoTHack' and enter:

        ```shell
        git add .
        ```

        ```shell
        git commit -m "repo setup"
        ```

        ```shell
        gh repo create <YOUR ORGANIZATION NAME>/AzureIoTHack --private --source=. --remote=upstream
        ```

    **Hint**: If you want to work jointly you need to add the other users to your repo like [this](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository).

1. We are going to use GitHub Actions for the deployment. GitHub Actions allow you to automate, customize and execute your software development workflows right in your repo. To use this we need to activate the Actions in our repo. Navigate to `Settings > Actions` there check `Allow all actions and reusable workflows`. In the upper menue the tab *Actions* should appear.

## Using projects

We want to use GitHub as our DevOps tool. So let's treat it like a real software development project and create some **user stories**. A user story is an informal, natural language description of a feature that we want to implement.

1. Navigate to the **Projects** within your GitHub organization. There select **New project**.

1. In the **Select Template** window select **Boards** and hit **Create**.

1. Rename the Project from 'untitled project' to something more specific and create your first **Todo** items. Name them as seen below.
    1. `Create Issues from Draft items`
    1. `Enable GitHub Actions to create resources in Azure`
    1. `Enable Terraform to create resources in Azure`
    1. `Edit the unique naming within GitHub Actions`
    1. `Edit the unique naming within Terraform`
    1. `Push the changes to GitHub`
    1. `Adapt the application running on the device`

1. As you can see currently they are all drafts. Draft items exist only in your project and are a quick way to build an overview while not going into detail right away. We want to turn them into issues and add some more information. Make sure **Issues** are activated on your repo. If you cannot see a Tab labled issues, navigate to `Settings > General`. When you scroll down you will find *Features*. There set the check next to **Issues**.
    Issues are used to track todos but also bugs, feature requests and more.

1. Now navigate back to your first work item in your projects board. Select it and add some details. Assign the task to someone and convert the Draft into an Issue. Make sure to select the **AzureIotHack** repository.

    **Hint**: If you want to work jointly you can assign tasks to your teammembers.

1. Close the item and on the board move the *Create Issues from Draft items* to **In Progress**.

1. Take some time to familiarize yourself with the options GitHub Projects offer you and turn all work items into Issues. 

1. After that you can drag the *Create Issues from Draft items* to **Done**. Select it and **Close the Issue**. This way you will also see less Issues within your Repo.

1. Move the *Enable GitHub Actions to create resources in Azure* to **In Progress**.

## Enable Azure for GitHub Actions

We need to allow our GitHub Actions to create resources within Azure. To do so there is a concept called [**service principal**](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals#service-principal-object) in [Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis).
There are two options you can either create the service principal yourself or it was created for you previously.

<details>
    <summary>If service principal details were provided to you</summary>
    

Your details should look something like this: `{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`
    
1. Within your GitHub repo navigate to `Settings > Actions > Secrets`. There add a repository secret. Name it `AZURE_CREDENTIALS` and add the value mentioned above `{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`

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

1. Push the changes by entering the following in your terminal within the correct directory:
    ```shell
    git add *
    ```
    ```shell
    git commit -m "add prefix"
    ```
    git 


## GitHub Action Workflows

We did create some workflows for you, but we deliberately added some bugs - you will have to fix them.



Go to the [next steps](./07_pi_missing.md)