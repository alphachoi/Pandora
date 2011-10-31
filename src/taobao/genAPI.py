#encoding=utf-8
'''
Created on 2011-5-27

@author: LiuTao
'''
import config
import urllib
from string import Template
from HTMLParser import HTMLParser
import pickle




class APICatParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.isCat = False
        self.cat_list = []
        
        

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            # 判断标签<li>的属性
            for name, value in attrs:
                class_name = value.rstrip()
                if  class_name == 'APIgory-list' or class_name == 'APIgory-list focus':
                    self.isCat = True
                    
        if tag == 'a' and  self.isCat == True:
            self.cat = {}
            for name, value in attrs:
                if name == 'title':
                    print value,
                    self.cat['title'] = value
                if name == 'href':
                    print value
                    self.cat['href'] = value
                      
                    
    def handle_endtag(self, tag):
        if tag == 'p':
            self.isCat = False
            self.cat = None
#        将API分类写入文件    
        if tag == 'a' and  self.isCat == True and self.cat != None and len(self.cat) > 0:
            self.cat_list.append(self.cat)
            
    def persisCat(self):
#       API分类持久化文件        
        output = open('data.pkl', 'wb')
        pickle.dump(self.cat_list, output, -1)
        output.close()

            
            
class APIMethodParser(HTMLParser):
                
    def __init__(self):
        HTMLParser.__init__(self)
        self.api_block = 0
        self.api_name = False
        self.api_list = []
        self.api_item = {}
        
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            for name, value in attrs:
                class_name = value.rstrip()
                if  class_name == 'api-list':
                    self.api_block += 1
        if tag == 'a' and self.api_block == 2:
            for name, value in attrs:
                if name == 'title':
                    self.api_item['method'] = value
        if tag == 'span' and self.api_block == 2 and len(attrs) == 0:
            self.api_name = True
                    
    def handle_data(self, data):   
        if self.api_name == True:
            self.api_item['intro'] = data
            self.api_name = False
            self.api_list.append({'intro':data, 'method':self.api_item['method']})    
                    
                     
    def handle_endtag(self, tag):
        if tag == 'div' and self.api_block == 2:
            self.api_block = 0  
                                            
class genAPI(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        
    def generation(self, tmp='method_tpl'):
        
        pkl_file = open('data.pkl', 'rb')
        self.cat_list = pickle.load(pkl_file)
        pkl_file.close()

        for index in range(len(self.cat_list)):
            print index, self.cat_list[index]['title']
        print '-1 all'
        
        print 'input num to generation api:'
        num = input()        
        
        api = {}
        if (num == -1):
            for index in range(len(self.cat_list)):
                print '---------开始生成', self.cat_list[index]['title'], '----------'
                item = self.parser_api(self.cat_list[index]['href'])
                api[self.cat_list[index]['title']] = item 
                print '---------生成', self.cat_list[index]['title'], '完毕----------'               
        else:
            print '---------开始生成', self.cat_list[num]['title'], '----------'
            item = self.parser_api(self.cat_list[num]['href'])
            api[self.cat_list[num]['title']] = item 
            print '---------生成', self.cat_list[num]['title'], '完毕----------'
            
        output = open('api.pkl', 'wb')
        pickle.dump(api, output, -1)
        output.close()
            
    def showapi(self):
        pkl_file = open('api.pkl', 'rb')
        api = pickle.load(pkl_file)
        pkl_file.close()    
        
        for key in api:
            print "---------------------", key, "------------------------------"
            methods = api[key]
            for method in methods:
                print method['intro'], method['method']
                
    def genAPI(self):
        pkl_file = open('api.pkl', 'rb')
        api = pickle.load(pkl_file)
        pkl_file.close()    
  
        f = open('method_tpl', 'r')
        tpl = Template(f.read())
        f.close();         
        
        for key in api:
            print
            print "#---------------------", key, "------------------------------"
            print
            methods = api[key]
            for method in methods:
                api_method = method['method']        
                m = api_method[7:].replace('.', '_')
                print tpl.substitute(intro=method['intro'], method_api=m, method=api_method)                      
    
    def parser_api(self, url):
        content = unicode(urllib.urlopen(url).read())
        api_parser = APIMethodParser()
        api_parser.feed(content)
        api_parser.close()
        return api_parser.api_list
     
#      api_root = config['api_doc_root']
#        
#      doc = pyq(url=api_root)
#      t = doc('.link')      
#      for i in t:
#        print doc(i).text()
#        doc_href = doc(i).attr('href')
#        api_cat = doc_href[doc_href.index("#") + 1:]
#
#
#        api_doc = pyq(url=api_url)   
#
#        api_name = api_doc('h1')
#        
#        print "#------------------" + api_name.text() + "------------------------"
#        api_desc = api_doc('.section:first')
#        
#        print "#", api_desc('div p').text()
#        print
#        api_list_sect = api_doc('.section:last')
#        
#        for ao in api_list_sect('tr'):
#            api_methed = api_list_sect(ao)("a").text()
#            methed = api_methed[7:].replace('.', '_')
#            print tpl.substitute(methed_api=methed, methed=api_methed)        
        
if __name__ == '__main__':
    
    
#    parser = APICatParser()
#    content = unicode(urllib.urlopen(config.get('api_doc_root')).read())
#    parser.feed(content)   
#    parser.persisCat()
#    parser.close()
    
    api_parser = genAPI()
    api_parser.genAPI()
#    gen = genAPI()
#    api_parser.generation()

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
