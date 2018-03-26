// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
import "babel-polyfill";
import {getStore} from "./utils/storage";
import {setWechatTitle} from "./utils/setWechatTitle";

Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  // 设置页面标题
  typeof to.meta.pageTitle !== undefined && setWechatTitle(to.meta.pageTitle)

  if (!to.path.includes('login') && !getStore('userInfo')) {
    next('/login')
  } else {
    store.commit('GET_USERINFO')
    next()
  }
})

Vue.use(ElementUI);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
})
