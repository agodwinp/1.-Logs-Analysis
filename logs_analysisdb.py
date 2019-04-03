# !/usr/bin/env python3
# Database code for the Project 1 "news" DB

import psycopg2
DBNAME = "news"
try:
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
except psycopg2.Error as e:
    print("Unable to connect to the database")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)


def get_most_popular_articles():
    '''Return top 3 most popular articles of all time'''
    query_pt1 = "select articles.title, count(*) as num from log_slug "
    query_pt2 = "join articles on articles.slug = log_slug.slug where "
    query_pt3 = "status='200 OK' group by articles.title "
    query_pt4 = "order by num desc limit 3;"
    query = query_pt1+query_pt2+query_pt3+query_pt4
    c.execute(query)
    top_3 = c.fetchall()
    return top_3


def get_most_popular_authors():
    '''Return authors in order of decreasing article views'''
    query = "select * from author_views"
    c.execute(query)
    authors = c.fetchall()
    return authors


def get_error_prone_days():
    '''Return the days that have had > 1% of requests leading to errors'''
    query_pt1 = "select date::text, pct_error from log_daily_pct_error "
    query_pt2 = "where pct_error > 1;"
    query = query_pt1+query_pt2
    c.execute(query)
    days = c.fetchall()
    db.close()
    return days
