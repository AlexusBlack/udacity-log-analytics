from tabulate import tabulate

def get_top3_articles(connection):
    request = '''
    select 
        articles.id, 
        title, 
        authors.name as author, 
        views
    from articles
        join articles_views on articles.id = articles_views.article
        join authors on articles.author = authors.id
    order by views desc
    limit 3;'''
    connection.execute(request)
    articles = connection.fetchall()

    print(tabulate(articles, headers=["Id", "Title", "Author", "Views"]))


def get_top10_authors(connection):
    request = '''
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
    limit 10;'''
    connection.execute(request)
    authors = connection.fetchall()

    print(tabulate(authors, headers=["Id", "Name", "Articles", "Views"]))

def top_authors_by_article_number(connection):
    request = '''
    select
        authors.id,
        authors.name,
        count(articles.id) as articles
    from articles
        join authors on articles.author = authors.id
    group by authors.id
    order by articles desc
    limit 3;'''
    connection.execute(request)
    authors = connection.fetchall()

    print(tabulate(authors, headers=["Id", "Name", "Articles"]))

def worst_days_in_history(connection):
    request = '''
    select 
        requests_by_day.day,
        requests_count,
        error_count,
        error_count::double precision / requests_count::double precision *100.0 as error_percent
    from requests_by_day
        join errors_by_day on requests_by_day.day = errors_by_day.day
    where (error_count::double precision / requests_count::double precision *100.0) > 1
    order by error_percent desc;'''
    connection.execute(request)
    days = connection.fetchall()

    print(tabulate(days, headers=["Day", "Requests", "Errors", "Percent"]))