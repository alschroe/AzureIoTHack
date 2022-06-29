# Set up your environment

To work properly with all the different moving bits and parts we want to connect in this Hackathon, we will have to do quite a bit of setting up. Make sure you have everything on hand that you need:

- your local machine (any computer or set up a virtual machine if you do not feel like installing any additional stuff on your machine)
- an Azure subscription (go to https://azure.microsoft.com/en-us/free/ and create a new free tier account). *This will only work once per Creditcard, if you have already used your free subscription, let us know and we will try to find a solution*
  <br>
  <br>

## Your Azure subscription

1. Set up your Azure Cloud Shell. To do so go to the Azure portal. You can find it under [portal.azure.com](https://portal.azure.com). Log into Azure with your account.
1. You might be seeing the wrong subscription right now. Select _Directories + subscriptions_ - the second icon right from the search bar in the upper menu. Switch to the correct directory if necessary and under _Default subscription filter_ only tag the subscription you want to work on.
   ![Image of the upper bar in the Azure portal with focus on the Directories + subscriptions icon](/images/00portalsub.png) > Have your portal in english - the original language is more helpful for technical tasks.
1. Now that you are in the right place, select the _Azure Clound Shell_ - the icon right next to the search bar in the upper menu. You will be prompted to set up a storage account. Make sure again to use the correct subscription in the dropdown menu and select _Create storage_. A PowerShell will open in your browser. In the dropdown you can also switch to Bash if you prefer this.
   ![Image of the upper bar in the Azure portal with focus on the Cloud Shell icon](/images/00portalshell.png)
   This created a new resource group within your subscription. A resource group is a logical container for all your resources aka Azure services. Within it a storage account was created.
   Take some time to get familiar with the portal. You can find more information about it [here](https://docs.microsoft.com/en-us/azure/azure-portal/azure-portal-overview). <br>
   <br>
   <br>

## Your local machine

We are going to set everything up, so you can work on Azure resources from your local machine. There are multiple options to interact with Azure and you can chose yourself how to do it later on.

1. (optional) Install Visual Studio Code from [here](https://code.visualstudio.com/Download) to handle any code you are going to need. You could of course use a different development environment, we just like this one.
1. (optional) Install the Windows Terminal. You can get it [here](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab). It is a command-line front-end and can run Command Prompt, PowerShell, WSL, SSH and an Azure Clound Shell Connector. Again there are other options, but we like this one.
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

1. You might need to restart your shell at this point. After that clone the current repository to your local machine.

   ```shell
   git clone https://github.com/alschroe/AzureIoTHack.git
   ```

   You can open it up in Visual Studio Code like this - or with the IDE of your choice.

   ```shell
   cd AzureIoTHack code .
   ```

   This should do for now. <br>
   <br>
Go to the [next steps](./01_emu_ml.md).
