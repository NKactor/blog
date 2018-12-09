

from django.conf.urls import url

from backweb import views

urlpatterns = [
    # 系统首页
    url(r'^index/', views.index, name='index'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 注册
    url(r'^register/', views.register, name='register'),
    # 注销登录
    url(r'^logout/', views.logout, name='logout'),
    # 文章展示
    url(r'^article/', views.article, name='article'),
    # 文章类型
    url(r'^cat/', views.category, name='category'),
    # 修改文章类型
    url(r'^update_cat/(\d+)', views.update_cat, name='update_cat'),
    # 删除类型
    url(r'^del_cat/(\d+)', views.del_cat, name='del_cat'),
    # 添加文章
    url(r'^add_art/', views.add_art, name='add_art'),
    # 修改文章
    url(r'^update_art/(\d+)', views.update_art, name='update_art'),
    # 删除文章
    url(r'^del_art/(\d+)', views.del_art, name='del_art'),
    # 用户设置
    url(r'^userset/', views.userset, name='userset'),
    # 修改更新用户
    url(r'^upuser/(\d+)', views.update_user, name='updateuser'),







]
