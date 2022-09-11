<template>
  <div class="discovery-container">
    <Musicplay />
    <!-- 轮播图 -->
    <el-carousel class :interval="4000" type="card">
      <el-carousel-item v-for="item in lbt" :key="item.key">
        <img :src="item.imageUrl" alt />
      </el-carousel-item>
    </el-carousel>
    <!-- 推荐歌单 -->
    <div class="recommend">
      <h3 class="title">推荐歌单</h3>
      <div class="items">
        <div
          class="item"
          v-for="item in recommendlist"
          :key="item.key"
          @click="toplaylist(item.id)"
        >
          <div class="img-wrap">
            <div class="desc-wrap">
              <span class="desc">{{ item.copywriter }}</span>
            </div>
            <img :src="item.picUrl" alt />
            <span class="iconfont icon-play" />
          </div>
          <p class="name">{{ item.name }}</p>
        </div>
      </div>
    </div>
    <!-- 最新音乐 -->
    <div class="news">
      <h3 class="title">最新音乐</h3>
      <div class="items">
        <div class="item" v-for="item in newsong" :key="item.key">
          <div class="img-wrap" @click="play(item.id)">
            <img :src="item.picUrl" alt />
            <span class="iconfont icon-play" />
          </div>
          <div class="song-wrap">
            <div class="song-name">{{ item.name }}</div>
            <div class="singer">{{ item.song.artists[0].name }}</div>
          </div>
        </div>
      </div>
    </div>
    <!-- 推荐MV -->
    <div class="mvs">
      <h3 class="title">推荐MV</h3>
      <div class="items">
        <div
          class="item"
          v-for="item in mvlist"
          :key="item.key"
          @click="mvplay(item.id)"
        >
          <div class="img-wrap">
            <img :src="item.picUrl" alt />
            <span class="iconfont icon-play" />
            <div class="num-wrap">
              <div class="iconfont icon-play" />
              <div class="num">{{ item.playCount }}</div>
            </div>
          </div>
          <div class="info-wrap">
            <div class="name">{{ item.name }}</div>
            <div class="singer">{{ item.artistName }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Musicplay from './MusicPlay.vue'
import { ref, provide } from 'vue'
import router from '@/router/index.js'
import axios from 'axios'
const lbt = ref([])
const recommendlist = ref([])
const newsong = ref([])
const songurl = ref([])
const mvlist = ref([])
provide('song_url', songurl)
axios({
  url: 'https://autumnfish.cn/banner'
}).then((res) => {
  lbt.value = res.data.banners
})
axios({
  url: 'https://autumnfish.cn/personalized',
  params: {
    limit: 15
  }
}).then((res) => {
  recommendlist.value = res.data.result
})
axios({
  url: 'https://autumnfish.cn/personalized/newsong'
}).then((res) => {
  newsong.value = res.data.result
})
axios({
  url: 'https://autumnfish.cn/personalized/mv'
}).then((res) => {
  mvlist.value = res.data.result
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
</script>

<style></style>
