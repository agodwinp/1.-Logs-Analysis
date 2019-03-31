# Python application that builds logs analysis report

from logs_analysisdb import get_most_popular_articles, get_most_popular_authors, get_error_prone_days

def most_popular_articles():
  '''Return the top 3 most popular articles'''
  title = [title for title, num in get_most_popular_articles()]
  return title

def most_popular_authors():
  '''Return the authors in descending order of article views'''
  authors = [name for name, num in get_most_popular_authors()]
  return authors

def error_prone_days():
  '''Return the days that received > 1% of errors for page requests'''
  error_days = get_error_prone_days()[0]
  error_days = [i for i in error_days]
  return error_days

if __name__ == '__main__':
  title = most_popular_articles()
  print "\n1. The 3 most popular articles of all time are:\n\n", title
  print "\n","-"*50
  authors = most_popular_authors()
  print "\n2. The most popular article authors of all time are:\n\n", authors
  print "\n","-"*50
  error_days = error_prone_days()
  print "\n3. The days that had > 1% of requests that led to an error are:\n\n", error_days
  print "\n","-"*50