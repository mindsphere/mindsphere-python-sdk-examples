# MindSphere SDK for Python # 
API clients and References.md

## Full documentation

The full documentation can be found at [https://developer.mindsphere.io/resources/mindsphere-sdk-python/sphinxdoc/index.html](https://developer.mindsphere.io/resources/mindsphere-sdk-python/sphinxdoc/index.html)

## Preparation

## 1 - Preparation
### Prerequisites to use the MindSphere SDK for Python ###
- 1. Python version 3.6.x or higher installed where application will be running.
- 2. User authorization token or app credentials with required scopes for Mindsphere Service APIs.
    - 2.1 Environment variables set up in local machine to run application in local. 
    - 2.2 When application hosting type is `SELF_HOSTED`, the variables must be configured on server.
    - 2.3 When hosting an application in Cloud Foundry, the variable must be present as application's environment variables. This is achieved by adding variables in the __*manifest.yml*__ file.

#### Environment Variables ####

Application Credentials
| Sr. No. | Environment Variable | Description |
|-----|--------------|--------------|
|1 | MDSP_OS_VM_APP_VERSION| Store App Version in environment variable named `MDSP_OS_VM_APP_VERSION`. | 
|2 | MDSP_OS_VM_APP_NAME| Store App Name in environment variable named `MDSP_OS_VM_APP_VERSION`. | 
|3 | MDSP_KEY_STORE_CLIENT_ID| Store App Client ID in environment variable named `MDSP_KEY_STORE_CLIENT_ID`. |
|4 | MDSP_KEY_STORE_CLIENT_SECRET| Store App Client Secret in environment variable named `MDSP_KEY_STORE_CLIENT_SECRET`. |
|5 | MDSP_HOST_TENANT | Store the name of the tenant on which application is hosted in environment variable named `MDSP_HOST_TENANT`. |
|6 | MDSP_USER_TENANT | Store the name of the tenant from which application is being accessed in environment variable named `MDSP_USER_TENANT`. |
|7 | HOST_ENVIRONMENT | Store the region in environment variable named `HOST_ENVIRONMENT`. If not specified, HOST_ENVIRONMENT defaults to `eu1` in region Europe 1 SDK and to `cn1` in region China 1 SDK.


- Above credentials ( App Credentials ) will suffice to use SDKs.
- For more information about credentials please visit [Token Handling](https://developer.mindsphere.io/resources/mindsphere-sdk-java-v2/token_handling_v2.html)
###### Note 
> App Credentials and Application Credentials refers to same concept. These terms might be used interchangeably in the document.


##### env:
  HOST_ENVIRONMENT: eu1
If not specified, HOST_ENVIRONMENT defaults to eu1 in region Europe 1 SDK and to cn1 in region China 1 SDK.

### Download
##### Downloading the MindSphere SDK for Python
Download the MindSphere SDK for Python from the [Siemens Industry Online Support (SIOS) Portal](https://support.industry.siemens.com/cs/document/109757603/mindsphere-sdk-for-java-and-node-js?dti=0&lc=en-US).

## 3 - Host Python Sample Project on MindSphere
MindSphere provides two ways to host an application - `Cloud Foundry Hosted` and `Self Hosted`.
For `Cloud Foundry Hosted` see 3A - 1 and for `Self Hosted` see 3A-2.

### 3A - 1 : Upload app to CloudFoundry and fetch app URL

The following steps describe way to deploy Python Sample Project on Cloud Foundry.
If you want to host your own application instead of sample project then skip to step 3(Push the App to CloudFoundry).

#### 1. Clone this repository.
####
```
git clone https://github.com/mindsphere/mindsphere-python-sdk-examples.git
```
#### 2. Install required dependencies.

- Download Python SDK from  [Download](#2---download).
- Unzip the downloaded file.
- Navigate to <some path where unzipped folder is located>/mindsphere-python-sdk_1.0.3/modules/
- Copy .whl files of required dependent service/services in 'requirements' folder. (For this project(mindsphere-sdk-python-examples) we will need all the .whl files but you can choose to use only required subset of all avaiable SDKs for your project.)
- `requirements` folder is already created for your convinience.
- For convinience, requirements.txt is populated with relative path to copied dependencies.

###### Note 
> There are two versions availalable for timeseries (3.3.2 and 3.4.1). Any of this two versions is suitable for `mindsphere-sdk-python-examples`. Make sure correct version is mentioned in requirements.txt before `pip install`.


#### 3. Push the App to CloudFoundry.
- Navigate to directory where cloned project directory is present. In this case navigate to sample-python-demo-app.

    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/directory-python.PNG" width="400">
    </p>
- In order to push app to CF, user must login to cloudfoundry. To login user can opt for either of two ways.
    - Jump to [Login to CF](#login-to-cf)
- At this point you are successfully logged in CF.
- Prepare manifest.yml file for pushing. File content pertinent to sample project are as :
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/manifest-python.PNG" width="400">
    </p>
- For convenience, sample manifest.yml is added in root directory of project.
- `path` specifies where to look for application. Here in this case, our app is located inside `mindsphere-python-sdk-examples` folder.
- Environment variables are listed under `env`. Since sample application demonstrates use of MindSphere SDKs, environemnt variables  are only specific for Token Generation. In case of other application, user can append the list with his/her own environment variables.
- As mentioned in 1 - Prerequisites, either of Tenant Credentials/ Application Credentials would suffice for getting token.
- In sample file variables for App redentials are mentioned but user can choose to either of two types available.
- As here opting for App Credentials, user will not have values of all environment variables at this point. In this scenario either put some dummy values or do not add variables at all. CF provides command to set environment variables hence they can be set later on.
- Now run the command `cf push`.
- Once application is successfully deployed check for app status using command `cf app routi`.
- Note down app URL displayed on screen.
<p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/cfappurlpython.PNG" width="400">
</p>

###### Note 
> During testing most common issue faced is : django.core.exceptions.ImproperlyConfigured: You're using the staticfiles app without having set the STATIC_ROOT setting to a filesystem path.
> If you face such issue then run the command `cf set-env <app> DISABLE_COLLECTSTATIC 1` and push the app again by `cf push`.
<p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/pythonerror.PNG" width="400">
</p>

### 3A - 2 : Deploy the application as Self Hosted Application.
- Self Hosted Applications are deployed by user on desired server.
- User must note down URL where application is hosted.

### Step 3A - 3 : Create Application in Developer Cockpit.

#### Save the Application
1. Open the **Developer Cockpit** from the Launchpad and select the **Dashboard tab**.
2. Click on **Create new application**.
3. Select Type Standard and Infrastructure MindSphere Cloud Foundry if you have deployed application in cloud foundry. In case of self-hosted application select Self Hosted.
4. Enter an arbitrary Display Name and an Internal Name which will be part of the application URL. The Internal Name cannot be changed after initial creation!
5. Enter a version number.
    - MindSphere supports a Major.Minor.Patch scheme.
    - Versions must start with a major number >= 1.
    - The version cannot be changed after saving.
6. Upload an icon for your application.(Optional step)
7. Enter the component name. The component name must be the same as specified in the __*manifest.yml*__ file.
    - In case of sample project `mindsphere-python-sdk-examples` component name will be **routi** and component url can be obtained by 
      running `cf app routi` on command line.
    - In case of Self Hosted Application, component name and URL will be as per customer's deployment strategy.
8. Add one endpoint for your component using /** to match all of your application paths.
9. Set the content-security-policy according to the examples:
    - For Europe1 :     default-src 'self' *.eu1.mindsphere.io; style-src * 'unsafe-inline'; script-src 'self' 'unsafe-inline' *.eu1.mindsphere.io; img-src * data:;
    - For Europe2:     default-src 'self' *.eu1.mindsphere.io *.eu2.mindsphere.io; style-src * 'unsafe-inline'; script-src 'self' 'unsafe-inline' *.eu1.mindsphere.io *.eu2.mindsphere.io; img-src * data:;
10.  Click on **Save**.

#### Add roles and Scopes
1. Switch to the Authorization Management tab.
2. Select the application you just created.
3. Create an application scope, e.g. <provided-application-name>.subtenant.
4. Add the following Core roles to enable access to the respective APIs. For this project - `mindsphere-python-sdk-examples`, you will need following API roles. If required roles are not added then endpoints specific to those services will not work as expected.
<p>
<img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/apirolespython.PNG" width="400">
</p>

#### Register the Application
1. Switch to the Dashboard tab.
2. Open the application details.
3. Click on Register.

#### Generate App Credentials
1. Switch to the Authorization Management tab.
2. Click on **App Credentials** tab.
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/acpython.PNG" width="400">
    </p>
3. Click on **Issue access** button.
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/issueaccessac.png" width="400">
    </p>
4. Select **Read And Write** .
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/readandwrite.PNG" width="400">
    </p>
5. Click on **Submit** button.
6. You will be presented with client ID and client secret for application.
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/cidcsecretpython.PNG" width="400">
    </p>
7. Store these values at secure location as they are displayed only once.

#### Set environment variables
1. In case of App Credentials, at this point you have all the required values for corresponding environment variables - 
`MDSP_OS_VM_APP_NAME`, `MDSP_OS_VM_APP_VERSION`, `MDSP_KEY_STORE_CLIENT_ID`,`MDSP_KEY_STORE_CLIENT_SECRET`,`MDSP_HOST_TENANT`, `MDSP_USER_TENANT`.

| Sr. No. | Environment Variable | Value |
|-----|--------------|--------------|
|1 | MDSP_OS_VM_APP_VERSION| Version you provided while creating application. | 
|2 | MDSP_OS_VM_APP_NAME| Internal name of your application(Can be seen in Application Details in Developer Cockpit). | 
|3 | MDSP_KEY_STORE_CLIENT_ID|  App Client ID displayed on screen in last step. |
|4 | MDSP_KEY_STORE_CLIENT_SECRET| App Client Secret displayed on screen in last step. |
|5 | MDSP_HOST_TENANT | Name of the tenant you are currently working upon. |
|6 | MDSP_USER_TENANT | This specifies the name of tenant which will use the application. Since we are currently in developing and testing phase, `MDSP_USER_TENANT` == `MDSP_HOST_TENANT`. |

2. Set the values of this environment variables in Cloud Foundry.
```
cf set-env routi <VARIABLE-NAME> <VARIABLE-VALUE>
```
If you have provided any other value for application name then modify the command accordingly.
As suggested by Cloud Foundry documentation, restage the app.
````
cf restage <APP-NAME>
````
3. In case of Self Hosted application, you need to store these values as per deployment strategy. Also make sure this values can be accessed in application.
      
#### Assign the App and Access via Launchpad
1. Navigate to MindSphere Launchpad -> Settings -> Users
2. Select a Developer you want to assign this application to. (You can assign it to yourself as well)
3. Scroll down a bit and click on **Edit direct assignments**.
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/assignapp.png" width="400">
    </p>
4. In the **Application Roles** section, search your application by internal name.
5. Select checkboxes for both admin and user.
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/addadminuser.PNG" width="400">
    </p>
6. Click on **Next**.
7. Click on **Save**.

Now concerned developer should be able to access the application via launchpad.

#### Access the application.
1. Navigate to MindSphere Launchpad.
2. Click on your application tile.
3. You should see something like :
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/swaggerui-changes/images/Accessapp.png" width="400">
    </p>    
4. By clicking on any endpoint showing on above image you should see like :
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/swaggerui-changes/images/putaspectcall.png" width="400">
    </p>
5. By clicking 'try it out' button you can make api call by putting correct parameters and requestbody. then you will get response like :
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/swaggerui-changes/images/respnseapi.png" width="400">
    </p>    
    
6. Domain url is **Application URL** displayed on Application details page.
    <p>
    <img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/master/images/appurl.PNG" width="400">
    </p>

###### Note 
> we required xsrf token for calling put,pots/patch,delete api. so we need to pass it in request header, This token is available in browser cache, we have fetched this token from cache and put it in request header, so we dont need to add this by manually.  



### 3B - Set up Python Sample Project For Local Machine

The following steps describe the way to set up a sample project to test on local machine.
This is to facilitate any bug resolution on local developer setup.
Please follow prerequisite section for environment variables, how to get them and how to store them.

##### 1. Clone this repository.
####
```
git clone https://github.com/mindsphere/mindsphere-python-sdk-examples.git
```
##### 2. Install required dependencies.

- Download Python SDK from  [Download](#2---download).
- Unzip the downloaded file.
- Navigate to <some path where unzipped folder is located>/mindsphere-python-sdk_1.0.3/modules/
- Copy .whl files of required dependent service/services in 'requirements' folder. (For this project(mindsphere-sdk-python-examples) we will need all the .whl files but you can choose to use only required subset of all avaiable SDKs for your project.)
- `requirements` folder is already created for your convinience.
- For convinience, requirements.txt is populated with relative path to copied dependencies.
- Navigate inside the root directory of project if you are not in there.
```
cd mindsphere-python-sdk-examples
```
- Run below command to install required dependecies mentioned in requirements.txt file.
```
pip install -r requirements.txt
```
###### Note 
> If you face errors while `pip install -r requirements.txt` mentioning particular '<file-name>.whl file not found' then kindly verify dependency file name in requirements folder and that mentioned in requirements.txt file. This could be also due to incorrect relative path mentioned in requirements.txt file. If so then modify path in requirements.txt wherever required.

##### 3. Run the app.
####
```
python manage.py runserver
```
##### 4. Access the app.
1. Navigate to 'http://127.0.0.1:8000' (You can use any browswer of your choice).
2. Domain URL in this case will be 'http://127.0.0.1:8000'.
<p>
<img src="https://github.com/mindsphere/mindsphere-python-sdk-examples/blob/swaggerui-changes/images/Homescreen.png" width="400">
</p>


## 4 - Prepare the app to hand it over to Operator Cockpit
Please refer [Handing over app to Operator Cockpit](https://developer.mindsphere.io/howto/howto-develop-and-register-an-application.html#handover-the-application-to-the-operator-tenant)
