<template>
  <div>
    <div
      class="header"
      style="background: url('../assets/bi1.png') 2 2; background-size: 2rem"
    >
      <!-- <img class="header_bg"  alt="" /> -->
      <div class="shujuji">shujuji</div>
      <ul class="ul_link">
        <li class="link">
          <router-link to="/"> <i class="el-icon-s-home" />首页 </router-link
          >&nbsp;&nbsp;|
        </li>
        <li class="link">
          <router-link to="/discuss">
            <i class="el-icon-s-comment" />论坛 </router-link
          >&nbsp;&nbsp;|
        </li>
        <li class="link">
          <router-link to="/idea">
            <i class="el-icon-question" />心得
          </router-link>
          &nbsp;&nbsp;|
        </li>
        <li class="link">
          <router-link to="/back"
            ><i class="el-icon-info" />反馈意见</router-link
          >
        </li>
      </ul>
      <div class="mid_search">
        <input
          type="text"
          class="search_box"
          @keyup.enter="search"
          v-model="query"
          placeholder="请输入搜索内容..."
        />
        <button class="btn search_btn" @click="search">搜索</button>
      </div>
      <button class="btn login_btn" @click="denglu">登录</button>
      <div class="box" v-if="active" @blur="loseAim">
        <h2>
          <span @click="change1">登录</span>|<span @click="change2">注册</span>
        </h2>
        <form class="login" v-if="exchange1" method="GET">
          <div class="inputBox">
            <label>账&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
            <input
              type="text"
              placeholder="请输入电话号码/Email"
              v-model="email"
              class="login_input"
            />
          </div>
          <div class="inputBox">
            <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
            <input class="login_input" type="password" name="" v-model="pwd" />
          </div>
          <input type="submit" class="submit" value="登录" @click="login" />
        </form>
        <form class="register" v-if="exchange2">
          <div class="inputBox">
            <label>账&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号</label>
            <input
              type="text"
              class="login_input"
              placeholder="请输入电话号码/Email"
              v-model="email"
            />
          </div>
          <div class="inputBox">
            <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
            <input
              class="login_input"
              type="password"
              name=""
              v-model="pwd"
            /><br />
          </div>
          <div class="inputBox">
            <label>确认密码</label>
            <input class="login_input" type="text" name="" v-model="repwd" />
          </div>
          <div class="inputBox">
            <label>验&nbsp;&nbsp;证&nbsp;&nbsp;码</label>
            <input
              class="login_input"
              type="text"
              name=""
              style="width: 4rem"
              v-model="code"
            />
            <input
              class="send_email"
              type="submit"
              style="height: 1.5rem; line-heigth: 1.5rem; font-weight: 400"
              value="发送邮件"
              @click="get_code"
            />
          </div>
          <div class="ok" v-if="check">{{ warning_msg }}</div>
          <input type="submit" class="submit" value="注册" @click="zhuce" />
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, watch } from "@vue/runtime-core";
import router from "@/router/index.js";
import axios from "axios";
const query = ref("");
const user_name = ref("");
const active = ref(false);
const style1 = ref({});
const check = ref(false);
// const ok = ref(false)
const exchange1 = ref(true);
const exchange2 = ref(false);
const warning_msg = ref("");
// const id= ref('')
const pwd = ref("");
const repwd = ref("");
const email = ref("");
const code = ref("");
const userState = reactive({
  email: "",
  pwd: "",
  repwd: "",
});
function search() {
  if (query.value === "") {
    alert("请输入内容");
  } else {
    router.push("/result?query=" + query.value);
  }
}

function initmsg() {
  // msg数据初始化
  // id = ''
  userState.email = "";
  userState.pwd = "";
  userState.repwd = "";
}
let loseAim = function () {
  initmsg();
  active.value = false;
};
function login() {
  if (userState.email.match(/.+@.+\..+/)) {
    const url = "/apis/login/" + userState.email + "&" + userState.pwd;
    axios.post(url).then((res) => {
      user_name.value = res.data;
      console.log(res.data);
      if (user_name.value !== "login_error") {
        active.value = !active.value;
        alert("登录成功，欢迎" + user_name.value);
        initmsg();
      } else {
        alert("登录失败，可能此账号未注册！");
      }
    });
  } else {
    alert("邮箱格式不匹配！");
  }
}

function change1() {
  exchange1.value = true;
  exchange2.value = false;
  initmsg();
}
function change2() {
  exchange1.value = false;
  exchange2.value = true;
  initmsg();
}
function denglu() {
  initmsg();
  active.value = !active.value;
  console.log(active.value);
  if (active.value) {
    style1.value = { filter: "blur(15px)" };
  } else {
    style1.value = {};
  }
}
watch(
  () => {
    userState.pwd;
  },
  () => {
    if (userState.pwd !== userState.repwd) {
      userState.warning_msg = "确认密码不一致！";
      check.value = true;
    } else if (pwd.value === repwd.value) {
      if (!pwd.value.match(/^(?![0-9]+$)(?![a-zA-Z]+$)[0-9a-zA-Z]{8,12}$/)) {
        warning_msg.value = "密码必须是8-12位且包含数值和字母！";
      } else {
        check.value = false;
      }
    }
  },
  {
    immediate: true,
    deep: true,
  }
);
function get_code() {
  console.log("get-code");
  // if (userState.email.match("\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*")) {
    const url = "/apis/ecode/" + userState.email;
    axios.post(url).then((data) => {
      data = data.data;
      if (data === "email-invalid") {
        alert("邮箱地址格式不正确.");
        return false;
      }
      if (data === "send-pass") {
        alert("邮箱验证码已成功发送，请查收.");
        return false;
      }
      if (data === "user-repeated") {
        userState.email = "";
        userState.pwd = "";
        userState.repwd = "";
        alert("邮箱已注册，请重新输入其他邮箱！");
        return false;
      }
      if (data === "send-fail") {
        alert("邮箱验证码未发送成功.");
        return false;
      }
    });
  // } else {
  //   alert("邮箱地址格式不正确1.");
  // }
}
function zhuce() {
  if (userState.email === "" || userState.pwd === "" || userState.code) {
    alert("请填写全所有信息！");
  }
  const url =
    "/apis/user/" +
    userState.email +
    "&" +
    userState.pwd +
    "&" +
    userState.code;
  axios.post(url).then((data) => {
    data = data.data;
    if (data === "ecode-error") {
      alert("验证码输入错误！");
    }
    if (data === "reg-pass") {
      alert("注册并登录成功");
      user_name.value = data.data.user_name;
      active.value = false;
    }
  });
}
</script>

<style scoped></style>
