<template>
    <div class="navbar">
        <button><router-link to="/">Home</router-link></button><br><br>
        <button><router-link to="/login">Login</router-link></button><br><br>
        <button><router-link to="/register">Register</router-link></button><br><br>
        <button @click="logOut">Logout</button><br><br>
    </div>
</template>

<script>
import axios from 'axios';
import { isAuthenticated } from '../helpers.js'

export default {
  name: 'navBar',
  methods: {
    logOut() {
      axios.get('logout')
      .then(response => {
        console.log(response);
        this.$router.push('/login')
        })
        .catch(error => {
        console.log(error);
      });
    }
  }
}
</script>