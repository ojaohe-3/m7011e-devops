# Devops
This repository conatins a local runnable instance of the project made for course M7011E, it includes a posgresql server, redis, keycloak and lastly the applications them self.
It also contains an ELK stack which requires some alteration inorder to make work, which is not included as part of project submission as it is not a straight forward process to do localy

## Pre Requirements
1. doecker
2. docker-compose
3. Lots of ram

## Setup
At first run, go to local-app and run the command
```
docker-compose up -d
```
This will promptly cause issues and some services to crash at startup. This is fine since the database is not setup yet

### Setup database
In imports you have a createscript
it includes all changes needed to the database
run these scripts on the created instance of the database, that by default should be
on localhost:5423, use psql or a sql compass software to access them and execute the script.
e.g.
```
psql -h localhost -p 5432 -d postgres -a -f ./createDatabases.sql -U postgres
```
The other applications might need to be restated manually in order for them to work

## Setup keycloak
First time it will fail because it expects a database called keycloak exists, either change that to a database that exists in the database or if you ran the script as above it should have created a database and login for keycloak.
Manual intevention might me necessary. Keycloak expects a user and database as detailed in its enviormental values

When keycloak finish starting, it will be in dev mode. This allows you to access its admin pannel, which by defult in this application is http://localhost:8090

login with the configured admin user, which should be default 
username: admin
password: admin

### Setup realm
For initial setup we need to create the realm. Fortunatly everything should already be created and we will import the configurations from a json file which should be in ./local-apps/imports/realms-export.json
to import the realm first create one by selecting realms in the top left corner as shown in the image
![image](https://github.com/user-attachments/assets/980916c1-30a6-4247-b883-4eec90faa3d0)
Then select create realm
![image](https://github.com/user-attachments/assets/7b4d1280-e42f-4f8d-bac2-a7d0a93fac55)
You can drag and drop the json file into the browser or select browse in the top right corner of the center text box
result should look something like this
![image](https://github.com/user-attachments/assets/7107297c-e027-4700-92cf-ae582eedc9c0)
Press create to setup the realm.

### Setup clients
By default client credentials might not match what is configured in the docker-composefile for the envs
We have to reset the credentials for the clients
Go to clients in keycloak, select the ```auth-server-client```
![image](https://github.com/user-attachments/assets/35bda823-adf8-4722-aacb-43394cb14cff)
Go to credential in the navigation bar at the top
![image](https://github.com/user-attachments/assets/f706937f-cfe9-4c76-8810-ef5003469daf)
Regenerate client secret and copy
Copy the key and paste it in the secret enviormental variable in ./local-app/envs/keycloakEnvs.env as such:
```
...
KEYCLOAK_CLIENT_SECRET=<secret>
...
```

### Setup system user
In order for the application to access its own user it needs to be created
go to keycloak panel, go into the-homeric-odyssey realm and select users in the left navigation bar
![image](https://github.com/user-attachments/assets/c1fdf848-3f0a-437e-b60c-7d7713fdfe96)
Create new user system users, remember join group systems in the bottom.
Default system username is configured to be 'admin' and password 'admin123' so we defere to that for this example
Other info is optional for the system.
here is a working example :
![image](https://github.com/user-attachments/assets/ccc9858a-8b73-4dcb-8519-6da36fee7c50)
Lastly give it a password by selecting 'credentials' in the top navigation bar
create a non temporary password, default setup with the solution is admin123.
Make sure the login coincides with what is configured in the configured values in ./local-app/envs/keycloakEnvs.env as such:
```
...
SYSTEM_USERNAME=admin
SYSTEM_PASSWORD=admin123
```
If you selected temporary password, you need to register the user, it can be done via keycloak email registry, but this is not setup by default.

![image](https://github.com/user-attachments/assets/7357a4de-ea90-4c20-beae-5ea02eab437d)

Lastly you can try to log in using this command
```bash
curl --location 'http://localhost:8090/realms/The-Homeric-Odyssey-Vendor/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=admin' \
--data-urlencode 'password=admin123' \
--data-urlencode 'client_id=auth-server-client' \
--data-urlencode 'client_secret=<client-secret-you-generated>' \
--data-urlencode 'scope=openid' \
--data-urlencode 'grant_type=password'
```
if you get an access_token you can copy it and past it in jwt.io and it should contain the following:
![image](https://github.com/user-attachments/assets/bc268d59-7f80-422b-bdea-315e8f8a6559)
if not the role will not map to system user so it is important.

### Creating any other users 
To create any other users you can simply do the previous step, just select a different goup to join.
e.g. vendor.
Scope id will give access to that scope in the application.
---

## Testing application
You likley need to down the docker-compose.yaml after all setup is completed
but after you restart you should be able to access the open api


