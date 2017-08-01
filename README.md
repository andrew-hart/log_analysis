# Log Analysis
This project was completed as part of the _Full Stack Web Developer Nanodegree Program_ at Udacity. The purpose of this project was get an introduction to sql and perform some basic queries on a large database. The database `news` is a mock database of a fictional news website, containing three tables `authors`, `articles` and `log`. The `authors` table holds information pertaining to the various authors, while the `articles` table hold information about each article like the author, title, body and time and the `log` table keeps a record of when each articles was accessed.

The questions for this assignment were as follows:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?  

A summary of the answers to these questions can be found in the `output.txt` file. 

# Requirements
The requirments for this assignment are as follows:  
-Virtual Box  
-Vagrant  
-Python 3: `3.6.1`  
-PostgreSQL: `9.5.7`  
-psycopgq: `2.7.3`  

# Setting up the Project
1. Install VirtualBox and Vagrant.
2. Clone or download the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) 
3. Clone or download [this](https://github.com/andrew-hart/log_analysis) repository
4. Unzip the `newdata`. The file inside is called `newsdata.sql`
5. Launch the Vagrant VM from inside the vagrant directory which is in in the fullstack-nanodegree-vm repository with the following command: `vagrant up`
6. Log in with the following command: `vagrant ssh`  
7.Navigate to the `vagrant` directory with the following command: `cd /vagrant`

# Setting up the Database
1. Load the data into your local database with the following command: `psql -d news -f newsdata.sql`
2. Connect to the database with the following command: `psql -d news`

# Views created for this project
To answer the third question the following views will need to be created:

To create the `errors` view run the following command:
`create view errors as select time::date as date, count(*) as errors from log where status = '404 NOT FOUND' group by date order by date;`  

To create the `total` view run the following command:
`create view total as select time::date as date, count(*) as total from log group by date order by date;`

# Running the queries
To run the the queries run the following command from the vagrant directory:
`python3 log_analysis.py`


