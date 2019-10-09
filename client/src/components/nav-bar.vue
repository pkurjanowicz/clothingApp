<template>
  <div class="hello">
    <h1>{{ welcome }}</h1>
  </div>
</template>

<script>
export default {
  name: 'appname',
  props: {
    welcome: String
  }
}
</script>

<style>
</style>
