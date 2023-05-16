from django.contrib.auth.models import AbstractUser
from django.db import models


class UserInfo(AbstractUser):
    nid = models.AutoField(primary_key=True)
    tel = models.CharField(verbose_name='手机号', max_length=12, null=True, blank=True)
    addr = models.CharField(max_length=8, verbose_name='用户地址信息', null=True, blank=True)
    name = models.CharField(max_length=8, verbose_name='姓名', null=True, blank=True)
    sex = models.CharField(max_length=2, verbose_name='性别', null=True, blank=True)
    age = models.IntegerField(verbose_name='用户年龄', null=True, blank=True)
    role = models.CharField(max_length=16, verbose_name='用户身份', default='普通用户')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户信息'


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='标题', max_length=256, null=True, blank=True)
    author = models.CharField(verbose_name='作者', max_length=256, null=True, blank=True)
    organ = models.CharField(verbose_name='学院', max_length=256, null=True, blank=True)
    source = models.CharField(verbose_name='来源', max_length=256, null=True, blank=True)
    keywords = models.CharField(verbose_name='关键词', max_length=256, null=True, blank=True)
    pub_time = models.CharField(verbose_name='时间', max_length=256, null=True, blank=True)
    first_duty = models.CharField(verbose_name='一作', max_length=256, null=True, blank=True)
    fund = models.CharField(verbose_name='详细介绍', max_length=256, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '文章数据'
