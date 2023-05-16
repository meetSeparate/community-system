<template>
  <h3 style="text-align: center; font-size: 18px; font-weight: bold; padding-bottom: 10px">缴费通知</h3>
  <div class="pay">
    <el-table :data="payData" style="width: 100%">
      <el-table-column prop="username" label="用户名"/>
      <el-table-column prop="name" label="姓名"/>
      <el-table-column prop="pay_type" label="缴费类型"/>
      <el-table-column prop="price" label="缴费金额"/>
      <el-table-column prop="pay_date" label="缴纳月份"/>
      <el-table-column prop="status" label="缴费状态"/>
      <el-table-column prop="create_date" label="创建时间"/>
      <el-table-column fixed="right" label="Operations" width="120">
        <template #default="scope">
          <el-button type="primary" size="small" @click="handleClick(scope.row)">缴费</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-pagination class="pager" background layout="prev, pager, next" :total="config.total" :page-size="config.limit"/>
  </div>
</template>

<script setup>
import {ref, getCurrentInstance, onMounted, reactive} from "vue";
import {useStore} from "vuex";

const {proxy} = getCurrentInstance()
const store = useStore()
const config = reactive({
  total: 10,
  limit: 13,
  page: 1,
  userid: store.state.userid
})

const payData = ref([])

onMounted(() => {
  getPay()
})

const getPay = async () => {
  let res = await proxy.$api.getPay(config)
  config.total = res.total
  payData.value = res.data
}

const handleClick = async (row) => {
  let res = await proxy.$api.changePayStatus(row)
  ElMessage({
    showClose: true,
    message: res.msg,
    type: 'success'
  })
  await getPay()
}
</script>

<style scoped lang="scss">
.pay {
  position: relative;
  height: 680px;

  .pager {
    position: absolute;
    right: 45%;
    bottom: 0;

    .el-pager {

      li {
        background-color: #fff;
      }
    }

  }
}
</style>