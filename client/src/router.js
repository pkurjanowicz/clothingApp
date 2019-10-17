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

const isAuthenticated = () => axios.get('checksession')
    .then(function (response){
      console.log(response.data)
      return response.data
    })
    .catch(function (error) {
    console.log(error);
  });


// isAuthenticated().then(function(result) {
//   return result.data
// });

// MovieLibrary.getGenres = function() {
//   var promise = new Promise(function(resolve, reject) {
//     /* missing implementation */
//     resolve(result);
//   });

//   return promise;
// };

// MovieLibrary.getGenres().then(function(result) {
//     // you can access the result from the promise here
// });

router.beforeEach((to, from, next) => {
  console.log('BeforeEach called')
  if (isAuthenticated() === 'False') {
    // console.log("This is isAuthenticated: " + isAuthenticated())
    console.log('stopped from going to next route')
    ('/login')
  } 
  else {
    console.log('made it to next route')
    next()
  }
})





