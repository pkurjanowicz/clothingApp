<template>
  <div class="modal-backdrop">
    <div class="modal">
      <header class="modal-header">
        <button class='x-out-button' @click="close"> X </button>
      </header>
      <section class="modal-body">
        <slot name="body">
          <div class='messages-box'>
            <ul v-for='messageValue in messages' 
            :key='messageValue' 
            :class="{'sentmessages': (messageValue[2] === 'sent'), 'recievedmessages': (messageValue[2] === 'recieved')}" >
                <li >{{ messageValue[1] }}</li>
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
          this.$emit('submitMessage', this.message)
          this.message = ''
      },
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
    height: 600px;
    width: 1000px;
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
}

.sentmessages {
    display: flex;
}

.sentmessages li{
    margin-left: auto;
    order: 2;
    background: blue;
    color: white;
}

.recievedmessages {
    display: flex;
}

.recievedmessages li{
    margin-right: auto;
    order: 2;
    background: rgb(179, 179, 179);
    color: black;
}


</style>
