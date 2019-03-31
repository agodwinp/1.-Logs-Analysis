# 1. Logs Analysis
Project 1 for Udacity FSND

***

**Arun Godwin Patel**

### Design
- The architecture for this application consists of a PostgreSQL database deployed on a Linux VM, along with a Python application that manages the queries and creation of the report.
- I used the 3 tables articles, authors and log to build this application. I also created 4 views (described below) to increase the processing done at the database level, and to return a concise result set to the Python application.
- The code itself consists of a module and a file:
    - logs_analysis.py: this module runs the Python application and returns a formatted report.
    - logs_analysisdb.py: this file consists of 3 functions that manage the SQL being pushed down and collects the result sets to be used by the application.
- I decided to create two code files to keep the SQL processing and formatting separate from each other, I found this made it simpler when thinking about how the database and application will communicate.

### How to run it
- First of all create the views described below within your database, so that the database is consistent with what I was using.
- Clone the logs_analysis.py and logs_analysisdb.py files into the same directory.
- From the command line, run the following and the report will be presented:

$ python logs_analysis.py

***

**Views**:
- log_slug
  - SQL: create view log_slug as select split_part(path, '/', 3) as slug, method, status from log;
  
- author_views
  - SQL: create view author_views as select name, num from authors join (select articles.author, count(log_slug.slug) as num from articles left join log_slug on articles.slug=log_slug.slug group by articles.author order by num desc) as a on authors.id=a.author;
  
- log_daily
  - SQL: create view log_daily as select date(time) as date, count(*) as requests from log group by date;
  
- log_daily_pct_error
  - SQL: create view log_daily_pct_error as select log_daily.date, requests, errors, (errors/requests::float)*100 as pct_error from log_daily join (select date(time) as date, count(*) as errors from log where status = '404 NOT FOUND' group by date) as a on log_daily.date=a.date;