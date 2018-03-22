// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css'
import "babel-polyfill";


Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (!to.path.includes('login') && !localStorage.getItem('userInfo')) {
    next('/login')
  } else {
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
