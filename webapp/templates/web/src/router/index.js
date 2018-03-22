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
          component: resolve => require(['../components/page/StockList.vue'], resolve)
        },
        {
          path: '/stock_new',
          component: resolve => require(['../components/page/StockNew.vue'], resolve)
        },
        {
          path: ':id',
          component: resolve => require(['../components/page/StockNew.vue'], resolve)
        },
        {
          path: '/customer_list',
          component: resolve => require(['../components/page/CustomerList.vue'], resolve)
        },
        {
          path: '/customer_list/:id',
          component: resolve => require(['../components/page/CustomerDetail.vue'], resolve)
        },
        {
          path: '/customer_new',
          component: resolve => require(['../components/page/CustomerNew.vue'], resolve)
        },
        {
          path: '/template_list',
          component: resolve => require(['../components/page/TemplateList.vue'], resolve)
        },
        {
          path: '/template_new',
          component: resolve => require(['../components/page/TemplateNew.vue'], resolve)
        },
        {
          path: '/template_list/:id',
          component: resolve => require(['../components/page/TemplateNew.vue'], resolve)
        },
        {
          path: '/admin_list',
          component: resolve => require(['../components/page/AdminList.vue'], resolve)
        },
        {
          path: '/admin_list/:id',
          component: resolve => require(['../components/page/AdminDetail.vue'], resolve)
        },
        {
          path: '/admin_new',
          component: resolve => require(['../components/page/AdminNew.vue'], resolve)
        }
      ]
    },
    {
      path: '/login',
      component: resolve => require(['../components/page/Login.vue'], resolve)
    },
  ]
})
