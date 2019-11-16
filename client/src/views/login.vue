<template>
  <div class="login-box">
    <div class="login-form">
        <h1>{{ title }}</h1>
        <input @keyup.enter.exact='checkUser' type="text" v-model="username" placeholder="Username"/>
        <input @keyup.enter.exact='checkUser' type="password" v-model="password" placeholder="Password"/>
        <button @click="checkUser" >Login</button>
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
      /* this setTimeout() allows for the session to be set and then will redirect*/
      setTimeout(() => this.$router.push({ path: '/'}), 300);
    }
  }
}
</script>

<style scoped>
.login-box {
    height: 420px;
    width: 300px;
    margin: 10% 42%;
    display: flex;
    justify-content: center;
}

.login-form {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    padding: 15%;
}

.login-form h1 {
    text-align: center;
    margin: 0 0 30%;
}

.login-form div {
    padding: 10% 0;
}
.login-form div a {
    color: #DA3548;
    font-size: 13px;
}
.login-form button {
    margin: 10% 0 0 ;
}
</style>
