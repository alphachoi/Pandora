#encoding=utf-8
'''
Created on 2011-3-16

@author: LiuTao
'''
import sqlite3

class SqliteDb(object):
    '''
    classdocs
    '''


    def __init__(self, db_config):
        '''
        Constructor
        '''
        self.conn = sqlite3.connect(db_config['path'])
        self.conn.row_factory = sqlite3.Row
        
        if(db_config['autocommit'] == True):
            self.conn.isolation_level = None
        
    def excute(self, sql, param=None):
        cursor = self.conn.cursor()
        if param != None:
            cursor.execute(sql, param)
        else:
            cursor.execute(sql)
        if sql.lstrip().upper().startswith("SELECT"):
            return cursor.fetchall()
            
class WeiBo(SqliteDb):
    '''
                微薄数据库模块
    '''
    def _init_(self, db_config):
        
        super(WeiBo, self)._init(db_config)
        
    '''初始化微薄模块数据库表'''
    def create_db(self):
        
        self.excute("drop table if exists wb_config")
        self.excute("create table wb_config (app_key string UNIQUE, app_secret string)")
 
        self.excute("drop table if exists wb_user")
        self.excute("create table wb_user (uid integer UNIQUE , access_key string , access_secret string)")
     
    '''设置oauth的consumer_token,具体含义见新浪微薄相关文档'''
    def setConsumerToken(self, token):
        
        self.excute("replace into wb_config(app_key,app_secret) values(:app_key,:app_secret)", token)
    
    '''获取access-token'''
    def getConsumerToken(self):
        
        return self.excute("select * from wb_config")        
    
    '''设置oauth的access-token,具体含义见新浪微薄相关文档'''
    def setAccessToken(self, token):
        
        self.excute("replace into wb_user(uid,access_key,access_secret) values(:uid,:access_key,:access_secret)", token)
    
    '''获取access-token'''
    def getAccessToken(self, uid):
        
        return self.excute("select access_key,access_secret from wb_user where uid=:uid", {'uid':uid})
