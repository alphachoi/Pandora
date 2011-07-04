#encoding=utf-8
'''
Created on 2011-6-2

@author: LiuTao
'''
import ConfigParser

class Config(object):
    '''
    classdocs
    '''
    

    def __init__(self, params):
        '''
        Constructor
        '''
    @staticmethod
    def set():
        config = ConfigParser.RawConfigParser()
        config.add_section('api')
        config.set('api', 'api_url', 'http://gw.api.taobao.com/router/rest')
        config.set('api', 'session_url', 'http://container.open.taobao.com/container')
        config.set('api', 'identify_url', 'http://container.api.taobao.com/container/identify')
        config.set('api', 'api_doc_root', 'http://my.open.taobao.com/apidoc/main.htm')
        config.set('api', 'api_doc_url', 'http://my.open.taobao.com/apidoc/content.htm')
        
        with open('taobao.cfg', 'wb') as configfile:
            config.write(configfile)
                
        
    @staticmethod    
    def get(key):
        config = ConfigParser.RawConfigParser()
        config.read('taobao.cfg')
        return config.get('api', key)

if __name__ == '__main__':  
    Config.set()
    print Config.get('identify_url')
