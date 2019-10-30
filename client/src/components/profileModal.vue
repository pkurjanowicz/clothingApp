<template>
<transition name="fade">
  <div class="modal-backdrop" @click='close()'>
    <div class="modal" @click.stop>
      <header class="modal-header">
        Setup Your Profile<br>
        <button class='x-out-button' @click="close"> X </button>
      </header>
      <section class="modal-body">
        <slot name="body">
        <p>Please select your timezone</p>
          <select type='text' v-model='timeZone'>
            <option value='EasternTime'>Eastern Time</option>
            <option value='CentralTime'>Central Time</option>
            <option value='MountainTime'>Mountain Time</option>
            <option value='PacificTime'>Pacific Time</option>
        </select><br><br><br><br>
          <button @click="submitTimeZone" type="submit" >Submit</button><br><br>
        </slot>
      </section>
    </div>
  </div>
</transition>
</template>


<script>
  export default {
    name: 'profileModal',
    props: ['username'],
    data() {
        return {
            timeZone: '',
        }
    },
    methods: {
      close() {
        this.$emit('close');
      },
      submitTimeZone(event){
          this.$emit('submitTimeZone', this.timeZone)
          this.timeZone = ''
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
    height: 500px;
    width: 400px;
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
    padding: 5% 5% 0 5%;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>