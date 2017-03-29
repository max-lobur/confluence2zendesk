#!/usr/bin/env python3
import sys
from common import zendesk


def search(text):
    results = zendesk().help_center_articles_search(query=text)['results']
    if not results:
        print("\nNothing found.")
    else:
        print("\nSearch results:\n")
    for r in results:
        print("{}; {}: {}".format(r['id'], r['title'], r['url']))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Usage: ./search.py 'text to search'")
    text = sys.argv[1]
    search(text)
