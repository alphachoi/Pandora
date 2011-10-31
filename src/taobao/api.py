#encoding=utf-8
'''
Created on 2011-5-9

@author: LiuTao
'''
from binder import bind_api
import config

class API(object):
    '''
    classdocs
    '''


    def __init__(self, key, secret, api_url=config.get('api_url'), session_url=config.get('session_url'), format="json", sign_method="md5", version="2.0"):
        '''
        Constructor
        '''
        self.app_key = key
        
        self.app_secret = secret
        
        self.gatewayUrl = api_url
        
        self.sessinkeyUrl = session_url
         
        self.format = format
        
        self.sign_method = sign_method
        
        self.api_version = version
        
        self.session = ""
        


#--------------------- 掌柜说API ------------------------------

    #判断是否是粉丝
    jianghu_fan_check = bind_api(
        method='taobao.jianghu.fan.check'
    )
    #关注一个掌柜说
    jianghu_fan_follow = bind_api(
        method='taobao.jianghu.fan.follow'
    )

#--------------------- 物流宝API ------------------------------

    #查询库存详情
    wlb_inventory_detail_get = bind_api(
        method='taobao.wlb.inventory.detail.get'
    )
    #库存同步
    wlb_inventory_sync = bind_api(
        method='taobao.wlb.inventory.sync'
    )
    #根据商品ID查询所有库存变更记录
    wlb_inventorylog_query = bind_api(
        method='taobao.wlb.inventorylog.query'
    )
    #添加单个物流宝商品
    wlb_item_add = bind_api(
        method='taobao.wlb.item.add'
    )
    #添加商品授权规则
    wlb_item_authorization_add = bind_api(
        method='taobao.wlb.item.authorization.add'
    )
    #删除授权关系
    wlb_item_authorization_delete = bind_api(
        method='taobao.wlb.item.authorization.delete'
    )
    #查询授权关系
    wlb_item_authorization_query = bind_api(
        method='taobao.wlb.item.authorization.query'
    )
    #创建商品组合关系
    wlb_item_combination_create = bind_api(
        method='taobao.wlb.item.combination.create'
    )
    #删除商品组合关系
    wlb_item_combination_delete = bind_api(
        method='taobao.wlb.item.combination.delete'
    )
    #根据商品id查询商品组合关系
    wlb_item_combination_get = bind_api(
        method='taobao.wlb.item.combination.get'
    )
    #创建商品的代销关系
    wlb_item_consignment_create = bind_api(
        method='taobao.wlb.item.consignment.create'
    )
    #删除商品的代销关系
    wlb_item_consignment_delete = bind_api(
        method='taobao.wlb.item.consignment.delete'
    )
    #分页查询物流宝商品的代销关系
    wlb_item_consignment_page_get = bind_api(
        method='taobao.wlb.item.consignment.page.get'
    )
    #查询可代销的物流宝商品
    wlb_item_consignment_query = bind_api(
        method='taobao.wlb.item.consignment.query'
    )
    #商品删除
    wlb_item_delete = bind_api(
        method='taobao.wlb.item.delete'
    )
    #根据商品ID获取商品信息
    wlb_item_get = bind_api(
        method='taobao.wlb.item.get'
    )
    #根据物流宝商品ID查询商品映射关系
    wlb_item_map_get = bind_api(
        method='taobao.wlb.item.map.get'
    )
    #根据外部实体查询映射的物流宝商品id
    wlb_item_map_get_by_extentity = bind_api(
        method='taobao.wlb.item.map.get.by.extentity'
    )
    #分页查询商品
    wlb_item_query = bind_api(
        method='taobao.wlb.item.query'
    )
    #商品映射同步
    wlb_item_synchronize = bind_api(
        method='taobao.wlb.item.synchronize'
    )
    #删除商品映射同步
    wlb_item_synchronize_delete = bind_api(
        method='taobao.wlb.item.synchronize.delete'
    )
    #物流宝商品修改
    wlb_item_update = bind_api(
        method='taobao.wlb.item.update'
    )
    #物流宝通知消息确认
    wlb_notify_message_confirm = bind_api(
        method='taobao.wlb.notify.message.confirm'
    )
    #物流宝通知消息查询接口
    wlb_notify_message_page_get = bind_api(
        method='taobao.wlb.notify.message.page.get'
    )
    #取消物流宝订单
    wlb_order_cancel = bind_api(
        method='taobao.wlb.order.cancel'
    )
    #物流宝订单已发货通知接口
    wlb_order_consign = bind_api(
        method='taobao.wlb.order.consign'
    )
    #创建物流宝订单
    wlb_order_create = bind_api(
        method='taobao.wlb.order.create'
    )
    #分页查询物流宝订单
    wlb_order_page_get = bind_api(
        method='taobao.wlb.order.page.get'
    )
    #新增物流宝订单调度规则
    wlb_order_schedule_rule_add = bind_api(
        method='taobao.wlb.order.schedule.rule.add'
    )
    #修改订单调度规则
    wlb_order_schedule_rule_update = bind_api(
        method='taobao.wlb.order.schedule.rule.update'
    )
    #分页查询物流宝订单商品详情
    wlb_orderitem_page_get = bind_api(
        method='taobao.wlb.orderitem.page.get'
    )
    #删除订单调度规则
    wlb_orderschedulerule_delete = bind_api(
        method='taobao.wlb.orderschedulerule.delete'
    )
    #查询某个卖家的所有订单调度规则
    wlb_orderschedulerule_query = bind_api(
        method='taobao.wlb.orderschedulerule.query'
    )
    #物流宝订单流转状态查询
    wlb_orderstatus_get = bind_api(
        method='taobao.wlb.orderstatus.get'
    )
    #补货统计查询
    wlb_replenish_statistics = bind_api(
        method='taobao.wlb.replenish.statistics'
    )
    #查询商家定购的所有服务
    wlb_subscription_query = bind_api(
        method='taobao.wlb.subscription.query'
    )
    #通过物流订单编号查询物流信息
    wlb_tmsorder_query = bind_api(
        method='taobao.wlb.tmsorder.query'
    )
    #根据交易号获取物流宝订单
    wlb_tradeorder_get = bind_api(
        method='taobao.wlb.tradeorder.get'
    )
    #根据物流宝订单编号查询物流宝订单概要信息
    wlb_wlborder_get = bind_api(
        method='taobao.wlb.wlborder.get'
    )

