# 1.-Logs-Analysis
Project 1 for Udacity FSND

Views:
- log_slug
SQL:create view log_slug as select split_part(path, '/', 3) as slug, method, status from log;
