import 'bootstrap/dist/css/bootstrap.css';
import BootstrapVue from 'bootstrap-vue';
import LoadScript from 'vue-plugin-load-script';
import Vue from 'vue';
import App from './App.vue';
import router from './router';


Vue.use(LoadScript);
Vue.use(BootstrapVue);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
