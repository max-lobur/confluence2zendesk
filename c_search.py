#!/usr/bin/env python3
import sys
from common import confluence, CONFLUENCE_URL


def search(text):
    url = "/rest/api/content/search?cql=title~'{0}' or text~'{0}'".format(text)
    results = confluence().get(url)['results']
    if not results:
        print("\nNothing found.")
    else:
        print("\nSearch results:\n")
    for r in results:
        print("{}; {}: {}{}".format(r['id'], r['title'],
                                    CONFLUENCE_URL, r['_links']['webui']))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Usage: ./c_search.py 'text to search'")
    text = sys.argv[1]
    search(text)
