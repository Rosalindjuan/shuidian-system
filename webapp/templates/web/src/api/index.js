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

// 模板列表 分页
export const templateListPage = (params) => {
  return http.fetchPost('/template_list_page', params)
}


// 模板详情
export const temGoodsList = (params) => {
  return http.fetchPost('/tem_detail', params)
}

// 更新模板
export const updateTemplate = (params) => {
  return http.fetchPost('/update_template', params)
}

// 删除模板
export const deleteTemplate = (params) => {
  return http.fetchPost('/delete_template', params)
}
// 新建客户
export const newCustomer = (params) => {
  return http.fetchPut('/customer', params)
}

// 客户列表
export const getCustomers = (params) => {
  return http.fetchPost('/customer', params)
}

// 获取客户
export const getCustomer = (params) => {
  return http.fetchGet('/customer', params)
}

// 添加付款信息
export const addCusRepay = (params) => {
  return http.fetchPost('/add_repay', params)
}

// 更新客户用料信息
export const updateCusGoods = (params) => {
  return http.fetchPost('/update_cus_goods', params)
}

// 修改客户信息
export const updateCustomer = (params) => {
  return http.fetchPost('/update_customer', params)
}
// 修改客户信息
export const addCusGoods = (params) => {
  return http.fetchPost('/add_cus_goods', params)
}


// 管理员列表信息
export const getAdminList = (params) => {
  return http.fetchGet('/set_admin', params)
}

// 新建管理员
export const newAdmin = (params) => {
  return http.fetchPut('/set_admin', params)
}

// 删除管理员
export const deleteAdmin = (params) => {
  return http.fetchPost('/set_admin', params)
}


// 获取管理员
export const getAdmin = (params) => {
  return http.fetchGet('/admin', params)
}

// 获取管理员
export const toLogin = (params) => {
  return http.fetchPost('/to_login', params)
}

// 导出客户列表详情
export const exportCusDetail = (params) => {
  return http.fetchPost('/export_cus_detail', params)
}
