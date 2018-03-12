import axios from 'axios'
axios.defaults.timeout = 10000
import qs from 'qs'
// import store from '../store'
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8'
export default {
  // get请求
  fetchGet (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.get(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        // store.commit('TOAST_STATE', {text: '访问异常', time: 2000})
        reject(error)
      })
    })
  },
  // post请求
  fetchPost (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.post(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        // store.commit('TOAST_STATE', {text: '访问异常', time: 2000})
        reject(error)
      })
    })
  },
  fetchPut (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.put(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        // store.commit('TOAST_STATE', {text: '访问异常', time: 2000})
        reject(error)
      })
    })
  },
  fetchDelete (url, params = {}) {
    return new Promise((resolve, reject) => {
      axios.delete(url, params).then(res => {
        resolve(res.data)
      }).catch(error => {
        // store.commit('TOAST_STATE', {text: '访问异常', time: 2000})
        reject(error)
      })
    })
  }
}
