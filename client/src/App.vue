<template>
  <div id="app">
    <registerPage register="Register"/>
    <loginPage login="Login"/>
  </div>
</template>

<script>
import registerPage from './components/register.vue'
import loginPage from './components/login.vue'

export default {
  name: 'app',
  components: {
    registerPage,
    loginPage
  },
}
</script>

<style>
</style>
