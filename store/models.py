import datetime
from bson.objectid import ObjectId
from umongo import Instance, Document, fields, validate, ValidationError
from . import instance


# 库存
@instance.register
class Stock(Document):
    name = fields.StringField(unique=True, required=True)  # 名称
    num = fields.IntField(missing=0)  # 数量
    unit = fields.StringField()  # 单位
    opening_price = fields.FloatField()  # 进价
    price = fields.FloatField()  # 单价
    opening_amount = fields.FloatField()  # 进价总额
    amount = fields.FloatField()  # 总额
    remarks = fields.StringField()  # 备注
    is_active = fields.BooleanField(missing=True)  # 记录有效性
    created_time = fields.DateTimeField(missing=datetime.datetime.now)  # 记录时间

    @classmethod
    async def create_stock(cls, name='', num=0, unit='', opening_price=0, price=0, remarks=''):
        stock = await cls.find_one({"name": name})
        if stock:
            return {'errcode': 1, 'msg': '已经有了库存，换个名字吧'}
        await cls(name=name,
                  num=num,
                  unit=unit,
                  opening_price=opening_price,
                  price=price,
                  opening_amount=opening_price * num,
                  amount=price * num,
                  remarks=remarks).commit()
        return {'errcode': 0, 'msg': ''}

    # 获取库存列表
    @classmethod
    async def get_stocks(cls, is_active=None):
        if is_active == 'true' or is_active == True:
            return await cls.find({"is_active": True}).to_list(length=None)
        return await cls.find({"is_active": False}).to_list(length=None)

    # 获取库存
    @classmethod
    async def get_stock(cls, id=''):
        try:
            return await cls.find_one({'id': ObjectId(id)})
        except:
            return None

    # 删除库存
    @classmethod
    async def delete_stock(cls, id=''):
        stock = await cls.get_stock(id)
        if stock:
            stock.is_active = False
            await stock.commit()
            return {'errcode': 0, 'msg': '已删除'}
        return {'errcode': 1, 'msg': '没有此货物'}

    # 修改库存
    @classmethod
    async def update_stock(cls, name='', num=0, unit='', opening_price=0, price=0, remarks=''):
        stock = await cls.find_one({"name": name})
        if stock:
            if stock.num == num and stock.unit == unit and stock.opening_price == opening_price and stock.price == price and stock.remarks == remarks:
                return {'errcode': 1, 'msg': '您没有任何修改'}
            stock.num = num
            stock.unit = unit
            stock.opening_price = opening_price
            stock.price = price
            stock.opening_amount = opening_price * num
            stock.amount = price * num
            stock.remarks = remarks
            await stock.commit()
            return {'errcode': 0, 'msg': ''}
        return {'errcode': 1, 'msg': '没有此货物'}


# 模板
@instance.register
class GoodsTemplate(Document):
    name = fields.StrField(unique=True, required=True)  # 名称
    goods = fields.ListField(fields.ReferenceField(Stock))  # 用料列表
    remarks = fields.StringField()  # 备注
    is_active = fields.BooleanField(missing=True)  # 记录有效性
    created_time = fields.DateTimeField(missing=datetime.datetime.now)  # 记录时间

    @classmethod
    async def new_goods_template(cls, name='', remarks='', goods=[]):
        stock = await cls.find_one({"name": name})
        if stock:
            return {'errcode': 1, 'msg': '模板已存在，换个名字吧'}
        list = []
        for item in goods:
            stock = await Stock.find_one({'name': item})
            list.append(stock)
        print('new_goods_template', list)
        await cls(name=name,
                  goods=list,
                  remarks=remarks).commit()
        return {'errcode': 0, 'msg': '添加成功'}

    # 获取模板信息
    @classmethod
    async def get_tem_goods_list(cls, id=''):
        try:
            data = await cls.find_one({'id': ObjectId(id)})
            list = []
            for good in data.goods:
                stock = await Stock.get_stock(good.pk)
                list.append(stock.name)
            return {'name': data.name, 'remarks': data.remarks, 'list': list}
        except:
            return None

    # 模板列表
    @classmethod
    async def goods_template_list(cls, is_active=None):
        if is_active == None:
            return await cls.find({"is_active": True}).to_list(length=None)
        return await cls.find({"is_active": is_active}).to_list(length=None)

    # 更新模板
    @classmethod
    async def update_goods_template(cls, name='', remarks='', good=[]):
        goods_tem = await cls.find_one({"name": name})
        if goods_tem:
            list = []
            for item in good:
                stock = await Stock.find_one({'name': item})
                list.append(stock)
            goods_tem.goods = list
            goods_tem.remarks = remarks
            await goods_tem.commit()
            return {'errcode': 0, 'msg': '修改成功'}
        return {'errcode': 1, 'msg': '没有此模板'}


# 顾客信息
@instance.register
class Customer(Document):
    name = fields.StrField()  # 姓名
    address = fields.StringField()  # 住址
    tel = fields.StringField()  # 电话号码
    remarks = fields.StringField()  # 备注
    is_active = fields.BooleanField(missing=True)  # 记录有效性
    created_time = fields.DateTimeField(missing=datetime.datetime.now)  # 记录时间

    @classmethod
    async def new_customer(cls, name='', address='', tel='', remarks=''):
        return await cls(name=name,
                         address=address,
                         tel=tel,
                         remarks=remarks).commit()


# 客户用料
@instance.register
class CustomerGoodsDetail(Document):
    customer = fields.ReferenceField(Customer)  # 顾客
    stock = fields.ReferenceField(Stock)  # 货物
    stock_num = fields.StringField()  # 数量
    stock_price = fields.StringField()  # 单价
    stock_amount = fields.StringField()  # 金额
    is_active = fields.BooleanField(missing=True)  # 记录有效性
    created_time = fields.DateTimeField(missing=datetime.datetime.now)  # 记录时间

    @classmethod
    async def new_c_detail(cls,customer_id='',stock_name='', stock_num='', stock_price='', stock_amount=''):
        customer = await Customer.find_one({'id': ObjectId(customer_id)})
        stock = await Stock.find_one({'name': stock_name})
        return await cls(customer=customer,
                         stock=stock,
                         stock_num=stock_num,
                         stock_price=stock_price,
                         stock_amount=stock_amount).commit()
