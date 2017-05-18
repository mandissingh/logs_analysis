# logs_analysis

## Introduction
Developing a database schema to connect with already created database and querying the datbase to get useful information. 

## Documents
* log.py : This file contains queries to print information retrieved from database.
* log.sql: This file contains views which are required in the queries in python file.

## Steps To Run The Application:
1. You should use terminal for Mac or Linux and Git Bash for Windows to run the application.
2. Install Virtual Box from here : https://www.virtualbox.org/wiki/Downloads
3. Install Vagrant from here : https://www.vagrantup.com/downloads.html
4. Start the virtual machine by using `vigrant up` command.
5. After downloading necessary files login to the Linux Vm using `vagrant ssh` command.
6. Copy log.py and log.sql to /vagrant directory.
7. Change the directory to the vagrant folder by using `cd /vagrant`
8. Open psql and import the given sql file using `\i log.sql` to your database.
9. Run the python file using `python log.py`
