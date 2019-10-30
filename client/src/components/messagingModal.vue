<template>
<transition name="fade">
  <div class="modal-backdrop" @click='close()'>
    <div class="modal" @click.stop>
      <header class="modal-header">
        <button class='x-out-button' @click="close"> X </button>
      </header>
      <section class="modal-body">
        <slot name="body">
          <div class='messages-box'>
            <!-- messages below are imported from the parent element(client/src/views/messages.vue) -->
            <ul v-for='messageValue in messages'
            :key='messageValue' 
            :class="{'sentmessages': (messageValue[2] === 'sent'), 'recievedmessages': (messageValue[2] === 'recieved')}" >
                <li >{{ messageValue[1] }}</li><br>
                <p>{{ messageValue[3] }}</p>
                <!-- messageValue[3] is the timestamp in UTC, need to figure out how to convert this to local time -->
            </ul>
            <br><br>
          </div>
          Send a message to {{ username }}<br><br>
          <textarea v-model='message' rows="4" cols="50" >Input your message here</textarea><br>
          <button @click="submitMessage" type="submit" >Send</button><br><br>
        </slot>
      </section>
      <footer class="modal-footer">
          <slot name="footer">
        </slot>
      </footer>
    </div>
  </div>
</transition>
</template>


<script>
import axios from 'axios';
import { isAuthenticated } from '../helpers.js'

  export default {
    name: 'messagingModal',
    props: ['username','messages'],
    data() {
        return {
            message: '',
            localTimeStamp: '',
        }
    },
    methods: {
      close() {
        this.$emit('close');
      },
      getMessages(){
          this.$emit('getMessages')
      },
      submitMessage(event){
        //this.message is passed up to the parent element(client/src/views/messages.vue)
          this.$emit('submitMessage', this.message) 
          this.message = ''
      },
      //possibly use this to convert the timestamp to local time? TODO
      convertToLocalTime(timeZoneValue) {
        timeZoneValue = timeZoneValue + 'UTC'
        console.log(timeZoneValue)
        var date = new Date(timeZoneValue);
        console.log(date)
        this.localTimeStamp = date.toString()
        console.log(this.localTimeStamp)
      }
    },
    mounted() {
        getMessages: {
          this.$emit('getMessages')
      }
    }
}
</script>

<style scoped>
.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal {
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    height: 500px;
    width: 800px;
}

.modal-header {
    padding: 20px 20px 0 20px;
    display: flex;
}

.x-out-button {
    margin-left: auto;
    order: 2;
}

.modal-footer {
    padding: 20px;
    display: flex;
}

.modal-footer {
    justify-content: center;
    align-items: center;
}

.modal-body {
    position: relative;
    padding: 20px;
}

.messages-box {
    display: flex;
    flex-direction: column;
}

.messages-box ul {
    padding: 0;
    margin: 2px;
    display: flex;
    flex-direction: column;
}

.sentmessages {
    display: flex;
}

.sentmessages li{
    margin-left: auto;
    order: 2;
    background: blue;
    color: white;
    padding: 5px;
    border-radius: 10px;
}

.recievedmessages {
    display: flex;
}

.recievedmessages li{
    margin-right: auto;
    order: 2;
    background: rgb(179, 179, 179);
    color: black;
    padding: 5px;
    border-radius: 10px;
}

.sentmessages p {
  margin-left: auto;
  order: 2;
  font-size: 12px;
  color: grey;
}

.recievedmessages p {
  margin-right: auto;
  order: 2;
  font-size: 12px;
  color: grey;
}

li {
  margin: 0px;
}

p {
  margin: 1px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}


</style>
