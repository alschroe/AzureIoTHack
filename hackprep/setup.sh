#! /bin/bash

# to execute the Script run: 
# . setup.sh 000-000-000-000-000 something.onmicrosoft.com
# . setup.sh <SUBSCRIPTION ID> <AAD PRIMARY DOMAIN>

for i in {1..14}
do
    az ad user create --display-name capuser$i --password Pa55w0rd$i --user-principal-name capuser$i@$2
    sp=$(az ad sp create-for-rbac --name "capuser$i-github-actions-sp" --sdk-auth --role contributor --scopes /subscriptions/$1)
    az role assignment create --assignee capuser$i@$2 --role contributor --scope /subscriptions/$1
    echo "Username: capuser$i@$2, Password: Pa55w0rd$i, SP: $sp" >> access.txt
done