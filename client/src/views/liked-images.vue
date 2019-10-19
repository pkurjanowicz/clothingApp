<template>
    <div class="likedImages">
        <h1>{{ title }}</h1>
        <p>Session user ID is: {{userSessionID}}</p>
        <button @click="getLikedImages()">Get Liked Images</button>
        <li v-for="image in likedImages" :key='image'>
            <img :src="image">
        </li>
    </div>
</template>

<script>
import axios from "axios";
import { isAuthenticated } from '../helpers.js'

export default {
    name: 'likedImages',
    props: ['title'],
    data() {
        return {
        userSessionID: '',
        likedImages: [],
        }
    },
    methods: {
        /* Gets all the user's liked images*/
        getLikedImages() {
            axios.post('/my-liked-images',{
                user_id: this.userSessionID,
            })
                .then(response => {
                console.log(response);
                this.likedImages = response.data.images
            })
                .catch(error => {
                console.log(error)
            })
        }
    },
    mounted() {
        /* checks the user session*/
        isAuthenticated().then(data => {
            if (data['session'] === false) {
            this.$router.push('/login')
            } else {
            this.userSessionID = data['user']
        }
        })
    }
}
</script>

<style>
</style>