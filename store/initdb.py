#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Created by rosalind at 2018/2/26

import asyncio
import datetime

from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Document, fields

# from parser import join_v2_pb2 as join_pb2
from store import instance
# from store.models import User, DeviceType, Device


@instance.register
class Person(Document):
    name = fields.StrField(default='John Doe')
    time = fields.DateTimeField(missing=datetime.datetime.now)
    #name = fields.StrField(missing='John Doe')


client = AsyncIOMotorClient('mongodb://{}:{}'
                            .format('127.0.0.1', 27017))
instance.init(client.shuidiansystem)
loop = asyncio.get_event_loop()


async def initdb():
    # await DeviceType.ensure_indexes()
    # await Device.ensure_indexes()
    # await User.ensure_indexes()
    # await DeviceType(type_id=join_pb2.DEVICE_ZJTY150, pwd='asdfasdfasdf',
    #                  img='http://163.com', desc='asdfsdfs').commit()
    p = Person()
    print(p.name)
    print(p._data.get('name'))
    p.name = 'asdfasdf'
    print(p._data.get('name'))
    del p.name
    print(p._data.get('name'))
    await p.commit()

loop.run_until_complete(initdb())