#--------------------- 淘客API ------------------------------

    #淘宝客类目推广URL
    taobaoke_caturl_get = bind_api(
        method='taobao.taobaoke.caturl.get'
    )
    #淘客商品转换
    taobaoke_items_convert = bind_api(
        method='taobao.taobaoke.items.convert'
    )
    #查询淘宝客推广商品详细信息
    taobaoke_items_detail_get = bind_api(
        method='taobao.taobaoke.items.detail.get'
    )
    #查询淘宝客推广商品
    taobaoke_items_get = bind_api(
        method='taobao.taobaoke.items.get'
    )
    #淘宝客关键词搜索URL
    taobaoke_listurl_get = bind_api(
        method='taobao.taobaoke.listurl.get'
    )
    #淘宝客报表查询
    taobaoke_report_get = bind_api(
        method='taobao.taobaoke.report.get'
    )
    #淘客店铺转换
    taobaoke_shops_convert = bind_api(
        method='taobao.taobaoke.shops.convert'
    )
    #淘宝客店铺搜索
    taobaoke_shops_get = bind_api(
        method='taobao.taobaoke.shops.get'
    )
    #工具联盟注册校验
    taobaoke_tool_relation = bind_api(
        method='taobao.taobaoke.tool.relation'
    )
    #虚拟卡查询
    taobaoke_virtualcard_get = bind_api(
        method='taobao.taobaoke.virtualcard.get'
    )

#--------------------- 评价API ------------------------------

    #新增单个评价
    traderate_add = bind_api(
        method='taobao.traderate.add'
    )
    #针对父子订单新增批量评价
    traderate_list_add = bind_api(
        method='taobao.traderate.list.add'
    )
    #搜索评价信息
    traderates_get = bind_api(
        method='taobao.traderates.get'
    )
    #商品评价查询接口
    traderates_search = bind_api(
        method='taobao.traderates.search'
    )

#--------------------- 营销API ------------------------------

    #定向优惠活动名称与描述违禁词检查
    marketing_promotion_kfc = bind_api(
        method='taobao.marketing.promotion.kfc'
    )
    #查询商品定向优惠策略
    marketing_promotions_get = bind_api(
        method='taobao.marketing.promotions.get'
    )
    #查询人群标签
    marketing_tags_get = bind_api(
        method='taobao.marketing.tags.get'
    )
    #查询某个卖家的店铺优惠券领取活动
    promotion_activity_get = bind_api(
        method='taobao.promotion.activity.get'
    )
    #买家查询当前所有优惠券信息
    promotion_coupon_buyer_search = bind_api(
        method='taobao.promotion.coupon.buyer.search'
    )
    #通过接口可以查询某个店铺优惠券的买家详细信息
    promotion_coupondetail_get = bind_api(
        method='taobao.promotion.coupondetail.get'
    )
    #查询卖家优惠券
    promotion_coupons_get = bind_api(
        method='taobao.promotion.coupons.get'
    )
    #限时打折详情查询
    promotion_limitdiscount_detail_get = bind_api(
        method='taobao.promotion.limitdiscount.detail.get'
    )
    #限时打折查询
    promotion_limitdiscount_get = bind_api(
        method='taobao.promotion.limitdiscount.get'
    )
    #搭配套餐查询
    promotion_meal_get = bind_api(
        method='taobao.promotion.meal.get'
    )

#--------------------- 信息安全API ------------------------------

    #关键词过滤匹配
    kfc_keyword_search = bind_api(
        method='taobao.kfc.keyword.search'
    )

