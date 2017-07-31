#!/usr/bin/env python3

import psycopg2
import datetime

class Answers():
    """This class provides the answers to the log analysis assingment"""

    def question_1(self):
        """Answers the first question"""
        DBNAME = "news"
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        query = ("""select title, count(*) as num from articles, log where 
                  log.path like CONCAT('%', articles.slug) group by title 
                  order by num  desc limit 3""")
        c.execute(query)
        a1 = c.fetchall()

        # Print the query for question 1
        for a in a1:
            print(a[0] + " - " + str(a[1]))

        db.close()

    def question_2(self):
        """Answers the second question"""
        DBNAME = "news"
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        query = ("""select name, count(*) as num  from authors, articles, log
                  where authors.id = articles.author and log.path like
                  CONCAT('%', articles.slug) group by name order by num desc""")
        c.execute(query)
        a2 = c.fetchall()

        # Print the query for question 2
        for a in a2:
            print(a[0] + " - " + str(a[1]))

        db.close()

    def question_3(self):
        """Answers the third question"""
        DBNAME = "news"
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("select * from error_table where results >= 1.0;")
        a3 = c.fetchall()

        # Print the query for question 3
        for a in a3:
            date = a[0].strftime('%b %d, %Y')
            error_percentage = a[1]
            print(date+ " - " + str(error_percentage)[0:4] + "%")

        db.close()

# Create an Answer object and call its methods to display answers
answer = Answers()
print("The most popular three articles of all time are:")
answer.question_1()
print("")
print("The most popular authors of all time are:")
answer.question_2()
print("")
print("The days with more than 1% of requests leading to errors are:")
answer.question_3()

        
        
