# What needs to be taken into consideration for a productive environment?

At this point we have a working solution - but is it going to run like this in production? No. Here are some important topics to consider for a prod environment.

## Staging environments

Part of agile development is early delivery, continual improvement and evolutionary development.
If you are serving a product to the customer that is being worked on continously in the background you want to have stages. Deploying new features directly into production or fixing bugs in a prod environment could lead to downtime of your application for the customer.
To avoid any bugs to reach to the customer there should be multiple versions of your application and changes should go through these stages before being served in production.
Currently we only have the **prod** stage. With CI/CD in place you can very easily add additional stages for eg. **dev** or **test**. DevOps tools like GitHub allow you to create these environments very easily.
Have a look at [this information](https://azure.microsoft.com/en-us/solutions/dev-test/#solution-architectures) if you are more interested in this.

You can also easily adapt the Terraform files and the GitHub Actions to create these environments. If you are done ahead of time create a **dev** environment without creating additional workflows.

## Security

The last thing that is usually thought about in projects is security and identity. Most devlopers see this topic more as a hustle. And there is a lot to consider and a lot at stake. When we talk about security we also need to talk about networking. Specifically if it comes to IoT solutions that by the nature of things need to communicate into the cloud and out of the cloud this needs to be considered.
Have a look at the [best practices](https://learn.microsoft.com/en-us/azure/security/fundamentals/best-practices-and-patterns) we offer for this.

## Device Management

As you have seen we only considered the cloud environment in the automation. In real life you would want to include the device side as well. And there is a lot to think about. You need to make sure codechanges are rolled out to all the devices, but you also need to run software updates, manage devices, add and delete them. Azure offers many solutions for this. Most commonly the [Azure IoT Hub](https://learn.microsoft.com/en-us/azure/iot-hub/iot-hub-devguide-device-twins) offers some features like *Device twins* that helps with this. Additionally Microsoft offers a SaaS solution - [IoT Central](https://learn.microsoft.com/en-us/azure/iot-central/core/overview-iot-central).