#--------------------- 物流API ------------------------------

    #查询地址区域
    areas_get = bind_api(
        method='taobao.areas.get'
    )
    #新增运费模板
    delivery_template_add = bind_api(
        method='taobao.delivery.template.add'
    )
    #删除运费模板
    delivery_template_delete = bind_api(
        method='taobao.delivery.template.delete'
    )
    #获取用户指定运费模板信息
    delivery_template_get = bind_api(
        method='taobao.delivery.template.get'
    )
    #修改运费模板
    delivery_template_update = bind_api(
        method='taobao.delivery.template.update'
    )
    #获取用户下所有模板
    delivery_templates_get = bind_api(
        method='taobao.delivery.templates.get'
    )
    #卖家地址库新增接口
    logistics_address_add = bind_api(
        method='taobao.logistics.address.add'
    )
    #卖家地址库修改
    logistics_address_modify = bind_api(
        method='taobao.logistics.address.modify'
    )
    #删除卖家地址库
    logistics_address_remove = bind_api(
        method='taobao.logistics.address.remove'
    )
    #查询卖家地址库
    logistics_address_search = bind_api(
        method='taobao.logistics.address.search'
    )
    #查询物流公司信息
    logistics_companies_get = bind_api(
        method='taobao.logistics.companies.get'
    )
    #无需物流（虚拟）发货处理
    logistics_dummy_send = bind_api(
        method='taobao.logistics.dummy.send'
    )
    #自己联系物流（线下物流）发货
    logistics_offline_send = bind_api(
        method='taobao.logistics.offline.send'
    )
    #取消物流订单接口
    logistics_online_cancel = bind_api(
        method='taobao.logistics.online.cancel'
    )
    #确认发货通知接口
    logistics_online_confirm = bind_api(
        method='taobao.logistics.online.confirm'
    )
    #在线订单发货处理（支持货到付款）
    logistics_online_send = bind_api(
        method='taobao.logistics.online.send'
    )
    #批量查询物流订单,返回详细信息
    logistics_orders_detail_get = bind_api(
        method='taobao.logistics.orders.detail.get'
    )
    #批量查询物流订单
    logistics_orders_get = bind_api(
        method='taobao.logistics.orders.get'
    )
    #查询支持起始地到目的地范围的物流公司
    logistics_partners_get = bind_api(
        method='taobao.logistics.partners.get'
    )
    #物流流转信息查询
    logistics_trace_search = bind_api(
        method='taobao.logistics.trace.search'
    )
    #添加邮费模板
    postage_add = bind_api(
        method='taobao.postage.add'
    )
    #删除单个运费模板
    postage_delete = bind_api(
        method='taobao.postage.delete'
    )
    #获取单个运费模板
    postage_get = bind_api(
        method='taobao.postage.get'
    )
    #修改邮费模板
    postage_update = bind_api(
        method='taobao.postage.update'
    )
    #获取卖家的运费模板
    postages_get = bind_api(
        method='taobao.postages.get'
    )
    #异步批量物流发货api
    topats_delivery_send = bind_api(
        method='taobao.topats.delivery.send'
    )

#--------------------- 在线订购API ------------------------------

    #订单记录导出
    vas_order_search = bind_api(
        method='taobao.vas.order.search'
    )
    #订购记录导出
    vas_subsc_search = bind_api(
        method='taobao.vas.subsc.search'
    )
    #订购关系查询
    vas_subscribe_get = bind_api(
        method='taobao.vas.subscribe.get'
    )

#--------------------- 交易API ------------------------------

    #获取异步任务结果
    topats_result_get = bind_api(
        method='taobao.topats.result.get'
    )
    #异步获取淘宝卖家绑定的支付宝账户的财务明细
    topats_trade_accountreport_get = bind_api(
        method='taobao.topats.trade.accountreport.get'
    )
    #异步批量获取交易订单详情api
    topats_trades_fullinfo_get = bind_api(
        method='taobao.topats.trades.fullinfo.get'
    )
    #交易订单帐务查询
    trade_amount_get = bind_api(
        method='taobao.trade.amount.get'
    )
    #卖家关闭一笔交易
    trade_close = bind_api(
        method='taobao.trade.close'
    )
    #获取交易确认收货费用
    trade_confirmfee_get = bind_api(
        method='taobao.trade.confirmfee.get'
    )
    #获取单笔交易的详细信息
    trade_fullinfo_get = bind_api(
        method='taobao.trade.fullinfo.get'
    )
    #获取单笔交易的部分信息(性能高)
    trade_get = bind_api(
        method='taobao.trade.get'
    )
    #对一笔交易添加备注
    trade_memo_add = bind_api(
        method='taobao.trade.memo.add'
    )
    #修改一笔交易备注
    trade_memo_update = bind_api(
        method='taobao.trade.memo.update'
    )
    #更新交易订单的销售属性
    trade_ordersku_update = bind_api(
        method='taobao.trade.ordersku.update'
    )
    #修改订单邮费价格
    trade_postage_update = bind_api(
        method='taobao.trade.postage.update'
    )
    #延长交易收货时间
    trade_receivetime_delay = bind_api(
        method='taobao.trade.receivetime.delay'
    )
    #更改交易的收货地址
    trade_shippingaddress_update = bind_api(
        method='taobao.trade.shippingaddress.update'
    )
    #交易快照查询
    trade_snapshot_get = bind_api(
        method='taobao.trade.snapshot.get'
    )
    #搜索当前会话用户作为买家达成的交易记录
    trades_bought_get = bind_api(
        method='taobao.trades.bought.get'
    )
    #搜索当前会话用户作为卖家已卖出的交易数据
    trades_sold_get = bind_api(
        method='taobao.trades.sold.get'
    )
    #搜索当前会话用户作为卖家已卖出的增量交易数据
    trades_sold_increment_get = bind_api(
        method='taobao.trades.sold.increment.get'
    )

