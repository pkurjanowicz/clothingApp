<template>
    <div class="navbar">
        <router-link to="/"><button class='navbar-btn'>Home</button></router-link>
        <router-link to="/upload"><button class='navbar-btn'>Upload</button></router-link>
        <router-link to="/my-images"><button class='navbar-btn'>My Images</button></router-link>
        <router-link to="/liked-images"><button class='navbar-btn'>My Liked Images</button></router-link>
        <router-link to="/messages"><button class='navbar-btn'>My Messages</button></router-link>
        <a href='' class="logout-slide-right"><button @click="logOut" class='navbar-logout'>Logout</button></a>
    </div>
</template>

<script>
import axios from 'axios';
import { isAuthenticated } from '../helpers.js'

export default {
  name: 'navBar',
  methods: {
    // function deletes user's session and redirects to login page
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