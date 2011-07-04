#coding=utf-8
'''
Created on 2011-3-4

@author: LiuTao
'''
from taobao.api import API
    
if __name__ == '__main__':
    
    api = API('12207348', '8b463172d3c30c57162c22039b41f3b9')
    
    
    items = api.items_onsale_get(fields="email,nick,user_id,sex,birthday,type,consumer_protection,alipy_account,aplipy_no,avatar,sex", nick='正牌小忍')
    print items
#    item = api.item_get(fields="detail_url,num_iid,title,nick,type,desc,skus,props_name,created,promoted_service,is_lightning_consignment,cid,seller_cids,props,input_pids,input_str,pic_url,num,valid_thru,list_time,delist_time,stuff_status,location,price,post_fee,express_fee,has_discount,freight_payer,modified,approve_status,auction_point,score,volume", num_iid="9833495893")
#    print item
     
     


