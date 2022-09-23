import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// 导入全局初始化样式
import './assets/index.css'
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';

const app = createApp(App)
app.component('QuillEditor', QuillEditor)
app.use(ElementPlus)
app.use(router)
app.mount('#app')



