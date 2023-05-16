import Mock from 'mockjs'
import home from './mockData/home.js'
import user from './mockData/user.js'

// 模拟首页表格数据
Mock.mock('/home/getData', home.getHomeData)

// 本地获取user列表
Mock.mock(/user\/getUser/, 'get', user.getUserList)
