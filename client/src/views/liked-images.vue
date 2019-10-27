<template>
    <div class="likedImages">
        <p v-if="message">{{ message }}</p>
        <div class="images-box">
            <li v-for="image in likedImages" :key='image'>
                <img :src="image">
            </li>
        </div>
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
        message: '',
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
                if (response.data.images.length === 0) {
                    this.message = 'No liked images yet'
                }
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
            this.getLikedImages()
        }
        })
    },
}
</script>

<style scoped>
.images-box {
    display: flex;
    flex-wrap: wrap;
    padding: 3% 0 0 0;
}
</style>