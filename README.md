# flask_6_api_management
Develop APIs with Flask and managed by Azure

## Schema

The GitHub repository contains three total Python files within separate folders. One is a basic Flask app to utilize a get request on a local level. The next is a Flasgger Flask app that uses the Flassger interface to interact with the requests on the Flask app. The third is the Azure Serverless Function Application, which can be deployed locally or accessed through a link. Screenshots of all of these functions are displayed in the screenshots folder.

## Flask Endpoint

1. Create a basic Flask application with an endpoint '/' to act as a landing page.
2. Designate a variable name to act as an argument within the URL, using: request.args.get('variable, 'default value if left null'
3. Return a message or function containing this argument.
4. To test, navigate to the endpoint where the argument was created. At the end of the URL, add ?(variablename)=(value), replacing the parenthesized terms with your values. If adding multiple arguments, separate them using '&'.

## Flasgger App

Flasgger is the package that will allow you to generate a user-friendly interface to observe and interact with the restful API operations within your Flask App. Screenshots of this endpoint are shown in the screenshots folder. To set this up:

1. Import swagger from Flasgger within your flask app.
2. Input the name of your Flask app as an argument within the Swagger function: Swagger(app)
3. Underneath the endpoint, input a description for the endpoint, the parameters defined within your function and their properties, and messages based on the status code of the request. The proper formatting for this text is shown within the app_flasgger.py file.
4. To access the Flasgger interface, use the endpoint /apidocs, which will bring you to the interactive interface of your Flask application's API requests.

## Azure API Integration

1. Install Azure Functions Core Tools using: sudo apt-get install azure-functions-core-tools-4
2. Create a local function in your repository using: func init LocalFunctionProj --python -m V2.  This will create a folder containing a number of files, including a .py file to run your app.
3. Insert your desired functions into the function_app.py file provided in the folder. The syntax is similar to Flask but not the same, so you cannot directly copy/paste your code from Flask. Here is an example of what the syntax should look like:

``import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")``

4. Run your function locally using: func start. This should bring you to an endpoint where Azure will verify that the app is running, and you can test the API requests using the endpoints and variables designated in your function.
5.  Create a resource group, storage account, and Azure Function App to host the app. These can be done in Azure directly or using Azure CLI. If using Azure CLI, use the following commands:
Resource Group: az group create --name (ResourceGroupName) --location (Region)
Storage Account: az storage account create --name (StorageAccountName) --location (Region) --resource-group (ResourceGroupName) --sku Standard_LRS
Azure Function App: az functionapp create --resource-group (ResourceGroupName) --consumption-plan-location (region) --runtime python --runtime-version 3.9 --functions-version 4 --name (AppName) --os-type linux --storage-account (StorageAccountName)

6. Deploy the app using: func azure functionapp publish (AppName)
7. Use the provided link to access your application. The link is shareable! The link to my application is: https://seanapphha504.azurewebsites.net/api/hello

## Issues

The only issue I came across during this process was with the Azure App deployment. My endpoints were working correctly on my local version, but when published I could not access my /hello endpoint. It presented me with a 401 error and said "Please contact the website owner". I thought it was maybe an issue with the settings of my storage account or resource group, as in my first attempt I used an already existing resource group and storage account. I created new versions using Azure CLI following the documentation exactly, however, I still had the same 401 error. I realized the issue was in my Python code in the following line:  ``app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)`` 

The 'FUNCTION' keyword means that in order to access this application's endpoints, I would need to use a key/function credentials system, which may be useful for a secure website, but was a roadblock for this assignment. I changed the keyword 'FUNCTION' to 'ANONYMOUS', which immediately solved my problem. I had no other issues with this assignment.


