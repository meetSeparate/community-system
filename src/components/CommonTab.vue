<template>
  <div class="tags">
    <el-tag
        v-for="(item, index) in tags"
        :key="item.name"
        :closable="item.name!=='home'"
        :effect="$route.name === item.name ? 'dark' : 'plain'"
        @click="changeMenu(item)"
        @close="handleClose(item, index)">
      {{ item.label }}
    </el-tag>
  </div>
</template>

<script setup>
import {useStore} from "vuex";
import {useRouter, useRoute} from "vue-router";

const store = useStore()
const router = useRouter()
const route = useRoute()

const tags = store.state.tabList
const changeMenu = (item) => {
  router.push({
    name: item.name
  })
}

const handleClose = (item, index) => {
  let length = tags.length
  store.commit('closeTag', item)
  if (item.name !== route.name) {
    return
  }
  if (index === length - 1) {
    router.push({
      name: tags[index - 1].name
    })
  } else {
    router.push({
      name: tags[index].name
    })
  }
}
</script>

<style scoped lang="scss">
.tags {
  padding: 20px;
  width: 100%;

  .el-tag {
    margin-right: 15px;
    cursor: pointer;
  }
}
</style>