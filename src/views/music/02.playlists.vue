<template>
  <div class="playlists-container">
    <!-- 同步 -->
    <div class="top-card">
      <div class="icon-wrap">
        <img :src="toplist.coverImgUrl" alt />
      </div>
      <div class="content-wrap">
        <div class="tag">精品歌单</div>
        <div class="title">{{ toplist.name }}</div>
        <div class="info">{{ toplist.description }}</div>
      </div>
      <img :src="toplist.coverImgUrl" alt class="bg" />
      <div class="bg-mask" />
    </div>
    <div class="tab-container">
      <!-- tab栏 顶部 -->
      <div class="tab-bar">
        <span
          class="item"
          :class="{ active: tag === '欧美' }"
          @click="tag = '欧美'"
          >欧美</span
        >
        <span
          class="item"
          :class="{ active: tag === '华语' }"
          @click="tag = '华语'"
          >华语</span
        >
        <span
          class="item"
          :class="{ active: tag === '流行' }"
          @click="tag = '流行'"
          >流行</span
        >
        <span
          class="item"
          :class="{ active: tag === '说唱' }"
          @click="tag = '说唱'"
          >说唱</span
        >
        <span
          class="item"
          :class="{ active: tag === '摇滚' }"
          @click="tag = '摇滚'"
          >摇滚</span
        >
        <span
          class="item"
          :class="{ active: tag === '全部' }"
          @click="tag = '全部'"
          >全部</span
        >
        <span
          class="item"
          :class="{ active: tag === '民谣' }"
          @click="tag = '民谣'"
          >民谣</span
        >
        <span
          class="item"
          :class="{ active: tag === '电子' }"
          @click="tag = '电子'"
          >电子</span
        >
        <span
          class="item"
          :class="{ active: tag === '轻音乐' }"
          @click="tag = '轻音乐'"
          >轻音乐</span
        >
        <span
          class="item"
          :class="{ active: tag === '影视原声' }"
          @click="tag = '影视原声'"
          >影视原声</span
        >
        <span
          class="item"
          :class="{ active: tag === 'ACG' }"
          @click="tag = 'ACG'"
          >ACG</span
        >
        <span
          class="item"
          :class="{ active: tag === '怀旧' }"
          @click="tag = '怀旧'"
          >怀旧</span
        >
        <span
          class="item"
          :class="{ active: tag === '治愈' }"
          @click="tag = '治愈'"
          >治愈</span
        >
        <span
          class="item"
          :class="{ active: tag === '旅行' }"
          @click="tag = '旅行'"
          >旅行</span
        >
      </div>
      <!-- tab的内容区域 -->
      <div class="tab-content">
        <div class="items">
          <div
            class="item"
            v-for="item in recommendlist"
            :key="item.key"
            @click="toplaylist(item.id)"
          >
            <div class="img-wrap">
              <div class="num-wrap">
                播放量:
                <span class="num">{{ item.subscribedCount }}</span>
              </div>
              <img :src="item.coverImgUrl" alt />
              <span class="iconfont icon-play" />
            </div>
            <p class="name">{{ item.name }}</p>
          </div>
        </div>
      </div>
    </div>
    <!-- 分页器 -->
    <el-pagination
      background
      layout="prev, pager, next"
      :total="total"
      :current-page="page"
      :page-size="20"
    />
  </div>
</template>

<script setup>
import { ref, watch } from '@vue/runtime-core'
import router from '@/router/index.js'
import axios from 'axios'

const tag = ref('全部')
const recommendlist = ref([])
const toplist = ref({})
const total = ref(0)
const page = ref(1)
axios({
  url: 'https://autumnfish.cn/top/playlist/highquality',
  params: {
    limit: 60,
    cat: '全部'
  }
}).then((res) => {
  toplist.value = res.data.playlists[0]
})
axios({
  url: 'https://autumnfish.cn/top/playlist',
  params: {
    limit: 60,
    //  分页
    offset: 0,
    cat: '全部'
  }
}).then((res) => {
  recommendlist.value = res.data.playlists
})
function toplaylist(id) {
  router.push('/playlist?q=' + id)
}
watch(tag, () => {
  axios({
    url: 'https://autumnfish.cn/top/playlist/highquality',
    params: {
      limit: 60,
      cat: tag.value
    }
  }).then((res) => {
    toplist.value = res.data.playlists[0]
  })
  axios({
    url: 'https://autumnfish.cn/top/playlist',
    params: {
      limit: 60,
      //  分页
      offset: 0,
      cat: tag.value
    }
  }).then((res) => {
    recommendlist.value = res.data.playlists
  })
})
</script>

<style></style>
