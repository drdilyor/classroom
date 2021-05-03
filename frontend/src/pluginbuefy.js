import Vue from 'vue'
import config, {setOptions, setVueInstance} from 'buefy/src/utils/config'
import {merge, Button, Icon, Navbar, SnackbarProgrammatic} from 'buefy'
import '@/assets/styles/buefy.scss'
import '@/assets/materialdesignicons/materialdesignicons.scss'

const options = {
}

window.Vue = Vue
setVueInstance(Vue)
setOptions(merge(config, options, true))

Vue.use(Button)
Vue.use(Icon)
Vue.use(Navbar)

if (!Vue.prototype.$buefy) Vue.prototype.$buefy = {}
Vue.prototype.$buefy.snackbar = SnackbarProgrammatic
