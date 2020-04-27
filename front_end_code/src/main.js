import Vue from 'vue'
import App from './App.vue'
import router from './router'
import './plugins/element.js'
import './assets/css/global.css'
import NProgress from 'nprogress'
import axios from 'axios'
axios.defaults.baseURL = 'http://url/api/v1/'
// 在request 拦截器中，展示进度条 NProgress.start()
axios.interceptors.request.use(config => {
  NProgress.start()
  config.headers.Authorization = window.sessionStorage.getItem('token')
  return config
})
axios.interceptors.response.use(config => {
  NProgress.done()
  return config
})
Vue.prototype.$http = axios
Vue.config.productionTip = false

// Vue.filter('dateFormat', function (originVal) {
//   const dt = new Date(originVal)
//   const y = dt.getFullYear()
//   const m = (dt.getMonth() + 1 + '').padStart(2, '0')
//   const d = (dt.getDate() + '').padStart(2, '0')
//   const hh = (dt.getHours() + '').padStart(2, '0')
//   const mm = (dt.getMinutes() + '').padStart(2, '0')
//   const ss = (dt.getSeconds() + '').padStart(2, '0')
//   return `${y}-${m}-${d} ${hh}:${mm}:${ss}`
// })

Vue.filter('dateFormat', function (originVal) {
  if (originVal == null || originVal === '') {
    return '暂无时间'
  } else {
    const d = new Date(originVal)
    const month = d.getMonth() + 1 < 10 ? '0' + (d.getMonth() + 1) : d.getMonth() + 1
    const day = d.getDate() < 10 ? '0' + d.getDate() : d.getDate()
    const hours = d.getHours() < 10 ? '0' + d.getHours() : d.getHours()
    const min = d.getMinutes() < 10 ? '0' + d.getMinutes() : d.getMinutes()
    const sec = d.getSeconds() < 10 ? '0' + d.getSeconds() : d.getSeconds()
    return d.getFullYear() + '-' + month + '-' + day + ' ' + hours + ':' + min + ':' + sec
  }
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
