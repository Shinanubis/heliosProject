import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home.vue'
import Food from '../views/Food.vue'

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
      path: '/:id',
      name: 'Food',
      component: Food,
    },

  ],
})
