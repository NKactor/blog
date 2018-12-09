
from django.db import models


class User(models.Model):
    """用户类型"""
    username = models.CharField(max_length=31, verbose_name='用户名')
    password = models.CharField(max_length=31, verbose_name='密码')
    sex = models.BooleanField(default=1, verbose_name='性别')
    birth = models.DateField(auto_now_add=True, verbose_name='生日')
    udesc = models.TextField(null=True, verbose_name='自我简介')
    head_img = models.ImageField(upload_to='headimg', null=True, verbose_name='头像')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    login_time = models.DateTimeField(auto_now=True)
    idDelete = models.BooleanField(default=0)

    class Meta:
        db_table = 'tb_user'
