<template>
  <div id="app">
    <navBar/>
    <!-- router view is referencing the router.js 
    file in order to create the routes -->
    <router-view></router-view>
  </div>
</template>

<script>
import navBar from './components/navBar.vue'

/* this page just mounts all the elements */
export default {
  name: 'app',
  components: {
    'navBar': navBar
  },
}

</script>

<style>
</style>
