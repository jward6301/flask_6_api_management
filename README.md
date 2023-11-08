# flask_6_api_management
HHA 504 Week 6 Assignment

## 1. Flask-based RESTful API:
* Create a python script utilzing Flask to be able to deploy an endpoint that can read a GET request.
* To view my code, click on the following link: https://github.com/jward6301/flask_6_api_management/blob/main/Flaskapp/function_app.py

## 2. Azure API deployment:
* You can either complete your python script before of after completing the first few steps. If you complete it beforehand, you will need to copy and paste the code into the files that will generate (this will occur in step 6).
1. To install Azure CLI, type `curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash` into the cloudshell terminal.
2. To ensure Azure is installed correctly, type `az` into the terminal.
3. You now have to connect to your Azure account to run the app. Type in `az login --use-device-code`. A link and a code will show up, copy the code and then click on the link and follow the instructions.
4. Now you need to install Azure Functions Core Tools for Linux using the following command: `sudo apt-get install azure-functions-core-tools-4`.
5. To create a folder and files that will be needed for your app, type the following command into the terminal: `func init <folder name> --python -m V2`.
6. In the function_app.py file that generated, create your flask code or paste the already created code into this file.
7. In the local.settings.json file, check if AzureWebJobsFeatureFlags is set to `EnableWorkerIndexing`, if not please change it.
8. Log into the Azure Portal using this link: https://azure.microsoft.com/en-us/get-started/azure-portal. Once logged in, using the Search bar, look up Storage Accounts. Open it and click Create. You can either use an existing resource group or create a new one, as well as a storage account name. Click create.
9. Open the new storage account and on the left hand menu search for access keys. Copy the connection key and return to cloud shell.
10. In the local.settings.json file, paste the connection key as the AzureWebJobsStorage setting.
11. To start your app, type `func start` into the terminal.
12. To create the API for your app in Azure, paste and modofy the following command: `az functionapp create --resource-group <your resource group name> --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name <your app name> --os-type linux --storage-account <your storage account name>` If you recieve any error codes, ensure that your resource group name and storage account name match the ones on Azure.
13. You will then have to finish publishing the API as it doesn't do it automatically. Paste and modify the following command: `func azure functionapp publish <your app name>`.
14. You can now check on Azure if this was created correctly, it may take a minute to update on Azure. Once it is ready, copy the URL that will be provided.
15. Paste the URL into your browser and add /api/hello. For example, my link was https://jessica504flaskapp.azurewebsites.net/api/hello.
16. To update the website to change the responses in the fields, change the URL. To update my fields, I added /api/hello?name=Frances&lastname=Smith&age=22&birthyear=2001 to my URL. It now looked like https://jessica504flaskapp.azurewebsites.net/api/hello?name=Frances&lastname=Smith&age=22&birthyear=2001
* My Azure App link: https://jessica504flaskapp.azurewebsites.net

## 3. OpenAPI Specification and Documentation:
* In this step you will update the flask app to include Flasgger/Swagger. Instructions on how to use swagger can be found at the following link: https://github.com/flasgger/flasgger (This documentation was provided from Professor Williams.
* To view the code I created for this step, click on the following link: https://github.com/jward6301/flask_6_api_management/blob/main/flasgger_app.py
* Once you have made all necessary changes to this file, you can deploy the app using instructions provided in a previous link.
* You must enter the following two commands in your terminal before deploying the app: `pip install -U setuptools` and `pip install flasgger==0.9.7b2`
* Once those commands are entered and your code is completed, you can run `python <file name>` and click on the url provided. This url will have to be updated based off of the documentation to update correctly.

## 4. Issues and Errors:
* The only issue I ran into was running the swagger steps. My URL was not working correctly. Eventually after going through the documentation again I was able to get it to work. I was missing part of the URL (the /#/ after apidocs).

