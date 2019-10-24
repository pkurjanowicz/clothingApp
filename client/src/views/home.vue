<template>
    <div class="home">
      <!-- <h1>{{ title }}</h1>
        <p>user session ID is: {{userSessionID}}</p> -->
        <img :src="randomImage">
        <br>
        <div class="like-dislike-btns">
          <button @click="likeImage()">Like</button>
          <button @click="dislikeImage()">Dislike</button>
        </div>
        <div>
          <modal v-if="isModalVisible" @close="closeModal()"/>
        </div>
    </div>
</template>


<script>
import axios from 'axios';
import { isAuthenticated } from '../helpers.js'
import modal from '/Users/peterkurjanowicz/Desktop/Interesting Projects/clothing_match_app/clothing_match_app/client/src/components/modal.vue';

export default {
  name: 'homePage',
  props: ['title'],
  components: {
      modal,
    },
  data() {
    return {
      file: '',
      userSessionID: null,
      randomImage: null,
      successfulUpload: '',
      matchSuccess: '',
      isModalVisible: false,
    }
  },
  methods: {
    closeModal() {
      this.isModalVisible = false;
    },
    findMatch() {
        axios.post('/find-match', {
          liker_id: this.userSessionID,
          image_link: this.randomImage,
        })
        .then(response => {
          this.matchSuccess = response.data['liked_image']
          console.log(this.matchSuccess)
            if (this.matchSuccess != '') {
            this.isModalVisible = true;
          }
        })
        .catch(error => {
          console.log(error)
        })
      },
    /* hits the endpoint like-image and adds that image
    to the likedimage table using that user ID as a 
    foreign key(linked to user table) */
    likeImage() {
      axios.post('like-image', {
        image_link: this.randomImage,
        user_id: this.userSessionID
      })
      .then(response => {
        console.log(response)
        axios.post('/random-image',{
          user_id: this.userSessionID
        })
          .then(response => {
        console.log(response.data.image_link);
        this.randomImage = response.data.image_link
        this.findMatch()
          })
      })
      .catch(error => {
        console.log(error)
      })
    },
    /* does the same thing as function 
    above except deletes entry */
    dislikeImage() {
      axios.post('dislike-image', {
        image_link: this.randomImage,
        user_id: this.userSessionID
      })
      .then(response => {
        console.log(response)
        axios.post('/random-image',{
          user_id: this.userSessionID
        })
          .then(response => {
            console.log(response.data.image_link);
            this.randomImage = response.data.image_link
          })
      })
      .catch(error => {
        console.log(error)
        axios.post('/random-image',{
          user_id: this.userSessionID
        })
        .then(response => {
            console.log(response.data.image_link);
            this.randomImage = response.data.image_link
          })
      })
    }
  },
  /* these functions run when page is loaded, check user 
  session and get random image from image table in the db */
  mounted() {
    isAuthenticated().then(data => {
      if (data['session'] === false) {
        this.$router.push('/login')
      } else {
        this.userSessionID = data['user']
        axios.post('/random-image',{
          user_id: this.userSessionID
        })
        .then(response => {
        console.log(response.data.image_link);
        this.randomImage = response.data.image_link
        })
      }
    });
    
  }
}
</script>

<style scoped>
.home {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    padding: 3% 0 0 0;
}
.home img {
    object-fit: contain;
}

.like-dislike-btns {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: row;
}
.like-dislike-btns button {
    margin: 3px;
}
</style>