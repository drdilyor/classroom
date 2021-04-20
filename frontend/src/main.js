import Vue from 'vue'
import './assets/styles/styles.scss'

import App from './App.vue'
import router from './routes'
import auth from './auth'
import api from './api'
import store from './store'

Vue.config.productionTip = false
Vue.prototype.$backend = 'http://localhost:8000'
Vue.prototype.$auth = auth
Vue.prototype.$api = api

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
