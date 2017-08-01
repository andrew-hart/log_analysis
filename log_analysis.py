#!/usr/bin/env python3

import psycopg2
import datetime


class Answers():
    """This class provides the answers to the log analysis assingment"""

    def question_1(self):
        """Answers the first question 'What are the most popular three artiles
        articles of all time?' and outputs the answer on the screen"""
        DBNAME = "news"
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        query = ("""SELECT title, count(*) as num
                    FROM articles, log
                    WHERE log.path LIKE CONCAT('%', articles.slug)
                    GROUP by title
                    ORDER BY num DESC
                    LIMIT 3""")
        c.execute(query)
        a1 = c.fetchall()
        db.close()

        # Print the query for question 1
        for a in a1:
            print(a[0] + " - " + str(a[1]))

    def question_2(self):
        """Answers the second question 'Who are the most popular article
        articles authors of all time?' and outputs the answer on the screen"""
        DBNAME = "news"
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        query = ("""SELECT name, count(*) as num
                    FROM authors, articles, log
                    WHERE authors.id = articles.author and log.path
                    LIKE CONCAT('%', articles.slug)
                    GROUP BY name
                    ORDER BY num DESC""")
        c.execute(query)
        a2 = c.fetchall()
        db.close()

        # Print the query for question 2
        for a in a2:
            print(a[0] + " - " + str(a[1]))

    def question_3(self):
        """Answers the third question 'On which days did more than 1% of
        requests lead to errors?' and outs the answer on the screen"""
        DBNAME = "news"
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute("""SELECT total.date, (100 * errors::float / total) AS
                     error_percentage
                     FROM total, errors
                     WHERE total.date = errors.date
                     AND (100 * errors::float / total) > 1""")
        a3 = c.fetchall()
        db.close()

        # Print the query for question 3
        for a in a3:
            print('{0:%B %d, %Y} - {1:.2f}% errors'.format(a[0], a[1]))

if __name__ == '__main__':
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
