import Vue from 'vue'
import vuetify from './plugins/vuetify'
import './plugins/base'
import App from './App.vue'
import router from './router'
import store from './store'
import Vue2Filters from 'vue2-filters'

Vue.config.productionTip = false

new Vue({
  vuetify,
  router,
  store,
  Vue2Filters,
  render: h => h(App),
}).$mount('#app')
