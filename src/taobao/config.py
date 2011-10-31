#encoding=utf-8
'''
Created on 2011-6-2

@author: LiuTao
'''
conf = {}
conf['api_url'] = 'http://gw.api.taobao.com/router/rest'
conf['setsession_url'] = 'http://container.open.taobao.com/container'
conf['identify_url'] = 'http://container.api.taobao.com/container/identify'
conf['api_doc_root'] = 'http://open.taobao.com/doc/api_cat_detail.htm?cat_id=1&category_id=102'
conf['api_doc_url'] = 'http://my.open.taobao.com/apidoc/content.htm'        
                         
def get(key):
        return conf[key]

if __name__ == '__main__':  
    
    print get('api_url')
#    print Config.get('session_url')
#    print Config.get('identify_url')
#    print base64.b64decode(urllib.unquote('aWZyYW1lPTEmdHM9MTMxMTc0MjYwNDY4MCZ2aXNpdG9yX2lkPTM5MDQ2ODEyJnZpc2l0b3Jfbmljaz3mraPniYzlsI%2Flv40%3D'))
