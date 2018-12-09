import datetime
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from backweb.UserForm import LoginForm, RegisterForm, AddArticle, EditArticle, CatType, UserInfo
from backweb.models import User
from web.models import Articles, ArticleType


def index(request):

    return render(request, 'backweb/index.html', {'username': request.user.username})


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')

    # 进行用户表单数据验证
    form = LoginForm(request.POST)

    # 判断验证是否通过
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        # 判断是否有这个用户
        user = User.objects.filter(username=username, password=password).first()
        if not user:
            errors = '该用户不存在！'
            return render(request, 'backweb/login.html', {'errors': errors})

        # 设置session值
        request.session['user_id'] = user.id
        # 修改登录时间
        user.login_time = datetime.datetime.now()
        user.save()
        # 跳转到首页
        return HttpResponseRedirect(reverse('backweb:index'))
    else:
        errors = form.errors
        return render(request, 'backweb/login.html', {'errors': errors})


def register(request):
    """注册"""
    if request.method == 'GET':
        return render(request, 'backweb/register.html')

    if request.method == 'POST':
        # 进行提交表单数据验证
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            udesc = form.cleaned_data.get('udesc')
            sex = form.cleaned_data.get('sex')
            birth = form.cleaned_data.get('birth')
            head_img = form.cleaned_data.get('head_img')
            # 判断用户是否已经存在
            if User.objects.filter(username=username, password=password):
                return render(request, 'backweb/register.html')
            else:
                # 创建用户
                if head_img:
                    User.objects.create(username=username, password=password, sex=sex, birth=birth, udesc=udesc, head_img=head_img)
                    return HttpResponseRedirect(reverse('backweb:login'))
                User.objects.create(username=username, password=password, sex=sex, birth=birth, udesc=udesc)
                return HttpResponseRedirect(reverse('backweb:login'))


def logout(request):
    # 注销登录
    # 删除Django_session表中的数据
    request.session.delete(request.session.session_key)
    return HttpResponseRedirect(reverse('backweb:login'))


def article(request):
    # 文章展示
    if request.method == 'GET':
        # 获取页数

        page = int(request.GET.get('page', 1))

        # 获取所有文章
        articles = Articles.objects.all()
        # 实现分页
        paginator = Paginator(articles, 5)

        # 获取分页中的第几页
        pages = paginator.page(page)

        return render(request, 'backweb/article.html', {'pages': pages, 'username': request.user.username})


def category(request):
    """文章类型"""
    if request.method == 'GET':
        # 获取当前所有的类型，仅仅获取一级类型（父类型）
        cats = ArticleType.objects.all()
        return render(request, 'backweb/category.html', {'cats': cats, 'username': request.user.username})

    if request.method == 'POST':
        # 修改数据或者添加数据
        # 接收用户端提交的类型数据
        form = CatType(request.POST)

        if form.is_valid():
            type_name = form.cleaned_data.get('type_name')
            f_type_id = form.cleaned_data.get('f_type_id')
            if f_type_id:
                ArticleType.objects.create(type_name=type_name, f_type_id=f_type_id)
            else:
                ArticleType.objects.create(type_name=type_name, count=0, f_type_id=None)

            return HttpResponseRedirect(reverse('backweb:category'))


def update_cat(request, id):
    if request.method == 'GET':
        # 修改类型
        cats = ArticleType.objects.all()
        cate = cats.get(id=id)
        return render(request, 'backweb/category.html', {'cats': cats,'cate': cate , 'username': request.user.username})

    if request.method == 'POST':
        # 接收用户端提交的类型数据
        form = CatType(request.POST)

        if form.is_valid():
            type_name = form.cleaned_data.get('type_name')
            f_type_id = form.cleaned_data.get('f_type_id')
            cat = ArticleType.objects.get(pk=id)
            cat.type_name = type_name
            if f_type_id:
                cat.f_type = ArticleType.objects.get(pk=f_type_id)
            cat.save()
            return HttpResponseRedirect(reverse('backweb:category'))


def del_cat(request, id):
    if request.method == 'GET':
        # 删除类型
        ArticleType.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('backweb:category'))


