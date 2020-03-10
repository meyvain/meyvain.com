#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Meytal Mitchell Vainstub'
SITENAME = 'Meytal Mitchell Vainstub'
SITEURL = ''
DESCRIPTION = 'Junior UX Research and Digital Anthropologist'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'theme'
DIRECT_TEMPLATES = ['index']
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False

STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
