/**
 * 项目总api管理
 */
import request from "./request.js";
import {Lm} from '../assets/js/signaturekey.js'

export default {
    getTableData : (params) => request({url: '/home/getTableData', method: 'get', data: params}),

    getCountData: () => request({url: '/home/getCountData', method: 'get'}),

    getChartData: () => request({url: '/home/getChartData', method: 'get'}),

    getUserList: (params) => request({url: '/user/', method: 'get', data: params, mock:false}),

    getNewData: (params) => request({url: '/news/', method: 'post', data: params, mock: false, headers: {signaturekey: Lm()}}),

    addUser: (data) => request({url: '/user/', method: 'post', data: data, mock: false}),

    editUser: (data) => request({url: '/editUser/', method: 'post', data: data, mock: false}),

    deleteUser: (data) => request({url: '/user/', method: 'delete', data: data, mock: false}),

    login: (data) => request({url: '/login/', method: 'post', data: data, mock: false}),

    sign: (data) => request({url: '/sign/', method: 'post', data: data, mock: false}),

    getFeedBack: (data) => request({url: '/feedback/', method: 'get', data:data, mock: false}),

    addFeedBack: (data) => request({url: '/feedback/', method: 'post', data: data, mock: false}),

    addApply: (data) => request({url: '/apply/', method: 'post', data: data, mock: false}),

    addDemand: (data) => request({url: '/demand/', method: 'post', data: data, mock: false}),

    getHeath: (data) => request({url: '/heath/', method: 'get', data: data, mock: false}),

    addHeath: (data) => request({
        url: '/heath/',
        method: 'post',
        data: data,
        mock: false,
    }),

    getPay: (data) => request({
        url: '/pay/',
        method: 'get',
        data: data,
        mock: false,
    }),

    changePayStatus: (data) => request({
        url: '/pay/',
        method: 'put',
        data: data,
        mock: false,
    }),

    getPersonal: (data) => request({
        url: '/personal/',
        method: 'get',
        data: data,
        mock: false,
    }),

    changePersonal: (data) => request({
        url: '/personal/',
        method: 'put',
        data: data,
        mock: false,
    })
}