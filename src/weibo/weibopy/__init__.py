
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

"""
weibo API library
"""
__version__ = '1.5'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

from weibo.weibopy.models import Status, User, DirectMessage, Friendship, SavedSearch, SearchResult, ModelFactory, IDSModel
from weibo.weibopy.error import WeibopError
from weibo.weibopy.api import API
from weibo.weibopy.cache import Cache, MemoryCache, FileCache
from weibo.weibopy.auth import BasicAuthHandler, OAuthHandler
from weibo.weibopy.streaming import Stream, StreamListener
from weibo.weibopy.cursor import Cursor

# Global, unauthenticated instance of API
api = API()

def debug(enable=True, level=1):

    import httplib
    httplib.HTTPConnection.debuglevel = level

