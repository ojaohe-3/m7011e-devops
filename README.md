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
For initial setup it is not sufficient to create a realm
![image](https://github.com/user-attachments/assets/980916c1-30a6-4247-b883-4eec90faa3d0)



