<template>
  <div class="mvs-container">
    <div class="filter-wrap">
      <div class="seciton-wrap">
        <span class="section-type">地区:</span>
        <ul class="tabs-wrap">
          <li class="tab">
            <span
              class="title"
              :class="{ active: tag === '全部' }"
              @click="tag = '全部'"
              >全部</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: tag === '内地' }"
              @click="tag = '内地'"
              >内地</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: tag === '港台' }"
              @click="tag = '港台'"
              >港台</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: tag === '欧美' }"
              @click="tag = '欧美'"
              >欧美</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: tag === '日本' }"
              @click="tag = '日本'"
              >日本</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: tag === '韩国' }"
              @click="tag = '韩国'"
              >韩国</span
            >
          </li>
        </ul>
      </div>
      <div class="type-wrap">
        <span class="type-type">类型:</span>
        <ul class="tabs-wrap">
          <li class="tab">
            <span
              class="title"
              :class="{ active: flag === '全部' }"
              @click="flag = '全部'"
              >全部</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: flag === '官方版' }"
              @click="flag = '官方版'"
              >官方版</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: flag === '原声' }"
              @click="flag = '原声'"
              >原声</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: flag === '现场版' }"
              @click="flag = '现场版'"
              >现场版</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: flag === '网易出品' }"
              @click="flag = '网易出品'"
              >网易出品</span
            >
          </li>
        </ul>
      </div>
      <div class="order-wrap">
        <span class="order-type">排序:</span>
        <ul class="tabs-wrap">
          <li class="tab">
            <span
              class="title"
              :class="{ active: label === '上升最快' }"
              @click="label = '上升最快'"
              >上升最快</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: label === '最热' }"
              @click="label = '最热'"
              >最热</span
            >
          </li>
          <li class="tab">
            <span
              class="title"
              :class="{ active: label === '最新' }"
              @click="label = '最新'"
              >最新</span
            >
          </li>
        </ul>
      </div>
    </div>
    <!-- mv容器 -->
    <!-- 推荐MV -->
    <div class="mvs">
      <div class="items">
        <div
          class="item"
          @click="mvplay(item.id)"
          v-for="item in mvlist"
          :key="item.key"
        >
          <div class="img-wrap">
            <img :src="item.cover" alt />
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
      <!-- 分页器 -->
      <el-pagination
        background
        layout="prev, pager, next"
        :total="total"
        :current-page="page"
        :page-size="5"
        :limit="limit"
      />
    </div>
  </div>
</template>

<script>
import { watch, ref } from '@vue/runtime-core'
import axios from 'axios'
const tag = ref('全部')
const flag = ref('全部')
const label = ref('上升最快')
const mvlist = ref([])
// const total = ref(20)
// const page = ref(1)
// const limit = ref(10)
axios({
  url: 'https://autumnfish.cn/mv/all',
  params: {
    // 1. `area`: 地区,可选值为：全部、内地、港台、欧美、日本、韩国、不填则为全部
    area: tag.value,
    //  2. `type`: 类型,可选值为：全部、官方版、原生、现场版、网易出品,不填则为全部
    type: flag.value,
    //  3. `order`: 排序,可选值为：上升最快、最热、最新、不填则为上升最快
    order: label.value,
    //  4. `limit`: 取出数量 , 默认为 30
    limit: 60
    //  5. `offset`: 偏移数量 , 用于分页 , 如 :( 页数 -1)*50, 其中 50 为 limit 的值 , 默认 为 0
  }
}).then((res) => {
  mvlist.value = res.data.data
})
// function mvplay(id) {
//   router.push('/mv?q=' + id)
// }
watch(tag, () => {
  axios({
    url: 'https://autumnfish.cn/mv/all',
    params: {
      // 1. `area`: 地区,可选值为：全部、内地、港台、欧美、日本、韩国、不填则为全部
      area: tag.value,
      //  2. `type`: 类型,可选值为：全部、官方版、原生、现场版、网易出品,不填则为全部
      type: flag.value,
      //  3. `order`: 排序,可选值为：上升最快、最热、最新、不填则为上升最快
      order: label.value,
      //  4. `limit`: 取出数量 , 默认为 30
      limit: 60
      //  5. `offset`: 偏移数量 , 用于分页 , 如 :( 页数 -1)*50, 其中 50 为 limit 的值 , 默认 为 0
    }
  }).then((res) => {
    mvlist.value = res.data.data
  })
})
watch(flag, () => {
  axios({
    url: 'https://autumnfish.cn/mv/all',
    params: {
      // 1. `area`: 地区,可选值为：全部、内地、港台、欧美、日本、韩国、不填则为全部
      area: tag.value,
      //  2. `type`: 类型,可选值为：全部、官方版、原生、现场版、网易出品,不填则为全部
      type: flag.value,
      //  3. `order`: 排序,可选值为：上升最快、最热、最新、不填则为上升最快
      order: label.value,
      //  4. `limit`: 取出数量 , 默认为 30
      limit: 60
      //  5. `offset`: 偏移数量 , 用于分页 , 如 :( 页数 -1)*50, 其中 50 为 limit 的值 , 默认 为 0
    }
  }).then((res) => {
    mvlist.value = res.data.data
  })
})
watch(label, () => {
  axios({
    url: 'https://autumnfish.cn/mv/all',
    params: {
      // 1. `area`: 地区,可选值为：全部、内地、港台、欧美、日本、韩国、不填则为全部
      area: tag.value,
      //  2. `type`: 类型,可选值为：全部、官方版、原生、现场版、网易出品,不填则为全部
      type: flag.value,
      //  3. `order`: 排序,可选值为：上升最快、最热、最新、不填则为上升最快
      order: label.value,
      //  4. `limit`: 取出数量 , 默认为 30
      limit: 60
      //  5. `offset`: 偏移数量 , 用于分页 , 如 :( 页数 -1)*50, 其中 50 为 limit 的值 , 默认 为 0
    }
  }).then((res) => {
    mvlist.value = res.data.data
  })
})
</script>

<style></style>
