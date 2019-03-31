#!/usr/bin/env python3
# 
# A buggy web service in need of a database.

from logs_analysisdb import get_most_popular

def most_popular():
  '''Main page of the forum.'''
  title = [title for title, num in get_most_popular()]
  return title

if __name__ == '__main__':
  title = most_popular()
  print "\n1. - The 3 most popular articles of all time are:\n\n", title
