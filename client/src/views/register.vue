<template>
<div class=register-box>
  <div class="register-form">
    <h1>{{ title }}</h1>
    <input type="text" v-model="username" placeholder="Username"/>
    <input type="password" v-model="password" placeholder="Password"/>
    <button @click="addUser">Register</button>
    <div><router-link to="/login">Already have an account?</router-link></div>
  </div>
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
    /* add a new user, note there is no 
    client side validation in place yet...*/ 
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

<style scoped>
.register-box {
    height: 420px;
    width: 300px;
    margin: 10% 42%;
    display: flex;
    justify-content: center;
}

.register-form {
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    padding: 15%;
}

.register-form h1 {
    text-align: center;
    margin: 0 0 30%;
}

.register-form div {
    padding: 10% 0;
}
.register-form div a {
    color: #DA3548;
    font-size: 13px;
}
.register-form button {
    margin: 10% 0 0 ;
}
</style>
