<template>
    <div class="myMessages">
        <div class="messagableUsers">
            <div v-if='cannotMessageUser' class="warning-message">
                {{cannotMessageUser}}
            </div>
            <div v-if='userNamesCurrentUserCanMessage != 0'>
            <h1>Pick a User</h1>
                <ul v-for="user in userNamesCurrentUserCanMessage" :key="user">
                    <button @click='makeMessagingModalVisibile(user)' >{{ user }}</button>
                </ul>
            </div>
            <div v-else>
                <p>You cannot message any users yet</p>
            </div>
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
        cannotMessageUser: '',
        timeZone: '',
        }
    },
    methods: {
        closeModal() {
            this.isModalVisible = false;
            this.yourMessages = '';
            this.$router.push('/messages')
            },
        makeMessagingModalVisibile(user) {
            this.isModalVisible = true;
            this.currentViewingMessages = user;
            this.secondUserName = user;
            this.getAllMessages()
            this.$router.push({ query: { user: user }}) /*Will use this to link to the my liked images page*/
        },
        submitMessage(value) {
            this.message = value; /*gettings value from child*/
            if (this.message !== "") {
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
            }
        },
        getAllowedMessageIds() {
            axios.post('/return_messagable_users',{
                current_user_id: this.userSessionID
            })
            .then(response => {
                this.userNamesCurrentUserCanMessage = response.data.user_list
                this.routeChange()
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
        },
        routeChange() {
            if (this.$route.query.user) {
                this.secondUserName = this.$route.query.user
                if (this.userNamesCurrentUserCanMessage.includes(this.secondUserName)) {
                    this.makeMessagingModalVisibile(this.secondUserName)
                } else {
                    this.cannotMessageUser = `You are not allowed to message ${this.secondUserName} yet, please match first`
                }
            }
        },
        getTimeZone() {
            axios.post('/getProfileData',{
                currentuser: this.userSessionID,
            })
            .then(response =>{
                console.log(response)
                this.timeZone = response.data.user_time
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
        this.getAllowedMessageIds()
        this.getTimeZone()
      }
    });
  }
}
</script>
<style scoped>

.warning-message {
    padding: 10px;
    background: rgba(255, 255, 0, 0.577);
}



@media only screen and (max-width: 450px) {
    .myMessages {
        padding: 20% 0 0 0;
    }
    .modal {
        width: 95%;
    }
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
    .myMessages {
        padding: 14% 0 0 0;
    }
    .modal {
        width: 95%;
    }
  }

</style>