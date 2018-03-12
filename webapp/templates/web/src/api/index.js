import http from './ajax'

// 新建库存
export const newStock = (params) => {
  return http.fetchPut('/new_stock', params)
}
// 库存列表
export const getStockList = (params) => {
  return http.fetchGet('/stock', params)
}
// 删除某库存
export const deleteStock = (params) => {
  return http.fetchPost('/stock', params)
}
// 获取某库存
export const getStock = (params) => {
  return http.fetchGet('/stock_detail', params)
}
//修改某库存
export const updateStock = (params) => {
  return http.fetchPost('/stock_detail', params)
}

//
//获取库存
export const getStocks = (params) => {
  return http.fetchPost('/get_stocks', params)
}

// 新建模板
export const newTemplate = (params) => {
  return http.fetchPost('/new_template', params)
}

// 模板列表
export const templateList = (params) => {
  return http.fetchPost('/template_list', params)
}


// 模板列表
export const temGoodsList = (params) => {
  return http.fetchPost('/tem_goods_list', params)
}

// 模板列表
export const updateTemplate = (params) => {
  return http.fetchPost('/update_template', params)
}
