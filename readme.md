# Clothing App 
## Description
The main function of this app is to allow users to upload images and then display those images to them. 
Liking images and disliking images will also allow users to find those images later. Messaging is also incorporated into the app to allow users to communicate. 

## Features
* Imgur photo upload
* Messenger
* Profile management
* Like or Dislike photos and matching with other users

## Prerequisites
* NodeJS v10.16.3
* Python 3.7+
* Pipenv
* sqlite3(for local db)


## Installation
* Fork the git repo
* Then create a new folder and clone the project into the folder. 
## Adjustments in code
* Sign up for an Imgur API account here: https://apidocs.imgur.com/?version=latest#intro
    * replace the client ID on line 39 in the upload.vue file in the client > views folder with your own client ID. 

## Installing Server Dependencies
* cd into the server folder and run this command:
    * ```pipenv install```

## Deployment Configuration(db)
### Network db 
    
* Please go over to AWS now and setup an postgres RDS database 
* Then create a .env file in the server directory with these values in it:
    ```DB_USER=
    DB_PASS=
    DB_URL=
    DB_NAME=
    RUN_ENVIRONMENT=network
    SECRET_KEY=
    HASH_VALUE=
### Local db 
* cd into the db folder and create a new sqlite3 database. 
* In the app.py file located in the server folder please replace `clothingapp.db` with the name of the db you just created. 

##### NOTE : if you would like to run a local instead of a network db please change the RUN_ENVIRONMENT= value from `network` to `local` in your .env file located in the server folder.

## Local Server Deployment
* cd into server folder and run the command: ```pipenv run python main.py```

## Front End Deployment
* in a new terminal tab cd into the client folder and run these commands in order:
    * ```npm install```
    * ```npm run build```
* Open up browser and load http://localhost:5000/


## Caveats and Good-To-Knows
* Register on the RDS database actually doesn't redirect the users to the home page after they register. This is likely due to how slow it is for the session to be set.(this is a bug)
## Next Steps
* fix bugs
    * User can send a blank message
    * Image doesn't size down automatically and can affect overall appearance of the pages.
* Features to add:
    * Password reset
    * verification on the register page and login page
    * Unread messages icon
    * reformat for mobile

To see the full Kanban board please go here: https://github.com/pkurjanowicz/clothingApp/projects/1

