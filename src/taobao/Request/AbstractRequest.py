#encoding=utf-8
'''
Created on 2011-3-7

@author: LiuTao
'''

class AbstractRequest(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.apiParas = dict()

    def getApiMethodName(self):
        raise NotImplementedError("abstract")

    def getApiParam(self):
        return self.apiParas
