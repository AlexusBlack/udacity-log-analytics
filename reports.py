def get_top3_articles(connection):
    connection.execute("select num, id, title from top3articles")
    articles = connection.fetchall()

    print("\n\nTOP 3 MOST VIEWED ARTICLES")
    print("Views\t Id\t Title")
    print("--------------------------")
    for article in articles:
        views = str(article[0])
        article_id = str(article[1])
        title = article[2]
        print(views + "\t " + article_id + "\t " + title)
