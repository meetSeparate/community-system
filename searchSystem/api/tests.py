import time
import requests
import re
import csv
import jieba
import collections
import numpy as np
import wordcloud
from matplotlib import pyplot as plt
from PIL import Image

'''
# https://zhuanlan.zhihu.com/p/619644410
'''
eeex = 'data'


def url_all(shop_id):  # 循环获取网页数据
    lst2 = []
    for i in range(10):
        # 通过观察得知 page=页数  网站最大显示100页数据
        url1 = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={shop_id}&score=0&sortType=5&page={i}&pageSize=10&isShadowSku=0&fold=1'
        lst2.append(url1)  # 将数据添加到列表中
    return lst2  # 将生成的json对象url 返回到函数调用处


def jdjx(urle):
    lst = []  # 创建空列表，用来做数据存储
    for ex in urle:  # 循环提取url
        url = ex  # 将生成的传入到虚拟变量中
        headers = {
            'cookie': 'unpl'
                      '=JF8EAK5nNSttUUNTBEtWTkAYQwgBW1kATh4EaG9XVFUMT1YCGgcbEEN7XlVdXxRKEh9vZBRUWVNJUA4ZCysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrBxoVEktYUV9YOEonBF9XNVdcWkpcAysDKxMgCQkIXVwNSR4FImIEU19YTlEEHjIaIhM; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_8960aedc99dd45948669c19e5360413b|1681284939666; __jdu=406314404; CA1AN5BV0CA8DS2EPC=6957115d0d1faf5775df806c92c8bb3a; PCA9D23F7A4B3CSS=bd58114656661861134dc4431fd34514; areaId=7; 3AB9D23F7A4B3CSS=jdd03CJUACNBLLLDA35ZTPZMDO4PSXP3N5UE6Z5CJOCJJJJBS4SRTBSQ6NLDIZMXNLG2AIUOJUHU57FKKIJLF536KUS7PZAAAAAMHORSEUZAAAAAACHSALMTWVZNGTMX; _gia_d=1; PCSYCityID=CN_410000_410100_0; shshshfp=ba274e6ecd4b12a5b1bec9e6a1ef0898; shshshfpa=3ea8f27a-a09f-972b-e0c0-8315c29b5aed-1681284944; shshshfpx=3ea8f27a-a09f-972b-e0c0-8315c29b5aed-1681284944; shshshfpb=zShMwN9C0EBCz1dpVJGJ-bQ; 3AB9D23F7A4B3C9B=CJUACNBLLLDA35ZTPZMDO4PSXP3N5UE6Z5CJOCJJJJBS4SRTBSQ6NLDIZMXNLG2AIUOJUHU57FKKIJLF536KUS7PZA; mt_xid=V2_52007VwYTVV9YV18eTCleDGdUQVcKWk4PHB4eQAAzABJODV4BUgMeSVlSNFRAAlRYUFwvShhfB3sCF05dW0NaG0IbWw5nACJQbVhiXx5NGl8MbwcUW21dU1MZ; jsavif=1; __jda=122270672.406314404.1681284938.1681284938.1681284940.1; __jdc=122270672; ipLoc-djd=7-482-484-60943; token=02a6aca5d3563fe9fb55ce643cd011f4,2,934047; shshshsID=1a89b38d70db6c123f7ad6b6ab6d8a41_3_1681284994245; __jdb=122270672.3.406314404|1.1681284940',
            # 这里换成自己的
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0'
        }
        respost = requests.get(url, headers=headers).text  # 发送请求返回text文本
        text = re.findall('"content":"(.*?)"', respost)  # 提取评论文件
        name = re.findall('"nickname":"(.*?)"', respost)  # 提取用户名字
        time1 = re.findall('"creationTime":"(.*?)"', respost)  # 提取用户时间
        for a, b, c in zip(name, text, time1):  # 通过zip函数压缩数据 在用循环提取数据
            dic = {}  # 创建虚拟字典
            # dic['用户名'] = a #将数据存入字典中
            a10 = b
            dic['评论内容'] = b  # 将数据存入字典中
            # dic['评论时间'] = c#将数据存入字典中
            print('评论内容:' + b, )  # 输出在run
            with open(f'api/{eeex}.txt', 'a+', encoding='utf-8-sig', newline='') as f:  # 文件名
                f.write(a10)
                f.write('\n')


def keshihu():
    with open(f'api/{eeex}.txt ', 'r', encoding='utf-8') as f:
        for i in f:
            a = i.strip('\n')  # 删除换行符
            b = a.replace(r'\n', '')  # 将\n删除
            with open(f'api/poecx.txt', 'a+', encoding='utf-8-sig', newline='') as c:
                c.write(b)
                c.write('\n')
    lst1 = []
    x_lst = []  # 高频词
    y_lst = []  # 评率
    f_name = f'api/poecx.txt'  # 文件地址
    with open(f_name, encoding='utf-8') as a:  # 将文件放入a中
        b = a.read()  # 对文件进行读操作
    words = jieba.lcut(b)  # words是直接生成一个装有词的列表，即list
    count = {}  # 定义一个字典
    for word in words:  # 枚举在文章中出现的词汇
        if len(word) < 2:  # 排除字长小于2的词
            continue
        else:  # 统计词频
            count[word] = count.get(word, 0) + 1
    list1 = list(count.items())  # 将字典中的键值对转化为列表
    list1.sort(key=lambda x: x[1], reverse=True)  # 对列表按照词频从大到小排列
    for i in range(10):  # 取出前十条数据
        dic = {}
        word, number = list1[i]  # 将列表中的word与number提取出来
        dic['高频词'] = word
        dic['频次'] = number
        lst1.append(dic)
        print("关键字：{:-<10}频次：{:+>8}".format(word, number))  # 输出word与number值、
    for i in lst1:
        x = i['高频词']
        x_lst.append(x)
        y = i['频次']
        y_lst.append(y)
    len_x = len(x_lst)
    plt.barh(range(len_x), y_lst, align='center', alpha=0.5)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.yticks(range(len_x), x_lst)
    plt.xlabel('高频词')
    plt.ylabel('频率')
    plt.title('分析词云图')
    plt.savefig(f'api/{eeex}分析图.png')
    fn = open(f'api/{eeex}.txt', encoding='utf-8')  # 打开文件
    string_data = fn.read()  # 读出整个文件
    fn.close()  # 关闭文件
    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
    string_data = re.sub(pattern, '', string_data)  # 将符合模式的字符去除
    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all=False)  # 精确模式分词
    object_list = []
    remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中',
                    u'在', u'了',
                    u'通常', u'如果', u'我们', u'需要']  # 自定义去除词库
    for word in seg_list_exact:  # 循环读出每个分词
        if word not in remove_words:  # 如果不在去除词库中
            object_list.append(word)  # 分词追加到列表
    # 词频统计
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
    # print(word_counts_top10)  # 输出检查
    # 词频展示
    mask = np.array(Image.open('api/a1.png'))  # 定义词频背景
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
        mask=mask,  # 设置背景图
        max_words=200,  # 最多显示词数
        max_font_size=100  # 字体最大值
    )
    wc.generate_from_frequencies(word_counts)  # 从字典生成词云
    image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
    wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    plt.savefig(f'static/img/{eeex}词云图.png', bbox_inches='tight')


def main(shop_id):  # 创建主函数
    urle = url_all(shop_id)  # 将函数返回值放到urle变量中   #初始化
    jdjx(urle)  # 传入url列表  #启动爬虫程序
    time.sleep(5)  # 等待5秒之后执行可视化
    keshihu()


