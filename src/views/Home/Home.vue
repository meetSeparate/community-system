<template>
  <el-row class="home" :gutter="20">
    <el-col :span="8" style="margin-top: 20px">
      <el-card shadow="hover">
        <div class="user">
          <img src="../../assets/image/104.jpg" alt="">
          <div class="userinfo">
            <p class="name" style="margin-bottom: 10px">{{ username }}</p>
            <p class="role">{{ role }}</p>
          </div>
        </div>

        <div class="login-info">
          <p>上次登录时间: <span>2023-04-20</span></p>
          <p>上次登录地点: <span>北京</span></p>
        </div>
      </el-card>

    </el-col>

    <el-col :span="16" style="margin-top: 20px">
      <el-card shadow="hover">
        <el-descriptions
            class="margin-top"
            title="个人信息"
            :column="2"
            size="default"
            border
        >
          <template #extra>
            <el-button type="primary" size="small" @click="dialogVisible = true">修改个人信息</el-button>
          </template>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">
                <el-icon :style="iconStyle">
                  <user/>
                </el-icon>
                用户名
              </div>
            </template>
            {{ personal.username }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">
                <el-icon :style="iconStyle">
                  <iphone/>
                </el-icon>
                姓名
              </div>
            </template>
            {{ personal.name }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">
                <el-icon :style="iconStyle">
                  <iphone/>
                </el-icon>
                性别
              </div>
            </template>
            {{ personal.sex }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">
                <el-icon :style="iconStyle">
                  <location/>
                </el-icon>
                年龄
              </div>
            </template>
            {{ personal.age }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">
                <el-icon :style="iconStyle">
                  <tickets/>
                </el-icon>
                出生日期
              </div>
            </template>
            {{ personal.birth }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">
                <el-icon :style="iconStyle">
                  <tickets/>
                </el-icon>
                用户角色
              </div>
            </template>
            {{ personal.role }}
          </el-descriptions-item>
          <el-descriptions-item>
            <template #label>
              <div class="cell-item">
                <el-icon :style="iconStyle">
                  <office-building/>
                </el-icon>
                地址
              </div>
            </template>
            {{ personal.addr }}
          </el-descriptions-item>
        </el-descriptions>
      </el-card>
    </el-col>

  </el-row>
  <el-dialog
      v-model="dialogVisible"
      title="修改个人信息"
      width="30%"
      :before-close="handleClose"
  >
    <el-form
        label-position="top"
        label-width="100px"
        :model="personal"
        style="max-width: 460px"
        ref="feedForm"
    >
      <el-form-item label="用户名" prop="username" :rules="{
        required: true,
        message: '用户名不能为空',
        trigger: 'blur',
      }">
        <el-input v-model="personal.username"/>
      </el-form-item>
      <el-form-item label="姓名" prop="name" :rules="{
        required: true,
        message: '姓名不能为空',
        trigger: 'blur',
      }">
        <el-input v-model="personal.name"/>
      </el-form-item>
      <el-form-item label="性别" prop="sex" :rules="{
        required: true,
        message: '性别不能为空',
        trigger: 'blur',
      }">
        <el-input v-model="personal.sex"/>
      </el-form-item>
      <el-form-item label="年龄" prop="age" :rules="{
        required: true,
        message: '年龄不能为空',
        trigger: 'blur',
      }">
        <el-input v-model="personal.age"/>
      </el-form-item>
      <el-form-item label="出生日期" prop="birth" :rules="{
        required: true,
        message: '出生日期不能为空',
        trigger: 'blur',
      }">
        <el-input v-model="personal.birth"/>
      </el-form-item>
      <el-form-item label="地址" prop="addr" :rules="{
        required: true,
        message: '地址不能为空',
        trigger: 'blur',
      }">
        <el-input v-model="personal.addr"/>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="handleCancel">取消</el-button>
        <el-button type="primary" @click="changePersonal">
          确定
        </el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script setup>

import {getCurrentInstance, onMounted, reactive, ref} from "vue";
import {useStore} from "vuex";

const store = useStore()
const {proxy} = getCurrentInstance()

const username = store.state.username
const userid = store.state.userid
const role = store.state.role
const dialogVisible = ref(false)

let personal = ref({})

onMounted(() => {
  getPersonal()
})

// 获取个人信息
const getPersonal = async () => {
  let res = await proxy.$api.getPersonal({userid: userid})
  personal.value = res.data
}

// 修改个人信息
const changePersonal = async () => {
  let res = await proxy.$api.changePersonal(personal.value)

  ElMessage({
    showClose: true,
    message: res.msg,
    type: 'success'
  })
  dialogVisible.value = false
  await getPersonal()
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
</script>

<style scoped lang="scss">
.home {
  margin-top: -20px;
  height: 680px;

  .user {
    display: flex;
    align-items: center;
    padding-bottom: 20px;
    border-bottom: 1px solid #ccc;
    margin-bottom: 20px;

    img {
      width: 150px;
      height: 150px;
      border-radius: 50%;
      margin-right: 40px;
    }
  }

  .login-info {
    p {
      line-height: 30px;
      font-size: 14px;
      color: #999;

      span {
        color: #666;
        margin-left: 60px;
      }
    }
  }

}
</style>