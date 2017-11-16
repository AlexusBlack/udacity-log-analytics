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

### articles with views
```sql
create view articles_views as
select articles.id as article, count(articles.id) as views
from log join articles
on (log.path = concat('/article/', articles.slug)) 
where method = 'GET' and status = '200 OK'
group by article;
```

### 3 Most viewed articles view

```sql
create view top3articles as
  select 
    articles.id, 
    title, 
    authors.name as author, 
    views
  from articles
    join articles_views on articles.id = articles_views.article
    join authors on articles.author = authors.id
  order by views desc
  limit 3;
```

### 10 Best authors view
```sql
create view top10authors as
  select 
    authors.id, 
    authors.name, 
    count(articles.id) as articles, 
    sum(articles_views.views) as views
  from articles
    join articles_views on articles.id = articles_views.article
    join authors on articles.author = authors.id
  group by authors.id
  order by views desc
  limit 10;
```