# What needs to be taken into consideration for a productive environment?

At this point we have a working solution - but is it going to run like this in production? No. Here are some important topics to consider for a prod environment.

## Staging environments

Part of agile development is early delivery, continual improvement and evolutionary development.
If you are serving a product to the customer that is being worked on continously in the background you want to have stages. Deploying new features directly into production could lead to downtime of your application for the customer.
To avoid any bugs to reach to the customer there should be multiple versions of your application and changes should go through these stages before being served in production.
Currently we only have the **prod** stage. With CI/CD in place you can very easily add additional stages for eg. **dev** or **test**.

## Security

## Edge and hybrid

## Device Management

This one is quite complex. You need to manage Devices, run Updates and many other things.