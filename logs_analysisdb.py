# "Database code" for the DB Forum.
import psycopg2

DBNAME = "news"

def get_most_popular_articles():
  """Return top 3 most popular articles of all time"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  query = "select articles.title, count(*) as num from log_slug join articles on articles.slug = log_slug.slug where method='GET' and status='200 OK' group by articles.title order by num desc limit 3;"
  c.execute(query)
  top_3 = c.fetchall()
  db.close()
  return top_3

def get_most_popular_authors():
  """Return authors in order of decreasing article views"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  query = "select * from author_views"
  c.execute(query)
  authors = c.fetchall()
  db.close()
  return authors

def get_error_prone_days():
  """Return the days that have had > 1% of requests leading to errors"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  query = "select date::text from log_daily_pct_error where pct_error > 1;"
  c.execute(query)
  days = c.fetchall()
  db.close()
  return days

