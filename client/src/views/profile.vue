<template>
    <div class="myProfile">
        <h2>{{ title }}</h2>
        <div class='profile-container' v-if='profileItems'>
            <ul v-for='(value, key) in profileItems' :key='(value, key)' >
                <li>{{ key }} : {{value}}</li>
            </ul>
        </div>
        <div>
            <button @click='profileSetup'>Setup your profile</button>
        </div>
        <div>
            <profileModal v-if="isModalVisible" 
            @close="closeModal()"
            @submitTimeZone='submitTimeZone'
            />
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { isAuthenticated } from '../helpers.js'
import profileModal from "../components/profileModal.vue"

export default {
    name: 'myProfile',
    props: ['title'],
        components: {
        profileModal,
    },
    data() {
        return {
            profileItems: [],
            timeZone: '',
            isModalVisible: false,
            userSessionID: '',
        }
    },
    methods: {
        closeModal() {
            this.isModalVisible = false;
        },
        profileSetup() {
            this.isModalVisible = true;
        },
        submitTimeZone(timeZone) {
            axios.post('/submitProfileData',{
                timezone: timeZone,
                currentuser: this.userSessionID,
            })
            .then(response => {
                console.log(response)
                this.profileItems = {'timezone':response.data.user_time}
                this.closeModal()
            })
            .catch(error => {
                console.log(error)
            })
        },
        getProfileData() {
            axios.post('/getProfileData',{
                currentuser: this.userSessionID,
            })
            .then(response =>{
                console.log(response)
                this.profileItems = {'timezone':response.data.user_time}
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
            this.getProfileData()
        }
        })
    }
}
</script>

<style scoped>
@media only screen and (max-width: 450px) {
    .myProfile {
        padding: 20% 0 0 0;
    }
  }
  
  /* Tablet Styles */
@media only screen and (min-width: 450px) and (max-width: 1025px) {
    .myProfile {
        padding: 14% 0 0 0;
    }
  }
</style>