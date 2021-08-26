https://github.com/alschroe/AzureIoTHack.git
https://git-scm.com/download/win
https://code.visualstudio.com/Download
https://www.microsoft.com/de-de/p/windows-terminal/9n0dx20hk701?rtc=1&activetab=pivot:overviewtab

# Set up your environment

To work properly with all the different moving bits and parts we want to connect in this Hackathon, we will have to do quite a bit of setting up. Make sure you have everything on hand that you need:
- your local machine (any computer or set up a virtual machine if you do not feel like installing any additional stuff on your machine)
- an Azure subscription (the trial subscription should do)
- a Raspberry Pi 4 with charging cable, Mini SD
- Potentially an SD Adapter depending on whether or not your device has an SD or Micro SD slot
- Optional but preferred: Desktop, keyboard, mouse
- a Sense HAT, which will collect all the data

## Your Azure subscription
1. Set up your Azure Cloud Shell. To do so go to the Azure portal. You can find it under [portal.azure.com](https://portal.azure.com). Log into Azure with your account. 
1. You might be seeing the wrong subscription right now. Select *Directories + subscriptions* - the second icon right from the search bar in the upper menue. Switch to the correct directory if necessary and under *Default subscription filter* only tag the subscription you want to work on.
    > Have your portal in english - the translation is not helpful for technical tasks.
1. Now that you are in the right place. Select the *Azure Clound Shell* - the icon right next to the search bar in the upper menue. You will be prompted to set up a storage account. Make sure again to use the correct subscription in the dropdown menue and select *Create storage*. A PowerShell will opern in your browser. In the dropdown you can also switch to Bash.
    This created a new resource group within your subscription. A resource group is a logical container for all your resources aka Azure services. Within it a storage account was created.
Take some time to get familiar with the portal. You can find more information about it [here](https://docs.microsoft.com/en-us/azure/azure-portal/azure-portal-overview).

## Your local machine
We are going to set everything up, so you can work on Azure resources from your local machine. There are multiple options to interact with Azure and you can chose yourself how to do it later on.
1. Install Visual Studio Code from [here](https://code.visualstudio.com/Download) to handle any code you are going to need. You could of course use a different development environment, we just like this one.
1. (optional) Install the Windows Terminal. You can get it [here](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab). It is a command-line front-end and can run Command Prompt, PowerShell, WSL, SSH and an Azure Clound Shell Connector. Again there are other options, but we like this one.
1. Open the shell and download the Azure CLI from [here](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli). You can also install it without manual downloading using the PowerShell:
    ```shell
    Invoke-WebRequest -Uri https://aka.ms/installazurecliwindows -OutFile .\AzureCLI.msi; Start-Process msiexec.exe -Wait -ArgumentList '/I AzureCLI.msi /quiet'; rm .\AzureCLI.msi
    ```
1. You might need to close and reopen your shell at this point. After that you can connect to your Azure subscription from the shell. To do so enter the following command:
    ```shell
    az login
    ```
    A login should pop up. Enter your credentials there. Now that we are locked into Azure we need to connect to the right subscription. It is possible that you have more than one subscription under the identity you logged in with. In the output from the shell you should see a detailed list of these subscriptions. If not the following command will print it out.
    ```shell
    az account list
    ```
    One of this subscriptions should be shown as ```"isDefault": "true"```. This is the one you are currently connected to. If this is not the right subscription switch like this:
    ```shell
    az account set --subscription <NAME OR ID OF YOUR SUBSCRIPTION>
    ``` 
    Now let's see if it works:
    ```shell
    az group list
    ```
    This should show you all the resource groups in your Azure subscription - so at least a resource group named "cloud-shell-storage-westeurope" you created in the previous section.
1. Get Git [here](https://git-scm.com/downloads) - it helps you to track changes in files, specifically code. We are going to need it to clone this repo to our local machine.
1. You might need to restart your shell at this point. After that clone the current repository to your local machine.
    ```shell
    git clone https://github.com/alschroe/AzureIoTHack.git
    ```
    You can open in up in Visual Studio Code.
    ```shell
    cd AzureIoTHack
    code .
    ```
1. Download the PuTTY installer from [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and install it.
This should do for now.

## Your Raspberry Pi
The Raspberry Pi is a single-board computer and needs to be properly setup so we can use it. Therefore we first need to install an OS - specifically the Raspberry Pi OS (not longer called Raspbian). As said in the beginning you are going to need a desktop monitor, a keyboard and a mouse to interact with this little computer. If you do not have these at home - or not the right cables to connect them to your Pi - you can also access it via SSH. We will offer you both options below.

### Option 1: WITH desktop, keyboard and mouse connected to the Pi
1. Let's start by downloading the Raspberry Pi OS from [here](https://www.raspberrypi.org/downloads.../). When installing it you will be asked to choose the correct Operating System. Click *CHOOSE OS* and select *Raspberry Pi OS (recommended)*
1. Insert the micro SD card into your local machine.
1. Under *SD Card* click *CHOOSE SD CARD* and make sure you select the right storage space that represents your micro SD card.
1. After that hit *WRITE*. This will flash the OS to your micro SD card. It might take a moment. After that hit *CONTINUE*
1. Now we want to set up our SSH connection. There are other options to this. But ours will be fast, uncomplicated and replicable in real world cases. In the folder *raspberrypi_setup* in this repo you will find two files. The *wpa_supplicant.conf* file contains all the information your Pi needs to connect to your home network. Open it and enter your network name and password. Don't forget to save the changes. The other file is called *ssh* - without file extension. This file will automatically enable SSH on your Pi.
    You will need to very shortly remove the micro SD card and insert it again into your local machine. Then access the boot folder on your micro SD card and paste the two files in them. Eject the SD card securely.
1. Instert the micro SD card into your Raspberry Pi.
1. Now first connect your desktop monitor, your keyboard and your mouse to the Raspberry Pi.
1. Connect your Pi to a power resource.
1. You might be prompted with a login.
    The default login is **pi** and the default password is **raspberry**.
1. 


### Option 2: WITHOUT desktop, keyboard and mouse connected to the Pi
SSH is the Secure Shell Protocol and used to securely connect to another device over an unsecure network.
1. Let's start by downloading the Raspberry Pi OS from [here](https://www.raspberrypi.org/downloads.../). When installing it you will be asked to choose the correct Operating System. Click *CHOOSE OS* and select *Raspberry Pi OS (other)* --> *Raspberry Pi OS Lite*.
1. Insert the micro SD card into your local machine.
1. Under *SD Card* click *CHOOSE SD CARD* and make sure you select the right storage space that represents your micro SD card.
1. After that hit *WRITE*. This will flash the OS to your micro SD card. It might take a moment. After that hit *CONTINUE*
1. Now we want to set up our SSH connection. There are other options to this. But ours will be fast, uncomplicated and replicable in real world cases. In the folder *raspberrypi_setup* in this repo you will find two files. The *wpa_supplicant.conf* file contains all the information your Pi needs to connect to your home network. Open it and enter your network name and password. Don't forget to save the changes. The other file is called *ssh* - without file extension. This file will automatically enable SSH on your Pi.
    You will need to very shortly remove the micro SD card and insert it again into your local machine. Then access the boot folder on your micro SD card and paste the two files in them. Eject the SD card securely.
1. Instert the micro SD card into your Raspberry Pi.
1. Connect your Pi to a power resource. Let it stew for a moment - maybe grab a coffee.
1. Open PuTTY - you installed it in the beginning.
    1. Under *Host Name (or IP addess)* enter ```rasypberrypi.local```.
    1. Under *Port* ```22``` should already be entered, if not do so.
    1. Lastly select *Open*
    1. You should be prompted for login. The default login is **pi** and the default password is **raspberry**.


## Your Sense HAT
