#!/usr/bin/python
#coding=gbk

'''
Created on Aug 2, 2010

@author: ting
'''

import unittest
from weibo.weibopy.auth import OAuthHandler, BasicAuthHandler
from weibo.weibopy.api import API

class Test(unittest.TestCase):
    
    consumer_key = "168563670"
    consumer_secret = "f974cc11afd8cde62ff845d0860ceda2"
    
    def __init__(self):
            """ constructor """
    
    def getAtt(self, key):
        try:
            return self.obj.__getattribute__(key)
        except Exception, e:
            print e
            return ''
        
    def getAttValue(self, obj, key):
        try:
            return obj.__getattribute__(key)
        except Exception, e:
            print e
            return ''
        
    def auth(self):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth_url = self.auth.get_authorization_url()
        print 'Please authorize: ' + auth_url
        verifier = raw_input('PIN: ').strip()
        self.auth.get_access_token(verifier)
        self.api = API(self.auth)
    def basicAuth(self, source, username, password):
        self.authType = 'basicauth'
        self.auth = BasicAuthHandler(username, password)
        self.api = API(self.auth, source=source)        
    def setToken(self, token, tokenSecret):
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.setToken(token, tokenSecret)
        self.api = API(self.auth)
    
    def friends_ids(self):
        fids = self.api.friends_ids()
        self.obj = fids
        ids = self.getAtt("ids")
        next_cursor = self.getAtt("next_cursor")
        previous_cursor = self.getAtt("previous_cursor")
        print "friends_ids---" + str(ids) + ":next_cursor" + str(next_cursor) + ":previous_cursor" + str(previous_cursor)
        
    def followers_ids(self):
        fids = self.api.followers_ids()
        self.obj = fids
        ids = self.getAtt("ids")
        next_cursor = self.getAtt("next_cursor")
        previous_cursor = self.getAtt("previous_cursor")
        print "followers_ids---" + str(ids) + ":next_cursor" + str(next_cursor) + ":previous_cursor" + str(previous_cursor)
        
test = Test()
#AccessToken的 key和Secret
test.setToken("2756ed2fea9e36f46fba2dd748f13872", "0b142a1e8538729158a7f01f0aebeab4")
test.friends_ids()
test.followers_ids()

