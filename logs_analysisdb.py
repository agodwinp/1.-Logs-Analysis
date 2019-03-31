# "Database code" for the DB Forum.
import psycopg2

DBNAME = "news"

def get_most_popular():
  """Return top 3 most popular articles of all time"""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  query = "select articles.title, count(*) as num from log_slug join articles on articles.slug = log_slug.slug where method='GET' and status='200 OK' group by articles.title order by num desc limit 3;"
  c.execute(query)
  top_3 = c.fetchall()
  db.close()
  return top_3

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  clean_content = bleach.clean(content)
  c.execute("insert into posts values (%s)", (clean_content,))
  c.execute("update posts set content = 'ALIEN LIFE FORM' where content like '%fuck%'")
  c.execute("delete from posts where content = 'ALIEN LIFE FORM'")
  db.commit()
  db.close()