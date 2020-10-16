import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Fish from '../views/Fish.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: '',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/fish',
      name: 'Fish',
      component: Fish,
    },
  ],
})
