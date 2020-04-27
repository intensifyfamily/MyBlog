import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home'
import ToDoList from '../components/todolist/ToDoList'
import Main from '../components/blog/Main'
import Article from '../components/blog/Article'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    redirect: '/blog/home',
    children: [
      {
        path: '/todolist',
        name: 'ToDoList',
        component: ToDoList
      },
      {
        path: '/blog/home',
        name: 'BlogHome',
        component: Main
      },
      {
        path: '/article/:articleId',
        name: 'Article',
        component: Article
      }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
