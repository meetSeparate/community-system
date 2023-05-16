<template>
  <main>
    <div class="main">
      <div class="news_content">

        <div class="left">
          <ul>
            <li :class="item.name === news_active ? 'active' : ''" v-for="item in news_init" :key="item.id"
                @click="getNewData(item.id, item.name, item.url, false, 0)"><img :src="item.url"
                                                                                 alt="">{{ item.name }}
            </li>
          </ul>
        </div>
        <div class="right">
          <div class="title">
            <img :src="news_active_url" alt="">
            <h2>{{ news_active }} · 热搜榜</h2>
          </div>
          <div class="body">
            <ul>
              <li v-for="item in news_list" :key="item.index">
                <span class="index">{{ item.index }}</span>
                <a :href="item.link" target="_blank">{{ item.title }}</a>
                <span class="num">{{ item.hotValue }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import {ref, getCurrentInstance, onMounted} from "vue";

const {proxy} = getCurrentInstance()
let news_list = ref([])
const news_init = [
  {
    name: '微博',
    id: 'KqndgxeLl9',
    url: 'https://file.ipadown.com/tophub/assets/images/media/s.weibo.com.png_50x50.png'
  },
  {
    name: '知乎',
    id: 'mproPpoq6O',
    url: 'https://file.ipadown.com/tophub/assets/images/media/zhihu.com.png_50x50.png'
  },
  {
    name: '微信',
    id: 'WnBe01o371',
    url: 'https://file.ipadown.com/tophub/assets/images/media/mp.weixin.qq.com.png_50x50.png'
  },
  {
    name: '百度',
    id: 'Jb0vmloB1G',
    url: 'https://file.ipadown.com/tophub/assets/images/media/baidu.com.png_50x50.png'
  },
  {
    name: '36氪',
    id: 'Q1Vd5Ko85R',
    url: 'https://file.ipadown.com/tophub/assets/images/media/36kr.com.png_50x50.png'
  },
  {
    name: '哔哩哔哩',
    id: '74KvxwokxM',
    url: 'https://file.ipadown.com/tophub/assets/images/media/bilibili.com.png_50x50.png'
  },
  {
    name: '抖音',
    id: 'DpQvNABoNE',
    url: 'https://file.ipadown.com/tophub/assets/images/media/iesdouyin.com.png_50x50.png'
  },
  {
    name: '拼多多',
    id: 'ARe1QZ2e7n',
    url: 'https://file.ipadown.com/tophub/assets/images/media/p.pinduoduo.com.png_50x50.png'
  },
  {name: 'CSDN论坛', id: 'K7GdajgeQy', url: 'https://files.codelife.cc/topsearch/K7GdajgeQy.png'}
]
let news_active = ref('微博')
let news_active_url = ref('https://file.ipadown.com/tophub/assets/images/media/s.weibo.com.png_50x50.png')

onMounted(() => {
  getNewData('KqndgxeLl9', '微博', 'https://file.ipadown.com/tophub/assets/images/media/s.weibo.com.png_50x50.png', true, 0)
})

const getNewData = (id, name, url, flag, size) => {
  if (name === news_active && !flag) {
    return
  }
  news_active.value = name
  news_active_url.value = url

  let data = {
    id,
  }
  if (size) {
    data.size = size
  }

  proxy.$api.getNewData(data).then(res => {
    news_list.value = res.data
  }).catch(e => {
    console.log(e)
  })

}

</script>

<style scoped lang="scss">
.main {
  width: 1200px;
  margin: 0 auto;
  height: 700px;

  .news_content {
    display: flex;
    min-height: 800px;
    background-color: white;
    border-radius: 5px;

    .left {
      width: 20%;
      border-right: 1px solid #f0eeee;

      ul {
        margin-top: 20px;

        img {
          height: 25px;
          border-radius: 5px;
          margin-right: 8px;
        }

        li {
          color: #333333;
          height: 40px;
          display: flex;
          align-items: center;
          padding-left: 30%;
          transition: all 0.1s;
        }

        li.active {
          background-color: #3a8ee6;
          color: white;
        }

        li:not(li.active) {
          cursor: pointer;

          &:hover {
            color: #3a8ee6;
          }
        }
      }
    }

    .right {
      width: 80%;
      padding: 20px;

      .title {
        display: flex;
        align-items: center;
        border-bottom: 1px solid #f0eeee;
        padding-bottom: 10px;

        img {
          width: 35px;
          border-radius: 50%;
          margin-right: 10px;
        }

        h2 {
          font-size: 20px;
        }
      }

      .body {
        margin-top: 10px;

        ul {
          list-style: none;

          li {
            height: 30px;
            align-items: center;
            display: flex;
            font-size: 14px;

            &:nth-child(1) {
              .index {
                background-color: #fe2d46;
                color: white;
              }
            }

            &:nth-child(2) {
              .index {
                background-color: #ff6600;
                color: white;
              }
            }

            &:nth-child(3) {
              .index {
                background-color: #faa90e;
                color: white;
              }
            }

            .index {
              width: 20px;
              height: 20px;
              border-radius: 5px;
              color: #333333;
              background-color: #f0f1f4;
              display: flex;
              align-items: center;
              justify-content: center;
              margin-right: 20px;

            }

            a {
              width: 77%;
              color: #333333;
              transition: all 0.2s;

              &:hover {
                color: #3a8ee6;
              }
            }

            .num {
              width: 20%;
              display: flex;
              justify-content: right;
            }
          }
        }
      }
    }
  }
}
</style>