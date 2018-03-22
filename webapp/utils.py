#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import json
import asyncio
import trafaret as T

import time
import hashlib
from random import Random

primitive_ip_regexp = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'

TRAFARET = T.Dict({
    T.Key('mongodb'):
        T.Dict({
            'database': T.String(),
            'user': T.String(),
            'password': T.String(),
            'host': T.String(),
            'port': T.Int(),
            'minsize': T.Int(),
            'maxsize': T.Int(),
        }),
    T.Key('wechat'):
        T.Dict({
            'appid': T.String(),
            'secret': T.String(),
            'token': T.String(),
        }),
    T.Key('pulsar'):
        T.Dict({
            'keep_alive': T.Int(),
            'bind': T.String(),
            'workers': T.Int(),
            'timeout': T.Int(),
            'max_requests': T.Int(),
        }),
    T.Key('redis'):
        T.Dict({
            'host': T.String(),
            'port': T.Int(),
            'minsize': T.Int(),
            'maxsize': T.Int(),
        }),
    # T.Key('host'): T.String(regex=primitive_ip_regexp),
    # T.Key('port'): T.Int(),
    T.Key('fernet_key'): T.String(),
    T.Key('debugtoolbar_enable'): T.Bool(),
    T.Key('pulsar_server_enable'): T.Bool(),
    T.Key('cdn'):
        T.Dict({
            'host': T.String(),
            'process_env': T.Bool(),
        }),
    T.Key('qiniu'):
        T.Dict({
            'access_key': T.String(),
            'secret_key': T.String(),
            'bucket_name': T.String(),
            'adir': T.String(),
            'replace_adir': T.String(),
        }),
})

SUPER_USER_TYPE = 1  # 超级管理员
COMMON_USER_TYPE = 2  # 普通管理员


# token的命名规则
# uid user_login 当前时间
# token过期时间为5小时

# 用户token
def generateUserToken(uid, user_login):
    data = uid + user_login + str(int(time.time()))
    token = hashlib.md5(data.encode("utf8"))
    # expiretime = int(time.time()) + 3600 * 5
    expiretime = int(time.time()) + 60 * 5
    userToken = {
        'token': token.hexdigest(),
        'expiretime': expiretime
    }
    return userToken


# 固定长度的随机字符串
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    ran = Random()
    for i in range(randomlength):
        str += chars[ran.randint(0, length)]
    return str
