from django.urls import path
from api.views import jingdongShop, user, login, admin_data, article

urlpatterns = [
    path('jingdongShop/', jingdongShop.JingDongShopView.as_view()),
    path('login/', login.LoginView.as_view()),
    path('sign/', login.SignView.as_view()),
    path('get_seven_data/', admin_data.get_seven_data),  # 获取七日用户注册
    path('get_time_data/', admin_data.get_time_data),  #
    path('get_keyword_data/', admin_data.get_keyword_data),  #
    path('get_source_data/', admin_data.get_source_data),  #
    path('get_author_data/', admin_data.get_author_data),  #
    path('userlur/', user.UserLurView.as_view()),
    path('article/', article.ArticleView.as_view()),
]
