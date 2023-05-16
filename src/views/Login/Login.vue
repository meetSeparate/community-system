<template>
  <div class="login-container">
    <el-card class="box-card">
      <div class="login-body">
        <div class="login-title">社区管理系统</div>
        <el-form ref="form" :model="userForm">
          <el-input placeholder="请输入用户名..." v-model="userForm.username" class="login-input">
            <template #prefix>
              <el-icon><UserFilled /></el-icon>
            </template>
          </el-input>
          <el-input placeholder="请输入密码..." v-model="userForm.password" class="login-input"
                    show-password>
            <template #prefix>
              <el-icon class="el-input__icon"><Lock /></el-icon>
            </template>
          </el-input>
          <div class="login-submit">
            <el-button type="primary" @click="login">登录</el-button>
          </div>
          <div class="other-submit">
            <a @click="toSign" class="sign-in-text">注册</a>
          </div>
        </el-form>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import {getCurrentInstance, reactive} from "vue";
import {useRouter} from "vue-router";
import {useStore} from "vuex";

const router = useRouter()
const store = useStore()
const {proxy} = getCurrentInstance()

const userForm = reactive({
  username: '',
  password: ''
})

// 登录
const login = async () => {
  let res = await proxy.$api.login(userForm)
  store.commit('Login', res)
  ElMessage({
    showClose: true,
    message: res.msg,
    type: 'success'
  })
  setTimeout(() => {
    router.push({
      name: 'home'
    })
  }, 500)
}


// 去注册页面
const toSign = () => {
  router.push({
    name: 'sign'
  })
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100%;
  background-color: #f1f1f1;
}

.login-body {
  padding: 30px;
  width: 400px;
  height: 100%;
}

.login-title {
  padding-bottom: 30px;
  text-align: center;
  font-weight: 600;
  font-size: 20px;
  color: #409EFF;
  cursor: pointer;
}

.login-input {
  margin-bottom: 20px;
}

.login-submit {
  display: flex;
  justify-content: center;
}

.sign-in-container {
  padding: 0 10px;
}

.sign-in-text {
  color: #409EFF;
  font-size: 16px;
  text-decoration: none;
  line-height: 28px;
  cursor: pointer;
}

.other-submit {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}

</style>