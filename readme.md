# Clothing App Description
The main function of this app is to allow users to upload images and then display those images to them. 
Liking images and disliking images will also allow users to find those images later. Messaging is also incorporated into the app to allow users to communicate. 

## Prerequisites
* NodeJS
* Python 3.7+
* Pipenv


## Installation
1. Fork the git repo
2. Then create a new folder and clone the project into the folder. 
3. Open up the code in a code editor and navigate to the hashutils.py file inside the server folder. On line 12 please replace ```INSERT_RANDOM_INT_HERE``` with a random int. 
4. Open up the app.py folder and go to line 9 and insert a random string into the secret_key1 = value. 
5. cd into the server folder and run this command:
    * ```pipenv install```
6. Please go over to AWS now and setup an postgres RDS database 
7. Then create a .env file in the server directory with these values in it:
`DB_USER=
DB_PASS=
DB_URL=
DB_NAME=
RUN_ENVIRONMENT=`
8. cd into the client folder and run these commands in order:
    * ```npm install```
    * ```npm run build```
9. Open up browser and load http://localhost:5000/


## Usage
To get the app running you need to use ```npm run build command``` and ```python main.py``` command in separate terminals in order get front end and back end running. 
The app runs through the main.py file. All routing done by vue router. Do not try to use the back end to route users(flask). This makes it so only one index.html file is necessary. 

