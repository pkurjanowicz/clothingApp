<template>
  <div class="modal-backdrop">
    <div class="modal">
      <section class="modal-body">
        <slot name="body">
          You've Got a Match!
        </slot>
      </section>
      <footer class="modal-footer">
          <slot name="footer">
            <button
              type="button"
              class="btn-green"
              @click="close"
            >
              Close
          </button>
        </slot>
      </footer>
    </div>
  </div>
</template>


<script>
  export default {
    name: 'modal',

    methods: {
      close() {
        this.$emit('close');
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

.modal-header,
.modal-footer {
    padding: 15%;
    display: flex;
}


.modal-footer {
    justify-content: center;
    align-items: center;
}

.modal-body {
    position: relative;
    padding: 20%;
}

</style>
