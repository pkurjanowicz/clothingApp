import Vue from 'vue'
import App from './App.vue'
import router from './router'

Vue.config.productionTip = false

/* just creating vue instance w/ router */
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
