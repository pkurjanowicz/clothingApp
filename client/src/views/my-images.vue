<template>
    <div class="myImages">
        <h1>{{ title }}</h1>
        <p>Session user ID is: {{userSessionID}}</p>
        <button @click="getAddedImages()">Get Liked Images</button>
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