#--------------------- 淘画报API ------------------------------

    #获取指定画报列表
    poster_appointedposters_get = bind_api(
        method='taobao.poster.appointedposters.get'
    )
    #根据频道ID获取频道信息
    poster_channel_get = bind_api(
        method='taobao.poster.channel.get'
    )
    #获取画报所有频道
    poster_channels_get = bind_api(
        method='taobao.poster.channels.get'
    )
    #根据画报ID获取商品
    poster_postauctions_get = bind_api(
        method='taobao.poster.postauctions.get'
    )
    #获取画报详情
    poster_posterdetail_get = bind_api(
        method='taobao.poster.posterdetail.get'
    )
    #获取指定频道Id的画报列表
    poster_posters_get = bind_api(
        method='taobao.poster.posters.get'
    )
    #搜索画报
    poster_posters_search = bind_api(
        method='taobao.poster.posters.search'
    )

#--------------------- 商品API ------------------------------

    #查询用户售后服务模板
    aftersale_get = bind_api(
        method='taobao.aftersale.get'
    )
    #添加一个商品
    item_add = bind_api(
        method='taobao.item.add'
    )
    #删除单条商品
    item_delete = bind_api(
        method='taobao.item.delete'
    )
    #得到单个商品信息
    item_get = bind_api(
        method='taobao.item.get'
    )
    #删除商品图片
    item_img_delete = bind_api(
        method='taobao.item.img.delete'
    )
    #添加商品图片
    item_img_upload = bind_api(
        method='taobao.item.img.upload'
    )
    #商品关联子图
    item_joint_img = bind_api(
        method='taobao.item.joint.img'
    )
    #商品关联属性图
    item_joint_propimg = bind_api(
        method='taobao.item.joint.propimg'
    )
    #更新商品价格
    item_price_update = bind_api(
        method='taobao.item.price.update'
    )
    #删除属性图片
    item_propimg_delete = bind_api(
        method='taobao.item.propimg.delete'
    )
    #添加或修改属性图片
    item_propimg_upload = bind_api(
        method='taobao.item.propimg.upload'
    )
    #宝贝/SKU库存修改
    item_quantity_update = bind_api(
        method='taobao.item.quantity.update'
    )
    #橱窗推荐一个商品
    item_recommend_add = bind_api(
        method='taobao.item.recommend.add'
    )
    #取消橱窗推荐一个商品
    item_recommend_delete = bind_api(
        method='taobao.item.recommend.delete'
    )
    #添加SKU
    item_sku_add = bind_api(
        method='taobao.item.sku.add'
    )
    #删除SKU
    item_sku_delete = bind_api(
        method='taobao.item.sku.delete'
    )
    #获取SKU
    item_sku_get = bind_api(
        method='taobao.item.sku.get'
    )
    #更新商品SKU的价格
    item_sku_price_update = bind_api(
        method='taobao.item.sku.price.update'
    )
    #更新SKU信息
    item_sku_update = bind_api(
        method='taobao.item.sku.update'
    )
    #根据商品ID列表获取SKU信息
    item_skus_get = bind_api(
        method='taobao.item.skus.get'
    )
    #获取用户宝贝详情页模板名称
    item_templates_get = bind_api(
        method='taobao.item.templates.get'
    )
    #更新商品信息
    item_update = bind_api(
        method='taobao.item.update'
    )
    #商品下架
    item_update_delisting = bind_api(
        method='taobao.item.update.delisting'
    )
    #一口价商品上架
    item_update_listing = bind_api(
        method='taobao.item.update.listing'
    )
    #根据外部ID取商品
    items_custom_get = bind_api(
        method='taobao.items.custom.get'
    )
    #搜索商品信息
    items_get = bind_api(
        method='taobao.items.get'
    )
    #得到当前会话用户库存中的商品列表
    items_inventory_get = bind_api(
        method='taobao.items.inventory.get'
    )
    #批量获取商品信息
    items_list_get = bind_api(
        method='taobao.items.list.get'
    )
    #获取当前会话用户出售中的商品列表
    items_onsale_get = bind_api(
        method='taobao.items.onsale.get'
    )
    #搜索商品信息
    items_search = bind_api(
        method='taobao.items.search'
    )
    #上传一个产品，不包括产品非主图和属性图片
    product_add = bind_api(
        method='taobao.product.add'
    )
    #获取一个产品的信息
    product_get = bind_api(
        method='taobao.product.get'
    )
    #删除产品非主图
    product_img_delete = bind_api(
        method='taobao.product.img.delete'
    )
    #上传单张产品非主图，如果需要传多张，可调多次
    product_img_upload = bind_api(
        method='taobao.product.img.upload'
    )
    #删除产品属性图
    product_propimg_delete = bind_api(
        method='taobao.product.propimg.delete'
    )
    #上传单张产品属性图片，如果需要传多张，可调多次
    product_propimg_upload = bind_api(
        method='taobao.product.propimg.upload'
    )
    #修改一个产品，可以修改主图，不能修改子图片
    product_update = bind_api(
        method='taobao.product.update'
    )
    #获取产品列表
    products_get = bind_api(
        method='taobao.products.get'
    )
    #搜索产品信息
    products_search = bind_api(
        method='taobao.products.search'
    )
    #根据外部ID取商品SKU
    skus_custom_get = bind_api(
        method='taobao.skus.custom.get'
    )

