<template>
  <div id="app">
    <navBar v-if="!main"/>
    <!-- router view is referencing the router.js 
    file in order to create the routes -->
    <router-view></router-view>
  </div>
</template>

<script>
import navBar from './components/navBar.vue'
import { isAuthenticated } from './helpers.js'

/* this page just mounts all the elements */
export default {
  name: 'app',
  data() {
    return {
      userSessionID: null,
    }
  },
  components: {
    'navBar': navBar,
  },
  /* this checks to make sure the path isn't login or register and then it will show the navbar*/
  computed: {
    main(){
          return this.$route.path === '/login' || this.$route.path === '/register'
      }
  }
}

</script>

<style>
body {
    font-family: Arial, Helvetica, sans-serif;
}

button:hover {
    background-color: white;
    border: 3px;
    border-color:  grey;
    border-style: solid;
    color: grey;
    transition-duration: .3s;
}

button {
    padding: 10px;
    background-color: grey;
    font-size: 15px;
    color: white;
    border: 3px;
    border-color: grey;
    border-style: solid;
}

a {
    text-decoration: none;
}

li {
    list-style-type: none;
    margin: 10px;
}

input[type=text], input[type=password] {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    box-sizing: border-box;
}

input[type=file] {
    display:none;
}
</style>
