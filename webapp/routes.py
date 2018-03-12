import pathlib
from .views import Home, StockList, newStock, StockDetail, getStocks, newTemplate, temList, temGoodsList, updateTemplate

import re

PROJECT_ROOT = pathlib.Path(__file__).parent

routes = [
    ('*', '/', Home, 'home', True),
    ('*', '/stock', StockList, 'stock', True),
    ('PUT', '/new_stock', newStock, 'new_stock', True),
    ('*', '/stock_detail', StockDetail, 'stock_detail', True),
    ('*', '/get_stocks', getStocks, 'get_stocks', True),
    ('POST', '/new_template', newTemplate, 'new_template', True),
    ('*', '/template_list', temList, 'template_list', True),
    ('POST', '/tem_goods_list', temGoodsList, 'tem_goods_list', True),
    ('POST', '/update_template', updateTemplate, 'update_template', True),

]


def setup_routes(app):
    # route part
    path = []
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])
        if route[4] is True:
            path.append(re.sub(r'{filename}$', '', route[1]))
    app.route_path = path

    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'templates/web/dist/static',
                          name='static')
