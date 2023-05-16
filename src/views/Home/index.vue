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

      <el-card shadow="hover" style="margin-top: 20px; height: 450px">
        <el-table :data="tableData">
          <el-table-column v-for="(value, key) in tableLabel"
                           :key="key"
                           :prop="key"
                           :label="value">

          </el-table-column>
        </el-table>
      </el-card>
    </el-col>

    <el-col :span="16" style="margin-top: 20px">
      <div class="name">
        <el-card
            v-for="(item, index) in countData"
            :key="item.name"
            :body-style="{ display: 'flex', padding: 0 }"
            >

          <component class="icons" :is="item.icon" :style="{background: item.color}"></component>
          <div class="details">
            <p class="num">￥{{ item.value }}</p>
            <p class="txt">{{ item.name }}</p>
          </div>
        </el-card>
      </div>

      <el-card style="height: 280px; margin-top: 10px">
        <div ref="echart" style="height: 280px"></div>
      </el-card>

      <div class="graph">
        <el-card style="height: 260px">
          <div ref="userEcharts" style="height: 240px"></div>
        </el-card>

        <el-card style="height: 260px">
          <div ref="videoEcharts" style="height: 240px"></div>
        </el-card>
      </div>
    </el-col>
  </el-row>
</template>

<script setup>
import {getCurrentInstance, onMounted, reactive, ref} from "vue";
import {useStore} from "vuex";
import * as echarts from 'echarts'

const {proxy} = getCurrentInstance()
const store = useStore()

let tableData = ref([])
const username = store.state.username
const role = store.state.role
let countData = ref([])

const getTableData = async () => {
  let res = await proxy.$api.getTableData()
  tableData.value = res.data
}

const getCountData = async () => {
  let res = await proxy.$api.getCountData()
  countData.value = res.data
}

onMounted(() => {
  getTableData()
  getCountData()
  getChartData()
})

// echarts配置
let xOptions = reactive({
// 图例文字颜色
  textStyle: {
    color: "#333",
  },
  grid: {
    left: "20%",
  },
// 提示框
  tooltip: {
    trigger: "axis",
  },
  xAxis: {
    type: "category", // 类目轴
    data: [],
    axisLine: {
      lineStyle: {
        color: "#17b3a3",
      },
    },
    axisLabel: {
      interval: 0,
      color: "#333",
    },
  },
  yAxis: [
    {
      type: "value",
      axisLine: {
        lineStyle: {
          color: "#17b3a3",
        },
      },
    },
  ],
  color: ["#2ec7c9", "#b6a2de", "#5ab1ef", "#ffb980", "#d87a80", "#8d98b3"],
  series: [],
})

let pieOptions = reactive({
  tooltip: {
    trigger: "item",
  },
  color: [
    "#0f78f4",
    "#dd536b",
    "#9462e5",
    "#a6a6a6",
    "#e1bb22",
    "#39c362",
    "#3ed1cf",
  ],
  series: [],
})

let orderData = reactive({
  xData: [],
  series: [],
})
let userData = reactive({
  xData: [],
  series: [],
})
let videoData = reactive({
  series: [],
})

// 获取数据
const getChartData = async () => {
  let res = await proxy.$api.getChartData()
  let orderRes = res.data.orderData
  let userRes = res.data.userData
  let videoRes = res.data.videoData

  orderData.xData = orderRes.date
  const keyArray = Object.keys(orderRes.data[0])
  const series = []
  keyArray.forEach((key) => {
    series.push({
      name: key,
      data: orderRes.data.map((item) => item[key]),
      type: "line",
    })
  })
  orderData.series = series
  xOptions.xAxis.data = orderData.xData
  xOptions.series = orderData.series

  // 折线图进行渲染
  let hEcharts = echarts.init(proxy.$refs['echart'])
  hEcharts.setOption(xOptions)

  // 柱状图进行渲染
  userData.xData = userRes.map((item) => item.date)
  userData.series = [
    {
      name: '新增用户',
      data: userRes.map((item) => item.new),
      type: "bar",
    },
    {
      name: '活跃用户',
      data: userRes.map((item) => item.active),
      type: "bar",
    },
  ]
  xOptions.xAxis.data = userData.xData
  xOptions.series = userData.series

  let uEcharts = echarts.init(proxy.$refs['userEcharts'])
  uEcharts.setOption(xOptions)

  // 饼状图配置
  videoData.series = [{
    data: videoRes,
    type: "pie",
  }]
  pieOptions.series = videoData.series
  let vEcharts = echarts.init(proxy.$refs['videoEcharts'])
  vEcharts.setOption(pieOptions)
}

const tableLabel = {
  name: "课程",
  todayBuy: "今日购买",
  monthBuy: "本月购买",
  totalBuy: "总购买"
}
</script>

<style scoped lang="scss">
.home {
  margin-top: -20px;

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

  .name {
    width: 100%;
    display: flex;
    flex-wrap: wrap;

    .el-card {
      height: 70px;
      width: 31%;
      margin: 5px;
    }

    .details {
      margin: 10px;
    }

    .icons {
      width: 30%;
      height: 70px;
      color: white;
      font-size: 30px;
      text-align: center;
      line-height: 70px;
    }

    .num {
      margin: 0;
      font-size: 18px;
    }

    .txt {
      margin-top: 8px;
      font-size: 10px;
      color: gray;
    }
  }

  .graph {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;

    .el-card {
      width: 48%;
    }
  }
}


</style>