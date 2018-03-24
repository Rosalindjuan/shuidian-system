import pathlib
from .views import Home, initData, StockList, newStock, StockDetail, getStockNames, newTemplate, temList, temListPage, \
    temDetail, updateTemplate, Customers, addRepay, updateCusGoods, updateCustomer, deleteTemplate, Adminitors, \
    Adminitor, login

import re

PROJECT_ROOT = pathlib.Path(__file__).parent

routes = [
    ('*', '/', Home, 'home', True),
    ('GET', '/init', initData, 'init', True),
    ('*', '/stock', StockList, 'stock', True),
    ('PUT', '/new_stock', newStock, 'new_stock', True),
    ('*', '/stock_detail', StockDetail, 'stock_detail', True),
    ('POST', '/get_stocks', getStockNames, 'get_stocks', True),
    ('POST', '/new_template', newTemplate, 'new_template', True),
    ('POST', '/template_list', temList, 'template_list', True),
    ('POST', '/template_list_page', temListPage, 'template_list_page', True),
    ('POST', '/tem_detail', temDetail, 'tem_detail', True),
    ('POST', '/update_template', updateTemplate, 'update_template', True),
    ('POST', '/delete_template', deleteTemplate, 'delete_template', True),
    ('*', '/customer', Customers, 'customer', True),
    ('POST', '/add_repay', addRepay, 'add_repay', True),
    ('POST', '/update_cus_goods', updateCusGoods, 'update_cus_goods', True),
    ('POST', '/update_customer', updateCustomer, 'update_customer', True),
    ('*', '/set_admin', Adminitors, 'set_admin', True),
    ('*', '/admin', Adminitor, 'admin', True),
    ('POST', '/to_login', login, 'to_login', True)

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
