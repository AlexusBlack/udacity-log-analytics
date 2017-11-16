#!/usr/bin/python3
'''Log analyzer software for Udacity'''

import psycopg2
import reports

def main():
    print("Starting log analysis")
    print("Requesting data")

    # Configuring connection
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    # What are the most popular three articles of all time?
    print("\n\nTOP 3 MOST VIEWED ARTICLES")
    reports.get_top3_articles(c)

    # Who are the most popular article authors of all time?
    print("\n\nTOP 10 AUTHORS")
    reports.get_top10_authors(c)

    # Which authors wrote most articles?
    print("\n\nTOP 3 AUTHORS BY ARTICLE NUMBER")
    reports.top_authors_by_article_number(c)

    # On which days did more than 1% of requests lead to errors?
    print("\n\nDAYS WITH MORE THEN 1% OF ERRORS")
    reports.worst_days_in_history(c)

    print("\n\n End of report. Have a good day.")

main()
