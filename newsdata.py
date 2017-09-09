#!/usr/bin/env python3

import psycopg2

# let this python file connect to the database
conn = psycopg2.connect("dbname=news")

cur = conn.cursor()

# create templates for the PostgreSQL that can make it easier to read
answer1 = ("select articles.title, count(*) as views "
           "from articles join log "
           "on log.path like concat('/article/', articles.slug) "
           "where log.status = '200 OK' "
           "group by articles.title "
           "order by views "
           "desc limit 3;")
answer2 = ("select name, count(*) as views "
           "from articles "
           "inner join log on log.path "
           "like concat('/article/', articles.slug) "
           "inner join authors on authors.id = articles.author "
           "where log.status = '200 OK' "
           "group by name "
           "order by views "
           "desc;")
answer3 = ("select view_by_date.date, "
           "round((errors::numeric/views)*100, 2) as percent "
           "from view_by_date join error_by_date "
           "on view_by_date.date = error_by_date.date "
           "where round((errors::numeric/views)*100, 2) > 1;")

# this execute the first query and runs it
cur.execute(answer1)
rows = cur.fetchall()
# this prints out the question and the answer
print "What are the most popular three articles of all time? " + '\n'
for row in rows:
    # format it to be more readable
    print （str(article), '-', str(views), 'views'）
print （'\n'）  # add a linebreak

# this execute the second query and runs it
cur.execute(answer2)
rows = cur.fetchall()
# this prints out the question and the answer
print "Who are the most popular article authors of all time? " + '\n'
for row in rows:
    # format it to be more readable
    print （str(name), '-', str(views), 'views'）
print （'\n'）

# this execute the third query and runs it
cur.execute(answer3)
rows = cur.fetchall()
# this prints out the question and the answer
print "On which days did more than 1% of requests lead to errors? " + '\n'
for row in rows:
    # format it to be more readable
    print （str(date), '-', str(percent) + '% errors'）
print （'\n'）  # add a linebreak

# this close the communication with the PostgreSQL
cur.close()
