import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'

import axios from "axios";

import './assets/main.css'

const pinia = createPinia();

axios.defaults.baseURL = "http://localhost:5000/api/v1/"

createApp(App).use(pinia).mount('#app')
