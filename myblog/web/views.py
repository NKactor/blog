from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import mixins, viewsets, request
from rest_framework.response import Response

from backweb.models import User
from web.article_filter import ArticleFilter, TypeFilter
from web.article_serializer import ArticleSerializer, CatSerializer, UserSerializer
from web.models import Articles, ArticleType


def index(request):
    if request.method == 'GET':
        return render(request, 'web/index.html')


def share(request):
    if request.method == 'GET':
        return render(request, 'web/share.html')


def userinfo(request):
    if request.method == 'GET':
        return render(request, 'web/about.html')


# http://127.0.0.1/api/web/index/
#  http://127.0.0.1/api/web/article/?title=第四章&contents=科技   查询接口

class ArticleView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    # 查询所有查询集
    queryset = Articles.objects.all()

    # 序列化
    serializer_class = ArticleSerializer

    # 过滤
    filter_class = ArticleFilter

    # 定义状态码
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            data = {}
            data['code'] = 500
            data['msg'] = '获取数据失败'
            return Response(data)


class CatView(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

    queryset = ArticleType.objects.all()

    serializer_class = CatSerializer

    # fliter_class = TypeFilter

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance = instance.articles_set
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            data = {}
            data['code'] = 500
            data['msg'] = '请求失败'
            return Response(data)


class UserInfoView(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = User.objects.all()

    serializer_class = UserSerializer

    # 定义状态码
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except:
            data = {}
            data['code'] = 500
            data['msg'] = '请求失败'
            return Response(data)


class ArtCat(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):

    queryset = Articles.objects.all()

    serializer_class = ArticleSerializer

    filter_class = TypeFilter


def diary(request):
    if request.method == 'GET':

        return render(request, 'web/diary.html')


def message(request):
    if request.method == 'GET':

        return render(request, 'web/message.html')
