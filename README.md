# Azure IoT Hackathon

Welcome! We plan to implement an Azure IoT solution with you.
To do so we have documented the process for you.
There are two ways to run through this Hackathon.

- Under **option 1** you will use a Raspberry Pi and a Sense HAT to retreive the necessary data. All the documentation will have **pi** in their name. So to set up for this option move to the [00_pi_setup.md](./challenges_pi/00_pi_setup.md).
- Under **option 2** you will use an online emulator for the Raspberry Pi and an additional sensor. All the documentation will have **emu** in theur name. So to set up for this option move to the [00_emu_setup.md](./challenges_emulator/00_emu_setup.md).

Please do the setup in advance since it will take some time.

If you are planning to go with **option 1** create the following architecture:

![Showing the menue in the Azure portal with the + create button being on the very left](/images/architecture.png)

| Challenge                                              | Content                                                                                                                                                          |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [01_pi_ml.md](./challenges_pi/01_pi_ml.md)             | Create an Azure Machine Learning model to predict whether it is raining or not from temperature and humidity data.                                               |
| [02_pi_iothub.md](./challenges_pi/02_pi_iothub.md)     | Use the Azure Iot hub to receive temperature and humidity data.                                                                                                  |
| [03_pi_app.md](./challenges_pi/03_pi_app.md)           | Send temperature and humidity data from your Pi to the Cloud.                                                                                                    |
| [04_pi_function.md](./challenges_pi/04_pi_function.md) | Create an Azure Function that upon the Azure IoT hub receiving the data from your Pi gets a prediction from the previously created Azure Machine Learning model. |

If you are planning to go with **option 2** create the following architecture:

![Showing the menu in the Azure portal with the + create button being on the very left](/images/architecture.png)

| Challenge                                                      | Content                                                                                                                                                                |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [01_emu_ml.md](./challenges_emulator/01_emu_ml.md)             | Create an Azure Machine Learning model to predict whether it is raining or not from temperature and humidity data.                                                     |
| [02_emu_iothub.md](./challenges_emulator/02_emu_iothub.md)     | Use the Azure Iot hub to receive temperature and humidity data.                                                                                                        |
| [03_emu_app.md](./challenges_emulator/03_emu_app.md)           | Send temperature and humidity data from your Emulator to the Cloud.                                                                                                    |
| [04_emu_function.md](./challenges_emulator/04_emu_function.md) | Create an Azure Function that upon the Azure IoT hub receiving the data from your Emulator gets a prediction from the previously created Azure Machine Learning model. |
