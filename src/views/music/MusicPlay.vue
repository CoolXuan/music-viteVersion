<template>
  <div>
    <audio :src="songurl" autoplay controls class="player" />
  </div>
</template>

<script setup>
import { inject } from 'vue'
const songurl = inject('song_url')
</script>

<style></style>
