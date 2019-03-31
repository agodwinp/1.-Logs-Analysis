# 1.-Logs-Analysis
Project 1 for Udacity FSND

Views:
- log_slug
  - SQL: create view log_slug as select split_part(path, '/', 3) as slug, method, status from log;
  
- author_views
  - SQL: create view author_views as select articles.author, count(log_slug.slug) as num from articles left join log_slug on articles.slug=log_slug.slug group by articles.author order by num desc;
