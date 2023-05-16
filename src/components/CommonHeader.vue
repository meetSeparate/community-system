<script setup>
import {useStore} from 'vuex'
import {computed} from "vue";
import {useRouter} from "vue-router";

const store = useStore()
const router = useRouter()

const changeCollapse = () => {
  store.commit('changeCollapse')
}

const current = computed(() => {
  return store.state.currentMenu
})

const getImgUrl = () => {
  return new URL('../assets/104.jpg', import.meta.url).href
}

const logout = () => {
  store.commit('Logout')

  router.push({
    name: 'login'
  })
}
</script>

<template>
  <el-header>
    <div class="l-content">
      <el-button size="small" @click="changeCollapse">
        <el-icon :size="20">
          <Menu/>
        </el-icon>
      </el-button>

      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
        <el-breadcrumb-item :to="current.path" class="bread">{{current.label}}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="r-content">
      <el-dropdown>
        <span class="el-dropdown-link">
<!--          <el-avatar :size="40" :src="getImgUrl()" />-->
          <img src="https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif?imageView2/1/w/80/h/80"
               class="user">
          <el-icon class="icons"><CaretBottom/></el-icon>
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item>个人中心</el-dropdown-item>
            <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </el-header>
</template>

<style scoped lang="scss">
header {
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #fff;
}

.r-content .user {
  cursor: pointer;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  border-style: none;
}

.l-content {
  display: flex;
  align-items: center;

  .el-button {
    margin-right: 20px;
  }

  h3 {
    color: #97a8c4;
    font-size: 14px;
  }
}

.icons {
  position: absolute;
  top: 18px;
}

</style>