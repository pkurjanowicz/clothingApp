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

<style scoped>
.navbar {
    display: flex;
    flex-direction: row;
    margin: 0 0 6% 0;
}

.navbar-btn {
    padding: 20px;
    height: 100%;
    background-color: grey;
    font-size: 15px;
    color: white;
    border: 3px;
    border-color: grey;
    border-style: solid;
}

.navbar-btn2 {
    background-color: #DA3548;
    padding: 20px;
    color: white;
    font-size: 15px;
    height: 100%;
    border: 3px;
    border-color: #DA3548;
    border-style: solid;
}

.navbar-logout {
    background-color: #DA3548;
    padding: 20px;
    color: white;
    font-size: 15px;
    height: 100%;
    border: 3px;
    border-color: #DA3548;
    border-style: solid;
}

.logout-slide-right {
    margin-left: auto;
    order: 2;
}

.navbar-btn:hover {
    background-color: white;
    border: 3px;
    border-color:  grey;
    border-style: solid;
    color: grey;
    transition-duration: .3s;
}

.navbar-btn2:hover {
    background-color: white;
    border: 3px;
    border-color:  #DA3548;
    border-style: solid;
    color: #DA3548;
    transition-duration: .3s;
}

.navbar-logout:hover {
    background-color: white;
    border: 3px;
    border-color:  #DA3548;
    border-style: solid;
    color: #DA3548;
    transition-duration: .3s;
}
</style>