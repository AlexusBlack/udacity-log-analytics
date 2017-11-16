# Udacity Log Analytics
Log analytics software for Udacity. This version supports 4 types of reports:
- Three most popular articles of all time
- Ten most popular article authors of all time
- Three authors who wrote most articles
- Days with more than 1% of requests lead to errors

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

## Report example
```
Starting log analysis
Requesting data


TOP 3 MOST VIEWED ARTICLES
  Id  Title                             Author                    Views
----  --------------------------------  ----------------------  -------
  26  Candidate is jerk, alleges rival  Rudolf von Treppenwitz   338647
  25  Bears love berries, alleges bear  Ursula La Multa          253801
  23  Bad things gone, say good people  Anonymous Contributor    170098


TOP 10 AUTHORS
  Id  Name                      Articles    Views
----  ----------------------  ----------  -------
   1  Ursula La Multa                  4   507594
   2  Rudolf von Treppenwitz           2   423457
   3  Anonymous Contributor            1   170098
   4  Markoff Chaney                   1    84557


TOP 3 AUTHORS BY ARTICLE NUMBER
  Id  Name                      Articles
----  ----------------------  ----------
   1  Ursula La Multa                  4
   2  Rudolf von Treppenwitz           2
   3  Anonymous Contributor            1


DAYS WITH MORE THEN 1% OF ERRORS
Day                          Requests    Errors    Percent
-------------------------  ----------  --------  ---------
2016-07-17 00:00:00+00:00       55907      1265    2.26269


 End of report. Have a good day.
```