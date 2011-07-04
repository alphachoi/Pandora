#encoding=utf-8
'''
Created on 2011-5-9

@author: LiuTao
'''
from binder import bind_api
from config import Config

class API(object):
    '''
    classdocs
    '''


    def __init__(self, key, secret, api_url=Config.get('api_url'), session_url=Config.get('session_url'), format="json", sign_method="md5", version="2.0"):
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
        
        self.session = "4061600XImpna0o98209fe3991208a2945f61b5da033b0e390468121"
        
#------------------用户API------------------------

# 提供了用户基本信息查询功能

    user_get = bind_api(
        method='taobao.user.get'
    )
    users_get = bind_api(
        method='taobao.users.get'
    )
#------------------产品API------------------------

# 提供了产品相关的发布，修改等功能

    product_add = bind_api(
        method='taobao.product.add'
    )
    product_get = bind_api(
        method='taobao.product.get'
    )
    product_img_delete = bind_api(
        method='taobao.product.img.delete'
    )
    product_img_upload = bind_api(
        method='taobao.product.img.upload'
    )
    product_propimg_delete = bind_api(
        method='taobao.product.propimg.delete'
    )
    product_propimg_upload = bind_api(
        method='taobao.product.propimg.upload'
    )
    product_update = bind_api(
        method='taobao.product.update'
    )
    products_get = bind_api(
        method='taobao.products.get'
    )
    products_search = bind_api(
        method='taobao.products.search'
    )
#------------------类目属性API------------------------

# 提供了标准类目，类目属性和类目属性值的查询功能

    itemcats_authorize_get = bind_api(
        method='taobao.itemcats.authorize.get'
    )
    itemcats_get = bind_api(
        method='taobao.itemcats.get'
    )
    itemprops_get = bind_api(
        method='taobao.itemprops.get'
    )
    itempropvalues_get = bind_api(
        method='taobao.itempropvalues.get'
    )
#------------------商品API------------------------

# 提供了商品以及商品相关的sku，邮费增加，修改功能

    aftersale_get = bind_api(
        method='taobao.aftersale.get'
    )
    item_add = bind_api(
        method='taobao.item.add'
    )
    item_delete = bind_api(
        method='taobao.item.delete'
    )
    item_get = bind_api(
        method='taobao.item.get'
    )
    item_img_delete = bind_api(
        method='taobao.item.img.delete'
    )
    item_img_upload = bind_api(
        method='taobao.item.img.upload'
    )
    item_joint_img = bind_api(
        method='taobao.item.joint.img'
    )
    item_joint_propimg = bind_api(
        method='taobao.item.joint.propimg'
    )
    item_propimg_delete = bind_api(
        method='taobao.item.propimg.delete'
    )
    item_propimg_upload = bind_api(
        method='taobao.item.propimg.upload'
    )
    item_quantity_update = bind_api(
        method='taobao.item.quantity.update'
    )
    item_recommend_add = bind_api(
        method='taobao.item.recommend.add'
    )
    item_recommend_delete = bind_api(
        method='taobao.item.recommend.delete'
    )
    item_sku_add = bind_api(
        method='taobao.item.sku.add'
    )
    item_sku_delete = bind_api(
        method='taobao.item.sku.delete'
    )
    item_sku_get = bind_api(
        method='taobao.item.sku.get'
    )
    item_sku_update = bind_api(
        method='taobao.item.sku.update'
    )
    item_skus_get = bind_api(
        method='taobao.item.skus.get'
    )
    item_update = bind_api(
        method='taobao.item.update'
    )
    item_update_delisting = bind_api(
        method='taobao.item.update.delisting'
    )
    item_update_listing = bind_api(
        method='taobao.item.update.listing'
    )
    items_custom_get = bind_api(
        method='taobao.items.custom.get'
    )
    items_get = bind_api(
        method='taobao.items.get'
    )
    items_inventory_get = bind_api(
        method='taobao.items.inventory.get'
    )
    items_list_get = bind_api(
        method='taobao.items.list.get'
    )
    items_onsale_get = bind_api(
        method='taobao.items.onsale.get'
    )
    items_search = bind_api(
        method='taobao.items.search'
    )
    postage_add = bind_api(
        method='taobao.postage.add'
    )
    postage_delete = bind_api(
        method='taobao.postage.delete'
    )
    postage_get = bind_api(
        method='taobao.postage.get'
    )
    postage_update = bind_api(
        method='taobao.postage.update'
    )
    postages_get = bind_api(
        method='taobao.postages.get'
    )
    skus_custom_get = bind_api(
        method='taobao.skus.custom.get'
    )