#--------------------- 收藏夹API ------------------------------

    #添加收藏夹
    favorite_add = bind_api(
        method='taobao.favorite.add'
    )
    #查询
    favorite_search = bind_api(
        method='taobao.favorite.search'
    )

#--------------------- 退款API ------------------------------

    #单笔退款详情
    refund_get = bind_api(
        method='taobao.refund.get'
    )
    #创建退款留言/凭证
    refund_message_add = bind_api(
        method='taobao.refund.message.add'
    )
    #退款留言/凭证列表查询
    refund_messages_get = bind_api(
        method='taobao.refund.messages.get'
    )
    #卖家拒绝退款
    refund_refuse = bind_api(
        method='taobao.refund.refuse'
    )
    #查询买家申请的退款列表
    refunds_apply_get = bind_api(
        method='taobao.refunds.apply.get'
    )
    #查询卖家收到的退款列表
    refunds_receive_get = bind_api(
        method='taobao.refunds.receive.get'
    )

#--------------------- 系统时间API ------------------------------


#--------------------- 旺旺API ------------------------------

    #平均等待时长
    wangwang_eservice_avgwaittime_get = bind_api(
        method='taobao.wangwang.eservice.avgwaittime.get'
    )
    #获取具体的聊天记录
    wangwang_eservice_chatlog_get = bind_api(
        method='taobao.wangwang.eservice.chatlog.get'
    )
    #获取聊天对象列表，查询时间段
    wangwang_eservice_chatpeers_get = bind_api(
        method='taobao.wangwang.eservice.chatpeers.get'
    )
    #聊天记录查询
    wangwang_eservice_chatrecord_get = bind_api(
        method='taobao.wangwang.eservice.chatrecord.get'
    )
    #获取评价详细
    wangwang_eservice_evals_get = bind_api(
        method='taobao.wangwang.eservice.evals.get'
    )
    #客服评价统计
    wangwang_eservice_evaluation_get = bind_api(
        method='taobao.wangwang.eservice.evaluation.get'
    )
    #获取组成员列表
    wangwang_eservice_groupmember_get = bind_api(
        method='taobao.wangwang.eservice.groupmember.get'
    )
    #获取登录日志
    wangwang_eservice_loginlogs_get = bind_api(
        method='taobao.wangwang.eservice.loginlogs.get'
    )
    #客服未回复人数
    wangwang_eservice_noreplynum_get = bind_api(
        method='taobao.wangwang.eservice.noreplynum.get'
    )
    #日累计在线时长
    wangwang_eservice_onlinetime_get = bind_api(
        method='taobao.wangwang.eservice.onlinetime.get'
    )
    #客服接待数
    wangwang_eservice_receivenum_get = bind_api(
        method='taobao.wangwang.eservice.receivenum.get'
    )
    #获取分流权重接口
    wangwang_eservice_streamweigths_get = bind_api(
        method='taobao.wangwang.eservice.streamweigths.get'
    )

#--------------------- 主动通知业务API ------------------------------

    #开通增量消息服务
    increment_customer_permit = bind_api(
        method='taobao.increment.customer.permit'
    )
    #关闭用户的增量消息服务
    increment_customer_stop = bind_api(
        method='taobao.increment.customer.stop'
    )
    #查询应用为用户开通的增量消息服务
    increment_customers_get = bind_api(
        method='taobao.increment.customers.get'
    )
    #获取商品变更通知信息
    increment_items_get = bind_api(
        method='taobao.increment.items.get'
    )
    #获取退款变更通知信息
    increment_refunds_get = bind_api(
        method='taobao.increment.refunds.get'
    )
    #获取交易和评价变更通知信息
    increment_trades_get = bind_api(
        method='taobao.increment.trades.get'
    )

