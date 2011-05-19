#coding=utf-8
'''
Created on 2011-3-4

@author: LiuTao
'''
from datetime import datetime
from taobao.api import API
from taobao.Request import TaobaokeRequest
from pyquery import PyQuery as pyq
from util import sqlite_db
    
if __name__ == '__main__':
    
#    wei_bo = sqlite_db.WeiBo({"path":"db", "autocommit":True})
#    wei_bo.create_db()
#    wei_bo.setAccessToken({'uid':1, 'access_key':"2756ed2fea9e36f46fba2dd748f13872", 'access_secret':'0b142a1e8538729158a7f01f0aebeab4'})
#    token = wei_bo.getToken(1)
#    print token
#    wei_bo.setAccessToken({'uid':1, 'access_key':"2756ed", 'access_secret':'0b142a1e8538729158a7f01f0aebeab4'})
#    token = wei_bo.getToken(1)
#    print token    
#    param = {'c':2, 'b':5, 'v':'34', 'a':'xxxx'}
#    
#    ts = sorted(param.items(), key=lambda param:param[0])    
#    
#    print type(param)
#    print type(ts)
    
    api = API('12207348', '8b463172d3c30c57162c22039b41f3b9')
    
    item = api.item_get(fields="detail_url,num_iid,title,nick,type,cid,seller_cids,props,input_pids,input_str,desc,pic_url,num", num_iid="9833495893")

    print item
    
#    req.apiParas['fields'] = 'user_id,nick,seller_credit'
#    req.apiParas['nicks'] = 'hz0799,南古月'
#    
#    print top.execute(req)
#    print u'中国'.encode('utf-8')
    
#    api_root = 'http://my.open.taobao.com/apidoc/main.htm'
#    
#    doc = pyq(url=api_root)
#    t = doc('.api-button')
#    
#    for i in t:
#        api_url = 'http://my.open.taobao.com/apidoc/content.htm'
#        doc_href = doc(i).attr('href')
#        api_cat = doc_href[doc_href.index("#") + 1:]
#        api_url = api_url + '?path=' + api_cat
#        api_doc = pyq(url=api_url)   
#
#        api_name = api_doc('h1')
#        
#        print "------------------" + api_name.text() + "------------------------"
#        print
#        api_desc = api_doc('.section:first')
#        
#        print api_desc('div p').text()
#        print
#        api_list_sect = api_doc('.section:last')
#        
#        for ao in api_list_sect('tr'):
#            print api_list_sect(ao)("a").text(), api_list_sect(ao)("td:last").text()
#        print
#    for sect in api_sect:
#        print sect.find('div/h2').text
#        print sect.find('div/div/')
#        print api_sect(sect)
 
#    f = open('title.txt', 'a')

        
#        href = pyq(i).attr('href')
#        api_url = 'http://my.open.taobao.com/apidoc/index.htm#categoryId:1'
#        api_doc = pyq(url=api_url)
#        print api_doc
#        tables = api_doc('para_table')
#        for table in tables:
#            print table
#        f.write(title.encode('utf-8'))
#    f.close
#        for j in pyq(i).find('dd a'):
#                print pyq(j).text(),
#                print '\n'
