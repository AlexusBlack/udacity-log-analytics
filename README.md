# Udacity Log Analytics
Log analytics software for Udacity

## Dependencies
- psycopg2
- tabulate

## How to run
Execute the command:
```
$ python3 analyze-log.py
```

## Views

This software uses some views from PostgreSQL database, make sure you have the views before using it.

### Articles with views
```sql
create view articles_views as
  select 
    articles.id as article, 
    count(articles.id) as views
  from log 
    join articles on (log.path = concat('/article/', articles.slug)) 
  where method = 'GET' and status = '200 OK'
  group by article;
```

### Requests by day
```sql
create view requests_by_day as
  select 
    date_trunc('day', time) as day, 
    count(log.id) as requests_count
  from log 
  group by day
  order by requests_count desc;
```

### Errors by day
```sql
create view errors_by_day as
  select 
    date_trunc('day', time) as day, 
    count(log.id) as error_count
  from log 
  where status != '200 OK'
  group by day
  order by error_count desc;
```