import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import path from 'path'

export default defineConfig({
  plugins: [vue()],
  define: {
    'process.env': {},
  },
  server: {
    proxy: {
      // '/api': {
      //   target: 'http://testapi.xuexiluxian.cn',
      //   changeOrigin: true,
      //   rewrite: (path) => path.replace(/^\/api/, '')
      // },
      '/apis': {
        target: '127.0.0.1:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/apis/, '')
      }
    }
  },
  resolve: {
    // 配置路径别名
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
});