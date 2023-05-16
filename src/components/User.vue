<template>
  <div class="operation">
    <el-button type="primary" @click="handleAdd">
      <el-icon>
        <Plus/>
      </el-icon>
      新增用户
    </el-button>
    <h3 style="font-weight: 500; font-size: 20px">{{info}}管理</h3>
    <el-form :inline="true" :model="formInline" class="demo-form-inline">
      <el-form-item label="请输入">
        <el-input v-model="formInline.value" placeholder="请输入用户名"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="searchUser">
          <el-icon>
            <Search/>
          </el-icon>
          搜索
        </el-button>
      </el-form-item>
    </el-form>
  </div>

  <div class="user-list">
    <el-table :data="userData" style="width: 100%">
      <el-table-column fixed
                       v-for="item in userHeader"
                       :key="item.prop"
                       :prop="item.prop"
                       :label="item.label"/>
      <el-table-column fixed="right" label="Operations">
        <template #default="scope">
          <el-button size="small" @click="handleEdit(scope.row)">编辑</el-button>
          <el-button type="danger" size="small" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-pagination
        small
        background
        layout="prev, pager, next"
        :total="config.total"
        class="mt-4 pager"
        :page-size="config.limit"
        @current-change="changePage"
    />
  </div>
  <el-dialog v-model="dialogFormVisible" :title="flag === 'add' ? '新增用户' : '编辑用户'" :before-close="handleClose">
    <el-form :model="userForm" ref="userTable" :rules="rules">
      <el-form-item label="用户名" :label-width="formLabelWidth" prop="username">
        <el-input v-model="userForm.username" autocomplete="off"/>
      </el-form-item>
      <el-form-item label="密码" :label-width="formLabelWidth" prop="password" v-show="flag === 'add'">
        <el-input v-model="userForm.password" autocomplete="off"/>
      </el-form-item>
      <el-form-item label="姓名" :label-width="formLabelWidth" prop="name">
        <el-input v-model="userForm.name" autocomplete="off"/>
      </el-form-item>
      <el-form-item label="性别" :label-width="formLabelWidth" prop="sex">
        <el-select v-model="userForm.sex" placeholder="请选择性别">
          <el-option label="男" value="男"/>
          <el-option label="女" value="女"/>
        </el-select>
      </el-form-item>
      <el-form-item label="年龄" :label-width="formLabelWidth" prop="age">
        <el-input v-model.number="userForm.age" autocomplete="off"/>
      </el-form-item>
      <el-form-item label="出生日期" :label-width="formLabelWidth" prop="birth">
        <el-date-picker
            style="width: 300px"
            v-model="userForm.birth"
            type="date"
            placeholder="Pick a day"
            size="default"
        />
      </el-form-item>
      <el-form-item label="地址" :label-width="formLabelWidth" prop="addr">
        <el-input v-model="userForm.addr" autocomplete="off"/>
      </el-form-item>
      <el-form-item label="用户角色" :label-width="formLabelWidth" prop="role">
        <el-select v-model="userForm.role" placeholder="请选择用户角色">
          <el-option label="超级管理员" value="超级管理员"/>
          <el-option label="社区管理员" value="社区管理员"/>
          <el-option label="普通用户" value="普通用户"/>
        </el-select>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="closeDialog">取消</el-button>
        <el-button type="primary" @click="addUser">
          确定
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>

import {onMounted, getCurrentInstance, ref, reactive} from "vue";

const {proxy} = getCurrentInstance()

onMounted(() => {
  getUserList(config)
})

const userData = ref([])
const props = defineProps({
  info: String,
})

let flag = ref('add')

// 用户展示分页搜索配置
const config = reactive({
  name: props.info,
  total: 0,
  page: 1,
  limit: 13,
})
const formInline = reactive({
  value: ''
})

// 表单width大小
const formLabelWidth = '140px'

// 新增用户Form表单
const userForm = reactive({
  nid: '',
  username: '',
  password: '',
  name: '',
  sex: '',
  age: '',
  birth: '',
  addr: '',
  role: ''
})

// 对话框显示的flag
const dialogFormVisible = ref(false)

