<template>
    <div class="myMessages">
        <div class="messagableUsers">
            <h1>Pick a User</h1>
                <ul v-for="user in userNamesCurrentUserCanMessage" :key="user">
                    <button @click='makeMessagingModalVisibile(user)' >{{ user }}</button>
                </ul>
        </div>
        <div>
          <messagingModal v-if="isModalVisible" 
          @close="closeModal()"
          @getMessages='getAllMessages()' 
          :username='currentViewingMessages'
          :messages='messages'
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
        messages: '',
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
            this.message = value; /*gettings value from child*/
            axios.post('/add_message', {
                first_user_id: this.userSessionID,
                second_user_name: this.secondUserName,
                message: this.message,
            })
            .then(response => {
                console.log(response)
                this.message = ''
                this.getAllMessages()
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
                current_user_id: this.userSessionID,
                second_user_name: this.secondUserName,
            })
            .then(response => {
                console.log(response.data.messages)
                this.messages = response.data.messages
                this.sentMessages = response.data.sent
                this.recievedMessages = response.data.recieved
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
        this.getAllMessages()
      }
    });
  }
}
</script>
<style scoped>

</style>