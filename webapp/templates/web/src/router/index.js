import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/stock_list'
    },
    {
      path: '/stock_list',
      component: resolve => require(['../components/common/Home.vue'], resolve),
      children: [
        {
          path: '/',
          component: resolve => require(['../components/page/StockList.vue'], resolve),
          meta: {pageTitle: '物料列表'},
        },
        {
          path: '/stock_new',
          component: resolve => require(['../components/page/StockNew.vue'], resolve),
          meta: {pageTitle: '新建物料'},
        },
        {
          path: ':id',
          component: resolve => require(['../components/page/StockNew.vue'], resolve),
          meta: {pageTitle: '物料详情'},
        },
        {
          path: '/customer_list',
          component: resolve => require(['../components/page/CustomerList.vue'], resolve),
          meta: {pageTitle: '客户列表'},
        },
        {
          path: '/customer_list/:id',
          component: resolve => require(['../components/page/CustomerDetail.vue'], resolve),
          meta: {pageTitle: '客户详情'},
        },
        {
          path: '/customer_new',
          component: resolve => require(['../components/page/CustomerNew.vue'], resolve),
          meta: {pageTitle: '新建客户'},
        },
        {
          path: '/template_list',
          component: resolve => require(['../components/page/TemplateList.vue'], resolve),
          meta: {pageTitle: '模板列表'},
        },
        {
          path: '/template_new',
          component: resolve => require(['../components/page/TemplateNew.vue'], resolve),
          meta: {pageTitle: '新建模板'},
        },
        {
          path: '/template_list/:id',
          component: resolve => require(['../components/page/TemplateNew.vue'], resolve),
          meta: {pageTitle: '模板详情'},
        },
        {
          path: '/admin_list',
          component: resolve => require(['../components/page/AdminList.vue'], resolve),
          meta: {pageTitle: '管理员列表'},
        },
        {
          path: '/admin_list/:id',
          component: resolve => require(['../components/page/AdminDetail.vue'], resolve),
          meta: {pageTitle: '管理员详情'},
        },
        {
          path: '/admin_new',
          component: resolve => require(['../components/page/AdminNew.vue'], resolve),
          meta: {pageTitle: '新建管理员'},
        }
      ]
    },
    {
      path: '/login',
      component: resolve => require(['../components/page/Login.vue'], resolve),
      meta: {pageTitle: '登录'},
    },
  ]
})