#--------------------- 类目API ------------------------------

    #查询B商家被授权品牌列表和类目列表
    itemcats_authorize_get = bind_api(
        method='taobao.itemcats.authorize.get'
    )
    #获取后台供卖家发布商品的标准商品类目
    itemcats_get = bind_api(
        method='taobao.itemcats.get'
    )
    #获取标准商品类目属性
    itemprops_get = bind_api(
        method='taobao.itemprops.get'
    )
    #获取标准类目属性值
    itempropvalues_get = bind_api(
        method='taobao.itempropvalues.get'
    )

#--------------------- 店铺API ------------------------------

    #添加卖家自定义类目
    sellercats_list_add = bind_api(
        method='taobao.sellercats.list.add'
    )
    #获取前台展示的店铺内卖家自定义商品类目
    sellercats_list_get = bind_api(
        method='taobao.sellercats.list.get'
    )
    #更新卖家自定义类目
    sellercats_list_update = bind_api(
        method='taobao.sellercats.list.update'
    )
    #获取卖家店铺的基本信息
    shop_get = bind_api(
        method='taobao.shop.get'
    )
    #获取卖家店铺剩余橱窗数量
    shop_remainshowcase_get = bind_api(
        method='taobao.shop.remainshowcase.get'
    )
    #更新店铺基本信息
    shop_update = bind_api(
        method='taobao.shop.update'
    )
    #获取前台展示的店铺类目
    shopcats_list_get = bind_api(
        method='taobao.shopcats.list.get'
    )

#--------------------- 淘花API ------------------------------

    #有声读物专辑详情
    taohua_audioreader_album_get = bind_api(
        method='taobao.taohua.audioreader.album.get'
    )
    #获取我的有声书库专辑列表
    taohua_audioreader_myalbums_get = bind_api(
        method='taobao.taohua.audioreader.myalbums.get'
    )
    #获取我的有声书库单曲列表
    taohua_audioreader_mytracks_get = bind_api(
        method='taobao.taohua.audioreader.mytracks.get'
    )
    #获取花匠推荐的有声读物专辑列表
    taohua_audioreader_recommend_get = bind_api(
        method='taobao.taohua.audioreader.recommend.get'
    )
    #搜索有声读物专辑
    taohua_audioreader_search = bind_api(
        method='taobao.taohua.audioreader.search'
    )
    #有声读物单曲试听地址
    taohua_audioreader_track_auditionurl_get = bind_api(
        method='taobao.taohua.audioreader.track.auditionurl.get'
    )
    #有声读物单曲下载地址
    taohua_audioreader_track_downloadurl_get = bind_api(
        method='taobao.taohua.audioreader.track.downloadurl.get'
    )
    #有声读物单曲详情
    taohua_audioreader_tracks_get = bind_api(
        method='taobao.taohua.audioreader.tracks.get'
    )
    #用户是否购买过该商品
    taohua_boughtitem_is = bind_api(
        method='taobao.taohua.boughtitem.is'
    )
    #获取子类目列表
    taohua_childcates_get = bind_api(
        method='taobao.taohua.childcates.get'
    )
    #获取文档目录
    taohua_directory_get = bind_api(
        method='taobao.taohua.directory.get'
    )
    #我喜欢商品
    taohua_item_like = bind_api(
        method='taobao.taohua.item.like'
    )
    #对指定商品进行评论
    taohua_itemcomment_add = bind_api(
        method='taobao.taohua.itemcomment.add'
    )
    #获取淘花指定商品的评论列表
    taohua_itemcomments_get = bind_api(
        method='taobao.taohua.itemcomments.get'
    )
    #文档详情
    taohua_itemdetail_get = bind_api(
        method='taobao.taohua.itemdetail.get'
    )
    #获取商品支付链接
    taohua_itempayurl_get = bind_api(
        method='taobao.taohua.itempayurl.get'
    )
    #获取商品资源下载地址
    taohua_itemresurl_get = bind_api(
        method='taobao.taohua.itemresurl.get'
    )
    #商品搜索列表接口
    taohua_items_search = bind_api(
        method='taobao.taohua.items.search'
    )
    #获取最新的更新信息
    taohua_latestupdateinfo_get = bind_api(
        method='taobao.taohua.latestupdateinfo.get'
    )
    #查询买家订单列表
    taohua_orders_get = bind_api(
        method='taobao.taohua.orders.get'
    )
    #获取商品预览链接
    taohua_previewurl_get = bind_api(
        method='taobao.taohua.previewurl.get'
    )
    #获取小二推荐的商品
    taohua_staffrecitems_get = bind_api(
        method='taobao.taohua.staffrecitems.get'
    )

