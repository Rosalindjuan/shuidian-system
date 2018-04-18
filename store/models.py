import datetime
from bson.objectid import ObjectId
from umongo import Instance, Document, fields, validate, ValidationError
from . import instance
import time
from webapp.utils import generateUserToken, SUPER_USER_TYPE, random_str, COMMON_USER_TYPE

@instance.register
class Users(Document):
    uid = fields.StringField(unique=True, required=True)  # 管理员uid
    token = fields.StrField(unique=True, required=True)  # 管理员登录token
    user = fields.StringField(unique=True, required=True)  # 管理员登录用户名
    password = fields.StringField()  # 管理员登录密码
    type = fields.StringField()  # 管理员类型 -- 超级管理员/普通管理员
    real_name = fields.StringField()  # 管理员真实姓名
    department = fields.StringField()  # 管理员部门
    position = fields.StringField()  # 管理员职位
    tel = fields.StringField()  # 移动电话
    email = fields.StringField()  # 邮箱
    qq = fields.StringField()  # qq号
    wechat = fields.StringField()  # 微信
    is_active = fields.BooleanField(missing=True)  # 记录有效性
    expires_time = fields.IntegerField()  # token过期时间
    created_time = fields.DateTimeField(missing=datetime.datetime.now)  # 记录时间

    class Meta:
        collection_name = 'users'

    # 新建管理员
    @classmethod
    async def new_user(cls, uid='', token='', user='', password='', real_name='', department='', position='', tel='', email='',
                       qq='', wechat='', type='普通管理员',expires_time=''):
        ifuser = await cls.find_one({"user": user})
        if ifuser:
            return {'errcode': 1, 'msg': '已经有了该用户，换个名字吧'}
        await cls(uid=uid,
                  token=token,
                  user=user,
                  password=password,
                  type=type,
                  real_name=real_name,
                  department=department,
                  position=position,
                  tel=tel,
                  email=email,
                  qq=qq,
                  wechat=wechat,
                  expires_time=expires_time).commit()
        return {'errcode': 0, 'msg': '添加成功'}

    # 查找管理员 用户登录
    @classmethod
    async def user_login(cls, user='', password=''):
        try:
            user = await cls.find_one({'user': user})
            if user.password == password:
                # print(user.expires_time , time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(user.expires_time)))
                if user.expires_time <= int(time.time()):
                    print('过期了')
                    type = COMMON_USER_TYPE if user.type == '普通管理员' else SUPER_USER_TYPE
                    user_login = str(type) + str(int(time.time())) + random_str()
                    userToken = generateUserToken(user.uid, user_login)
                    user.token = userToken['token']
                    user.expires_time = userToken['expiretime']
                    await user.commit()
                return {'errcode': 0, 'msg': '用户登录成功', 'data': {'user': user.user,'token':user.token}}
            else:
                return {'errcode': 1, 'msg': '密码错误，请重新输入密码'}
        except:
            return {'errcode': 1, 'msg': '没有该用户'}

    # 更新管理员
    @classmethod
    async def update_user(cls, id='', department='', position='', tel='', email='', qq='', wechat=''):
        ifuser = await cls.find_one({"id": ObjectId('id')})
        if ifuser:
            ifuser.department = department
            ifuser.position = position
            ifuser.tel = tel
            ifuser.email = email
            ifuser.qq = qq
            ifuser.wechat = wechat
            await ifuser.commit()
            return {'errcode': 0, 'msg': '已修改'}
        return {'errcode': 1, 'msg': '没有此管理员'}

    # 获取管理员列表
    @classmethod
    async def get_users(cls):
        return await cls.find({"is_active": True}).sort([('created_time', -1)]).to_list(length=None)

    # 用户token
    @classmethod
    async def get_user_token(cls, user='',token=''):
        try:
            return await cls.find_one({"user": user, 'token': token})
        except:
            return None


    # 获取管理员列表
    @classmethod
    async def get_user(cls, id=''):
        try:
            return await cls.find_one({"id": ObjectId(id)})
        except:
            return None

    # 删除管理员
    @classmethod
    async def delete_user(cls, id=''):
        try:
            user = await cls.find_one({"id": ObjectId(id)})
            user.is_active = False
            await user.commit()
            return {'errcode': 0, 'msg': '已删除'}
        except:
            return {'errcode': 1, 'msg': '没有此管理员,请检查管理员列表'}


