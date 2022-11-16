# Set up your environment

To work properly with all the different moving bits and parts we want to connect in this Hackathon, we will have to do quite a bit of setting up. Make sure you have everything on hand that you need:

- Your local machine: Any computer or set up a virtual machine if you do not feel like installing any additional stuff on your machine.
- An Azure subscription: It has been created for you and you should have received your access credentials. Go to [https://portal.azure.com](https://portal.azure.com) and try login in with your credentials. If this is not possible, please reach out to your contact person.

## Your Azure subscription

1. Set up your Azure Cloud Shell. To do so go to the Azure portal. You can find it under [portal.azure.com](https://portal.azure.com). Log into Azure with your account.
1. You might be seeing the wrong subscription right now. Select _Directories + subscriptions_ - the second icon right from the search bar in the upper menu. Switch to the correct directory if necessary and under _Default subscription filter_ only tag the subscription you want to work on.
   ![Image of the upper bar in the Azure portal with focus on the Directories + subscriptions icon](/images/00portalsub.png) > Have your portal in english - the original language is more helpful for technical tasks.
1. Now that you are in the right place, select the _Azure Cloud Shell_ - the icon right next to the search bar in the upper menu. You will be prompted to set up a storage account. Make sure again to use the correct subscription in the dropdown menu and select _Create storage_. A PowerShell will open in your browser. In the dropdown you can also switch to Bash if you prefer this.
   ![Image of the upper bar in the Azure portal with focus on the Cloud Shell icon](/images/00portalshell.png)
   This created a new resource group within your subscription. A resource group is a logical container for all your resources aka Azure services. Within it a storage account was created.
   Take some time to get familiar with the portal. You can find more information about it [here](https://docs.microsoft.com/en-us/azure/azure-portal/azure-portal-overview). <br>
   <br>
   <br>

## Your local machine

We are going to set everything up, so you can work on Azure resources from your local machine. There are multiple options to interact with Azure and you can chose yourself how to do it later on.

1. (optional) Install Visual Studio Code from [here](https://code.visualstudio.com/Download) to handle any code you are going to need. You could of course use a different development environment, we just like this one.
1. (optional) Install the Windows Terminal. You can get it [here](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab). It is a command-line front-end and can run Command Prompt, PowerShell, WSL 2, SSH and an Azure Clound Shell Connector. Again there are other options, but we like this one.
1. The Azure command-line interface (Azure CLI) is a set of commands used to create and manage Azure resources. The Azure CLI is available across Azure services and is designed to get you working quickly with Azure, with an emphasis on automation. Open the shell and download the Azure CLI from [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli). You can also install it without manual downloading using the PowerShell (Run as Administrator):
   ```shell
   Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi'; rm .\AzureCLI.msi
   ```
1. You might need to close and reopen your shell at this point. After that, you can connect to your Azure subscription from the shell. To do so enter the following command:

   ```shell
   az login
   ```

   A login should pop up. Enter your credentials there. Now that we are logged into Azure we need to connect to the right subscription. It is possible that you have more than one subscription under the identity you logged in with. In the output from the shell, you should see a detailed list of these subscriptions. If not the following command will print it out.

   ```shell
   az account list
   ```

   One of these subscriptions should be shown as `"isDefault": "true"`. This is the one you are currently connected to. If this is not the right subscription switch like this:

   ```shell
   az account set --subscription <NAME OR ID OF YOUR SUBSCRIPTION>
   ```

   Now let's see if it works:

   ```shell
   az group list
   ```

   This should show you all the resource groups in your Azure subscription - so at least a resource group named "cloud-shell-storage-westeurope" you created in the previous section.

   **Hint**: To learn more about the most important Azure CLI commands, check out this [link](https://docs.microsoft.com/en-us/cli/azure/get-started-with-azure-cli).

1. Get Git [here](https://git-scm.com/downloads) - it helps you to track changes in files, specifically code. We are going to need it to clone this repo to our local machine.

   **Hint**: To learn more about version control with Git, follow this [free and simple learning path](https://docs.microsoft.com/en-us/learn/modules/intro-to-git/).

1. If you haven't yet, create a [GitHub](https://github.com/join) account. This service for software development and version control is used by over 83 million developers and we will use it for automation later on.

1. Connect to your GitHub account from your local machine by entering:

    ```shell
    git config --global user.name "<YOUR USER NAME>"
    ```

    ```shell
    git config --global user.email "<YOUR USER EMAIL>"
    ```

1. You might need to restart your shell at this point. After that, create a new GitHub organization. A GitHub organization gives you and your team the opportunity to collaboarate on GitHub, which serves a a container for your shared work. To find out more about organizations, check out this [link](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/about-organizations)

   To create the organization follow these steps:

   - Click on your profile icon in the upper right corner and click on _Your organizations_:
   ![Image of menu, where you can find your GitHub organizations, repositories, projects and profile information](/images/00creatorg.png)
   - Create a _New organization_ and give it a unique name (e.g. iot-hackathon-_yourname_). Make sure to select _Create a free organization_ to avoid costs.
   - Skip the step of adding more organization members. This is where you would add your team members if your were to work on a project. However, you do not need to add any organization members for this hackathon.
   - Skip the next steps as well and click _Submit_.

   Your organization has now been created. Click around to check out the UI of a GitHub organization.

1. As a next step, create a [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) of the GitHub repository you will be working with. A fork is a copy of a repository that you manage. Forks let you make changes to a project without affecting the original repository.

   Please follow these steps:

   - Go to the [repository](https://github.com/alschroe/AzureIoTHack), click on _Fork_ and create one:
   ![Image of AzureIoTHack repository, which shows where to click to create a fork](/images/00createfork.png)
   - Select your newly created organization as the _Owner_ and do not change the Repository name.

   You have now successfully forked the repository and should be on the page of the fork within your GitHub organization.

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the current repository to your local machine. This enables you to work locally on your computer.
   
   Follow these steps:

   - Copy this link under _Code_ -> _HTTPS_.
   - Copy the below command and replace ```https://github.com/<YOUR_ORG>/AzureIoTHack.git``` with the copied link.

   ```shell
   git clone https://github.com/<YOUR_ORG>/AzureIoTHack.git
   ```

   You can open it up in Visual Studio Code like this - or with the IDE of your choice.

   ```shell
   cd AzureIoTHack code .
   ```

   This should do for now. <br>
   <br>

**We are looking forward to the hackathon with all of you!**

To start with the challenges, you now have 2 options:
You can train a Machine Learning model using Automated Machine Learning or you can use the Azure Machine Learning Designer.

Go to the [next steps](./01_emu_ml.md).