#------------------交易API------------------------

# 提供了订单下载，修改收货地址、修改交易备注等功能

    refund_get = bind_api(
        method='taobao.refund.get'
    )
    refund_message_add = bind_api(
        method='taobao.refund.message.add'
    )
    refund_messages_get = bind_api(
        method='taobao.refund.messages.get'
    )
    refund_refuse = bind_api(
        method='taobao.refund.refuse'
    )
    refunds_apply_get = bind_api(
        method='taobao.refunds.apply.get'
    )
    refunds_receive_get = bind_api(
        method='taobao.refunds.receive.get'
    )
    trade_amount_get = bind_api(
        method='taobao.trade.amount.get'
    )
    trade_close = bind_api(
        method='taobao.trade.close'
    )
    trade_confirmfee_get = bind_api(
        method='taobao.trade.confirmfee.get'
    )
    trade_fullinfo_get = bind_api(
        method='taobao.trade.fullinfo.get'
    )
    trade_get = bind_api(
        method='taobao.trade.get'
    )
    trade_memo_add = bind_api(
        method='taobao.trade.memo.add'
    )
    trade_memo_update = bind_api(
        method='taobao.trade.memo.update'
    )
    trade_ordersku_update = bind_api(
        method='taobao.trade.ordersku.update'
    )
    trade_receivetime_delay = bind_api(
        method='taobao.trade.receivetime.delay'
    )
    trade_shippingaddress_update = bind_api(
        method='taobao.trade.shippingaddress.update'
    )
    trade_snapshot_get = bind_api(
        method='taobao.trade.snapshot.get'
    )
    trades_bought_get = bind_api(
        method='taobao.trades.bought.get'
    )
    trades_sold_get = bind_api(
        method='taobao.trades.sold.get'
    )
    trades_sold_increment_get = bind_api(
        method='taobao.trades.sold.increment.get'
    )
#------------------评价API------------------------

# 提供了评价的添加和查询功能

    traderate_add = bind_api(
        method='taobao.traderate.add'
    )
    traderate_list_add = bind_api(
        method='taobao.traderate.list.add'
    )
    traderates_get = bind_api(
        method='taobao.traderates.get'
    )
    traderates_search = bind_api(
        method='taobao.traderates.search'
    )
#------------------物流API------------------------

# 提供了发货，物流单详情，区域地址和物流公司信息查询功能

    areas_get = bind_api(
        method='taobao.areas.get'
    )
    logistics_address_add = bind_api(
        method='taobao.logistics.address.add'
    )
    logistics_address_modify = bind_api(
        method='taobao.logistics.address.modify'
    )
    logistics_address_remove = bind_api(
        method='taobao.logistics.address.remove'
    )
    logistics_address_search = bind_api(
        method='taobao.logistics.address.search'
    )
    logistics_companies_get = bind_api(
        method='taobao.logistics.companies.get'
    )
    logistics_dummy_send = bind_api(
        method='taobao.logistics.dummy.send'
    )
    logistics_offline_send = bind_api(
        method='taobao.logistics.offline.send'
    )
    logistics_online_cancel = bind_api(
        method='taobao.logistics.online.cancel'
    )
    logistics_online_confirm = bind_api(
        method='taobao.logistics.online.confirm'
    )
    logistics_online_send = bind_api(
        method='taobao.logistics.online.send'
    )
    logistics_orders_detail_get = bind_api(
        method='taobao.logistics.orders.detail.get'
    )
    logistics_orders_get = bind_api(
        method='taobao.logistics.orders.get'
    )
    logistics_partners_get = bind_api(
        method='taobao.logistics.partners.get'
    )
    logistics_trace_search = bind_api(
        method='taobao.logistics.trace.search'
    )
#------------------收费API------------------------

# 提供了增值服务的订购、订单等相关信息查询

    guarantyfunds_get = bind_api(
        method='taobao.guarantyfunds.get'
    )
    vas_order_search = bind_api(
        method='taobao.vas.order.search'
    )
    vas_subsc_search = bind_api(
        method='taobao.vas.subsc.search'
    )
    vas_subscribe_get = bind_api(
        method='taobao.vas.subscribe.get'
    )
#------------------店铺API------------------------

