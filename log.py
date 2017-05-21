#!/usr/bin/env python

import psycopg2


# Database connection function
def connect(database_name="news"):
    try:
        dataname = 'news'
        db = psycopg2.connect('dbname={}'.format(dataname))
        # Connecting to the databse
        cursor = db.cursor()
        return db, cursor
    except:
        print("Error connecting to database")


# Error calculation function to show errors more than 1%
def Errors():
    connection, cursor = connect()
    # Fetching days with more than 1% errors
    query = """SELECT view1.time, (fault::float * 100)/( total::float)
            AS no_of_error FROM view1, view2 WHERE view1.time = view2.time
            AND(fault::float * 100)/( total::float) >= 1.0;"""
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    cursor.close()
    print "Days with more than 1 percent errors\n"
    for i in range(0, len(result), 1):
        print str(result[i][0]) + "-> " + str(result[i][1]) + "%"


# Function displaying popular authors
def popular_authors():
    connection, cursor = connect()
    # Query to fetch popular authors
    query = """ SELECT COUNT(articles.author),authors.name
            FROM log, articles, authors WHERE path LIKE '/article%'
            AND log.path = CONCAT('/article/',articles.slug) AND
            articles.author = authors.id
            GROUP BY articles.author, authors.name
            ORDER BY count(path) DESC;"""
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    cursor.close()
    print "Popular Authors:\n"
    for i in range(0, len(result), 1):
        print result[i][1] + "-> " + str(result[i][0])


# Function displaying popular articles
def popular_articles():
    connection, cursor = connect()
    # Fetching popular articles
    query = """SELECT title, COUNT(title) AS number FROM log, articles
            WHERE path = CONCAT('/article/', articles.slug) GROUP BY
            title ORDER BY number DESC LIMIT 3;"""
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()
    cursor.close()
    print "Popular Articles:\n"
    for i in range(0, len(result), 1):
        print result[i][0] + "-> " + str(result[i][1])

print"\n"
popular_articles()
print "\n"
popular_authors()
print "\n"
Errors()
print "\n"
