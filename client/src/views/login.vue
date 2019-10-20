<template>
  <div class="login-box">
    <div class="login-form">
        <h1>{{ title }}</h1>
        <input type="text" v-model="username" placeholder="Username"/>
        <input type="password" v-model="password" placeholder="Password"/>
        <button @click="checkUser">Login</button>
        <div><router-link to="/register">Register</router-link></div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { isAuthenticated } from '../helpers.js'

export default {
  name: 'loginPage',
  props: ['title'],
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    /* authenticates the user in the db */
    checkUser() {
      axios.post('checklogin', {
        username: this.username, 
        password: this.password
        })
        .then(function (response) {
        console.log(response);
        })
        .catch(function (error) {
        console.log(error);
      });
      this.username = '';
      this.password = '';
      let userSessionName = isAuthenticated().then(data => { 
        /* I am using this promise to delay the page load 
        to not allow it to be redirected back to login path */
        this.$router.push({ path: '/'})
    })
  }
  }
}
</script>

<style>
</style>
