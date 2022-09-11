<template>
  <div>
    <div class="color-black" style="text-align: center; margin-top: 0.4rem">
      请上传本人名片照片
    </div>
    <div class="rz-picter">
      <img :src="avatar" class="img-avatar" />
      <input
        type="file"
        name="avatar"
        id="uppic"
        accept="image/gif,image/jpeg,image/jpg,image/png"
        @change="changeImage($event)"
        ref="avatarInput"
        class="uppic"
      />
    </div>
    <div class="yzbtn">立即认证</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const avatar = ref('../assets/logo.png')
if (document.getElementById('uppic').value.length === '') {
  console.log('请上传图片')
}
function changeImage(e) {
  var file = e.target.files[0]
  var reader = new FileReader()
  var that = this
  reader.readAsDataURL(file)
  reader.onload = function (e) {
    that.avatar = this.result
  }
}
</script>

<style>
.rz-notice img {
  height: 0.22rem;
  width: 0.22rem;
}

.rz-picter {
  height: 3rem;
  width: 6rem;
  margin: 0.3rem auto;
  border: 0.01rem solid #ededed;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.uppic {
  height: 3rem;
  width: 6rem;
  margin: 0 auto;
  opacity: 0;
  z-index: 99999;
}
.img-avatar {
  position: absolute;
}
/*立即验证*/

.yzbtn {
  width: 90%;
  height: 0.8rem;
  background: #ff6600;
  border-radius: 0.06rem;
  margin: 30px auto;
  text-align: center;
  line-height: 0.8rem;
  color: #ffffff;
}
</style>
