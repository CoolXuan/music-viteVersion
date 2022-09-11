<template>
  <div class="result-container">
    <Musicplay />
    <div class="title-wrap">
      <h2 class="title">{{ $route.query.query }}</h2>
      <span class="sub-title">找到{{ count }}个结果</span>
    </div>
    <el-tabs v-model="activeIndex">
      <el-tab-pane label="歌曲" name="songs">
        <table class="el-table">
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
              @click="play(item.id)"
              v-for="(item, key) in list"
              :key="item.key"
            >
              <td>{{ key + 1 }}</td>
              <td>
                <div class="song-wrap">
                  <div class="name-wrap">
                    <span>{{ item.name }}</span>
                    <span v-if="item.mvid != 0" class="iconfont icon-mv" />
                  </div>
                  <span v-if="item.alias ? true : false">{{
                    item.alias[0]
                  }}</span>
                </div>
              </td>
              <td>{{ item.artists[0].name }}</td>
              <td>{{ item.album.name }}</td>
              <td>{{ item.duration }}</td>
            </tr>
          </tbody>
        </table>
      </el-tab-pane>
      <el-tab-pane label="歌单" name="lists">
        <div class="items">
          <div
            class="item"
            v-for="item in playlists"
            :key="item.key"
            @click="toplaylist(item.id)"
          >
            <div class="img-wrap">
              <div class="num-wrap">
                播放量:
                <span class="num">{{ item.playCount }}</span>
              </div>
              <img :src="item.coverImgUrl" alt />
              <span class="iconfont icon-play" />
            </div>
            <p class="name">{{ item.name }}</p>
          </div>
        </div>
      </el-tab-pane>
      <el-tab-pane label="MV" name="mv">
        <div class="items mv">
          <div
            class="item"
            v-for="item in mvs"
            :key="item.key"
            @click="mvplay(item.id)"
          >
            <div class="img-wrap">
              <img :src="item.cover" alt />
              <span class="iconfont icon-play" />
              <div class="num-wrap">
                <div class="iconfont icon-play" />
                <div class="num">{{ item.playCount }}</div>
              </div>
              <span class="time">{{ item.time }}</span>
            </div>
            <div class="info-wrap">
              <div class="name">{{ item.name }}</div>
              <div class="singer">{{ item.artistName }}</div>
            </div>
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup>
import { ref, watch, provide } from '@vue/runtime-core'
import Musicplay from './MusicPlay.vue'
import { useRoute } from 'vue-router'
import router from '@/router/index.js'
import axios from 'axios'
const mvs = ref([])
const songurl = ref('')
const playlists = ref([])
const count = ref(0)
const activeIndex = ref('songs')
const list = ref('songs')
const route = useRoute()
provide('song_url', songurl)
axios({
  url: 'https://autumnfish.cn/search',
  params: {
    limit: 100,
    keywords: route.query.query
  }
}).then((res) => {
  list.value = res.data.result.songs
  count.value = res.data.result.songCount
  for (let i = 0; i < list.value.length; i++) {
    const time = parseInt(list.value[i].duration / 1000)
    const sec = parseInt((list.value[i].duration / 1000) % 60)
    const min = parseInt(time / 60)
    list.value[i].duration = min + ':' + sec
  }
})
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
function toplaylist(id) {
  router.push('/playlist?q=' + id)
}
function mvplay(id) {
  router.push('/mv?q=' + id)
}
watch(activeIndex, () => {
  let type = 1
  switch (activeIndex.value) {
    case 'songs':
      type = 1
      break
    case 'lists':
      type = 1000
      break
    case 'mv':
      type = 1004
      break
    default:
      break
  }
  if (type === 1) {
    axios({
      url: 'https://autumnfish.cn/search',
      params: {
        limit: 100,
        keywords: route.query.query
      }
    }).then((res) => {
      list.value = res.data.result.songs
      count.value = res.data.result.songCount
      for (let i = 0; i < list.value.length; i++) {
        const time = parseInt(list.value[i].duration / 1000)
        const sec = parseInt((list.value[i].duration / 1000) % 60)
        const min = parseInt(time / 60)
        list.value[i].duration = min + ':' + sec
      }
    })
  } else if (type === 1000) {
    axios({
      url: 'https://autumnfish.cn/search',
      params: {
        limit: 100,
        keywords: route.query.query,
        type
      }
    }).then((res) => {
      playlists.value = res.data.result.playlists
      count.value = res.data.result.playlistCount
    })
  } else {
    axios({
      url: 'https://autumnfish.cn/search',
      params: {
        limit: 50,
        keywords: route.query.query,
        type
      }
    }).then((res) => {
      mvs.value = res.data.result.mvs
      count.value = res.data.result.mvCount
      for (let i = 0; i < mvs.value.length; i++) {
        const time = parseInt(mvs.value[i].duration / 1000)
        const sec = parseInt((mvs.value[i].duration / 1000) % 60)
        const min = parseInt(time / 60)
        mvs.value[i].time = min + ':' + sec
      }
    })
  }
})
</script>

<style></style>
