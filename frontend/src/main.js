import Vue from 'vue'
import './assets/styles/styles.scss'

import App from './App.vue'
import router from './routes'
import auth from './auth'

Vue.config.productionTip = false
Vue.prototype.$backend = 'http://localhost:8000'
Vue.prototype.$auth = auth

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