#--------------------- 媒体平台API ------------------------------

    #新增图片分类信息
    picture_category_add = bind_api(
        method='taobao.picture.category.add'
    )
    #获取图片分类信息
    picture_category_get = bind_api(
        method='taobao.picture.category.get'
    )
    #删除图片空间图片
    picture_delete = bind_api(
        method='taobao.picture.delete'
    )
    #获取图片信息
    picture_get = bind_api(
        method='taobao.picture.get'
    )
    #上传单张图片
    picture_upload = bind_api(
        method='taobao.picture.upload'
    )

#--------------------- 分销API ------------------------------

    #获取供应商的合作关系信息
    fenxiao_cooperation_get = bind_api(
        method='taobao.fenxiao.cooperation.get'
    )
    #更新合作关系等级
    fenxiao_cooperation_update = bind_api(
        method='taobao.fenxiao.cooperation.update'
    )
    #新增等级折扣
    fenxiao_discount_add = bind_api(
        method='taobao.fenxiao.discount.add'
    )
    #修改等级折扣
    fenxiao_discount_update = bind_api(
        method='taobao.fenxiao.discount.update'
    )
    #获取折扣信息
    fenxiao_discounts_get = bind_api(
        method='taobao.fenxiao.discounts.get'
    )
    #查询商品下载记录
    fenxiao_distributor_items_get = bind_api(
        method='taobao.fenxiao.distributor.items.get'
    )
    #获取分销商信息
    fenxiao_distributors_get = bind_api(
        method='taobao.fenxiao.distributors.get'
    )
    #分销商等级查询
    fenxiao_grades_get = bind_api(
        method='taobao.fenxiao.grades.get'
    )
    #获取分销用户登录信息
    fenxiao_login_user_get = bind_api(
        method='taobao.fenxiao.login.user.get'
    )
    #确认收款
    fenxiao_order_confirm_paid = bind_api(
        method='taobao.fenxiao.order.confirm.paid'
    )
    #查询采购单信息
    fenxiao_orders_get = bind_api(
        method='taobao.fenxiao.orders.get'
    )
    #添加产品
    fenxiao_product_add = bind_api(
        method='taobao.fenxiao.product.add'
    )
    #更新产品
    fenxiao_product_update = bind_api(
        method='taobao.fenxiao.product.update'
    )
    #查询产品线列表
    fenxiao_productcats_get = bind_api(
        method='taobao.fenxiao.productcats.get'
    )
    #查询产品列表
    fenxiao_products_get = bind_api(
        method='taobao.fenxiao.products.get'
    )

#--------------------- 店铺会员管理API ------------------------------

    #卖家查询等级规则
    crm_grade_get = bind_api(
        method='taobao.crm.grade.get'
    )
    #卖家创建一个分组
    crm_group_add = bind_api(
        method='taobao.crm.group.add'
    )
    #将一个分组添加到另外一个分组
    crm_group_append = bind_api(
        method='taobao.crm.group.append'
    )
    #删除分组
    crm_group_delete = bind_api(
        method='taobao.crm.group.delete'
    )
    #分组移动
    crm_group_move = bind_api(
        method='taobao.crm.group.move'
    )
    #修改一个已经存在的分组
    crm_group_update = bind_api(
        method='taobao.crm.group.update'
    )
    #查询卖家的分组
    crm_groups_get = bind_api(
        method='taobao.crm.groups.get'
    )
    #查询分组任务是否完成
    crm_grouptask_check = bind_api(
        method='taobao.crm.grouptask.check'
    )
    #编辑会员资料
    crm_memberinfo_update = bind_api(
        method='taobao.crm.memberinfo.update'
    )
    #获取卖家的会员（基本查询）
    crm_members_get = bind_api(
        method='taobao.crm.members.get'
    )
    #给一批会员添加一个分组
    crm_members_group_batchadd = bind_api(
        method='taobao.crm.members.group.batchadd'
    )
    #批量删除分组
    crm_members_groups_batchdelete = bind_api(
        method='taobao.crm.members.groups.batchdelete'
    )
    #增量获取卖家会员
    crm_members_increment_get = bind_api(
        method='taobao.crm.members.increment.get'
    )
    #获取卖家会员（高级查询）
    crm_members_search = bind_api(
        method='taobao.crm.members.search'
    )
    #分组规则添加
    crm_rule_add = bind_api(
        method='taobao.crm.rule.add'
    )
    #分组规则删除
    crm_rule_delete = bind_api(
        method='taobao.crm.rule.delete'
    )
    #设置规则适用的分组
    crm_rule_group_set = bind_api(
        method='taobao.crm.rule.group.set'
    )
    #获取规则
    crm_rules_get = bind_api(
        method='taobao.crm.rules.get'
    )
    #卖家取消店铺vip的优惠
    crm_shopvip_cancel = bind_api(
        method='taobao.crm.shopvip.cancel'
    )

