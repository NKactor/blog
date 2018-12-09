from django.db import models

from backweb.models import User


class ArticleType(models.Model):
    """文章类型"""
    type_name = models.CharField(max_length=60, verbose_name='文章类型')
    f_type = models.ForeignKey('self', null=True)
    count = models.IntegerField(verbose_name='文章数量', null=True, blank=True)

    class Meta:
        db_table = 'tb_type'

    def __str__(self):
        return self.type_name

    def __unicode__(self):
        return self.type_name


class Articles(models.Model):
    """文章模型"""
    title = models.CharField(max_length=80, verbose_name='文章标题')
    desc = models.CharField(max_length=60, verbose_name='文章描述', null=True, blank=True)
    contents = models.TextField(verbose_name='正文')
    author = models.CharField(max_length=31, verbose_name='作者')
    icon = models.ImageField(upload_to='article', null=True)
    create_time = models.DateField(auto_now_add=True, verbose_name='创建时间')
    up_time = models.DateField(auto_now=True, verbose_name='修改时间')
    art_type = models.ForeignKey(ArticleType)
    user = models.ForeignKey(User)

    class Meta:
        db_table = 'tb_article'

    def __str__(self):
        return self.title
