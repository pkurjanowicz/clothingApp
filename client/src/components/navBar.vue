<template>
    <div>
        <div class="navbar">
            <!-- router-link is actually linked to the router.js file -->
            <router-link to="/"><button class='navbar-btn'>Home</button></router-link>
            <router-link to="/upload"><button class='navbar-btn'>Upload</button></router-link>
            <router-link to="/my-images"><button class='navbar-btn'>My Images</button></router-link>
            <router-link to="/liked-images"><button class='navbar-btn'>My Liked Images</button></router-link>
            <router-link to="/messages"><button class='navbar-btn'>My Messages</button></router-link>
            <router-link to="/profile"><button class='navbar-logout' >My Profile</button></router-link>
            <a href='' class="logout-slide-right"><button @click="logOut" class='navbar-logout'>Logout</button></a>
        </div>
        <Slide class='mobile-navbar'>
        <a id="home" href="/"><span>Home</span></a>
        <a id="home" href="/upload"><span>Upload</span></a>
        <a id="home" href="/my-images"><span>My Images</span></a>
        <a id="home" href="/liked-images"><span>My Liked Images</span></a>
        <a id="home" href="/messages"><span>My Messages</span></a>
        <a id="home" href="/profile"><span>My Profile</span></a>
        <a id="home" href="" @click="logOut"><span>Logout</span></a>
        </Slide>
    </div>
</template>

<script>
import axios from 'axios';
import { isAuthenticated } from '../helpers.js'
import { Slide } from 'vue-burger-menu'  

export default {
  name: 'navBar',
  components: {
        Slide 
    },
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
    },
  }
}
</script>

<style scoped>
.navbar {
    display: flex;
    flex-direction: row;
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
.mobile-navbar {
    display:none;
}

@media only screen and (max-width: 450px) {
  .navbar {
    display:none;
    }
  .mobile-navbar {
    display:block;
    }
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
  .navbar {
    display:none;
    }
  .mobile-navbar {
    display:block;
    }
  }

</style>