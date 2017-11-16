# udacity-log-analytics
Log analytics software for Udacity

## 3 Most viewed articles view

```sql
create view top3articles as
select articles.id, title, slug, count(articles.id) as num
from log join articles
on (log.path = concat('/article/', articles.slug)) 
where method = 'GET' and status = '200 OK'
group by articles.id
order by num desc
limit 3;
```