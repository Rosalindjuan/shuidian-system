import aiohttp_jinja2
from aiohttp import web

from store.models import Stock, GoodsTemplate,Customer
import json


class Home(web.View):
    @aiohttp_jinja2.template('web/dist/index.html')
    async def get(self):
        return {}


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
        for item in stocks:
            list.append({'id': str(item.id), 'name': item.name, 'unit': item.unit, 'num': item.num, 'price': item.price,
                         'amount': item.amount,
                         'opening_price': item.opening_price, 'opening_amount': item.opening_amount,
                         'remarks': item.remarks})
        return web.json_response({'errcode': 0, 'msg': '', 'data': {'list': list, 'count': 1000}})

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
        data.append({'name': l.name, 'remarks': l.remarks, 'id': str(l.id),'goods': goods_list['list']})
    return web.json_response({'errcode': 0, 'msg': '', 'data': {'list': data}})


# 模板货物列表
async def temGoodsList(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    data = await GoodsTemplate.get_tem_goods_list(requestData['id'])
    if data:
        return web.json_response({'errcode': 0, 'msg': '', 'data': data})
    return web.json_response({'errcode': 1, 'msg': '无此模板'})


async def updateTemplate(request):
    requestData = json.loads((await request.content.read()).decode('utf-8'))
    result = await GoodsTemplate.update_goods_template(requestData['name'], requestData['remarks'], requestData['goods'])
    return web.json_response(result)


# 客户
class Customers(web.View):
    # 新建客户
    async def put(self):
        requestData = json.loads((await self.request.content.read()).decode('utf-8'))
        await Customer.new_customer(requestData['name'],requestData['address'],requestData['tel'],requestData['remarks'])
        # query = dict(self.request.query)
        # stocks = await Stock.get_stocks(query['result'])
        # list = []
        # for item in stocks:
        #     list.append({'id': str(item.id), 'name': item.name, 'unit': item.unit, 'num': item.num, 'price': item.price,
        #                  'amount': item.amount,
        #                  'opening_price': item.opening_price, 'opening_amount': item.opening_amount,
        #                  'remarks': item.remarks})
        # return web.json_response({'errcode': 0, 'msg': '', 'data': {'list': list, 'count': 1000}})

    # 删除某库存
    # async def post(self):
    #     requestData = json.loads((await self.request.content.read()).decode('utf-8'))
    #     result = await Stock.delete_stock(requestData['id'])
    #     return web.json_response(result)
