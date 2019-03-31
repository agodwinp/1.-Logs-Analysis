# 1.-Logs-Analysis
Project 1 for Udacity FSND

Views:
- log_slug
  - SQL: create view log_slug as select split_part(path, '/', 3) as slug, method, status from log;
  
- author_views
  - SQL: create view author_views as select name, num from authors join (select articles.author, count(log_slug.slug) as num from articles left join log_slug on articles.slug=log_slug.slug group by articles.author order by num desc) as a on authors.id=a.author;
  
- log_daily
  - SQL: create view log_daily as select date(time) as date, count(*) as requests from log group by date;
  
- log_daily_pct_error
  - SQL: create view log_daily_pct_error as select log_daily.date, requests, errors, (errors/requests::float)*100 as pct_error from log_daily join (select date(time) as date, count(*) as errors from log where status = '404 NOT FOUND' group by date) as a on log_daily.date=a.date;
