# !/usr/bin/env python3
# Python application that creates the News Reporter

from logs_analysisdb import get_most_popular_articles
from logs_analysisdb import get_most_popular_authors, get_error_prone_days


def most_popular_articles():
    '''Return the top 3 most popular articles'''
    title = [title for title, num in get_most_popular_articles()]
    views = [num for title, num in get_most_popular_articles()]
    return title, views


def most_popular_authors():
    '''Return the authors in descending order of article views'''
    authors = [name for name, num in get_most_popular_authors()]
    reads = [num for name, num in get_most_popular_authors()]
    return authors, reads


def error_prone_days():
    '''Return the days that received > 1% of errors for page requests'''
    errors = [(date, pct_error) for date, pct_error in get_error_prone_days()]
    error_days = [i[0] for i in errors]
    pct = [i[1] for i in errors]
    return error_days, pct


if __name__ == '__main__':
    print("\nWelcome to the News Reporter!")
    print("-----------------------------")
    title, views = most_popular_articles()
    print("\n1. The 3 most popular articles of all time are:\n")
    n = 0
    for i in title:
        print("   ~", i, "was viewed", views[n], "times")
        n += 1
    authors, reads = most_popular_authors()
    print("\n2. The most popular article authors of all time are:\n")
    n = 0
    for i in authors:
        print("   ~", i, "with", reads[n], "views")
        n += 1
    error_days, pct = error_prone_days()
    print("\n3. Days that had > 1% of requests leading to an error are:\n")
    n = 0
    for i in error_days:
        print("   ~", i, "had an error rate of", str(round(pct[n], 2))+"%")
        n += 1
    print("\n-----------------------------\n")
    print("Created by Arun Godwin Patel\n")
