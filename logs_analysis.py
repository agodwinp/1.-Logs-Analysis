#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from logs_analysisdb import get_most_popular_articles, get_most_popular_authors

def most_popular_articles():
  '''Main page of the forum.'''
  title = [title for title, num in get_most_popular_articles()]
  return title

def most_popular_authors():
  """"""
  authors = [name for name, num in get_most_popular_authors()]
  return authors

if __name__ == '__main__':
  title = most_popular_articles()
  print "\n1. - The 3 most popular articles of all time are:\n\n", title
  authors = most_popular_authors()
  print "\n\n2. - The most popular article authors of all time are:\n\n", authors
