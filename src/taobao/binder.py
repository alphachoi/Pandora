#encoding=utf-8
'''
Created on 2011-3-4

@author: LiuTao
'''
from datetime import datetime
import urllib
import urllib2
import hashlib
import json
def bind_api(**config):

    class APIMethod(object):
        '''
        classdocs
        '''
        method = config['method']
    
        def __init__(self, api, kargs):
            '''
            Constructor
            '''
            self.app_key = api.app_key
            
            self.app_secret = api.app_secret
            
            self.gatewayUrl = api.gatewayUrl
            
            self.sessinkeyUrl = api.sessinkeyUrl
             
            self.format = api.format
            
            self.sign_method = api.sign_method
            
            self.api_version = api.api_version
            
            self.param = kargs
            
            self.session = api.session
             
        def generateSign(self, p):
            
            
            param = sorted(p.items(), key=lambda p:p[0])      
            
            stringToBeSigned = self.app_secret
            for (k, v) in param:
                stringToBeSigned = stringToBeSigned + k + str(v)
                
            stringToBeSigned += self.app_secret
            
            return hashlib.md5(stringToBeSigned).hexdigest().upper() 
        
        @staticmethod
        def __send(self, url, apiParams):
            
            postBodyString = urllib.urlencode(apiParams)
            try:       
                f = urllib2.urlopen(url, postBodyString)
            except Exception as inst:
                print inst
                return None
            return f
            
        def execute(self):
            
            sysParams = dict()
            sysParams["app_key"] = self.app_key
            sysParams["v"] = self.api_version
            sysParams["format"] = self.format
            sysParams["sign_method"] = self.sign_method
            sysParams["method"] = self.method
            sysParams["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sysParams["session"] = self.session 
            
            api_param = self.param
            
            p = sysParams.copy()
            
            p.update(api_param)
            
            sysParams["sign"] = self.generateSign(p)
            
            sysParams = sorted(sysParams.items(), key=lambda sysParams:sysParams[0])   
            
            requestUrl = self.gatewayUrl + "?" + urllib.urlencode(sysParams)
            
            resp = self.__send(self, requestUrl, api_param)
            
            respWellFormed = False
            
            if(resp == None):
                return None
            
            if self.format == 'json':
                respObject = json.load(resp)
                if respObject != None:
                    respWellFormed = True
            
            if respWellFormed == False:
                print "format erro"
                return None
            else:
                if 'error_response' in respObject:
                    print respObject['error_response']['msg']
                    if 'code' in respObject['error_response']:
                        print respObject['error_response']['code']
                    return None
                else:
                    return respObject

    def _call(api, **kargs):
        method = APIMethod(api, kargs)
        return method.execute()      

    return _call
