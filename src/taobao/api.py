#encoding=utf-8
'''
Created on 2011-5-9

@author: LiuTao
'''
from binder import bind_api

class API(object):
    '''
    classdocs
    '''


    def __init__(self, key, secret, api_url='http://gw.api.taobao.com/router/rest', session_url='http://container.open.taobao.com/container', format="json", sign_method="md5", version="2.0"):
        '''
        Constructor
        '''
        self.app_key = '12207348'
        
        self.app_secret = '8b463172d3c30c57162c22039b41f3b9'
        
        self.gatewayUrl = api_url
        
        self.sessinkeyUrl = session_url
         
        self.format = format
        
        self.sign_method = sign_method
        
        self.api_version = version
        
    #
    item_get = bind_api(
        method='taobao.item.get'
    )