# 提供了店铺查询，店铺自定义类目的查询和更新，图片空间图片的查询和删除等功能

    item_templates_get = bind_api(
        method='taobao.item.templates.get'
    )
    picture_category_add = bind_api(
        method='taobao.picture.category.add'
    )
    picture_category_get = bind_api(
        method='taobao.picture.category.get'
    )
    picture_delete = bind_api(
        method='taobao.picture.delete'
    )
    picture_get = bind_api(
        method='taobao.picture.get'
    )
    picture_upload = bind_api(
        method='taobao.picture.upload'
    )
    sellercats_list_add = bind_api(
        method='taobao.sellercats.list.add'
    )
    sellercats_list_get = bind_api(
        method='taobao.sellercats.list.get'
    )
    sellercats_list_update = bind_api(
        method='taobao.sellercats.list.update'
    )
    shop_get = bind_api(
        method='taobao.shop.get'
    )
    shop_remainshowcase_get = bind_api(
        method='taobao.shop.remainshowcase.get'
    )
    shop_update = bind_api(
        method='taobao.shop.update'
    )
    shopcats_list_get = bind_api(
        method='taobao.shopcats.list.get'
    )
#------------------分销API------------------------

# 提供了分销商信息和采购单信息的查询以及分销产品的添加和更新等功能

    fenxiao_cooperation_get = bind_api(
        method='taobao.fenxiao.cooperation.get'
    )
    fenxiao_cooperation_update = bind_api(
        method='taobao.fenxiao.cooperation.update'
    )
    fenxiao_discount_add = bind_api(
        method='taobao.fenxiao.discount.add'
    )
    fenxiao_discount_update = bind_api(
        method='taobao.fenxiao.discount.update'
    )
    fenxiao_discounts_get = bind_api(
        method='taobao.fenxiao.discounts.get'
    )
    fenxiao_distributor_items_get = bind_api(
        method='taobao.fenxiao.distributor.items.get'
    )
    fenxiao_distributors_get = bind_api(
        method='taobao.fenxiao.distributors.get'
    )
    fenxiao_grades_get = bind_api(
        method='taobao.fenxiao.grades.get'
    )
    fenxiao_order_confirm_paid = bind_api(
        method='taobao.fenxiao.order.confirm.paid'
    )
    fenxiao_orders_get = bind_api(
        method='taobao.fenxiao.orders.get'
    )
    fenxiao_product_add = bind_api(
        method='taobao.fenxiao.product.add'
    )
    fenxiao_product_update = bind_api(
        method='taobao.fenxiao.product.update'
    )
    fenxiao_productcats_get = bind_api(
        method='taobao.fenxiao.productcats.get'
    )
    fenxiao_products_get = bind_api(
        method='taobao.fenxiao.products.get'
    )
#------------------画报API------------------------

# 提供了无线画报业务频道、画报的获取。

    huabao_channel_get = bind_api(
        method='taobao.huabao.channel.get'
    )
    huabao_channels_get = bind_api(
        method='taobao.huabao.channels.get'
    )
    huabao_poster_get = bind_api(
        method='taobao.huabao.poster.get'
    )
    huabao_poster_goodsinfo_get = bind_api(
        method='taobao.huabao.poster.goodsinfo.get'
    )
    huabao_posters_get = bind_api(
        method='taobao.huabao.posters.get'
    )
    huabao_specialposters_get = bind_api(
        method='taobao.huabao.specialposters.get'
    )
#------------------旺旺API------------------------

# 提供了旺旺聊天记录，平均等待时间，客服评价统计，客服未回复人数和客服接待数等绩效考核功能

    wangwang_eservice_avgwaittime_get = bind_api(
        method='taobao.wangwang.eservice.avgwaittime.get'
    )
    wangwang_eservice_chatlog_get = bind_api(
        method='taobao.wangwang.eservice.chatlog.get'
    )
    wangwang_eservice_chatpeers_get = bind_api(
        method='taobao.wangwang.eservice.chatpeers.get'
    )
    wangwang_eservice_chatrecord_get = bind_api(
        method='taobao.wangwang.eservice.chatrecord.get'
    )
    wangwang_eservice_evaluation_get = bind_api(
        method='taobao.wangwang.eservice.evaluation.get'
    )
    wangwang_eservice_groupmember_get = bind_api(
        method='taobao.wangwang.eservice.groupmember.get'
    )
    wangwang_eservice_noreplynum_get = bind_api(
        method='taobao.wangwang.eservice.noreplynum.get'
    )
    wangwang_eservice_onlinetime_get = bind_api(
        method='taobao.wangwang.eservice.onlinetime.get'
    )
    wangwang_eservice_receivenum_get = bind_api(
        method='taobao.wangwang.eservice.receivenum.get'
    )
