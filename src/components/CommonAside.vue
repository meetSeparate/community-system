<template>
  <el-aside :width="!$store.state.collapse ? '200px' : '64px'">
    <el-menu class="el-menu-vertical-demo"
             :collapse="$store.state.collapse"
             background-color="#304156"
             text-color="rgb(191, 203, 217)"
             :collapse-transition="false"
             default-active="home">

      <h3 v-show="!$store.state.collapse">社区管理系统</h3>
      <h3 v-show="$store.state.collapse">系统</h3>
      <el-menu-item :index="item.name" v-for="(item, index) in noChildren()" :key="item.path" @click="clickMenu(item)">
        <component class="icons" :is="item.icon"></component>
        <span>{{ item.label }}</span>
      </el-menu-item>

      <el-sub-menu :index="item.label" v-for="item in hasChildren()" :key="item.label">
        <template #title>
          <component class="icons" :is="item.icon"></component>
          <span>{{ item.label }}</span>
        </template>
        <el-menu-item-group>
          <el-menu-item :index="subItem.path" v-for="subItem in item.children" :key="subItem.path" @click="clickMenu(subItem)">
            <!--            <component class="icons" :is="subItem.icon"></component>-->
            <span>{{ subItem.label }}</span>
          </el-menu-item>
        </el-menu-item-group>
      </el-sub-menu>

    </el-menu>
  </el-aside>
</template>

<script setup>
import {useRouter} from 'vue-router'
import {useStore} from "vuex";

const router = useRouter()
const store = useStore()

const list = store.state.menu

const noChildren = () => {
  return list.filter((item) => !item.children)
}

const hasChildren = () => {
  return list.filter((item) => item.children)
}


const clickMenu = (item) => {
  store.commit('selectMenu', item)
  router.push({
    name: item.name
  })
}
</script>

<style scoped lang="scss">
.el-menu {
  h3 {
    line-height: 50px;
    text-align: center;
    color: rgb(191, 203, 217);
    margin-right: 25px;
  }
  font-weight: 600;
}


.icons {
  width: 16px;
  height: 16px;
  //margin-right: 5px;
}

.el-aside {
  height: 100%;
  background-color: #304156;
  border-right: none;
}

.el-menu-item, .el-sub-menu__title {

  &:hover {
    background-color: #263445 !important;
  }

}

.el-sub-menu {
  display: grid;


  .el-menu-item {
    background-color: #1f2d3d;

    &:hover {
      background-color: #001528 !important;
    }
  }
}

span {
  padding-left: 10px;
}

</style>