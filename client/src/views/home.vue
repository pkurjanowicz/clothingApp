<template>
    <div class="home">
        <h1>{{ title }}</h1>
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
          <button @click="addImage()">Submit</button>
          <br><br>
          <p>user session ID is: {{userSessionID}}</p>
          <img :src="randomImage">
          <br>
          <button @click="likeImage()">Like</button>
          <button @click="dislikeImage()">Dislike</button>
    </div>
</template>

<script>
import axios from 'axios';
import { isAuthenticated } from '../helpers.js'
var session = '{{ session }}';

export default {
  name: 'homePage',
  props: ['title'],
  data() {
    return {
      file: '',
      userSessionID: null,
      randomImage: null,
    }
  },
  methods: {
    addImage() {
      let formData = new FormData();
      formData.append('image', this.file);
      console.log('>> formData >> ', formData);
      axios.post('https://api.imgur.com/3/image', formData, {
        headers: {
          'Authorization': 'Client-ID aeebe6e47294974',
          'Content-Type': 'multipart/form-data'
          },
        })
        .then(response => {
          //TODO insert code to send data to the database
          axios.post('/addimage', {
              link: response.data.data.link,
              user_id: this.userSessionID
            })
            .then(response => {
              console.log(response);
            })
            .catch(error => {
              console.log(error);
            });
        console.log(response.data.data.link);
        })
        .catch(error => {
        console.log(error);
      });
    },
    handleFileUpload(){
        this.file = this.$refs.file.files[0];
    },
    likeImage() {
      axios.post('like-image', {
        image_link: this.randomImage,
        user_id: this.userSessionID
      })
      .then(response => {
        console.log(response)
        axios.get('/random-image')
          .then(response => {
        console.log(response.data.image_link);
        this.randomImage = response.data.image_link
          })
      })
      .catch(error => {
        console.log(error)
      })
    },
    dislikeImage() {
      axios.post('dislike-image', {
        image_link: this.randomImage,
        user_id: this.userSessionID
      })
      .then(response => {
        console.log(response)
        axios.get('/random-image')
          .then(response => {
            console.log(response.data.image_link);
            this.randomImage = response.data.image_link
          })
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
    });
    axios.get('/random-image')
    .then(response => {
        console.log(response.data.image_link);
        this.randomImage = response.data.image_link
    })
  }
}
</script>