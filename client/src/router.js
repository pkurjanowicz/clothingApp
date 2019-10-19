import Vue from 'vue'
import VueRouter from 'vue-router';
import axios from 'axios';

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
  { path: '/liked', 
    component: 'liked', 
    props: {
      title: 'Liked Images' 
    },
  },
]
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/views/${route.component}.vue`)
  }
})
Vue.use(VueRouter)

const router = new VueRouter({
  routes,
  mode: 'history'
})
export default router




