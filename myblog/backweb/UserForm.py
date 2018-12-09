
from django import forms


class LoginForm(forms.Form):
    # 登录表单数据检验
    username = forms.CharField(required=True, min_length=4, max_length=10,
                               error_messages={
                                   'require': '用户名不能为空！',
                                   'min_length': '用户名不能少于4个字符！',
                                   'max_length': '用户名最多不能超过10个字符！'
                               })
    password = forms.CharField(required=True, min_length=6, max_length=16,
                               error_messages={
                                   'require': '密码不能为空！',
                                   'min_length': '密码不能少于6位！',
                                   'max_length': '密码不能超过16位！'
                               })


class RegisterForm(forms.Form):
    # 注册表单验证
    username = forms.CharField(required=True, min_length=4, max_length=10,
                               error_messages={
                                   'require': '用户名不能为空！',
                                   'min_length': '用户名不能少于4个字符！',
                                   'max_length': '用户名最多不能超过10个字符！'
                               })
    password = forms.CharField(required=True, min_length=6, max_length=16,
                               error_messages={
                                   'require': '密码不能为空！',
                                   'min_length': '密码不能少于6位！',
                                   'max_length': '密码不能超过16位！'
                               })

    udesc = forms.CharField(required=True, min_length=5,
                             error_messages={
                                 'require': '自我描述是必填项！',
                                 'min_length': '自我描述不能少于5个字符！',
                             })
    sex = forms.IntegerField(required=True)

    head_img = forms.ImageField(required=False)


class AddArticle(forms.Form):
    """添加文章检验"""
    title = forms.CharField(min_length=5, max_length=30, required=True,
                            error_messages={
                                'required': '文章标题必填！',
                                'min_length': '标题不能少于5个字符！',
                                'max_length': '标题不能超过30个字符！'
                            })
    desc = forms.CharField(min_length=20, max_length=100, required=True,
                           error_messages={
                               'required': '文章描述必填！',
                               'min_length': '描述不能少于20个字符！',
                               'max_length': '描述不能超过100个字符！'
                           })

    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填！'
                              })

    icon = forms.ImageField(required=True,
                            error_messages={
                                'required': '文章首图必选！'
                            })
    art_type = forms.CharField(required=True,
                                  error_messages={
                                      'required': '请为你的文章选个类型吧！'
                                  })


class EditArticle(forms.Form):
    """添加文章检验"""
    title = forms.CharField(min_length=5, max_length=30, required=True,
                            error_messages={
                                'required': '文章标题必填！',
                                'min_length': '标题不能少于5个字符！',
                                'max_length': '标题不能超过30个字符！'
                            })
    desc = forms.CharField(min_length=20, max_length=100, required=True,
                           error_messages={
                               'required': '文章描述必填！',
                               'min_length': '描述不能少于20个字符！',
                               'max_length': '描述不能超过100个字符！'
                           })

    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容必填！'
                              })

    icon = forms.ImageField(required=False)

    art_type = forms.CharField(required=True,
                                  error_messages={
                                      'required': '请为你的文章选个类型吧！'
                                  })


class CatType(forms.Form):

    type_name = forms.CharField(max_length=20, required=True,
                                error_messages={
                                    'require': '类型名不能为空！',
                                    'max_length': '类型名不能超过20个字符！'
                                })
    f_type_id = forms.CharField(required=False)


class UserInfo(forms.Form):

    username = forms.CharField(max_length=31, required=True,min_length=4,
                                error_messages={
                                    'require': '用户名不能为空！',
                                    'max_length': '用户名不能超过30个字符！',
                                    'min_length': '用户名不能少于4个字符！'
                                })
    password = forms.CharField(required=False, min_length=6, max_length=16,
                               error_messages={
                                   'require': '密码不能为空！',
                                   'max_length': '密码不能超过16个字符！',
                                   'min_length': '密码不能少于4个字符！'
                               })
    udesc = forms.CharField(required=False)
    sex = forms.CharField(required=True)
    head_img = forms.ImageField(required=False)
    birth = forms.DateField(required=False)

