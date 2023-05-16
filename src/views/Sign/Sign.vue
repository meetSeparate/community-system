<template>
  <div class="sign-in-container">
    <el-card class="box-card">
      <div class="sign-in-body">
        <div class="sign-in-title">注册</div>
        <el-input placeholder="请输入用户名..." maxlength="11" v-model="userInfo.username"
                  class="sign-in-input" clearable>
          <template #prefix>
            <el-icon class="el-input__icon"><UserFilled /></el-icon>
          </template>
        </el-input>
        <el-input placeholder="请输入密码..." show-password maxlength="16" v-model="userInfo.password"
                  class="sign-in-input" clearable>
          <template #prefix>
            <el-icon class="el-input__icon"><Lock /></el-icon>
          </template>
        </el-input>
        <el-input placeholder="请再次输入密码..." show-password maxlength="16" v-model="userInfo.re_password" class="sign-in-input" clearable>
          <template #prefix>
            <el-icon class="el-input__icon"><Lock /></el-icon>
          </template>
        </el-input>
        <div class="sign-in-submit">
          <el-button type="primary" @click="sign">提交</el-button>
        </div>
        <div class="login-container">
          <span @click="toLogin" class="login-text">登录</span>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import {getCurrentInstance, reactive} from "vue";
import {useRouter} from "vue-router";

const router = useRouter()
const {proxy} = getCurrentInstance()
const userInfo = reactive({
  username: '',
  password: '',
  re_password: ''
})

// 去登录页面
const toLogin = () => {
  router.push({
    name: 'login'
  })
}

// 注册
const sign = async () => {
  let res = await proxy.$api.sign(userInfo)
  ElMessage({
    showClose: true,
    message: res.msg,
    type: 'success'
  })
  setTimeout(() => {
    router.push({
      name: 'login'
    })
  }, 500)
}
</script>

<style scoped>
.sign-in-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  background-color: #f1f1f1;
}

.sign-in-body {
  padding: 30px;
  width: 400px;
  height: 100%;
}

.sign-in-title {
  padding-bottom: 30px;
  text-align: center;
  font-weight: 600;
  font-size: 20px;
  color: #409EFF;
}

.sign-in-input {
  margin-bottom: 20px;
}

.sign-in-submit {
  display: flex;
  justify-content: center;
}

.login-container {
  padding: 0 10px;
}

.login-text {
  color: #409EFF;
  font-size: 16px;
  cursor: pointer;
}
</style>