# Log Analysis
This project was completed as part of the _Full Stack Web Developer Nanodegree Program_ at Udacity. The purpose of this project was get an introduction to sql and perform some basic queries on a large database. The database `news` is a mock database of a fictional news website, containing three tables `authors`, `articles` and `log`. The `authors` table holds information pertaining to the various authors, while the `articles` table hold information about each article like the author, title, body and time and the `log` table keeps a record of when each articles was accessed.

The questions for this assignment were as follows:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors? <br />
A summary of the answers to these questions can be found in the `output.txt` file. 

# Requirements
The requirments for this assignment are as follows:
-Python 3: `3.6.1`  
-PostgreSQL: `9.5.7`  
-psycopgq: `2.7.3`  

# How To Setup the Peoject
1. Install VirtualBox and Vagrant.
2. Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository and make a local copy
2. Download the data here
3. Download the `news` database from here 
4. 



# Views created for this project
To answer the third question the following views were created: <br />
`create view errors as select time::date as date, count(*) as errors from log where status = '404 NOT FOUND' group by date order by date;
` <br /> <br />
`create view total as select time::date as date, count(*) as total from log group by date order by date;
` <br /> <br />
`create view summary as select date.total, errors.errors, total.total from errors, total where errors.date = total.date;
` <br /> <br />
`create view error_table as select date, 100 * (CAST(errors as float)/Cast(total as float)) as results from summary;
` <br />