const userHeader = ref([
  {
    prop: 'username',
    label: '用户名',
  },
  {
    prop: 'name',
    label: '姓名'
  },
  {
    prop: 'sex',
    label: '性别'
  },
  {
    prop: 'age',
    label: '年龄'
  },
  {
    prop: 'birth',
    label: '出生日期'
  },
  {
    prop: 'addr',
    label: '地址'
  },
  {
    prop: 'role',
    label: '用户角色'
  }

])

// 新增和编辑用户的表单验证
const rules = reactive({
  username: [
    {required: true, message: '请输入用户名', trigger: 'blur'},
  ],
  password: [
    {required: true, message: '请输入密码', trigger: 'blur'},
  ],
  name: [
    {required: true, message: '请输入姓名', trigger: 'blur'},
  ],
  sex: [
    {
      required: true,
      message: '请选择性别',
      trigger: 'blur',
    },
  ],
  age: [
    {
      required: true,
      message: '请输入年龄',
      trigger: 'blur',
    },
    {
      type: 'number',
      message: '年龄必须为数字类型',
      trigger: 'blur',
    }
  ],
  birth: [
    {
      type: 'date',
      required: true,
      message: '请选择日期',
      trigger: 'blur',
    },
  ],
  addr: [
    {
      required: true,
      message: '请输入地址',
      trigger: 'blur',
    },
  ],
  role: [
    {
      required: true,
      message: '请选择用户角色',
      trigger: 'blur',
    },
  ],
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

// 获取用户列表
const getUserList = async (config) => {
  let res = await proxy.$api.getUserList(config)
  config.total = res.total
  userData.value = res.data
}

// 分页
const changePage = (page) => {
  config.page = page
  getUserList(config)
}

// 搜索
const searchUser = () => {
  config.name = formInline.value
  getUserList(config)
}

// 新增以及编辑用户
const addUser = () => {
  proxy.$refs.userTable.validate(async (valid) => {
    if (valid) {
      if (flag.value === 'add') {
        userForm.birth = timeFormat(userForm.birth)
        let res = await proxy.$api.addUser(userForm)
        proxy.$refs.userTable.resetFields()
        dialogFormVisible.value = false
        ElMessage({
          showClose: true,
          message: '成功！',
          type: 'success'
        })
        getUserList(config)
      } else {
        let res = await proxy.$api.editUser(userForm)
        proxy.$refs.userTable.resetFields()
        dialogFormVisible.value = false
        ElMessage({
          showClose: true,
          message: '成功！',
          type: 'success'
        })
        getUserList(config)
      }
    } else {
      ElMessage({
        showClose: true,
        message: '请输入正确的内容',
        type: 'error'
      })
    }
  })

}

const handleClose = (down) => {
  proxy.$refs.userTable.resetFields()
  down()
}

const closeDialog = () => {
  proxy.$refs.userTable.resetFields()
  dialogFormVisible.value = false
}

// 编辑用户开关
const handleEdit = (row) => {
  flag.value = 'edit'
  dialogFormVisible.value = true
  proxy.$nextTick(() => {
    Object.assign(userForm, row)
  })
}

// 新增用户开关
const handleAdd = () => {
  flag.value = 'add'
  dialogFormVisible.value = true
}

// 删除用户
const handleDelete = (row) => {
  ElMessageBox.confirm(
      '确定删除此用户吗？',
      'Warning',
      {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }
  )
      .then(() => {
        proxy.$api.deleteUser(row)
        ElMessage({
          showClose: true,
          type: 'success',
          message: '删除成功',
        })
        getUserList(config)
      })
      .catch(() => {
        ElMessage({
          showClose: true,
          type: 'info',
          message: '取消删除',
        })
      })
}
</script>

<style scoped lang="scss">
.user-list {
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

:deep(.el-pagination.is-background .el-pager li:not(.is-disabled)) {
  background-color: #fff !important; //修改默认的背景色
}

:deep(.el-pagination.is-background .el-pager li:not(.is-disabled).is-active) {
  background-color: #409eff !important; //修改默认的背景色
}

.operation {
  display: flex;
  justify-content: space-between;
}


.el-button--text {
  margin-right: 15px;
}

.el-select {
  width: 300px;
}

.el-input {
  width: 300px;
}

.dialog-footer button:first-child {
  margin-right: 10px;
}

:deep(.el-input .el-input__wrapper) {
  width: 100% !important;
}

</style>

