<template>
    <div class="myImages">
        <button @click="getAddedImages()">Get My Images</button>
        <p v-if="message">{{ message }}</p>
        <div class="images-box">
            <li v-for="image in addedImages" :key='image'>
                <img :src="image">
            </li>
        </div>
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
        message: '',
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
                if (response.data.images.length === 0) {
                    this.message = 'No uploaded images yet'
                }
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

<style scoped>
.images-box {
    display: flex;
    flex-wrap: wrap;
    padding: 3% 0 0 0;
}
</style>