#------------------淘客API------------------------

# 提供了淘宝客商品列表和淘宝客单品详情推广，店铺推广，类目和关键字推广以及淘客报表查询等功能

    taobaoke_caturl_get = bind_api(
        method='taobao.taobaoke.caturl.get'
    )
    taobaoke_items_convert = bind_api(
        method='taobao.taobaoke.items.convert'
    )
    taobaoke_items_detail_get = bind_api(
        method='taobao.taobaoke.items.detail.get'
    )
    taobaoke_items_get = bind_api(
        method='taobao.taobaoke.items.get'
    )
    taobaoke_listurl_get = bind_api(
        method='taobao.taobaoke.listurl.get'
    )
    taobaoke_report_get = bind_api(
        method='taobao.taobaoke.report.get'
    )
    taobaoke_shops_convert = bind_api(
        method='taobao.taobaoke.shops.convert'
    )
    taobaoke_shops_get = bind_api(
        method='taobao.taobaoke.shops.get'
    )
    taobaoke_tool_relation = bind_api(
        method='taobao.taobaoke.tool.relation'
    )
    taobaoke_virtualcard_get = bind_api(
        method='taobao.taobaoke.virtualcard.get'
    )
#------------------增量API------------------------

# 提供了商品，交易，退款和评价的增量数据的查询功能。。增量即为数据或状态的变更。

    increment_app_subscribe = bind_api(
        method='taobao.increment.app.subscribe'
    )
    increment_authorizemessages_get = bind_api(
        method='taobao.increment.authorizemessages.get'
    )
    increment_items_get = bind_api(
        method='taobao.increment.items.get'
    )
    increment_refunds_get = bind_api(
        method='taobao.increment.refunds.get'
    )
    increment_subscribemessage_get = bind_api(
        method='taobao.increment.subscribemessage.get'
    )
    increment_trades_get = bind_api(
        method='taobao.increment.trades.get'
    )
#------------------系统API------------------------

# 提供了系统时间查询和tp订购授权功能

    time_get = bind_api(
        method='taobao.time.get'
    )
#------------------物流宝API------------------------

# 提供了物流宝库存，商品，订单和发货等功能

    wlb_inventory_detail_get = bind_api(
        method='taobao.wlb.inventory.detail.get'
    )
    wlb_inventory_sync = bind_api(
        method='taobao.wlb.inventory.sync'
    )
    wlb_inventorylog_query = bind_api(
        method='taobao.wlb.inventorylog.query'
    )
    wlb_item_add = bind_api(
        method='taobao.wlb.item.add'
    )
    wlb_item_authorization_add = bind_api(
        method='taobao.wlb.item.authorization.add'
    )
    wlb_item_authorization_delete = bind_api(
        method='taobao.wlb.item.authorization.delete'
    )
    wlb_item_authorization_query = bind_api(
        method='taobao.wlb.item.authorization.query'
    )
    wlb_item_combination_create = bind_api(
        method='taobao.wlb.item.combination.create'
    )
    wlb_item_combination_delete = bind_api(
        method='taobao.wlb.item.combination.delete'
    )
    wlb_item_combination_get = bind_api(
        method='taobao.wlb.item.combination.get'
    )
    wlb_item_consignment_create = bind_api(
        method='taobao.wlb.item.consignment.create'
    )
    wlb_item_consignment_delete = bind_api(
        method='taobao.wlb.item.consignment.delete'
    )
    wlb_item_consignment_page_get = bind_api(
        method='taobao.wlb.item.consignment.page.get'
    )
    wlb_item_delete = bind_api(
        method='taobao.wlb.item.delete'
    )
    wlb_item_get = bind_api(
        method='taobao.wlb.item.get'
    )
    wlb_item_map_get = bind_api(
        method='taobao.wlb.item.map.get'
    )
    wlb_item_map_get_by_extentity = bind_api(
        method='taobao.wlb.item.map.get.by.extentity'
    )
    wlb_item_query = bind_api(
        method='taobao.wlb.item.query'
    )
    wlb_item_synchronize = bind_api(
        method='taobao.wlb.item.synchronize'
    )
    wlb_item_synchronize_delete = bind_api(
        method='taobao.wlb.item.synchronize.delete'
    )
    wlb_item_update = bind_api(
        method='taobao.wlb.item.update'
    )
    wlb_notify_message_confirm = bind_api(
        method='taobao.wlb.notify.message.confirm'
    )
    wlb_notify_message_page_get = bind_api(
        method='taobao.wlb.notify.message.page.get'
    )
    wlb_order_cancel = bind_api(
        method='taobao.wlb.order.cancel'
    )
    wlb_order_consign = bind_api(
        method='taobao.wlb.order.consign'
    )
    wlb_order_create = bind_api(
        method='taobao.wlb.order.create'
    )
    wlb_order_page_get = bind_api(
        method='taobao.wlb.order.page.get'
    )
    wlb_order_schedule_rule_add = bind_api(
        method='taobao.wlb.order.schedule.rule.add'
    )
    wlb_order_schedule_rule_update = bind_api(
        method='taobao.wlb.order.schedule.rule.update'
    )
    wlb_orderitem_page_get = bind_api(
        method='taobao.wlb.orderitem.page.get'
    )
    wlb_orderschedulerule_delete = bind_api(
        method='taobao.wlb.orderschedulerule.delete'
    )
    wlb_orderschedulerule_query = bind_api(
        method='taobao.wlb.orderschedulerule.query'
    )
    wlb_orderstatus_get = bind_api(
        method='taobao.wlb.orderstatus.get'
    )
    wlb_replenish_statistics = bind_api(
        method='taobao.wlb.replenish.statistics'
    )
    wlb_subscription_query = bind_api(
        method='taobao.wlb.subscription.query'
    )
    wlb_tmsorder_query = bind_api(
        method='taobao.wlb.tmsorder.query'
    )
    wlb_tradeorder_get = bind_api(
        method='taobao.wlb.tradeorder.get'
    )
    wlb_wlborder_get = bind_api(
        method='taobao.wlb.wlborder.get'
    )
