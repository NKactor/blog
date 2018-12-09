
from rest_framework import serializers

from backweb.models import User
from web.models import Articles, ArticleType


class ArticleSerializer(serializers.ModelSerializer):
    # User.articles = serializers.StringRelatedField(many=True)
    # 指定序列化模型
    class Meta:
        model = Articles
        # 指定序列化字段
        fields = [ 'id','title', 'desc', 'contents', 'icon', 'create_time']


class CatSerializer(serializers.ModelSerializer):

     class Meta:
         model = ArticleType
         fields = ['id', 'type_name', 'count']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','udesc', 'head_img']



