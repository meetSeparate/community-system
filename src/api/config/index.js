/**
 * 环境配置文件
 * 开发环境
 * 生产环境
 * 测试环境
 */

// 拿到当前环境
const env = import.meta.env.MODE || 'development'

const EnvConfig = {
    development: {
        baseApi: 'http://127.0.0.1:8000/api',
        mockApi: 'https://www.fastmock.site/mock/178e65956eb9b88c72415a4b39d99bdf/api'
    },

    test: {
        baseApi: '//test.future.com/api',
        mockApi: 'https://www.fastmock.site/mock/178e65956eb9b88c72415a4b39d99bdf/api'
    },

    production: {
        baseApi: '//production.future.com/api',
        mockApi: 'https://www.fastmock.site/mock/178e65956eb9b88c72415a4b39d99bdf/api'
    },
}

export default {
    env,
    // mock总开关
    mock: true,
    ...EnvConfig[env]
}