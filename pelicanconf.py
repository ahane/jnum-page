#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alec Hanefeld'
SITENAME = u'juicy numbers'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'de'

THEME = u'../pelican-bootstrap3'
BOOTSTRAP_THEME = 'paper'
SITELOGO = 'images/jn-logo.png'
HIDE_SITENAME = True
HIDE_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = False
HIDE_ARCHIVE = True

# Tell Pelican to add 'extra/custom.css' to the output dir
STATIC_PATHS = ['extra/custom.css', 'images/']

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'}
}

CUSTOM_CSS = 'static/custom.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
