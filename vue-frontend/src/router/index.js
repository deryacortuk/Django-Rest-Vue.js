import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import HomeView from '../views/HomeView.vue'

import ProductView from '../views/ProductView.vue'
import SearchView from '../views/SearchView.vue'
import CartView from '../views/CartView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import AccountView from '../views/AccountView.vue'
import OrderView from '../views/OrderView.vue'
import SuccessView from '../views/SuccessView.vue'
import VideoList from '../views/VideosView.vue'
import CustomerView from '../views/CustomerView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/tutorial',
    name: 'Videos',
    component: VideoList
  },
  {
    path: '/my-list',
    name: 'VideoList',
    component: CustomerView
  },
  {
    path: '/register',
    name: 'Register',
    component: SignupView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/account',
    name: 'Account',
    component: AccountView,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: OrderView,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: SuccessView,
    meta: {
      requiredLogin: true
    }
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchView
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartView
  },
  {
    path: '/:product_slug',
    name: 'Product',
    component: ProductView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
    if(to.matched.some(record => record.meta.requiredLogin) && !store.state.isAuthenticated) {
      next({name: 'Login', query: {to: to.path }})
    } else {
      next()
    }
})

export default router