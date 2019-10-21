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
import { isAuthenticated } from '/Users/peterkurjanowicz/Desktop/Interesting Projects/clothing_match_app/clothing_match_app/client/src/helpers.js'

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
</style>
