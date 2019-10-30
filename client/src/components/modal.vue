<template>
<transition name="fade">
  <div class="modal-backdrop" @click='close()'>
    <div class="modal" @click.stop>
      <header class="modal-header">
        You've Got a Match!<br>
        <button class='x-out-button' @click="close"> X </button>
      </header>
      <section class="modal-body">
        <slot name="body">
          Send a message to {{ username }}<br><br>
          <textarea v-model='message' rows="3" cols="35" >Input your message here</textarea><br>
          <button @click="submitMessage" type="submit" >Send</button><br><br>
        </slot>
      </section>
    </div>
  </div>
</transition>
</template>


<script>
  export default {
    name: 'modal',
    props: ['username'],
    data() {
        return {
            message: '',
        }
    },
    methods: {
      close() {
        this.$emit('close');
      },
      submitMessage(event){
          this.$emit('submitMessage', this.message)
          this.message = ''
      },
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
    height: 300px;
    width: 300px;
}

.modal-header {
    padding: 20px 20px 0 20px;
    display: flex;
}

.x-out-button {
    margin-left: auto;
    order: 2;
}

.modal-body {
    position: relative;
    padding: 15% 5% 0 5%;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>
