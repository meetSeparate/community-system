<template>
  <div class="common-layout">
    <el-container class="lay-container">
      <common-aside/>
      <el-container class="r-container">
        <common-header/>
        <common-tab/>
        <el-main>
          <router-view/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import CommonHeader from '../components/CommonHeader.vue'
import CommonAside from '../components/CommonAside.vue'
import CommonTab from '../components/CommonTab.vue'

</script>

<style scoped>
.r-container {
  flex-wrap: wrap;
  align-content: flex-start;
}

.common-layout {
  height: 100%;
}

.lay-container {
  height: 100%;
}
</style>