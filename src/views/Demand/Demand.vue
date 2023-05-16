<template>
  <h3 style="text-align: center; font-size: 18px; font-weight: bold">用户需求</h3>
  <div class="apply">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>提交需求</span>
          <el-button class="button" type="primary" size="small" @click="submitDemand">提交</el-button>
        </div>
      </template>
      <el-form
          label-position="top"
          label-width="100px"
          :model="demandForm"
          style="max-width: 460px"
          ref="demand"
      >
        <el-form-item label="具体需求" prop="content" :rules="{
        required: true,
        message: '需求内容不能为空',
        trigger: 'blur',
      }">
          <el-input type="textarea" rows="5" v-model="demandForm.content"/>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import {ref, reactive, getCurrentInstance} from "vue";
import {useStore} from "vuex";

const store = useStore()
const {proxy} = getCurrentInstance()
const demandForm = reactive({
  userid: store.state.userid,
  content: '',
})

const submitDemand = async () => {
  let res = await proxy.$api.addDemand(demandForm)
  ElMessage({
    showClose: true,
    message: res.msg,
    type: 'success'
  })
  proxy.$refs.demand.resetFields()
}

</script>

<style scoped>
.apply {
  height: 680px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 480px;
}
</style>