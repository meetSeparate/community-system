from django.utils.safestring import mark_safe
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app01.models import *
from django.utils.translation import gettext_lazy as _


# Register your models here.

class UserInfoAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "tel", "sex", "age", "role")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )

    list_display = ("username", "name", "tel", "role", "is_staff")

    list_filter = ("is_staff", "is_superuser", "is_active", "groups")

    search_fields = ("username", "name", "role")


class ArticleResources(resources.ModelResource):
    class Meta:
        model = Article
        import_id_fields = ['id']


class ArticleAdmin(ImportExportModelAdmin):
    list_display = ['id', 'title', 'author', 'organ', 'source', 'keywords', 'pub_time', 'first_duty', 'fund']

    list_filter = ['first_duty']

    search_fields = ['source', 'title']

    list_per_page = 30

    resource_class = ArticleResources


admin.site.register(UserInfo, UserInfoAdmin)

admin.site.register(Article, ArticleAdmin)


admin.site.site_header = '文章数据分析系统后台管理'

admin.site.site_title = '文章数据分析系统后台管理'
