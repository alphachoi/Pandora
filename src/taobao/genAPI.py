#encoding=utf-8
'''
Created on 2011-5-27

@author: LiuTao
'''
from config import Config
from pyquery import PyQuery as pyq
from string import Template
class genAPI(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def generation(self, tmp='method_tpl'):
      f = open(tmp, 'r')
      tpl = Template(f.read())
      f.close();        
      api_root = Config.get('api_doc_root')
        
      doc = pyq(url=api_root)
      t = doc('.api-button')      
      for i in t:
        api_url = Config.get('api_doc_url')
        doc_href = doc(i).attr('href')
        api_cat = doc_href[doc_href.index("#") + 1:]
        api_url = api_url + '?path=' + api_cat
        api_doc = pyq(url=api_url)   

        api_name = api_doc('h1')
        
        print "#------------------" + api_name.text() + "------------------------"
        api_desc = api_doc('.section:first')
        
        print "#", api_desc('div p').text()
        print
        api_list_sect = api_doc('.section:last')
        
        for ao in api_list_sect('tr'):
            api_methed = api_list_sect(ao)("a").text()
            methed = api_methed[7:].replace('.', '_')
            print tpl.substitute(methed_api=methed, methed=api_methed)        
        
if __name__ == '__main__':        
    gen = genAPI()
    gen.generation()

#            arr = api_methed.split('.')
            
#            print api_list_sect(ao)("a").text(), api_list_sect(ao)("td:last").text()

#    for sect in api_sect:
#        print sect.find('div/h2').text
#        print sect.find('div/div/')
#        print api_sect(sect)
# 
#    f = open('title.txt', 'a')
#
#        
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
