<template>
    <div class="upload">
        <!-- <h1>{{ title }}</h1>
        <p>user session ID is: {{userSessionID}}</p> -->
          <label class="custom-file-upload">
            Upload Image
            <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/><br><br>
          </label><br>
          <p v-if="file">Selection Successful! Click submit to upload</p>
          <button @click="addImage()">Submit</button><br>
          <p v-if="successfulUpload">{{ successfulUpload }}<p>
          <p style="display:none">{{userSessionID}}</p>
    </div>
</template>

<script>
import axios from 'axios';
import { isAuthenticated } from '../helpers.js'

export default {
  name: 'uploadPage',
  props: ['title'],
  data() {
    return {
      file: '',
      userSessionID: null,
      successfulUpload: '',
    }
  },
  methods: {
    /* This function adds an image to imgur via the 
    API and then adds that image w/ user session to database */
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
          axios.post('/addimage', {
              link: response.data.data.link,
              user_id: this.userSessionID
            })
            .then(response => {
              console.log(response);
              this.successfulUpload = 'Success!'
              this.file = ''
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
    //this is bound to file input section in html
    handleFileUpload(){
        this.file = this.$refs.file.files[0]
        this.successfulUpload = ''
    },
  },
  /* these functions run when page is loaded, check user 
  session and get random image from image table in the db */
  mounted() {
    isAuthenticated().then(data => {
      if (data['session'] === false) {
        this.$router.push('/login')
      } else {
        this.userSessionID = data['user']
        console.log(this.userSessionID)
      }
    });
  }
}
</script>

<style scoped>
.custom-file-upload {
    border: 1px solid #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px 12px 4px 12px;
    cursor: pointer;
    margin: 30px 0 0;
}

.upload {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    flex-direction: column;
}

@media only screen and (max-width: 450px) {
    .upload {
        padding: 20% 0 0 0;
    }
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
    .upload {
        padding: 14% 0 0 0;
    }
  }
</style>