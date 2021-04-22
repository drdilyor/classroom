import Vue from 'vue'
import VueToasted from 'vue-toasted';
import './assets/styles/styles.scss'

import App from './App.vue'
import router from './routes'
import auth from './auth'
import api from './api'
import store from './store'

import Loading from '@/components/Loading.vue'

Vue.use(VueToasted, {
    iconPack : 'material',
});

Vue.config.productionTip = false
Vue.prototype.$backend = 'http://localhost:8000'
Vue.prototype.$auth = auth
Vue.prototype.$api = api
Vue.component('Loading', Loading)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')
