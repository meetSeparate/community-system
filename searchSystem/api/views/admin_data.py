import datetime
from app01.models import UserInfo, Article
from django.http import JsonResponse


# 获取七日用户登录注册数量
def get_seven_data(request):
    today = datetime.date.today()
    seven_data = {
        'date': [],
        'login_data': [],
        'sign_data': []
    }
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)

        login_count = UserInfo.objects.filter(last_login__year=date.year,
                                              last_login__month=date.month,
                                              last_login__day=date.day).count()

        sign_count = UserInfo.objects.filter(date_joined__year=date.year,
                                             date_joined__month=date.month,
                                             date_joined__day=date.day).count()
        seven_data['date'].append(date.strftime('%m-%d'))
        seven_data['login_data'].append(login_count)
        seven_data['sign_data'].append(sign_count)
    return JsonResponse(seven_data)


def get_time_data(request):
    res = {
        'name': [],
        'number': []
    }

    for i in range(2012, 2023):
        res['name'].append(str(i) + '年')
        count = 0
        article_list = Article.objects.all()
        for article in article_list:
            pub_time = article.pub_time
            if pub_time.split('/')[2] == str(i):
                count += 1
        res['number'].append(count)
        print(count)
        i += 1
    return JsonResponse(res)


def get_keyword_data(request):
    res = {
        'data': [
            {'name': '智慧教育'},
            {'name': '商务英语函电'},
            {'name': '教学模式构建'},
            {'name': '智慧教学'},
            {'name': '融入社会'},
            {'name': '罪犯改造'},
            {'name': '改革目标'},
            {'name': '思政课程'},
            {'name': '互联网+'},
            {'name': '教学模式'},
        ]
    }

    for data in res['data']:
        data['value'] = Article.objects.filter(keywords__contains=data['name']).count()
    return JsonResponse(res)


def get_source_data(request):
    res = {
        'name': [],
        'number': []
    }
    article_list = Article.objects.filter(source__contains='大学')[30:90]

    for article in article_list:
        for i in range(len(res['name']) - 1):
            if res['name'][i] == article.source:
                res['number'][i] += 1
                break
        else:
            res['name'].append(article.source)
            res['number'].append(1)

    return JsonResponse(res)


def get_author_data(request):
    res = {
        'name': [],
        'number': [],
    }
    article_query = Article.objects
    article_list = article_query.all()[:70]

    for article in article_list:
        res['name'].append(article.first_duty)
        res['number'].append(article_query.filter(author__contains=article.first_duty).count())

    return JsonResponse(res)
