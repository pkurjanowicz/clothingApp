<template>
  <div class="hello">
    <h1>{{ register }}</h1>
    <input type="text" v-model="username" placeholder="Username"/><br><br>
    <input type="password" v-model="password" placeholder="Password"/><br><br>
    <button @click="addUser">Register</button><br><br>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'registerPage',
  props: ['register'],
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
        .then(function (response) {
        console.log(response);
        })
        .catch(function (error) {
        console.log(error);
      });
      this.username = '';
      this.password = '';
    }
  }
}
</script>

<style>
</style>
