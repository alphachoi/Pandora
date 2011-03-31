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


class TopClient(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.app_key = '12207348'
        
        self.app_secrect = '8b463172d3c30c57162c22039b41f3b9'
        
        self.gatewayUrl = 'http://gw.api.taobao.com/router/rest'
        
        self.sessinkeyUrl = 'http://container.open.taobao.com/container'
         
        self.format = 'json'
        
        self.sign_method = 'md5'
        
        self.api_version = '2.0'
         
    def generateSign(self, param):
        
        param = sorted(param.items(), key=lambda param:param[0])      
        
        stringToBeSigned = self.app_secrect
        for (k, v) in param:
            stringToBeSigned = stringToBeSigned + k + v
            
        stringToBeSigned += self.app_secrect
        
        return hashlib.md5(stringToBeSigned).hexdigest().upper() 
    
    @staticmethod
    def __send(self, url, apiParams):
        
        postBodyString = urllib.urlencode(apiParams)
        try:       
            f = urllib2.urlopen(url, postBodyString)
        except urllib2.HTTPError, e:
            print e
        return f
        
    def execute(self, request, session=None):
        
        sysParams = dict()
        sysParams["app_key"] = self.app_key
        sysParams["v"] = self.api_version
        sysParams["format"] = self.format
        sysParams["sign_method"] = self.sign_method
        sysParams["method"] = request.getApiMethodName()
        sysParams["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        api_param = request.getApiParam()
        
        p = sysParams.copy()
        
        p.update(api_param)
        
        sysParams["sign"] = self.generateSign(p)
        
        sysParams = sorted(sysParams.items(), key=lambda sysParams:sysParams[0])   
        
        requestUrl = self.gatewayUrl + "?" + urllib.urlencode(sysParams)
        
        resp = self.__send(self, requestUrl, api_param)
        
        respWellFormed = False
        
        if self.format == 'json':
            respObject = json.load(resp)
            if respObject != None:
                respWellFormed = True
        
        if respWellFormed == False:
            print "format erro"
        else:
            if 'error_response' in respObject:
                print "erro code " + respObject['error_response']['msg']
            else:
                for (k, v) in respObject.iteritems():
                    return v

            
