<template>
  <div>
    <el-button type="primary" @click="dialogVisible = true" style="margin-bottom: 10px">
      <el-icon>
        <Plus/>
      </el-icon>
      健康打卡
    </el-button>
    <h3 style="text-align: center; font-size: 18px; font-weight: bold; padding-bottom: 10px">健康打卡</h3>
  </div>
  <div class="heath">
    <el-table :data="heathData" style="width: 100%">
      <el-table-column prop="username" label="用户名"/>
      <el-table-column prop="name" label="姓名"/>
      <el-table-column prop="temperature" label="体温"/>
      <el-table-column prop="status" label="健康状况"/>
      <el-table-column prop="create_date" label="创建时间"/>
    </el-table>

    <el-pagination class="pager" background layout="prev, pager, next" :total="config.total" :page-size="config.limit"/>
  </div>
  <el-dialog
      v-model="dialogVisible"
      title="每日健康打卡"
      width="30%"
      :before-close="handleClose"
  >
    <el-form
        label-position="top"
        label-width="100px"
        :model="formLabelAlign"
        style="max-width: 460px"
        ref="feedForm"
    >
      <el-form-item label="体温" prop="temperature" :rules="{
        required: true,
        message: '体温不能为空',
        trigger: 'blur',
      }">
        <el-input v-model="formLabelAlign.temperature"/>
      </el-form-item>
      <el-form-item label="健康状况" prop="status" :rules="{
        required: true,
        message: '健康状况不能为空',
        trigger: 'blur',
      }">
        <el-input v-model="formLabelAlign.status"/>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleCancel">取消</el-button>
        <el-button type="primary" @click="addHeath">
          确定
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import {ref, reactive, getCurrentInstance, onMounted} from "vue";
import {useStore} from "vuex";

const {proxy} = getCurrentInstance()
const store = useStore()

// 分页及搜索配置
const config = reactive({
  userid: store.state.userid,
  name: '', // 搜索关键词
  total: 10,
  page: 1,
  limit: 13,
})

const formLabelAlign = reactive({
  userid: store.state.userid,
  temperature: '',
  status: '',
})

const heathData = ref([])
const dialogVisible = ref(false)

onMounted(() => {
  getHeath()
})

// 获取个人打卡
const getHeath = async () => {
  let res = await proxy.$api.getHeath(config)
  heathData.value = res.data
  config.total = res.total
}

// 关闭前回调
const handleClose = (down) => {
  proxy.$refs.feedForm.resetFields()
  down()
}

// 取消事件
const handleCancel = () => {
  proxy.$refs.feedForm.resetFields()
  dialogVisible.value = false
}

// 每日打卡
const addHeath = async () => {
  let res = await proxy.$api.addHeath(formLabelAlign)
  ElMessage({
    showClose: true,
    message: res.msg,
    type: 'success',
  })
  proxy.$refs.feedForm.resetFields()
  dialogVisible.value = false
  await getHeath()
}
</script>

<style scoped lang="scss">
.heath {
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