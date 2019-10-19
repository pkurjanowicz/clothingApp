<template>
  <div class="register">
    <h1>{{ title }}</h1>
    <input type="text" v-model="username" placeholder="Username"/><br><br>
    <input type="password" v-model="password" placeholder="Password"/><br><br>
    <button @click="addUser">Register</button><br><br>
  </div>
</template>

<script>
import axios from "axios";
import { isAuthenticated } from '../helpers.js'

export default {
  name: 'registerPage',
  props: ['title'],
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    addUser() {
      axios.post('adduser', {
        username: this.username, 
        password: this.password
        })
        .then(response => {
        console.log(response);
        })
        .catch(error => {
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
  },
}
</script>

<style>
</style>
