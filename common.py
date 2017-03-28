import logging
import sys
import os

import atlassian
import zdesk


def setup_logging():
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)
setup_logging()


def get_conf_opt(name, default=None):
    try:
        return os.environ[name]
    except KeyError:
        if default is not None:
            return default
        raise Exception("{} env var must be set. See README.".format(name))


CONFLUENCE_URL = get_conf_opt('CONFLUENCE_URL')
CONFLUENCE_USER = get_conf_opt('CONFLUENCE_USER')
CONFLUENCE_PASSWORD = get_conf_opt('CONFLUENCE_PASSWORD')

CREATE_AS_DRAFT = (get_conf_opt('CREATE_AS_DRAFT', "0") == "1")

ZENDESK_URL = get_conf_opt('ZENDESK_URL')
ZENDESK_EMAIL = get_conf_opt('ZENDESK_EMAIL')
ZENDESK_PASSWORD = get_conf_opt('ZENDESK_PASSWORD')


def confluence():
    return atlassian.Confluence(CONFLUENCE_URL, CONFLUENCE_USER,
                                CONFLUENCE_PASSWORD)


def zendesk():
    return zdesk.Zendesk(ZENDESK_URL, ZENDESK_EMAIL, ZENDESK_PASSWORD)