def add_art(request):
    """添加文章"""
    if request.method == 'GET':
        # 返回文章添加页面
        # 获取当前所有的类型，仅仅获取一级类型（父类型）
        cats = ArticleType.objects.filter(f_type=None)
        return render(request, 'backweb/add_article.html', {'cats': cats, 'username': request.user.username})

    if request.method == 'POST':
        # 添加文章
        # form检查用户提交数据（文章标题、内容、描述、图片）
        form = AddArticle(request.POST, request.FILES)

        # 判断是否检验通过
        if form.is_valid():
            # 成功
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            content = form.cleaned_data.get('content')
            author = request.user.username
            user_id = request.user.id
            icon = form.cleaned_data.get('icon')
            type_id = form.cleaned_data.get('art_type')
            art_type = ArticleType.objects.get(pk=int(type_id))
            art_type.count += 1
            art_type.save()
            Articles.objects.create(title=title,
                                    desc=desc,
                                    contents=content,
                                    author=author,
                                    art_type=art_type,
                                    user_id=user_id,
                                    icon=icon)
            return HttpResponseRedirect(reverse('backweb:article'))

        else:
            # 失败
            # 获取当前所有的类型，仅仅获取一级类型（父类型）
            cats = ArticleType.objects.filter(f_type=None)
            # 获取错误信息
            errors = form.errors
            return render(request, 'backweb/add_article.html',
                          {'errors': errors,
                           'cats': cats })


def update_art(request, id):
    """文章修改"""
    if request.method == 'GET':
       #  获取需要修改的文章内容
       article = Articles.objects.filter(pk=id).first()
       # 获取当前所有的类型，仅仅获取一级类型（父类型）
       cats = ArticleType.objects.filter(f_type=None)

       return render(request, 'backweb/add_article.html',
                     {
                         'article': article,
                         'cats': cats,
                         'username': request.user.username
                      })

    if request.method == 'POST':
        # 说明用户提交了数据需要进行数据验证
        form = EditArticle(request.POST, request.FILES)

        if form.is_valid():
            # 成功
            # 保存数据并返回文章展示页面
            title = form.cleaned_data.get('title')
            desc = form.cleaned_data.get('desc')
            content = form.cleaned_data.get('content')
            author = request.user.username
            user_id = request.user.id
            type_id = form.cleaned_data.get('art_type')
            art_type = ArticleType.objects.get(pk=int(type_id))
            # 获取文章对象
            article = Articles.objects.filter(pk=id).first()
            if art_type.id != article.art_type.id:
                art_type.count += 1
                art_type.save()

            # 修改属性
            article.title = title
            article.desc = desc
            article.content = content
            article.art_type = art_type
            # 修改时图片可以改可不改，所以需要做判断
            icon = form.cleaned_data.get('icon')
            if icon:
                article.icon = icon
            article.save()
            return HttpResponseRedirect(reverse('backweb:article'))

        else:
            # 失败获取失败信息
            errors = form.errors
            # 获取文章
            article = Articles.objects.filter(pk=id).first()

            # 获取当前所有的类型，仅仅获取一级类型（父类型）
            cats = ArticleType.objects.filter(f_type=None)

            # 返回当前渲染的页面
            return render(request, 'backweb/add_article.html',
                          {
                              'errors': errors,
                              'article': article,
                              'cats': cats
                          })


def del_art(request, id):
    """删除文章"""
    if request.method == 'GET':
        # 获取文章并删除文章
        article = Articles.objects.filter(pk=id).first()
        article.art_type.count -= 1
        article.art_type.save()
        article.delete()
        return HttpResponseRedirect(reverse('backweb:article'))


def userset(request):
    if request.method == 'GET':
        user = request.user
        art_count = user.articles_set.count()
        return render(request, 'backweb/manage_user.html', {'username': user, 'count': art_count})


def update_user(request, id):
    if request.method == 'GET':
        user = User.objects.filter(pk=id).first()
        return render(request, 'backweb/update_user.html', {'user': user})

    if request.method == 'POST':
        # 表单数据验证
        form = UserInfo(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            udesc = form.cleaned_data.get('udesc')
            head_img = form.cleaned_data.get('head_img')
            sex = form.cleaned_data.get('sex')
            birth = form.cleaned_data.get('birth')
            user = User.objects.filter(pk=id).first()
            if head_img:
                user.head_img = head_img
            if birth:
                user.birth = birth
            user.sex =sex
            user.username = username
            user.udesc = udesc
            user.save()
            return HttpResponseRedirect(reverse('backweb:userset'))









