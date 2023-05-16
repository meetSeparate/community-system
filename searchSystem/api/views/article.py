from django.views import View
from django.http import JsonResponse
from app01.models import Article
from api.config.pagination import Pagination


class ArticleView(View):
    def get(self, request):
        res = {
            'code': 400,
            'msg': 'success',
            'data': [],
            'total': 10
        }

        article = Article.objects.all()
        total = article.count()
        limit = request.GET.get('limit')
        page = request.GET.get('page')
        pager = Pagination(
            current_page=int(page),
            all_count=int(total),
            limit=int(limit),
        )
        article_list = article[pager.start: pager.end]
        res['total'] = total
        for article1 in article_list:
            res['data'].append({
                'id': article1.id,
                'title': article1.title,
                'author': article1.author,
                'organ': article1.organ,
                'source': article1.source,
                'keywords': article1.keywords,
                'pub_time': article1.pub_time,
                'first_duty': article1.first_duty,
            })

        res['code'] = 200
        return JsonResponse(res)