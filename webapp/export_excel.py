import xlwt
from xlwt import *
from store.models import Customer,CustomerGoodsDetail,CustomerRepayDetail


style0 = xlwt.easyxf(num_format_str='#,##0.00')  # 数字的格式
font_center = xlwt.easyxf('font: bold on; align: wrap on, vert centre, horiz center')  # 居中 加粗
font_vert_center = xlwt.easyxf('align: wrap on, vert centre')  # 居中 加粗
style_datetime = xlwt.easyxf('align: wrap on, vert centre,horiz left', num_format_str='D-MMM-YY')


async def export_customer_detail(path, customer_id):
    customer = await Customer.get_customer(customer_id)
    customer_goods = await CustomerGoodsDetail.get_customer_goods(customer_id)
    customer_repay = await CustomerRepayDetail.get_repay_list(customer_id)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(customer.name)
    # write_merge 合并单元格
    # 单元格的宽度
    ws.col(0).width = 3333
    ws.col(6).width = 3333
    ws.col(7).width = 3333
    ws.write_merge(0, 0, 0, 7, customer.name + ' -- 物料使用列表详情', font_center)
    ws.write(1, 0, '名称', font_center)
    ws.write(1, 1, '单价', font_center)
    ws.write(1, 2, '数量', font_center)
    ws.write(1, 3, '金额', font_center)
    ws.write(1, 5, '总额', font_center)
    ws.write(1, 6, '已付款金额', font_center)
    ws.write(1, 7, '付款日期', font_center)
    col = t = 1
    sum = 0
    for item in customer_goods:
        if item.stock_num > 0:
            col += 1
            ws.write(col, 0, item.stock_name)
            ws.write(col, 1, item.stock_price)
            ws.write(col, 2, item.stock_num)
            ws.write(col, 3, item.stock_amount)
            sum += item.stock_amount

    for itemR in customer_repay:
        t += 1
        ws.write(t, 6, itemR.money)
        ws.write(t, 7, itemR.time)
    ws.write(2, 5, sum)
    wb.save(path)
