from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

from backweb.models import User
import re


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 允许访问的页面不需要进行验证

        # if re.fullmatch('/web/\w+/', request.path) or request.path in ['/backweb/login/', '/backweb/register/', '/backweb/logout/']:
        #     return None
        # 127.0.0.1/api/web/article/
        if re.match(r'/api/web/.*', request.path):
            return None

        if re.match(r'/web/.*', request.path):
            return None

        if request.path in ['/backweb/login/', '/backweb/register/']:
            return None

        if re.match(r'/media/.*', request.path):
            return None

        if re.fullmatch(r'/backweb/\w+/\d*', request.path) and request.path not in ['/backweb/login/', '/backweb/register/', '/backweb/logout/']:
            # 判断请求中是否有session值，有允许访问，没有返回相应页面
            user_id = request.session.get('user_id')

            if not user_id:
                return HttpResponseRedirect(reverse('backweb:login'))

            # 设置登录账号的用户
            user = User.objects.get(pk=user_id)
            request.user = user
            # 返回None让请求继续往下执行
            return None
        return HttpResponseRedirect(reverse('backweb:login'))

    def process_response(self, request, response):
        return response