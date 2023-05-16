<template>
  <div>
    <el-button type="primary" @click="dialogVisible = true" style="margin-bottom: 10px">
      <el-icon>
        <Plus/>
      </el-icon>
      新增反馈
    </el-button>
    <h3 style="text-align: center; font-size: 18px; font-weight: bold; padding-bottom: 10px">社区反馈</h3>
  </div>
  <div class="feedback">
    <el-table :data="feedData" style="width: 100%">
      <el-table-column prop="username" label="用户名"/>
      <el-table-column prop="name" label="姓名"/>
      <el-table-column prop="content" label="反馈内容"/>
      <el-table-column prop="create_date" label="创建时间"/>
    </el-table>

    <el-pagination class="pager" background layout="prev, pager, next" :total="config.total" :page-size="config.limit"/>
  </div>

  <el-dialog
      v-model="dialogVisible"
      title="提交社区反馈"
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
      <el-form-item label="内容" prop="content" :rules="{
        required: true,
        message: '反馈内容不能为空',
        trigger: 'blur',
      }">
        <el-input type="textarea" rows="10" v-model="formLabelAlign.content"/>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleCancel">取消</el-button>
        <el-button type="primary" @click="addFeedback">
          确定
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>
import {ref, onMounted, getCurrentInstance, reactive} from "vue";
import {useStore} from "vuex";

const store = useStore()
const {proxy} = getCurrentInstance()
const feedData = ref([])
const dialogVisible = ref(false)

// 用户ID
const userid = store.state.userid

// 新增反馈表单
const formLabelAlign = reactive({
  userid: userid,
  content: ''
})


// 分页及搜索配置
const config = reactive({
  name: '', // 搜索关键词
  total: 10,
  page: 1,
  limit: 13,
})

onMounted(() => {
  getFeedBack()
})

// 获取社区反馈
const getFeedBack = async () => {
  let res = await proxy.$api.getFeedBack(config)
  config.total = res.total
  feedData.value = res.data
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

// 新增反馈
const addFeedback = async () => {
  let res = await proxy.$api.addFeedBack(formLabelAlign)
  ElMessage({
    showClose: true,
    message: res.msg,
    type: 'success'
  })
  proxy.$refs.feedForm.resetFields()
  dialogVisible.value = false
  getFeedBack(config)
}
</script>

<style scoped lang="scss">
.feedback {
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