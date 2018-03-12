import argparse
import asyncio
import logging

import aiohttp_jinja2
import jinja2
# import aiohttp
from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient
from trafaret_config import commandline

from .middlewares import setup_middlewares
from .routes import setup_routes
from .utils import TRAFARET

from store import instance
#
# import aioredis
# from functools import partial
# import json
# import ujson

async def init_db(app):
    # creating a client
    conf = app.config['mongodb']
    client = AsyncIOMotorClient(
        'mongodb://{}:{}'.format(conf['host'], conf['port']))

    app.db_client = client
    app.db = client[conf['database']]
    instance.init(app.db)
    # print(app.db)


async def close_db(app):
    app.db_client.close()


def load_config(argv, path='config/join.yaml'):
    ap = argparse.ArgumentParser()
    commandline.standard_argparse_options(ap,
                                          default_config=path)
    #
    # define your command-line arguments here
    #
    options = ap.parse_args(argv)

    return commandline.config_from_options(options, TRAFARET)
#

from collections import defaultdict

def init_aiohttp_app(loop, logger=None, client_max_size=None, config=None):
    if logger:
        app = web.Application(loop=loop, logger=logger)
    else:
        app = web.Application(loop=loop)

    # load config from yaml file in current dir
    app.config = config

    # setup Jinja2 template renderer
    aiohttp_jinja2.setup(
        app, loader=jinja2.PackageLoader('webapp', 'templates'))


    # database
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    app.connection = defaultdict(set)

    # setup views and routes
    setup_routes(app)
    setup_middlewares(app)

    return app

def run_app(argv):

    config = load_config(argv)
    pulsar_config = config['pulsar']
    # init logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger('app.views')
    loop = asyncio.get_event_loop()

    host, port = pulsar_config['bind'].split(':')
    app = init_aiohttp_app(loop=loop, logger=logger, config=config)
    web.run_app(app,
                host=host,
                port=int(port))