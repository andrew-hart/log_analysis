# Log Analysis
This project was completed as part of the _Full Stack Web Developer Nanodegree Program_ at Udacity. The purpose of this project was get an introduction to sql and perform some basic queries on a large database. This project summarizes the results of the those queries in the `output.txt` file. 

# How To Use
Fork the `log_analysis` repository <br />
Make a local copy the `log_analysis` repository <br />
Connect to the `news` database <br />
Run `log_analysis.py` <br />

# Views created for this project
To answer the third question the following views were created
`create view errors as select time::date as date, count(*) as errors from log where status = '404 NOT FOUND' group by date order by date;
` <br />
`create view total as select time::date as date, count(*) as total from log group by date order by date;
` <br />
`create view summary as select date.total, errors.errors, total.total from errors, total where errors.date = total.date;
` <br />
`create view error_table as select date, 100 * (CAST(errors as float)/Cast(total as float)) as results from summary;
` <br />