#--------------------- 聚划算API ------------------------------

    #根据类目获取商品Id列表
    ju_catitemids_get = bind_api(
        method='taobao.ju.catitemids.get'
    )
    #获取当日的生活服务类城市
    ju_cities_get = bind_api(
        method='taobao.ju.cities.get'
    )
    #获取生活服务类的团信息接口
    ju_citygroup_get = bind_api(
        method='taobao.ju.citygroup.get'
    )
    #根据城市获取生活服务团商品
    ju_cityitems_get = bind_api(
        method='taobao.ju.cityitems.get'
    )
    #根据终端类型分配团
    ju_group_assign = bind_api(
        method='taobao.ju.group.assign'
    )
    #根据团id获取团对象
    ju_group_get = bind_api(
        method='taobao.ju.group.get'
    )
    #根据终端类型获取组id列表
    ju_groupids_get = bind_api(
        method='taobao.ju.groupids.get'
    )
    #根据终端类型和平台ID获取商品id列表
    ju_itemids_get = bind_api(
        method='taobao.ju.itemids.get'
    )
    #根据商品id列表获取商品列表
    ju_items_get = bind_api(
        method='taobao.ju.items.get'
    )
    #根据终端类型随机分配一个今天的商品列表
    ju_todayitems_get = bind_api(
        method='taobao.ju.todayitems.get'
    )

#--------------------- 无线画报API ------------------------------

    #取频道信息
    huabao_channel_get = bind_api(
        method='taobao.huabao.channel.get'
    )
    #取画报频道
    huabao_channels_get = bind_api(
        method='taobao.huabao.channels.get'
    )
    #取画报详情
    huabao_poster_get = bind_api(
        method='taobao.huabao.poster.get'
    )
    #取得画报相关商品信息
    huabao_poster_goodsinfo_get = bind_api(
        method='taobao.huabao.poster.goodsinfo.get'
    )
    #取指定频道Id的画报列表
    huabao_posters_get = bind_api(
        method='taobao.huabao.posters.get'
    )
    #获取指定画报列表
    huabao_specialposters_get = bind_api(
        method='taobao.huabao.specialposters.get'
    )

#--------------------- 子账号管理API ------------------------------

    #查询指定账户的子账号列表
    sellercenter_subusers_get = bind_api(
        method='taobao.sellercenter.subusers.get'
    )

#--------------------- 酒店API ------------------------------

    #酒店发布接口
    hotel_add = bind_api(
        method='taobao.hotel.add'
    )
    #单酒店查询接口
    hotel_get = bind_api(
        method='taobao.hotel.get'
    )
    #根据酒店名称/别名获得对应酒店
    hotel_name_get = bind_api(
        method='taobao.hotel.name.get'
    )
    #单订单查询接口
    hotel_order_get = bind_api(
        method='taobao.hotel.order.get'
    )
    #多订单查询接口
    hotel_orders_search = bind_api(
        method='taobao.hotel.orders.search'
    )
    #商品发布接口
    hotel_room_add = bind_api(
        method='taobao.hotel.room.add'
    )
    #单商品查询接口
    hotel_room_get = bind_api(
        method='taobao.hotel.room.get'
    )
    #商品图片删除接口
    hotel_room_img_delete = bind_api(
        method='taobao.hotel.room.img.delete'
    )
    #商品图片上传接口
    hotel_room_img_upload = bind_api(
        method='taobao.hotel.room.img.upload'
    )
    #商品更新接口
    hotel_room_update = bind_api(
        method='taobao.hotel.room.update'
    )
    #多商品查询接口
    hotel_rooms_search = bind_api(
        method='taobao.hotel.rooms.search'
    )
    #酒店发布者发布酒店增量查询接口
    hotel_sold_hotels_increment_get = bind_api(
        method='taobao.hotel.sold.hotels.increment.get'
    )
    #搜索当前会话用户作为卖家已卖出的增量交易数据
    hotel_sold_orders_increment_get = bind_api(
        method='taobao.hotel.sold.orders.increment.get'
    )
    #房型发布者发布房型增量查询接口
    hotel_sold_types_increment_get = bind_api(
        method='taobao.hotel.sold.types.increment.get'
    )
    #房型发布接口
    hotel_type_add = bind_api(
        method='taobao.hotel.type.add'
    )
    #根据房型名称/别名获得对应房型
    hotel_type_name_get = bind_api(
        method='taobao.hotel.type.name.get'
    )
    #酒店更新接口
    hotel_update = bind_api(
        method='taobao.hotel.update'
    )
    #多酒店查询接口
    hotels_search = bind_api(
        method='taobao.hotels.search'
    )

#--------------------- 用户API ------------------------------

    #获取单个用户信息
    user_get = bind_api(
        method='taobao.user.get'
    )
    #获取多个用户信息
    users_get = bind_api(
        method='taobao.users.get'
    )

#--------------------- 淘代码API ------------------------------

    #获取淘代码相关信息
    taocode_get = bind_api(
        method='taobao.taocode.get'
    )



