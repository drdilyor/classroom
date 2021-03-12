import Vue from 'vue'
import 'materialize-css/dist/css/materialize.min.css'

import App from './App.vue'
import router from './routes'

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
