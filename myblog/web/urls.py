
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from web import views

# 获取一个简单路由对象
router = SimpleRouter()

# 产生一个路由地址,注册地址
router.register('article', views.ArticleView)
router.register('art', views.ArtCat)
# http://127.0.0.1/api/web/cat/
# 获取类型
router.register('cat', views.CatView)
# 获取关于我的信息
# http://127.0.0.1/api/web/userinfo/
router.register('userinfo', views.UserInfoView)

urlpatterns = [
    # http://127.0.0.1/api/web/index/
    url(r'^index/', views.index, name='index'),
    # 相册页
    url(r'^share/', views.share, name='share'),
    # 关于我
    url(r'^about/', views.userinfo, name='about'),
    # 日记
    url(r'^diary/', views.diary, name='diary'),
    # 留言
    url(r'^message/', views.message, name='message'),
]
# 将产生的URL添加到urlpatterns中
urlpatterns += router.urls

