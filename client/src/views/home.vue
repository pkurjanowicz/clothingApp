<template>
    <div class="home">
        <h1>{{ title }}</h1>
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
          <button @click="addImage()">Submit</button>
          <br><br>
          <p>user session ID is: {{userSessionID}}</p>
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
      userSessionID: '',
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
        .then(function (response) {
          //TODO insert code to send data to the database
        console.log(response.data.data.link);
        })
        .catch(function (error) {
        console.log(error);
      });
    },
    handleFileUpload(){
        this.file = this.$refs.file.files[0];
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