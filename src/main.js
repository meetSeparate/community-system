import { createApp } from 'vue'
// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'
import App from './App.vue'
import router from "./router";
import './assets/style/index.scss'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import store from "./store/index.js";
import './api/mock.js'
import api from './api/api.js'


const app = createApp(App)
// app.use(ElementPlus)
app.config.globalProperties.$api = api
app.use(router).use(store)
app.mount('#app')
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
