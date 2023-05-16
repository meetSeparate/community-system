import {createStore} from "vuex";

export default createStore({
    state: {
        collapse: false,
        currentMenu: {},
        tabList: [
            {
                path: '/',
                name: 'home',
                label: '首页',
                icon: 'home'
            },
        ],
        token: localStorage.getItem('token'),
        username: localStorage.getItem('username'),
        userid: localStorage.getItem('userid'),
        role: localStorage.getItem('role'),
        menu: JSON.parse(localStorage.getItem('menu'))
    },

    mutations: {
        changeCollapse(state, context) {
            state.collapse = !state.collapse
        },

        selectMenu(state, val) {
            // val.name === 'home' ? state.currentMenu = {} : state.currentMenu = val
            if (val.name === 'home') {
                state.currentMenu = {}
            } else {
                state.currentMenu = val
                let result = state.tabList.findIndex(item => item.name === val.name)
                result === -1 ? state.tabList.push(val) : ''
            }
        },

        closeTag(state, val) {
            let res = state.tabList.findIndex(item => item.name === val.name)
            state.tabList.splice(res, 1)
        },

        // 登录
        Login(state, val) {
            state.token = val.token
            state.username = val.username
            state.userid = val.userid
            state.role = val.role
            state.menu = val.menu
            localStorage.setItem('token', val.token)
            localStorage.setItem('username', val.username)
            localStorage.setItem('userid', val.userid)
            localStorage.setItem('role', val.role)
            localStorage.setItem('menu', JSON.stringify(val.menu))
        },

        // 退出登录
        Logout(state) {
            state.token = ''
            state.username = ''
            state.userid = ''
            state.role = ''
            state.menu = []
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')
            localStorage.removeItem('role')
            localStorage.removeItem('menu')
        }
    }
})