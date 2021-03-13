import Vue from 'vue'
import './assets/scss/styles.scss'

import App from './App.vue'
import router from './routes'

Vue.config.productionTip = false
Vue.prototype.$backend = 'http://localhost:8000'

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