#------------------信息安全API------------------------

# 提供了关键词过滤匹配功能

    kfc_keyword_search = bind_api(
        method='taobao.kfc.keyword.search'
    )
#------------------淘代码API------------------------

# 

    taocode_get = bind_api(
        method='taobao.taocode.get'
    )
#------------------收藏夹API------------------------

# 提供了收藏夹添加和查询功能

    favorite_add = bind_api(
        method='taobao.favorite.add'
    )
    favorite_search = bind_api(
        method='taobao.favorite.search'
    )
#------------------异步API------------------------

# 批量执行不同时进行的任务，目前开放的API支持异步发货以及异步交易订单详情查询。

    topats_delivery_send = bind_api(
        method='taobao.topats.delivery.send'
    )
    topats_result_get = bind_api(
        method='taobao.topats.result.get'
    )
    topats_trade_accountreport_get = bind_api(
        method='taobao.topats.trade.accountreport.get'
    )
    topats_trades_fullinfo_get = bind_api(
        method='taobao.topats.trades.fullinfo.get'
    )
#------------------营销API------------------------

# 提供淘宝营销工具的业务，包括店铺优惠券、会员关系管理等；商家必须已经订购了营销工具才能使用这些接口获取数据。

    marketing_promotion_add = bind_api(
        method='taobao.marketing.promotion.add'
    )
    marketing_promotion_delete = bind_api(
        method='taobao.marketing.promotion.delete'
    )
    marketing_promotions_get = bind_api(
        method='taobao.marketing.promotions.get'
    )
    marketing_tag_add = bind_api(
        method='taobao.marketing.tag.add'
    )
    marketing_tag_delete = bind_api(
        method='taobao.marketing.tag.delete'
    )
    marketing_tags_get = bind_api(
        method='taobao.marketing.tags.get'
    )
    marketing_taguser_add = bind_api(
        method='taobao.marketing.taguser.add'
    )
    marketing_taguser_delete = bind_api(
        method='taobao.marketing.taguser.delete'
    )
    promotion_activity_add = bind_api(
        method='taobao.promotion.activity.add'
    )
    promotion_activity_cancel = bind_api(
        method='taobao.promotion.activity.cancel'
    )
    promotion_activity_delete = bind_api(
        method='taobao.promotion.activity.delete'
    )
    promotion_activity_get = bind_api(
        method='taobao.promotion.activity.get'
    )
    promotion_coupon_add = bind_api(
        method='taobao.promotion.coupon.add'
    )
    promotion_coupon_send = bind_api(
        method='taobao.promotion.coupon.send'
    )
    promotion_coupondetail_get = bind_api(
        method='taobao.promotion.coupondetail.get'
    )
    promotion_coupons_get = bind_api(
        method='taobao.promotion.coupons.get'
    )
    promotion_meal_add = bind_api(
        method='taobao.promotion.meal.add'
    )
    promotion_meal_delete = bind_api(
        method='taobao.promotion.meal.delete'
    )
    promotion_meal_get = bind_api(
        method='taobao.promotion.meal.get'
    )
    promotion_meal_update = bind_api(
        method='taobao.promotion.meal.update'
    )
    promotion_members_get = bind_api(
        method='taobao.promotion.members.get'
    )
