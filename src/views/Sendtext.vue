<template>
  <div class="sendtext">
    <span class="title_label">标题：</span
    ><input type="text" class="title_box" placeholder="请输入搜索内容..." />
    <div class="foot">
      <span class="title_label">投稿类型：</span>
      <el-select
        class="tougao inline_block"
        v-model="value"
        placeholder="投稿类型"
      >
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        />
      </el-select>
      <span class="title_label">阅读积分：</span
      ><input class="tougao inline_block" v-model="jifen" placeholder="1-10" />
      <el-switch
        class="inline_block type_author"
        v-model="value2"
        active-color="#13ce66"
        inactive-color="#ff4949"
        active-text="自制"
        inactive-text="转载"
      />

      <button class="btn text_submit">提交</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Sendtext',
  data() {
    return {
      options: [
        {
          value: '选项1',
          label: '技术交流'
        },
        {
          value: '选项2',
          label: '经验分享'
        },
        {
          value: '选项3',
          label: '论点杂谈'
        },
        {
          value: '选项4',
          label: '其他'
        }
      ],
      value: '',
      jifen: '',
      value2: true
    }
  }
}
</script>

<style scoped="scoped"></style>
