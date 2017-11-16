#!/usr/bin/python3
'''Log analyzer software for Udacity'''

import psycopg2
import reports


def main():
    ''' General logic for our log analyser, calls all of reports '''

    print("Starting log analysis")
    print("Requesting data")

    # Configuring connection
    database = psycopg2.connect("dbname=news")
    connection = database.cursor()

    # What are the most popular three articles of all time?
    print("\n\nTOP 3 MOST VIEWED ARTICLES")
    reports.show_top3_articles(connection)

    # Who are the most popular article authors of all time?
    print("\n\nTOP 10 AUTHORS")
    reports.show_top10_authors(connection)

    # Which authors wrote most articles?
    print("\n\nTOP 3 AUTHORS BY ARTICLE NUMBER")
    reports.show_authors_by_article_number(connection)

    # On which days did more than 1% of requests lead to errors?
    print("\n\nDAYS WITH MORE THEN 1% OF ERRORS")
    reports.show_worst_days_in_history(connection)

    print("\n\nEnd of report. Have a good day.")


main()
