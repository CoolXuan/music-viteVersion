<template>
  <div class="sendtext">
    <span class="title_label">标题：</span><input type="text" class="title_box" placeholder="请输入搜索内容..." />
    <QuillEditor style="height: 600px; margin-bottom: 10px" content-type="html" v-model:content="content"
      :toolbar="op.mo.toolbar" />
    <div class="foot">
      <span class="title_label">投稿类型：</span>
      <el-select class="tougao inline_block" v-model="value" placeholder="投稿类型">
        <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
      </el-select>
      <span class="title_label">阅读积分：</span><input class="tougao inline_block" v-model="jifen" placeholder="1-10" />
      <el-switch class="inline_block type_author" v-model="value2" active-color="#13ce66" inactive-color="#ff4949"
        active-text="自制" inactive-text="转载" />
      <button class="btn text_submit" @click="submitText">提交</button>
    </div>
  </div>
</template>

<script>
import { QuillEditor } from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css'
export default {
  name: 'Sendtext',
  data() {
    return {
      op: {
        debug: "info",
        mo: {
          toolbar: [
            "bold",
            "italic",
            "underline",
            "strike", // toggled buttons
            "blockquote",
            "image",
            // "code-block",

            { header: 1 },
            { header: 2 }, // custom button values
            { list: "ordered" },
            { list: "bullet" },
            // { script: "sub" },
            // { script: "super" }, // superscript/subscript
            { indent: "-1" },
            { indent: "+1" }, // outdent/indent
            { direction: "rtl" }, // text direction

            { size: ["small", false, "large", "huge"] }, // custom dropdown
            { header: [1, 2, 3, 4, 5, 6, false] },

            { color: [] },
            { background: [] }, // dropdown with defaults from theme
            { font: [] },
            { align: [] },
            "clean", // remove formatting button
          ],
        },
        placeholder: "编辑您的内容...",
        theme: "snow",
      },
      content: '123',
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
  },
  components: {
    QuillEditor
  }
}
</script>

<style scoped="scoped">

</style>
