import { createRouter, createWebHashHistory } from 'vue-router'
// 导入对应的路由
import Notfound from '../components/Notfound.vue'
import Discuss from '../views/Discuss.vue'
import Idea from '../views/Idea.vue'
import Back from '../views/Back.vue'
import Home from '../views/Home.vue'
import Author from '../views/Author.vue'
import Changedata from '../views/Changedata.vue'
import Sendtext from '../views/Sendtext.vue'

import discovery from '../views/music/01.discovery.vue'
import playlists from '../views/music/02.playlists.vue'
import songs from '../views/music/03.songs.vue'
import mvs from '../views/music/04.mvs.vue'
import result from '../views/music/05.result.vue'
import playlist from '../views/music/06.playlist.vue'
import mv from '../views/music/07.mv.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: discovery
  },
  {
    path: '/discuss',
    name: 'Discuss',
    component: Discuss
  },
  {
    path: '/idea',
    name: 'Idea',
    component: Idea
  },
  {
    path: '/Back',
    name: 'Back',
    component: Back
  },
  {
    path: '/Home',
    name: 'Home',
    component: Home
  },
  {
    path: '/author',
    name: 'author',
    component: Author
  },
  {
    path: '/changedata',
    name: 'Changedata',
    component: Changedata
  },
  {
    path: '/sendtext',
    name: 'Sendtext',
    component: Sendtext
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'Notfound',
    component: Notfound
  },
  {
    // 发现音乐
    path: '/discovery',
    component: discovery
  },
  {
    // 推荐歌单
    path: '/playlists',
    component: playlists
  },
  {
    // 推荐歌单
    path: '/playlist',
    component: playlist
  },
  {
    // 最新音乐
    path: '/songs',
    component: songs
  },
  {
    // 最新音乐
    path: '/mvs',
    component: mvs
  },
  // mv详情
  {
    path: '/mv',
    component: mv
  },
  // 搜索结果页
  {
    path: '/result',
    component: result
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