# 物料
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

    class Meta:
        collection_name = 'stock'

    @classmethod
    async def create_stock(cls, name='', num=0, unit='', opening_price=0, price=0, remarks=''):
        stock = await cls.find_one({"name": name})
        if stock:
            return {'errcode': 1, 'msg': '已经有了物料，换个名字吧'}
        await cls(name=name,
                  num=num,
                  unit=unit,
                  opening_price=opening_price,
                  price=price,
                  opening_amount=opening_price * num,
                  amount=price * num,
                  remarks=remarks).commit()
        return {'errcode': 0, 'msg': '添加成功'}

    # 获取物料列表
    @classmethod
    async def get_stocks(cls, is_active=None):
        if is_active == 'true' or is_active == True:
            return await cls.find({"is_active": True}).sort([('created_time', 1)]).to_list(length=None)
        return await cls.find({"is_active": False}).sort([('created_time', 1)]).to_list(length=None)

    @classmethod
    async def get_stocks_count(cls):
        return await cls.find({"is_active": True}).count()

    # 获取物料
    @classmethod
    async def get_stock(cls, id=''):
        try:
            return await cls.find_one({'id': ObjectId(id)})
        except:
            return None

    # 删除物料
    @classmethod
    async def delete_stock(cls, id=''):
        try:
            stock = await cls.get_stock(id)
            stock.is_active = False
            await stock.commit()
            return {'errcode': 0, 'msg': '已删除'}
        except:
            return {'errcode': 1, 'msg': '没有此物料,请检查物料列表'}

    # 修改物料
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
            return {'errcode': 0, 'msg': '已修改'}
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
        # print('new_goods_template', list)
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
        if is_active == None or is_active == 'true':
            return await cls.find({"is_active": True}).sort([('created_time', -1)]).to_list(length=None)
        return await cls.find({"is_active": is_active}).sort([('created_time', -1)]).to_list(length=None)

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

    # 删除模板
    @classmethod
    async def delete_goods_template(cls, id=''):
        try:
            goods_tem = await cls.find_one({'id': ObjectId(id)})
            goods_tem.is_active = False
            await goods_tem.commit()
            return {'errcode': 0, 'msg': '已删除'}
        except:
            return {'errcode': 1, 'msg': '没有此模板,请仔细检查模板'}


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

    @classmethod
    async def get_customers(cls, is_active=None):
        if is_active == None or is_active == 'true':
            return await cls.find({"is_active": True}).sort([('created_time', -1)]).to_list(length=None)
        return await cls.find({"is_active": is_active}).sort([('created_time', -1)]).to_list(length=None)


    @classmethod
    async def get_customer(cls, id=''):
        try:
            return await cls.find_one({"id": ObjectId(id)})
        except:
            return None

    @classmethod
    async def update_customer(cls, id='', address='', tel='', remarks=''):
        customer = await cls.find_one({"id": ObjectId(id)})
        if customer:
            customer.address = address
            customer.tel = tel
            customer.remarks = remarks
            await customer.commit()
            return {'errcode': 0, 'msg': '修改成功'}
        return {'errcode': 1, 'msg': '修改失败，请稍后再试'}


# 客户用料
@instance.register
class CustomerGoodsDetail(Document):
    customer = fields.ReferenceField(Customer)  # 顾客
    stock_name = fields.StringField()  # 货物
    stock_num = fields.IntField(missing=0)  # 数量
    stock_price = fields.FloatField(missing=0)  # 单价
    stock_amount = fields.FloatField(missing=0)  # 金额
    is_active = fields.BooleanField(missing=True)  # 记录有效性
    created_time = fields.DateTimeField(missing=datetime.datetime.now)  # 记录时间

    @classmethod
    async def new_c_detail(cls, customer_id='', stock_name=''):
        customer = await Customer.find_one({'id': ObjectId(customer_id)})
        stock = await Stock.find_one({'name': stock_name})
        detail = await cls.find_one({'customer': ObjectId(customer_id), 'stock_name': stock_name})
        if customer and stock:
            if detail:
                pass
            else:
                c_detail = await cls(customer=customer,
                          stock_name=stock_name,
                          stock_price=stock.price).commit()
                return {'id': str(c_detail.inserted_id),'stock_name': stock_name, 'stock_num': 0,'stock_price': stock.price, 'stock_amount': 0}
        return None

    @classmethod
    async def get_customer_goods(cls, customer_id=''):
        return await cls.find({'customer': ObjectId(customer_id)}).to_list(length=None)

    @classmethod
    async def update_customer_goods(cls, id='', customer_id='', num=0, price=0):
        customer_goods = await cls.find_one({'id': ObjectId(id), 'customer': ObjectId(customer_id)})
        if customer_goods:
            customer_goods.stock_num = num
            customer_goods.stock_price = price
            customer_goods.stock_amount = num * price
            await customer_goods.commit()


# 客户付款金额
@instance.register
class CustomerRepayDetail(Document):
    customer = fields.ReferenceField(Customer)  # 顾客
    money = fields.StringField()  # 金额
    time = fields.StringField()  # 付款时间
    is_active = fields.BooleanField(missing=True)  # 记录有效性
    created_time = fields.DateTimeField(missing=datetime.datetime.now)  # 记录时间

    @classmethod
    async def new_repay(cls, customer_id='', money='', time=''):
        customer = await Customer.find_one({'id': ObjectId(customer_id)})
        try:
            await cls(customer=customer,
                      money=money,
                      time=time).commit()
            return {'errcode': 0, 'msg': '添加成功'}
        except:
            return {'errcode': 1, 'msg': '添加失败'}

    @classmethod
    async def get_repay_list(cls, customer_id=''):
        return await cls.find({'customer': ObjectId(customer_id)}).to_list(length=None)
