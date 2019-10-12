<template>
    <div class="navbar">
        <button><router-link to="/">Home</router-link></button><br><br>
        <button><router-link to="/login">Login</router-link></button><br><br>
        <button><router-link to="/register">Register</router-link></button><br><br>
    </div>
</template>

<script>

export default {
  name: 'navBar',
}
</script>