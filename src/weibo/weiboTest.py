'''
Created on 2011-3-22

@author: LiuTao
'''
from weibo.weibopy import auth
from weibo.weibopy.api import API  
from util import sqlite_db

if __name__ == '__main__':
    
    wei_bo = sqlite_db.WeiBo()
    wei_bo.create_db()
    
    wei_bo.setConsumerToken({'app_key':'168563670', 'app_secret':'f974cc11afd8cde62ff845d0860ceda2'})
    wei_bo.setAccessToken({'uid':1, 'access_key':"2756ed2fea9e36f46fba2dd748f13872", 'access_secret':'0b142a1e8538729158a7f01f0aebeab4'})
    
    access_token = wei_bo.getAccessToken(1)
    
    oauth_handler = auth.OAuthHandler()
    oauth_handler.set_access_token('2756ed2fea9e36f46fba2dd748f13872', '0b142a1e8538729158a7f01f0aebeab4')

    client = API(oauth_handler)
    
    timeline = client.friends_timeline()
    
    for status in timeline:
        print status.user.name + ":" + status.text
