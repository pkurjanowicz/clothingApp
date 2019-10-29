import Vue from 'vue'
import VueRouter from 'vue-router';
import axios from 'axios';

/* this is creating all router paths. When a user lands on the path
vue router will load component(this corresponds with the file names 
  in "view" folder). Props are just data we want to pass to the 
  html. */
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
  { path: '/my-images', 
    component: 'my-images', 
    props: {
      title: 'My Added Images' 
    },
  },
  { path: '/liked-images', 
    component: 'liked-images', 
    props: {
      title: 'My Liked Images' 
    },
  },
  { path: '/upload', 
    component: 'upload', 
    props: {
      title: 'Upload' 
    },
  },
  { path: '/messages', 
    component: 'messages', 
    props: {
      title: 'Your Messages' 
    },
  },
  { path: '/profile', 
    component: 'profile', 
    props: {
      title: 'Your Profile' 
    },
  },
]
/* this variable actually maps the 
route to the component in the views folder*/
const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/views/${route.component}.vue`)
  }
})
Vue.use(VueRouter)

/* this creates an instance 
of vuerouter and exports it*/ 
const router = new VueRouter({
  routes,
  mode: 'history'
})
export default router




