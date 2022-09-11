<template>
  <div class="content">
    <div class="home">
      <!-- 轮播图 -->
      <div>
        <el-carousel :interval="4000" type="card" height="200px">
          <!-- <el-carousel-item v-for="(item, index) in lbt" :key="index">
            <img class="lbtimg" :src="item.imageUrl" />
          </el-carousel-item> -->
        </el-carousel>
      </div>
      <!-- 轮播图 -->
      <div class="article">
        <div class="article_content">
          <img src="../assets/logo.png" alt="" class="summary_img" />
          <div class="summary">
            <a class="a_title" href="#">用心看世界</a>
            <div class="article_info">
              作者:cx&nbsp;&nbsp;文章类型:科学&nbsp;&nbsp;发表时间:2021-13-14
              5:20
            </div>
            <div class="text_summary">
              wo的法律看见分厘卡顺丰大件安抚安康时间分厘卡看来都是风景啊发觉得分厘卡的房间咖啡唉可怜的激发了开发商开发
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Main',
  data() {
    return {
      lbt: ''
    }
  },
  created() {
    axios({
      url: 'https://autumnfish.cn/banner'
    }).then(res => {
      this.lbt = res.data.banners
      console.log(this.lbt)
    })
  }
}
</script>

<style scoped>
.content {
  background-color: rgb(0, 0, 0);
  border-radius: 0.4rem;
  height: auto;
}
.lbtimg {
  border-radius: 0.4rem;
  height: 200px;
  width: 100%;
  z-index: -1;
}
.article {
  overflow: hidden;
  padding: 0.5rem 0.5rem 0.5rem 0.5rem;
  padding: auto;
}
.article_content {
  border-radius: 0.4rem;
  background-color: rgba(230, 223, 223, 0.705);
  width: 100%;
  height: 5.11rem;
  transition: transform 0.1s ease-in 0.05s;
}
.article_content:hover {
  transform: scale(1.01);
}
.summary_img {
  float: left;
  width: 10%;
  margin-right: 1rem;
  width: 4rem;
  height: 4rem;
}
.summary {
  border-radius: 0.4rem;
  float: left;
  width: 90%;
  height: auto;
}
.a_title {
  text-decoration: none;
  font-size: 1.4rem;
  font-weight: 800;
  color: rgb(101, 27, 240);
}
.article_info {
  margin-top: 0.2rem;
  margin-bottom: 0.2rem;
  font-size: 0.8rem;
  font-weight: 400;
}
.text_summary {
  font-weight: 500;
}
</style>
