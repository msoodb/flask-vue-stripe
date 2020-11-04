import Vue from 'vue';
import Router from 'vue-router';
import Books from './components/Books.vue';
import Foo from './components/Foo.vue';
import Order from './components/Order.vue';
import OrderComplete from './components/OrderComplete.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/order/:id',
      name: 'Order',
      component: Order,
    },
    {
      path: '/complete/:id',
      name: 'OrderComplete',
      component: OrderComplete,
    },
    {
      path: '/foo',
      name: 'Foo',
      component: Foo,
    },
  ],
});
