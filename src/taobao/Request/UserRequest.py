#encoding=utf-8
'''
Created on 2011-3-7

@author: LiuTao
'''
import AbstractRequest

#获取单个用户信息
class getUserReq(AbstractRequest.AbstractRequest):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(getUserReq, self).__init__()
        
    def getApiMethodName(self):
        return "taobao.user.get"

#获取多个用户信息    
class getUsersReq(AbstractRequest.AbstractRequest):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(getUsersReq, self).__init__()
        
    def getApiMethodName(self):
        return "taobao.users.get"
