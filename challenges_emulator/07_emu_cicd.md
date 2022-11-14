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

## Enable Azure

We need to allow our GitHub Actions to create resources within Azure. To do so there is a concept called [**service principal**](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals#service-principal-object) in [Azure AD](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-whatis).
There are two options you can either create the service principal yourself or it was created for you previously.

<details>
    <summary>If service principal details were provided to you</summary>
    

Your details should look something like this: `{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`
    
1. Within your GitHub repo navigate to `Settings > Secrets`. There add a repository secret. Name it `AZURE_SP` and add the value mentioned above `{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`

</details>


<details>
    <summary>If you need to create a service principal</summary>
    

1. From your local terminal enter the following
    ```shell
    az ad sp create-for-rbac --name "<NAME>-github-actions-sp" --sdk-auth --role contributor --scopes /subscriptions/<SUBSCRIPTION_ID>
    ```

1. Store the following part of the output that will be returned in your terminal to an editor: `{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`

1. Within your GitHub repo navigate to `Settings > Secrets`. There add a repository secret. Name it `AZURE_SP` and add the value mentioned above 
`{"clientId":"xxx","clientSecret":"xxx","subscriptionId":"xxx", "tenantId":"xxx"}`.

</details>

## GitHub Action Workflows

We did create some workflows for you, but we deliberately added some bugs - you will have to fix them.



Go to the [next steps](./07_pi_missing.md)