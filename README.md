# MindSphere SDK for Python # 
API clients and References.md

## Full documentation

The full documentation can be found at [https://developer.mindsphere.io/resources/mindsphere-sdk-node/jsdoc/index.html](https://developer.mindsphere.io/resources/mindsphere-sdk-node/jsdoc/index.html)

## Preparation
### Prerequisites to use the MindSphere SDK for Python ###
Python version 8 or higher
User authorization token or service credentials with required scopes for Mindsphere Service APIs
Environment variable HOST_ENVIRONMENT is set to current region. When hosting an application in Cloud Foundry, the variable must be added to the manifest file:


##### env:
  HOST_ENVIRONMENT: eu1
If not specified, HOST_ENVIRONMENT defaults to eu1 in region Europe 1 SDK and to cn1 in region China 1 SDK.

### Download
##### Downloading the MindSphere SDK for Python
Download the MindSphere SDK for Python from the [Siemens Industry Online Support (SIOS) Portal](https://support.industry.siemens.com/cs/document/109757603/mindsphere-sdk-for-java-and-node-js?dti=0&lc=en-US).

## Set up Python Sample Project

The following steps describe the way to set up a sample project to test . You can of course further create .

### Step 1: Clone this repository and Install dependencies
```
git clone https://github.com/mindsphere/mindsphere-python-sdk-examples.git
```
```
cd mindsphere-python-sdk-examples
```
##### Adding MindSphere SDK for Python Dependency¶
Copy the whl files into a folder named `repo` in the root of your project, e.g. repo.
Add the modules into the requirements.txt file like the following
```
repo/mindsphere_core-x.y.z-py3-none-any.whl
repo/{service_name}-z.y.z-py3-none-any.whl
```

###### Note
> {x.y.z} is the version number of the MindSphere Core or Service SDK for Python (e.g. 1.0.0).

### Step 2: Upload app to CloudFoundry and fetch app URL
1. Zip your application for deploying on cloud foundry.
2. Login into cf using this cmd  : `cf login -a [cloudfoundry_login_url] -sso - AWS INT`
3. Select the `org` and `create space` based on the appname you've created with version and target it
4. Once it is targeted, push the app into cf using `cf push` cmd
5. Get the app url by using the cmd `cf apps` and store it for use in further steps

### Step 3: Login to Mindsphere Application
> Your tenant application url will be in the format : https://[tenantName].[region].mindsphere.io
##### Login using your tenant Credentials #####
Login to your tenant on this sign in page for mindsphere.
<p>
<img src="https://github.com/mindsphere/mindsphere-node-sdk-examples/blob/master/images/LoginPage.PNG" width="400">
</p>

##### Mindsphere Dashboard #####
After successful login mindsphere dashboard will appear.
<p>
<img src="https://github.com/mindsphere/mindsphere-node-sdk-examples/blob/master/images/MindsphereDashboard.PNG" width="600">
</p>

##### Open Developer Cockpit #####
Open Developer Cockpit Application in the Dashboard
<p>
<img src="https://github.com/mindsphere/mindsphere-node-sdk-examples/blob/master/images/DeveloperCockpit.PNG" width="200">
</p>

### Step 4: Create a subtenant, an aspect type and asset types

##### Subtenant

In launchpad go to `Settings` -> `SubTenants` -> `Create SubTenant`

##### Aspects, Types and Assets

1. **Creating Aspects**

In launchpad go to `Asset Manager` -> `Aspects` -> `Create Aspects`

a)   Choose category as `dynamic`.

b)  Add variables to the aspect as follows and save it.

| Name | DataType | Unit | Max. Length |
|--------------|--------------|--------------|--------------|
| FLWHEEL | STRING | C | 255 |
| FRWHEEL | STRING | C | 255 |
| RLWHEEL | STRING | C | 255 |
| RRWHEEL | STRING | C | 255 |

2. **Creating Types**

a) Under `Aspects` -> Browse `Aspects`.

b) Browse the created Aspect and add it to the `Types`.

c) Save it.

3. **Creating Assets**

a)  Search for the created `Type` and add it to the `Asset`.

b) Save it.

### Step 5 : Creating SDK App
1. Login to your tenant
2. Open `Developer Cockpit`.
3. `Create new application` -> `Standard` -> `CloudFoundry` -> `AppName`, `Version` and `Description`
4. Add component url with routi as app name
5. Add Roles and Scopes
6. Save it and register after adding roles and scopes