<template>
  <div class="mv-container">
    <div class="mv-wrap">
      <h3 class="title">mv详情</h3>
      <!-- mv -->
      <div class="video-wrap">
        <video controls :src="mvurl" />
      </div>
      <!-- mv信息 -->
      <div class="info-wrap">
        <div class="singer-info">
          <div class="avatar-wrap">
            <img :src="detail.cover" alt="" />
          </div>
          <span class="name">{{ detail.artists[0].name }}</span>
        </div>
        <div class="mv-info">
          <h2 class="title">{{ detail.name }}</h2>
          <span class="date">发布：{{ detail.publishTime }}</span>
          <span class="number">播放：{{ detail.playCount }}次</span>
          <p class="desc">
            {{ detail.desc }}
          </p>
        </div>
      </div>
      <!-- 精彩评论 -->
      <div class="comment-wrap">
        <p class="title">
          最新评论
          <span class="number">({{ hottotal }})</span>
        </p>
        <div class="comments-wrap">
          <div class="item" v-for="(item, key) in comments" :key="key">
            <div class="icon-wrap">
              <img :src="item.user.avatarUrl" alt />
            </div>
            <div class="content-wrap">
              <div class="content">
                <span class="name">{{ item.user.nickname }}</span>
                <span class="comment">{{ item.content }}</span>
              </div>
              <div class="re-content" v-if="item.beReplied.length != 0">
                <span class="name">{{ item.beReplied[0].user.nickname }}</span>
                <span class="comment">{{ item.beReplied[0].content }}</span>
              </div>
              <div class="date">2020-02-12 17:26:11</div>
            </div>
          </div>
        </div>
      </div>
      <!-- 最新评论 -->
      <div class="comment-wrap">
        <p class="title">
          所有评论<span class="number">({{ total }})</span>
        </p>
        <div class="comments-wrap">
          <div class="item" v-for="(item, key) in comments" :key="key">
            <div class="icon-wrap">
              <img :src="item.user.avatarUrl" alt="" />
            </div>
            <div class="content-wrap">
              <div class="content">
                <span class="name">{{ item.user.nickname }}</span>
                <span class="comment">{{ item.content }}</span>
              </div>
              <div class="re-content" v-if="item.beReplied.length != 0">
                <span class="name">{{ item.beReplied[0].user.nickname }}</span>
                <span class="comment">{{ item.beReplied[0].content }}</span>
              </div>
              <div class="date">2020-02-12 17:26:11</div>
            </div>
          </div>
        </div>
      </div>
      <!-- 分页器 -->
      <el-pagination
        @current-change="handleCurrentChange"
        background
        layout="prev, pager, next"
        :total="total"
        :current-page="page"
        :page-size="20"
        :limit="limit"
      />
    </div>
    <div class="mv-recommend">
      <h3 class="title">相关推荐</h3>
      <div class="mvs">
        <div class="items">
          <div
            class="item"
            v-for="(item, key) in simimv"
            :key="key"
            @click="mvplay(item.id)"
          >
            <div class="img-wrap">
              <img :src="item.cover" alt="" />
              <span class="iconfont icon-play" />
              <div class="num-wrap">
                <div class="iconfont icon-play" />
                <div class="num">{{ item.playCount }}</div>
              </div>
              <span class="time">{{ item.d }}</span>
            </div>
            <div class="info-wrap">
              <div class="name">{{ item.name }}</div>
              <div class="singer">{{ item.artistName }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from '@vue/runtime-core'
import { useRoute } from 'vue-router'
import router from '@/router/index.js'
import axios from 'axios'
const route = useRoute()
const hottotal = ref(0)
const total = ref(0)
const comments = ref([])
const hotcomments = ref([])
const simimv = ref([])
const detail = ref({})
const mvurl = ref([])
const page = ref(1)
const limit = ref(30)
axios({
  url: 'https://autumnfish.cn/comment/mv',
  params: {
    id: route.query.q
  }
}).then((res) => {
  comments.value = res.data.comments
  hotcomments.value = res.data.hotComments
  hottotal.value = hotcomments.value.length
  total.value = res.data.total
})
axios({
  url: 'https://autumnfish.cn/mv/url',
  params: {
    id: route.query.q
  }
}).then((res) => {
  mvurl.value = res.data.data.url
})
axios({
  url: 'https://autumnfish.cn/simi/mv',
  params: {
    mvid: route.query.q
  }
}).then((res) => {
  simimv.value = res.data.mvs
  for (let i = 0; i < simimv.value.length; i++) {
    const time = parseInt(simimv.value[i].duration / 1000)
    const sec = parseInt((simimv.value[i].duration / 1000) % 60)
    const min = parseInt(time / 60)
    simimv.value[i].d = min + ':' + sec
  }
})
axios({
  url: 'https://autumnfish.cn/mv/detail',
  params: {
    mvid: route.query.q
  }
}).then((res) => {
  detail.value = res.data.data
})
function mvplay(id) {
  router.push('/mv?q=' + id)
}
function handleCurrentChange(val) {
  // 保存页码
  page.value = val
  // 重新获取数据
  axios({
    url: 'https://autumnfish.cn/comment/playlist',
    params: {
      id: route.query.q,
      limit: 30,
      offset: (page.value - 1) * 10
    }
  }).then((res) => {
    total.value = res.data.total
  })
}
</script>
<style></style>
