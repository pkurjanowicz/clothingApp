import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', 
    component: 'home', 
    props: {
      title: 'Home Page',
      },
    },
  { path: '/login', 
    component: 'login', 
    props: {
      title: 'Login' 
    }
  },
  { path: '/register', 
    component: 'register', 
    props: {
      title: 'Register' 
    },
  },
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/views/${route.component}.vue`)
  }
})
Vue.use(Router)
export default new Router({
  routes,
  mode: 'history'
})
