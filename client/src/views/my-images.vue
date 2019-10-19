<template>
    <div class="myImages">
        <h1>{{ title }}</h1>
        <p>Session user ID is: {{userSessionID}}</p>
        <button @click="getAddedImages()">Get My Images</button>
        <li v-for="image in addedImages" :key='image'>
            <img :src="image">
        </li>
    </div>
</template>

<script>
import axios from "axios";
import { isAuthenticated } from '../helpers.js'

export default {
    name: 'myImages',
    props: ['title'],
    data() {
        return {
        userSessionID: '',
        addedImages: [],
        }
    },
    methods: {
        /* gets all the images this user 
        uploaded to images table in db*/ 
        getAddedImages() {
            axios.post('/all-my-images',{
                user_id: this.userSessionID,
            })
                .then(response => {
                console.log(response);
                this.addedImages = response.data.images
            })
                .catch(error => {
                console.log(error)
            })
        }
    },
    mounted() {
        /* checks the user session */
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