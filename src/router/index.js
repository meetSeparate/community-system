import {createRouter, createWebHashHistory} from "vue-router";
import store from "../store/index.js";

const routes = [
    {
        path: '/',
        redirect: '/login',
    },
    {
        path: '/main',
        name: 'main',
        component: () => import('../views/Main.vue'),
        redirect: '/main/home',
        children: [
            {
                path: 'home',
                name: 'home',
                component: () => import('../views/Home/index.vue')
            },

            {
                path: 'superUser',
                name: 'superUser',
                component: () => import('../views/User/SuperUser.vue')
            },
            {
                path: 'manageUser',
                name: 'manageUser',
                component: () => import('../views/User/ManageUser.vue')
            },
            {
                path: 'commonUser',
                name: 'commonUser',
                component: () => import('../views/User/CommonUser.vue')
            },
            {
                path: 'new',
                name: 'new',
                component: () => import('../views/New/New.vue')
            },
            {
                path: 'location',
                name: 'location',
                component: () => import('../views/Location/Location.vue')
            },

            {
                path: 'feedback',
                name: 'feedback',
                component: () => import('../views/FeedBack/FeedBack.vue')
            },

            {
                path: 'apply',
                name: 'apply',
                component: () => import('../views/Apply/Apply.vue')
            },

            {
                path: 'demand',
                name: 'demand',
                component: () => import('../views/Demand/Demand.vue')
            },

            {
                path: 'heath',
                name: 'heath',
                component: () => import('../views/Heath/Heath.vue')
            },

            {
                path: 'pay',
                name: 'pay',
                component: () => import('../views/Pay/Pay.vue')
            }

        ]
    },

    {
        path: '/login',
        name: 'login',
        component: () => import('../views/Login/Login.vue')
    },
    {
        path: '/sign',
        name: 'sign',
        component: () => import('../views/Sign/Sign.vue')
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    let token = store.state.token;
    if (token) {
        if (to.name === 'login' || to.name === 'sign') {
            next('/main/home')
        } else {
            next()
        }
    } else {
        if (to.name !== 'login' && to.name !== 'sign') {
            next('/login')
        } else {
            next()
        }
    }
})

export default router