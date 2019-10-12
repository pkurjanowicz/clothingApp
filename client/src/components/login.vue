<template>
    <div class="hello">
        <h1>{{ title }}</h1>
        <input type="text" v-model="username" placeholder="Username"/><br><br>
        <input type="password" v-model="password" placeholder="Password"/><br><br>
        <button @click="checkUser">Login</button><br><br>
    </div>
</template>

<script>
import axios from "axios";

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
    }
  }
}
</script>

<style>
</style>
