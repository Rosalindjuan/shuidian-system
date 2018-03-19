import aiohttp_jinja2
from aiohttp import web

from store.models import Users, Stock, GoodsTemplate, Customer, CustomerGoodsDetail, CustomerRepayDetail, Users
import json


class Home(web.View):
    @aiohttp_jinja2.template('web/dist/index.html')
    async def get(self):
        return {}


# 初始化数据
async def initData(request):
    await Users.new_user('admin', '888888', type='超级管理员')
    text = "系统初始化成功!<a href='" + str(request.url.parent) + "'>登录后台</a>"
    response = aiohttp_jinja2.render_template('base.html', request, {'code': text})
    return response


# 新建库存
async def newStock(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await Stock.create_stock(requestData['name'], requestData['num'], requestData['unit'],
                                      float(requestData['opening_price']), float(requestData['price']),
                                      requestData['remarks'])
    return web.json_response(result)


class StockDetail(web.View):
    # 某库存详情
    async def get(self):
        query = dict(self.request.query)
        stock = await Stock.get_stock(query['id'])
        if stock:
            data = {'name': stock.name, 'unit': stock.unit, 'num': stock.num, 'price': stock.price,
                    'amount': stock.amount,
                    'opening_price': stock.opening_price, 'opening_amount': stock.opening_amount,
                    'remarks': stock.remarks}
            return web.json_response({'errcode': 0, 'msg': '', 'data': data})
        return web.json_response({'errcode': 1, 'msg': '无此货物'})

    # 修改某库存
    async def post(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await Stock.update_stock(requestData['name'], int(requestData['num']), requestData['unit'],
                                          int(requestData['opening_price']), int(requestData['price']),
                                          requestData['remarks'])
        return web.json_response(result)


class StockList(web.View):
    # 库存列表
    async def get(self):
        query = dict(self.request.query)
        stocks = await Stock.get_stocks(query['result'])
        list = []
        perPage = 10
        for item in stocks[(int(query['page']) - 1) * perPage: perPage * int(query['page'])]:
            list.append({'id': str(item.id), 'name': item.name, 'unit': item.unit, 'num': item.num, 'price': item.price,
                         'amount': item.amount,
                         'opening_price': item.opening_price, 'opening_amount': item.opening_amount,
                         'remarks': item.remarks})
        return web.json_response(
            {'errcode': 0, 'msg': '', 'data': {'list': list, 'count': len(stocks), 'perPage': perPage}})

    # 删除某库存
    async def post(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await Stock.delete_stock(requestData['id'])
        return web.json_response(result)


# 库存列表 名称
async def getStocks(request):
    stocks = await Stock.get_stocks(True)
    list = []
    for item in stocks:
        list.append(item.name)
    return web.json_response({'errcode': 0, 'msg': '', 'data': {'list': list}})


# 创建模板
async def newTemplate(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await GoodsTemplate.new_goods_template(requestData['name'], requestData['remarks'], requestData['goods'])
    return web.json_response(result)


# 模板列表
async def temList(request):
    list = await GoodsTemplate.goods_template_list()
    data = []
    for l in list:
        goods_list = await GoodsTemplate.get_tem_goods_list(str(l.id))
        data.append({'name': l.name, 'remarks': l.remarks, 'id': str(l.id), 'goods': goods_list['list']})
    return web.json_response({'errcode': 0, 'msg': '', 'data': {'list': data}})


# 模板货物列表
async def temGoodsList(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    data = await GoodsTemplate.get_tem_goods_list(requestData['id'])
    if data:
        return web.json_response({'errcode': 0, 'msg': '', 'data': data})
    return web.json_response({'errcode': 1, 'msg': '无此模板'})


# 修改模板信息
async def updateTemplate(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await GoodsTemplate.update_goods_template(requestData['name'], requestData['remarks'],
                                                       requestData['goods'])
    return web.json_response(result)


# 删除模板
async def deleteTemplate(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await GoodsTemplate.delete_goods_template(requestData['id'])
    return web.json_response({'errcode': 0, 'msg': '已删除'})


# 客户
class Customers(web.View):
    # 新建客户
    async def put(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        # print(requestData)
        if len(requestData['checkedStocks']) > 0:
            customer = await Customer.new_customer(requestData['form']['name'], requestData['form']['address'],
                                                   requestData['form']['tel'], requestData['form']['remarks'])
            # print(customer.inserted_id)
            for i in requestData['checkedStocks']:
                await CustomerGoodsDetail.new_c_detail(customer.inserted_id, i)
            return web.json_response({'errcode': 0, 'msg': '创建新客户成功'})
        return web.json_response({'errcode': 1, 'msg': '请选择客户所需的物料'})

    # 获取客户列表
    async def post(self):
        customers = await Customer.get_customers()
        data = []
        for i in customers:
            data.append({'id': str(i.id), 'name': i.name, 'tel': i.tel, 'address': i.address, 'remarks': i.remarks})
        return web.json_response({'errcode': 0, 'msg': '', 'data': data})

    # 客户信息
    async def get(self):
        query = dict(self.request.query)
        customer = await Customer.get_customer(query['id'])
        customer_goods = await CustomerGoodsDetail.get_customer_goods(query['id'])
        customer_repay = await CustomerRepayDetail.get_repay_list(query['id'])
        goods_list = []
        repay_list = []

        if customer_goods:
            for goods in customer_goods:
                goods_list.append(
                    {'id': str(goods.id), 'stock_name': goods.stock_name, 'stock_num': goods.stock_num,
                     'stock_price': goods.stock_price,
                     'stock_amount': goods.stock_amount})

        if customer_repay:
            for repay in customer_repay:
                repay_list.append(
                    {'amount': repay.money, 'time': repay.time})
        if customer:
            data = {'name': customer.name, 'tel': customer.tel, 'address': customer.address,
                    'remarks': customer.remarks}
            return web.json_response(
                {'errcode': 0, 'msg': '', 'data': {'info': data, 'goods_list': goods_list, 'repay_list': repay_list}})
        return web.json_response({'errcode': 1, 'msg': '无此客户'})


# 添加客户付款信息
async def addRepay(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    print(requestData)
    if requestData['amount'] and requestData['time']:
        result = await CustomerRepayDetail.new_repay(requestData['id'], requestData['amount'], requestData['time'])
        return web.json_response(result)
    else:
        return web.json_response({'errcode': 1, 'msg': '请填写完整'})


# 更新客户基本信息
async def updateCustomer(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    print('updateCustomer', requestData)
    result = await Customer.update_customer(requestData['id'], requestData['form']['address'],
                                            requestData['form']['tel'], requestData['form']['remarks'])

    return web.json_response(result)


# 更新客户用料信息
async def updateCusGoods(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    print('updateCusGoods', requestData)
    for i in requestData['goodsList']:
        await CustomerGoodsDetail.update_customer_goods(i['id'], requestData['id'], i['stock_num'], i['stock_price'])

    return web.json_response({'errcode': 0, 'msg': '修改成功'})


class Adminitors(web.View):
    # 管理员列表
    async def get(self):
        users = await Users.get_users()
        list = []
        for i in users:
            list.append(
                {'id': str(i.id), 'username': i.user, 'type': i.type ,'name': i.real_name, 'tel': i.tel, 'is_active': i.is_active})
        return web.json_response({'errcode': 0, 'msg': '', 'data': {'list': list}})

    # 新建管理员
    async def put(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        print(requestData)
        if requestData['password'] == requestData['surePsd']:
            result = await Users.new_user(requestData['username'], requestData['password'], requestData['name'],
                                          requestData['department'],
                                          requestData['position'], requestData['tel'], requestData['email'],
                                          requestData['qq'],
                                          requestData['wechat'])
            return web.json_response(result)
        return web.json_response({'errcode': 1, 'msg': '两次密码不一致'})

    # 删除管理员
    async def post(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await Users.delete_user(requestData['id'])
        return web.json_response(result)


class Adminitor(web.View):
    async def get(self):
        query = dict(self.request.query)
        user = await Users.get_user(query['id'])
        if user:
            data = {'username': user.user, 'name': user.real_name, 'tel': user.tel, 'department': user.department,
                    'position': user.position, 'email': user.email, 'qq': user.qq, 'wechat': user.wechat}
            return web.json_response({'errcode': 0, 'msg': '', 'data': data})

        return web.json_response({'errcode': 1, 'msg': '无该管理员！'})
