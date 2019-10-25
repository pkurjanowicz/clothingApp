<template>
  <div class="modal-backdrop">
    <div class="modal">
      <section class="modal-body">
        <slot name="body">
          Messages from
          {{ username }}<br><br>
          <textarea v-model='message' rows="4" cols="50" >Input your message here</textarea><br>
          <button @click="submitMessage" type="submit" >Send</button>
          <button @click="getMessages"> Get Messages</button><br>
          <ul v-for='messageValue in messages' :key='messageValue'>
            <li>{{ messageValue }}</li>
          </ul><br>
        </slot>
      </section>
      <footer class="modal-footer">
          <slot name="footer">
            <button @click="close"> Close</button>
        </slot>
      </footer>
    </div>
  </div>
</template>


<script>
  export default {
    name: 'messagingModal',
    props: ['username', 'messages'],
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
      }
    },
  };
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

.modal-header,
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

</style>
