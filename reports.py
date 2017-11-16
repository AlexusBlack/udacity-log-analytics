from tabulate import tabulate

def get_top3_articles(connection):
    connection.execute("select * from top3articles")
    articles = connection.fetchall()

    print(tabulate(articles, headers=["Id", "Title", "Author", "Views"]))


def get_top10_authors(connection):
    connection.execute("select * from top10authors")
    authors = connection.fetchall()

    print(tabulate(authors, headers=["Id", "Name", "Articles", "Views"]))
