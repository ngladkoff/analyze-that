import 'core-js/stable'
import Vue from 'vue'
import App from './App'
import router from './router'
import CoreuiVue from '@coreui/vue'
import { iconsSet as icons } from './assets/icons/icons.js'
import store from './store'
import Amplify from 'aws-amplify';
import '@aws-amplify/ui-vue';
import aws_exports from './aws-exports';
import { I18n } from 'aws-amplify';
import axios from 'axios'
import VueAxios from 'vue-axios'

I18n.setLanguage('es');

const dict = {
  'es': {
    'Sign In': "Ingresar",
    'Sign Up': "Registrarse",
    'Sign in to your account': "Ingresar a su cuenta",
    'Forgot your password?': "Olvidó su contraseña?",
    'Reset password': "Resetear contraseña",
    'No account?': "No tiene cuenta?",
    'Create account': "Crear cuenta"
  }
}

I18n.putVocabularies(dict);

Amplify.configure(aws_exports);

Vue.config.performance = true
Vue.use(CoreuiVue)
Vue.prototype.$log = console.log.bind(console)
Vue.use(VueAxios, axios)

new Vue({
  el: '#app',
  router,
  store,
  icons,
  template: '<App/>',
  components: {
    App
  }
})
