'''
Created on 2011-3-16

@author: LiuTao
'''
import unittest
import sqlite3

from util.sqlite_db import *
from datetime import datetime

class SqliteDBTest(unittest.TestCase):


    def setUp(self):
        self.sqlite = SqliteDb(dict({'path':'sqlitedb.db'}))


    def tearDown(self):
        pass

    def testCreate(self):
        self.sqlite.excute('''create table user (
                id   integer primary key, 
                name varchar unique,
                pwd  varchar unique,
                register_time timestamp,
                update_time timestamp,
                type integer default 0
            )''')
        
    def testInsert(self):
        self.sqlite.excute("insert into user(id,name,pwd,register_time) values (:id,:name,:pwd,:register_time)",
                            {'id':1, 'name':'root', 'pwd':'ksdx12', 'register_time':datetime.now()})
        
#    def testDel(self):
#        self.sqlite.excute("drop table user")

    def testSelect(self):
        print self.sqlite.excute("select * from user")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
#    unittest.main()
    conn = sqlite3.connect('sqlitedb.db')
    c = conn.cursor()
    for t in [('IBM', 'ibm123'),
              ('MSOFT', 'msoft123'),
              ('HP', 'hp123'),
         ]:
        print type(t)
#        c.execute('insert into user(name,pwd) values (?,?)', t)

#    c.execute("insert into user(id,name,pwd,register_time) values (:id,:name,:pwd,:register_time)",
#                            {'id':1, 'name':'root', 'pwd':'ksdx12', 'register_time':datetime.now()})
    conn.commit()
    c.execute('select * from user')
    for row in c:
        print row

