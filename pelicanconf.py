#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#
# About the site
#
AUTHOR = u'DataLad Team'
SITENAME = u'DataLad'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'
LOCALE = u'en_US.UTF-8'

#
# Configure Pelican a bit
#
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'better_tables', 'headerid', 'sitemap' ]
SITEMAP = { 'format': 'xml' }

THEME = 'theme/'

# Disable all feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

HEADERID_LINK_CHAR = '&#xe805;'

#
# Configure the site
#
STATIC_PATHS = ['asciicast', 'css', 'js', 'img', 'badges']
MENUITEMS = [ ('About', '/about.html', None),
              ('Integrations', '/integrations.html', None),
              ('Get DataLad', 'http://handbook.datalad.org/r.html?install', '_blank'),
              ('Features', 'http://handbook.datalad.org/r.html?about', '_blank'),
              ('Datasets', '/datasets.html', None),
              ('Development', '/development.html', None),
              ('User Handbook', 'http://handbook.datalad.org', '_blank'),
              ('Developer Docs', 'http://docs.datalad.org', '_blank'),
]
DEFAULT_PAGINATION = False

# We prefer document-relative URLs
RELATIVE_URLS = True
