<template>
  <div class="playlist-container">
    <Musicplay />
    <div class="top-wrap">
      <div class="img-wrap">
        <img :src="playlist.coverImgUrl" alt />
      </div>
      <div class="info-wrap">
        <p class="title">{{ playlist.name }}</p>
        <div class="author-wrap">
          <img class="avatar" :src="playlist.creator.avatarUrl" alt />
          <span class="name">{{ playlist.creator.nickname }}</span>
          <span class="time">{{ playlist.createTime }} 创建</span>
        </div>
        <div class="play-wrap">
          <span class="iconfont icon-circle-play" />
          <span class="text">播放全部</span>
        </div>
        <div class="tag-wrap">
          <span class="title">标签:</span>
          <ul>
            <li v-for="(t, key) in playlist.tags" :key="key">{{ t }}</li>
          </ul>
        </div>
        <div class="desc-wrap">
          <span class="title">简介:</span>
          <span class="desc">{{ playlist.description }}</span>
        </div>
      </div>
    </div>
    <el-tabs v-model="activeIndex">
      <el-tab-pane label="歌曲列表" name="1">
        <table class="el-table playlit-table">
          <thead>
            <th>&nbsp;</th>
            <th>&nbsp;</th>
            <th>音乐标题</th>
            <th>歌手</th>
            <th>专辑</th>
            <th>时长</th>
          </thead>
          <tbody>
            <tr
              class="el-table__row"
              v-for="(item, key) in tracks"
              :key="key"
              @click="play(item.id)"
            >
              <td>{{ key + 1 }}</td>
              <td>
                <div class="img-wrap">
                  <img :src="item.al.picUrl" alt />
                  <span class="iconfont icon-play" />
                </div>
              </td>
              <td>
                <div class="song-wrap">
                  <div class="name-wrap">
                    <span>{{ item.name }}</span>
                    <span class="iconfont icon-mv" />
                  </div>
                  <span v-if="item.alia != 0">{{ item.alia[0] }}</span>
                </div>
              </td>
              <td>
                {{ item.ar[0].name }}
                <span v-if="item.ar[1] != undefined"
                  >/{{ item.ar[1].name }}</span
                >
              </td>
              <td>{{ item.al.name }}</td>
              <td>{{ item.t }}</td>
            </tr>
          </tbody>
        </table>
      </el-tab-pane>
      <el-tab-pane label="评论" name="2">
        <!-- 精彩评论 -->
        <div class="comment-wrap">
          <p class="title">
            精彩评论
            <span class="number">{{ hottotal }}</span>
          </p>
          <div class="comments-wrap">
            <div class="item" v-for="(item, key) in hotcomments" :key="key">
              <div class="icon-wrap">
                <img :src="item.user.avatarUrl" alt />
              </div>
              <div class="content-wrap">
                <div class="content">
                  <span class="name">{{ item.user.nickname }}</span>
                  <span class="comment">{{ item.content }}</span>
                </div>
                <div class="re-content" v-if="item.beReplied.length != 0">
                  <span class="name">{{
                    item.beReplied[0].user.nickname
                  }}</span>
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
            最新评论
            <span class="number">({{ total }})</span>
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
                  <span class="name">{{
                    item.beReplied[0].user.nickname
                  }}</span>
                  <span class="comment">{{ item.beReplied[0].content }}</span>
                </div>
                <div class="date">2020-02-12 17:26:11</div>
              </div>
            </div>
          </div>
        </div>

        <!--分页器 -->
        <el-pagination
          @current-change="handleCurrentChange"
          background
          layout="prev, pager, next"
          :total="total"
          :current-page="page"
          :page-size="5"
        />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup>
import { ref, provide } from '@vue/runtime-core'
import Musicplay from './MusicPlay.vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
const route = useRoute()
const hotcomments = ref([])
const total = ref(0)
const hottotal = ref(0)
const comments = ref([])
const tracks = ref([])
const playlist = ref([])
const songurl = ref('')
// const activeIndex = ref('1')
const page = ref(1)
provide('song_url', songurl)
axios({
  url: 'https://autumnfish.cn/playlist/detail',
  params: {
    id: route.query.q
  }
}).then((res) => {
  playlist.value = res.data.playlist
  tracks.value = res.data.playlist.tracks
  for (let i = 0; i < tracks.value.length; i++) {
    const time = parseInt(tracks.value[i].dt / 1000)
    const sec = parseInt((tracks.value[i].dt / 1000) % 60)
    const min = parseInt(time / 60)
    tracks.value[i].t = min + ':' + sec
  }
})
// 获取热门评论
axios({
  url: 'https://autumnfish.cn/comment/hot',
  params: {
    id: route.query.q,
    type: 2
  }
}).then((res) => {
  hotcomments.value = res.data.hotComments
  hottotal.value = res.data.total
})
// 获取最新评论
axios({
  url: 'https://autumnfish.cn/comment/playlist',
  params: {
    id: route.query.q,
    limit: 30
  }
}).then((res) => {
  comments.value = res.data.comments
  total.value = res.data.total
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
    comments.value = res.data.comments
    total.value = res.data.total
  })
}
</script>

<style></style>
