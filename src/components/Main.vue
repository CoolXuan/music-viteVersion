<template>
  <div class="main_content">
    <!-- <div class="bg">
      <img src="/shujuji/src/assets/bg.jpg" alt="" />
    </div> -->
    <!-- <video class="bg" loop muted autoplay >
      <source src="../assets/vm2.mp4" />
    </video> -->
    <div class="main">
      <router-view />
    </div>
    <div class="recomand_box">
      <div class="author_info">
        <div class="head_img">
          <img src="../assets/logo.png" alt="" />
        </div>
        <div class="usr_id">未登录</div>
      </div>
      <div class="nav_author">
        <ul>
          <li class="author_link">
            <router-link to="/author">
              &nbsp;&nbsp;<i class="el-icon-s-custom" />个人中心</router-link
            >
          </li>
          <li class="author_link">
            <router-link to="/changedata">
              &nbsp;&nbsp;
              <i class="el-icon-postcard" />修改信息</router-link
            >
          </li>
          <li class="author_link">
            <router-link to="/sendtext">
              &nbsp;&nbsp;<i class="el-icon-edit" />发布文章</router-link
            >
          </li>
        </ul>
      </div>
      <div class="others_recommand">
        <div class="nav">
          <div class="others_recommand_title">
            <h3>🥰<i>聆听心声</i>🥰</h3>
          </div>
          <ul>
            <li class="author_link">
              <router-link to="/discovery">
                &nbsp;&nbsp; <span class="iconfont icon-find-music" />
                发现音乐
              </router-link>
            </li>
            <li class="author_link">
              <router-link to="/playlists">
                &nbsp;&nbsp; <span class="iconfont icon-music-list" />
                推荐歌单
              </router-link>
            </li>
            <li class="author_link">
              <router-link to="/songs">
                &nbsp;&nbsp; <span class="iconfont icon-music" />
                最新音乐
              </router-link>
            </li>
            <li class="author_link">
              <router-link to="/mvs">
                &nbsp;&nbsp; <span class="iconfont icon-mv" />
                最新MV
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
// import router from '@/router/index.ts'
// import axios from 'axios'
export default defineComponent({
  name: 'HelloWorld'
})
</script>

<style></style>
