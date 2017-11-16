def get_top3_articles(connection):
    connection.execute("select num, id, title from top3articles")
    articles = connection.fetchall()

    print("Views\t Id\t Title")
    print("--------------------------")
    for article in articles:
        views = str(article[0])
        article_id = str(article[1])
        title = article[2]
        print(views + "\t " + article_id + "\t " + title)

def get_top10_authors(connection):
    connection.execute("select * from top10authors")
    articles = connection.fetchall()

    print("Views\t Id\t Name")
    print("--------------------------")
    for article in articles:
        views = str(article[2])
        author_id = str(article[0])
        name = article[1]
        print(views + "\t " + author_id + "\t " + name)