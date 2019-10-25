<template>
    <div class="myMessages">
        <!-- {{ title }}
        <div v-if="userNamesCurrentUserCanMessage.length != 0">
            <h3>Who do you want to message?</h3>
            <textarea v-model="message" rows="4" cols="50" >Input your message here</textarea><br>
            <select v-model="secondUserName" >
                <option :value='user' v-for="user in userNamesCurrentUserCanMessage" :key="user">{{ user }}</option>
            </select><br><br>
            <button @click="submitMessage" type="submit">Send</button>
            <button @click='getAllMessages'>Get all Messages</button>
        </div> -->
        <!-- <p v-else>You cannot message anyone, you have not matched :( </p> -->
        <div class="message-box">
            <div class="message-item">
                <ul v-for="user in userNamesCurrentUserCanMessage" :key="user">
                    <button @click='makeMessagingModalVisibile(user)' >{{ user }}</button>
                </ul>
                <!-- Make a link to each li to display a model view of all messages for that user(create a new endpoint)
                Put the ability to create a new message for that user inside that modal view as well -->
            </div>
        </div>
        <div>
          <messagingModal v-if="isModalVisible" 
          @close="closeModal()" 
          :username='currentViewingMessages'
          @getMessages='getAllMessages()'
          :messages='yourMessages' 
          @submitMessage='submitMessage'
          />
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { isAuthenticated } from '../helpers.js'
import messagingModal from '/Users/peterkurjanowicz/Desktop/Interesting Projects/clothing_match_app/clothing_match_app/client/src/components/messagingModal.vue';

export default {
    name: 'myMessages',
    components: {
        messagingModal,
    },
    data() {
        return {
        yourMessages: '',
        message: '',
        secondUserName: '',
        userSessionID: '',
        userNamesCurrentUserCanMessage: 0,
        isModalVisible: false,
        currentViewingMessages: '',
        }
    },
    methods: {
        closeModal() {
            this.isModalVisible = false;
            this.yourMessages = '';
            },
        makeMessagingModalVisibile(user) {
            this.isModalVisible = true;
            this.currentViewingMessages = user;
            this.secondUserName = user;
        },
        submitMessage(value) {
            this.message = value;
            axios.post('/add_message', {
                first_user_id: this.userSessionID,
                second_user_name: this.secondUserName,
                message: this.message,
            })
            .then(response => {
                console.log(response)
                this.message = ''
            })
            .catch(error => {
            console.log(error)
        })
        },
        getAllowedMessageIds() {
            axios.post('/return_messagable_users',{
                current_user_id: this.userSessionID
            })
            .then(response => {
                this.userNamesCurrentUserCanMessage = response.data.user_list
            })
            .catch(error => {
            console.log(error)
            })
        },
        getAllMessages() {
            axios.post('/get_all_messages', {
                current_user_id: this.userSessionID
            })
            .then(response => {
                this.yourMessages = response.data.messages
            })
        }
    },
    mounted() {
    isAuthenticated().then(data => {
      if (data['session'] === false) {
        this.$router.push('/login')
      } else {
        this.userSessionID = data['user']
        this.getAllowedMessageIds()
      }
    });
  }
}
</script>
<style scoped>

</style>