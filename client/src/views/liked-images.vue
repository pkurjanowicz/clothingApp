<template>
    <div class="likedImages">
        <div class="images-box">
            <p v-if="message">{{ message }}</p>
            <li v-for="image in likedImages" :key='image'>
                <a :href="'/messages?user='+image[1]">
                    <div class="image-link-box">
                        <img :src="image[0]">
                        <span class='text-wrapper'>{{image[1]}}</span>
                    </div>
                </a>
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
.likedImages {
    max-width: 500px;
}
.images-box {
    display: flex;
    flex-wrap: wrap;
    padding: 3% 0 0 0;
}

.image-link-box {
    position:relative;
    text-decoration: none;
}

.text-wrapper {
    width: 100%;
    height: 100%;
    padding: 10px 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    color: #fff;
    opacity: 0;
    margin: 0 0 10px 0;
}
.images-box li img {
    max-width: 600px
}

.image-link-box:hover .text-wrapper{
    transition: all 0.8s ease;
    background: rgba(0, 0, 0, 0.6);
    opacity: 1;
}
@media only screen and (max-width: 450px) {
    .images-box li img {
      max-width: 100%;
    }
    .images-box li span {
     display:none;
    }
    .images-box {
        padding: 20% 0 0 0;
    }
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
    .images-box li img {
      max-width: 100%;
    }
    .images-box {
        padding: 14% 0 0 0;
    }
    .images-box li span {
     display:none;
    }
  }

</style>