#------------------淘花API------------------------

# 提供了淘花网查询买家订单，商品搜索，类目查询，商品详情，用户是否购买过某商品等接口。

    taohua_audioreader_album_get = bind_api(
        method='taobao.taohua.audioreader.album.get'
    )
    taohua_audioreader_recommend_get = bind_api(
        method='taobao.taohua.audioreader.recommend.get'
    )
    taohua_audioreader_search = bind_api(
        method='taobao.taohua.audioreader.search'
    )
    taohua_audioreader_tracks_get = bind_api(
        method='taobao.taohua.audioreader.tracks.get'
    )
    taohua_boughtitem_is = bind_api(
        method='taobao.taohua.boughtitem.is'
    )
    taohua_childcates_get = bind_api(
        method='taobao.taohua.childcates.get'
    )
    taohua_item_like = bind_api(
        method='taobao.taohua.item.like'
    )
    taohua_itemcomment_add = bind_api(
        method='taobao.taohua.itemcomment.add'
    )
    taohua_itemcomments_get = bind_api(
        method='taobao.taohua.itemcomments.get'
    )
    taohua_itemdetail_get = bind_api(
        method='taobao.taohua.itemdetail.get'
    )
    taohua_itempayurl_get = bind_api(
        method='taobao.taohua.itempayurl.get'
    )
    taohua_itemresurl_get = bind_api(
        method='taobao.taohua.itemresurl.get'
    )
    taohua_items_search = bind_api(
        method='taobao.taohua.items.search'
    )
    taohua_latestupdateinfo_get = bind_api(
        method='taobao.taohua.latestupdateinfo.get'
    )
    taohua_orders_get = bind_api(
        method='taobao.taohua.orders.get'
    )
    taohua_previewurl_get = bind_api(
        method='taobao.taohua.previewurl.get'
    )
    taohua_staffrecitems_get = bind_api(
        method='taobao.taohua.staffrecitems.get'
    )
#------------------酒店API------------------------

# 淘宝酒店业务

    hotel_add = bind_api(
        method='taobao.hotel.add'
    )
    hotel_get = bind_api(
        method='taobao.hotel.get'
    )
    hotel_order_get = bind_api(
        method='taobao.hotel.order.get'
    )
    hotel_orders_search = bind_api(
        method='taobao.hotel.orders.search'
    )
    hotel_room_add = bind_api(
        method='taobao.hotel.room.add'
    )
    hotel_room_get = bind_api(
        method='taobao.hotel.room.get'
    )
    hotel_room_img_delete = bind_api(
        method='taobao.hotel.room.img.delete'
    )
    hotel_room_img_upload = bind_api(
        method='taobao.hotel.room.img.upload'
    )
    hotel_room_update = bind_api(
        method='taobao.hotel.room.update'
    )
    hotel_rooms_search = bind_api(
        method='taobao.hotel.rooms.search'
    )
    hotel_type_add = bind_api(
        method='taobao.hotel.type.add'
    )
    hotel_update = bind_api(
        method='taobao.hotel.update'
    )
    hotels_search = bind_api(
        method='taobao.hotels.search'
    )
#------------------聚划算API------------------------

# 提供聚划算业务相关的接口，目前提供了聚划算团购商品的查询接口

    ju_cities_get = bind_api(
        method='taobao.ju.cities.get'
    )
    ju_citygroup_get = bind_api(
        method='taobao.ju.citygroup.get'
    )
    ju_group_assign = bind_api(
        method='taobao.ju.group.assign'
    )
    ju_group_get = bind_api(
        method='taobao.ju.group.get'
    )
    ju_groupids_get = bind_api(
        method='taobao.ju.groupids.get'
    )


