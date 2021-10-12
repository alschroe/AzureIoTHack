# Azure IoT Hackathon

Welcome! We plan to implement an Azure IoT solution with you.
To do so we have documented the process for you.
There are two ways to run through this Hackathon.

- Under **option 1** you will use a Raspberry Pi and a Sense HAT to retreive the necessary data. All the documentation will start with a **0**. So to set up for this option move to the [00_pi_setup.md](./00_pi_setup.md).
- Under **option 2** you will use an online emulator for the Raspberry Pi and an additional sensor. All the documentation will start with a **1**. So to set up for this option move to the [10_emulator_setup.md](./10_emulator_setup.md).

Please do the setup in advance since it will take some time.

If you are planning to go with **option 1** create the following architecture:

![Showing the menue in the Azure portal with the + create button being on the very left](/images/architecture.png)

| Challenge | Content |
| ------ | --------- |
| [01_pi_ml.md](./01_pi_ml.md) | Create an Azure Machine Learning model to predict whether it is raining or not from temperature and humidity data. |
| [02_pi_iothub.md](./02_pi_iothub.md) | Use the Azure Iot hub to receive temperature and humidity data. |
| [03_pi_app.md](./03_pi_app.md) | Send temperature and humidity data from your Pi to the Cloud. |
| [04_pi_funciton.md](./04_pi_funciton.md) | Create an Azure Function that upon the Azure IoT hub receiving the data from your Pi gets a prediction from the previously created Azure Machine Learning model. |

