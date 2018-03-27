import aiohttp_jinja2
from aiohttp import web

from store.models import Users, Stock, GoodsTemplate, Customer, CustomerGoodsDetail, CustomerRepayDetail, Users
import json
import time
from .utils import random_str, generateUserToken, SUPER_USER_TYPE, COMMON_USER_TYPE


class Home(web.View):
    @aiohttp_jinja2.template('web/dist/index.html')
    async def get(self):
        return {}


# 初始化数据
async def initData(request):
    uid = random_str()
    user_login = str(SUPER_USER_TYPE) + str(int(time.time())) + random_str()
    userToken = generateUserToken(uid, user_login)
    print(userToken)
    await Users.new_user(uid, userToken['token'], 'admin', '888888', type='超级管理员', expires_time=userToken['expiretime'])
    text = "系统初始化成功!<a href='" + str(request.url.parent) + "'>登录后台</a>"
    response = aiohttp_jinja2.render_template('base.html', request, {'code': text})
    return response


# 用户登录
async def login(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await Users.user_login(requestData['username'], requestData['password'])
    return web.json_response(result)


# 判断用户是否过期
async def judgeUser(requestData, funcName):
    user = await Users.get_user_token(requestData['username'], requestData['token'])
    if user:
        if user.expires_time <= int(time.time()):
            return {'errcode': 2, 'msg': 'token已过期，请重新登录'}
        else:
            # 没有过期的代码逻辑
            return await funcName(requestData)
    return {'errcode': 2, 'msg': '无该用户，请重新登录'}


# 用户里面操作的逻辑
class UserLogic:
    # 创建库存
    async def createStock(self, requestData):
        return await Stock.create_stock(requestData['name'], requestData['num'], requestData['unit'],
                                        float(requestData['opening_price']), float(requestData['price']),
                                        requestData['remarks'])

    # 修改库存
    async def updateStock(self, requestData):
        return await Stock.update_stock(requestData['name'], int(requestData['num']), requestData['unit'],
                                        int(requestData['opening_price']), int(requestData['price']),
                                        requestData['remarks'])

    # 库存详情
    async def getStockDetail(self, requestData):
        stock = await Stock.get_stock(requestData['id'])
        if stock:
            data = {'name': stock.name, 'unit': stock.unit, 'num': stock.num, 'price': stock.price,
                    'amount': stock.amount, 'opening_price': stock.opening_price,
                    'opening_amount': stock.opening_amount,
                    'remarks': stock.remarks}
            return {'errcode': 0, 'msg': '', 'data': data}
        return {'errcode': 1, 'msg': '无此货物'}

    # 分页库存列表
    async def stockPagination(self, requestData):
        stocks = await Stock.get_stocks(requestData['result'])
        stockList = []
        perPage = 10
        for item in stocks[(int(requestData['page']) - 1) * perPage: perPage * int(requestData['page'])]:
            stockList.append(
                {'id': str(item.id), 'name': item.name, 'unit': item.unit, 'num': item.num, 'price': item.price,
                 'amount': item.amount,
                 'opening_price': item.opening_price, 'opening_amount': item.opening_amount,
                 'remarks': item.remarks})
        return {'errcode': 0, 'msg': '', 'data': {'list': stockList, 'count': len(stocks), 'perPage': perPage}}

    # 删除物料
    async def deleteStock(self, requestData):
        return await Stock.delete_stock(requestData['id'])

    # 物料名称列表
    async def getStockNames(self, requestData):
        stocks = await Stock.get_stocks(True)
        namelist = []
        for item in stocks:
            namelist.append(item.name)
        return {'errcode': 0, 'msg': '', 'data': {'list': namelist}}

    # 创建模板
    async def createTem(self, requestData):
        return await GoodsTemplate.new_goods_template(requestData['name'], requestData['remarks'], requestData['goods'])

    # 模板详情
    async def templateDetail(self, requestData):
        data = await GoodsTemplate.get_tem_goods_list(requestData['id'])
        if data:
            return {'errcode': 0, 'msg': '', 'data': data}
        return {'errcode': 1, 'msg': '无此模板'}

    # 更新模板
    async def updateTem(self, requestData):
        return await GoodsTemplate.update_goods_template(requestData['name'], requestData['remarks'],
                                                         requestData['goods'])

    async def getTemList(self, requestData):
        temList = await GoodsTemplate.goods_template_list()
        data = []
        for item in temList:
            goods = await GoodsTemplate.get_tem_goods_list(str(item.id))
            data.append({'name': item.name, 'remarks': item.remarks, 'id': str(item.id), 'goods': goods['list']})
        return {'errcode': 0, 'msg': '', 'data': {'list': data}}

    # 模板列表 分页
    async def getTemListPage(self, requestData):
        temList = await GoodsTemplate.goods_template_list(requestData['result'])
        data = []
        perPage = 10
        for item in temList[(int(requestData['page']) - 1) * perPage: perPage * int(requestData['page'])]:
            data.append({'name': item.name, 'remarks': item.remarks, 'id': str(item.id)})
        return {'errcode': 0, 'msg': '', 'data': {'list': data, 'count': len(temList), 'perPage': perPage}}

    # 删除模板
    async def deleteTem(self, requestData):
        return await GoodsTemplate.delete_goods_template(requestData['id'])

    # 创建客户
    async def createCustomer(self, requestData):
        if len(requestData['checkedStocks']) > 0:
            customer = await Customer.new_customer(requestData['form']['name'], requestData['form']['address'],
                                                   requestData['form']['tel'], requestData['form']['remarks'])
            for i in requestData['checkedStocks']:
                await CustomerGoodsDetail.new_c_detail(customer.inserted_id, i)
            return {'errcode': 0, 'msg': '创建新客户成功'}
        return {'errcode': 1, 'msg': '请选择客户所需的物料'}

    # 获取客户信息
    async def getCustomer(self, requestData):
        customer = await Customer.get_customer(requestData['id'])
        customer_goods = await CustomerGoodsDetail.get_customer_goods(requestData['id'])
        customer_repay = await CustomerRepayDetail.get_repay_list(requestData['id'])
        goods_list = []
        repay_list = []
        if customer_goods:
            for goods in customer_goods:
                goods_list.append(
                    {'id': str(goods.id), 'stock_name': goods.stock_name, 'stock_num': goods.stock_num,
                     'stock_price': goods.stock_price, 'stock_amount': goods.stock_amount})
        if customer_repay:
            for repay in customer_repay:
                repay_list.append({'amount': repay.money, 'time': repay.time})
        if customer:
            data = {'name': customer.name, 'tel': customer.tel, 'address': customer.address,
                    'remarks': customer.remarks}
            return {'errcode': 0, 'msg': '', 'data': {'info': data, 'goods_list': goods_list, 'repay_list': repay_list}}
        return {'errcode': 1, 'msg': '无此客户'}

    # 更新客户信息
    async def updateCus(self, requestData):
        return await Customer.update_customer(requestData['id'], requestData['form']['address'],
                                              requestData['form']['tel'], requestData['form']['remarks'])

    # 添加客户付款信息
    async def addCusRepay(self, requestData):
        if requestData['amount'] and requestData['time']:
            result = await CustomerRepayDetail.new_repay(requestData['id'], requestData['amount'], requestData['time'])
        else:
            result = {'errcode': 1, 'msg': '请填写完整'}
        return result

    # 更新客户的物料
    async def updateCusGoods(self, requestData):
        for i in requestData['goodsList']:
            await CustomerGoodsDetail.update_customer_goods(i['id'], requestData['id'], i['stock_num'],
                                                            i['stock_price'])
        return {'errcode': 0, 'msg': '修改成功'}

    # 获取客户列表 分页
    async def getCusList(self, requestData):
        customers = await Customer.get_customers(requestData['result'])
        data = []
        perPage = 10
        for item in customers[(int(requestData['page']) - 1) * perPage: perPage * int(requestData['page'])]:
            data.append({'id': str(item.id), 'name': item.name, 'tel': item.tel, 'address': item.address,
                         'remarks': item.remarks})
        return {'errcode': 0, 'msg': '', 'data': {'list': data, 'count': len(customers), 'perPage': perPage}}

    # 客户详情，添加物料
    async def addCusGoods(self,requestData):
        data = []
        for item in requestData['checkedStocks']:
            detail = await CustomerGoodsDetail.new_c_detail(requestData['customer_id'], item)
            if detail:
                data.append(detail)
        return {'errcode': 0, 'msg': '添加物料成功','data': {'list': data}}

    # 新建管理员
    async def createAdmin(self, requestData):
        if requestData['password'] == requestData['surePsd']:
            uid = random_str()
            ifuser = True
            while ifuser:
                ifuser = await Users.find_one({"uid": uid})
                if ifuser:
                    uid = random_str()
                else:
                    ifuser = False
            user_login = str(COMMON_USER_TYPE) + str(int(time.time())) + random_str()
            userToken = generateUserToken(uid, user_login)
            result = await Users.new_user(uid, userToken['token'], requestData['user'], requestData['password'],
                                          requestData['name'], requestData['department'], requestData['position'],
                                          requestData['tel'], requestData['email'], requestData['qq'],
                                          requestData['wechat'], expires_time=userToken['expiretime'])
            return result
        return {'errcode': 1, 'msg': '两次密码不一致'}

    # 管理员详情
    async def getAdminDetail(self, requestData):
        user = await Users.get_user(requestData['id'])
        if user:
            data = {'username': user.user, 'name': user.real_name, 'tel': user.tel, 'department': user.department,
                    'position': user.position, 'email': user.email, 'qq': user.qq, 'wechat': user.wechat}
            return {'errcode': 0, 'msg': '', 'data': data}

        return {'errcode': 1, 'msg': '无该管理员！'}

    # 删除管理员
    async def deleteAdmin(self, requestData):
        return await Users.delete_user(requestData['id'])

    #管理员列表 分页
    async def getAdmins(self,requestData):
        users = await Users.get_users()
        data = []
        perPage = 10
        for i in users[(int(requestData['page']) - 1) * perPage: perPage * int(requestData['page'])]:
            data.append({'id': str(i.id), 'username': i.user, 'type': i.type, 'name': i.real_name, 'tel': i.tel,
                         'is_active': i.is_active})
        return {'errcode': 0, 'msg': '', 'data': {'list': data, 'count': len(users), 'perPage': perPage}}


# 物料

# 新建物料
async def newStock(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().createStock)
    return web.json_response(result)


class StockDetail(web.View):
    # 某物料详情
    async def get(self):
        query = dict(self.request.query)
        requestData = {'id': query['id'], 'token': query['token'], 'username': query['username']}
        result = await judgeUser(requestData, UserLogic().getStockDetail)
        return web.json_response(result)

    # 修改某物料
    async def post(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await judgeUser(requestData, UserLogic().updateStock)
        return web.json_response(result)


class StockList(web.View):
    # 物料列表 有分页
    async def get(self):
        query = dict(self.request.query)
        requestData = {'token': query['token'], 'username': query['username'], 'result': query['result'],
                       'page': query['page']}
        result = await judgeUser(requestData, UserLogic().stockPagination)
        return web.json_response(result)

    # 删除某物料
    async def post(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await judgeUser(requestData, UserLogic().deleteStock)
        return web.json_response(result)


# 物料名称列表
async def getStockNames(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().getStockNames)
    return web.json_response(result)


# 模板接口

# 创建模板
async def newTemplate(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().createTem)
    return web.json_response(result)


# 模板详情
async def temDetail(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().templateDetail)
    return web.json_response(result)


# 修改模板信息
async def updateTemplate(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().updateTem)
    return web.json_response(result)


# 模板列表 分页
async def temListPage(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().getTemListPage)
    return web.json_response(result)


# 模板列表 所有列表
async def temList(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().getTemList)
    return web.json_response(result)


# 删除模板
async def deleteTemplate(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().deleteTem)
    return web.json_response(result)


# 客户
class Customers(web.View):
    # 新建客户
    async def put(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await judgeUser(requestData, UserLogic().createCustomer)
        return web.json_response(result)

    # 获取客户列表
    async def post(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await judgeUser(requestData, UserLogic().getCusList)
        return web.json_response(result)

    # 客户信息
    async def get(self):
        query = dict(self.request.query)
        requestData = {'token': query['token'], 'username': query['username'], 'id': query['id']}
        result = await judgeUser(requestData, UserLogic().getCustomer)
        return web.json_response(result)


# 更新客户基本信息
async def updateCustomer(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().updateCus)
    return web.json_response(result)


# 添加客户付款信息
async def addRepay(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().addCusRepay)
    return web.json_response(result)


# 更新客户用料信息
async def updateCusGoods(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().updateCusGoods)
    return web.json_response(result)

# 添加物料 客户详情
async def addCusGoods(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await judgeUser(requestData, UserLogic().addCusGoods)
    return web.json_response(result)

class Adminitors(web.View):
    # 新建管理员
    async def put(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await judgeUser(requestData, UserLogic().createAdmin)
        return web.json_response(result)

    # 管理员列表
    async def get(self):
        query = dict(self.request.query)
        requestData = {'token': query['token'], 'username': query['username'], 'page': query['page'], 'result': query['result']}
        result = await judgeUser(requestData, UserLogic().getAdmins)
        return web.json_response(result)


    # 删除管理员
    async def post(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        result = await judgeUser(requestData, UserLogic().deleteAdmin)
        return web.json_response(result)


class Adminitor(web.View):
    # 管理员详情
    async def get(self):
        query = dict(self.request.query)
        requestData = {'username': query['username'], 'token': query['token'], 'id': query['id']}
        result = await judgeUser(requestData, UserLogic().getAdminDetail)
        return web.json_response(result)
