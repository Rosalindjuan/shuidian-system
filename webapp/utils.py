#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by jason at 2017/3/4
import functools
import json
import asyncio
import trafaret as T


from time import time
from aiohttp import web, abc


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