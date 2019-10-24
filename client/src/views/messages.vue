<template>
    <div class="myMessages">
        {{ title }}
        <div class="message-box">
            <div class="message-item">
                <ul v-for="message in yourMessages" :key="message">
                    <li>{{ message }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { isAuthenticated } from '../helpers.js'

export default {
    name: 'myMessages',
    props: ['title'],
    data() {
        return {
        yourMessages: []
        }
    }
}
</script>
<style scoped>

</style>