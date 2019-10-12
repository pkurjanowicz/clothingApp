<template>
  <div id="app">
    <navBar/>
    <router-view></router-view>
  </div>
</template>

<script>
import navBar from './components/navBar.vue'

export default {
  name: 'app',
  components: {
    'navBar': navBar
  },
}

</script>

<style>
</style>
