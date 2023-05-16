<template>
  <h3 style="text-align: center; font-size: 18px; font-weight: bold">居民申请</h3>

  <div class="apply">
    <el-card class="box-card">
      <template #header>
        <div class="card-header">
          <span>提交申请</span>
          <el-button class="button" type="primary" size="small" @click="submitApply">提交</el-button>
        </div>
      </template>
      <el-form
          label-position="top"
          label-width="100px"
          :model="applyForm"
          style="max-width: 460px"
          ref="apply"
      >
        <el-form-item label="类型" prop="type" :rules="{
        required: true,
        message: '请选择申请类型',
        trigger: 'blur',
      }">
          <el-select v-model="applyForm.type" placeholder="请选择申请类型">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
        </el-form-item>
        <el-form-item label="申请时间" prop="apply_date" :rules="{
        required: true,
        message: '请选择申请日期',
        trigger: 'blur',
      }">
          <el-date-picker
              v-model="applyForm.apply_date"
              type="date"
              placeholder="选择申请日期"
              size="default"
          />
        </el-form-item>
        <el-form-item label="具体内容" prop="content">
          <el-input type="textarea" rows="5" v-model="applyForm.content"/>
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

const options = ref([
  {
    label: '外出申请',
    value: '外出申请'
  },
  {
    label: '心理咨询申请',
    value: '心理咨询申请'
  },
  {
    label: '报修申请',
    value: '报修申请'
  }
])
const userid = store.state.userid
const applyForm = reactive({
  userid: userid,
  type: '',
  content: '',
  apply_date: '',
})

// 时间格式化
const timeFormat = (date) => {
  let time = new Date(date)
  let year = time.getFullYear()
  let month = time.getMonth() + 1
  let day = time.getDay()

  function add(m) {
    return m < 10 ? "0" + m : m
  }

  return year + '-' + add(month) + '-' + add(day)
}

const submitApply = async () => {
  applyForm.apply_date = timeFormat(applyForm.apply_date)
  let res = await proxy.$api.addApply(applyForm)
  ElMessage({
    showClose: true,
    message: res.msg,
    type: 'success'
  })
  proxy.$refs.apply.resetFields()
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