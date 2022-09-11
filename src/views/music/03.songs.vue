<template>
  <div class="songs-container">
    <Musicplay />
    <div class="tab-bar">
      <span class="item" :class="{ active: tag === '0' }" @click="tag = '0'"
        >全部</span
      >
      <span class="item" :class="{ active: tag === '7' }" @click="tag = '7'"
        >华语</span
      >
      <span class="item" :class="{ active: tag === '96' }" @click="tag = '96'"
        >欧美</span
      >
      <span class="item" :class="{ active: tag === '8' }" @click="tag = '8'"
        >日本</span
      >
      <span class="item" :class="{ active: tag === '16' }" @click="tag = '16'"
        >韩国</span
      >
    </div>
    <!-- 底部的table -->
    <table class="el-table playlit-table">
      <thead>
        <th>&nbsp;</th>
        <th>音乐标题</th>
        <th>歌手</th>
        <th>专辑</th>
        <th>时长</th>
      </thead>
      <tbody>
        <tr
          class="el-table__row"
          v-for="(item, key) in musiclist"
          :key="item.key"
        >
          <td>{{ key + 1 }}</td>
          <td>
            <div class="img-wrap">
              <img :src="item.album.blurPicUrl" alt />
              <span class="iconfont icon-play" @click="play(item.id)" />
            </div>
          </td>
          <td>
            <div class="song-wrap">
              <div class="name-wrap">
                <span>{{ item.name }}</span>
                <span class="iconfont icon-mv" @click="mvplay(item.id)" />
              </div>
              <span>{{ item.album.company }}</span>
            </div>
          </td>
          <td>{{ item.artists[0].name }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.d }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { watch, ref, provide } from '@vue/runtime-core'
import Musicplay from './MusicPlay.vue'
import router from '@/router/index.js'
import axios from 'axios'
const musiclist = ref([])
const songurl = ref('')
const tag = ref('0')
provide('song_url', songurl)
axios({
  url: 'https://autumnfish.cn/top/song',
  params: {
    type: tag.value
  }
}).then((res) => {
  musiclist.value = res.data.data
  for (let i = 0; i < musiclist.value.length; i++) {
    const time = parseInt(musiclist.value[i].duration / 1000)
    const sec = parseInt((musiclist.value[i].duration / 1000) % 60)
    const min = parseInt(time / 60)
    musiclist.value[i].d = min + ':' + sec
  }
})
function mvplay(id) {
  router.push('/mv?q=' + id)
}
function play(id) {
  axios({
    url: 'https://autumnfish.cn/song/url',
    params: {
      id
    }
  }).then((res) => {
    songurl.value = res.data.data[0].url
  })
}
watch(tag, () => {
  axios({
    url: 'https://autumnfish.cn/top/song',
    params: {
      type: tag.value
    }
  }).then((res) => {
    musiclist.value = res.data.data
  })
})
</script>

<style></style>
