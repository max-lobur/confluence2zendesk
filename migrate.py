#!/usr/bin/env python3
import sys
import json
from common import confluence, zendesk, CREATE_AS_DRAFT


def move(target_section_id, article_id):
    mode = "view"
    try:
        confl_article = confluence().get_page_by_id(
            article_id, expand="metadata.labels,body.{}".format(mode))
    except json.JSONDecodeError:
        print("Malformed server response. Debug with curl sample above.")
        exit(1)

    zd_article = {"article": {
        'title': confl_article['title'],
        'body': confl_article['body'][mode]['value'],
        # label_names only available on certain plans.
        'label_names': [l['name'] for l in
                        confl_article['metadata']['labels']['results']],
        'draft': CREATE_AS_DRAFT,
    }}
    zendesk().help_center_section_article_create(
        target_section_id, zd_article)


if __name__ == "__main__":
    try:
        assert len(sys.argv) == 3
        zendesk_sec_id = sys.argv[1]
        art_id = sys.argv[2]
    except AssertionError:
        print("Usage: ./migrate.py <target_zendesk_section_id> "
              "<confluence_article_id>")
        exit(1)

        move(zendesk_sec_id, art_id)
