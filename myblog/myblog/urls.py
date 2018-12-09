"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static

from myblog.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 引入前端路由
    url(r'^web/', include('web.urls', namespace='web')),
    # 接口url
    url(r'^api/web/', include('web.urls')),
    # 引入后端路由
    url(r'^backweb/', include('backweb.urls', namespace='backweb'))
]

# 告诉Django，解析media文件夹中的静态文件
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)