from django.views import View
from django.http import JsonResponse
from api.tests import main


class JingDongShopView(View):
    def post(self, request):
        res = {
            'code': 412,
            'msg': 'success',
            'data': ''
        }
        value = request.data.get('value')
        shop_id = str(value)[20:32]
        main(shop_id)
        return JsonResponse(res)
