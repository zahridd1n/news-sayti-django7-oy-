from rest_framework.serializers import ModelSerializer
from main import models
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name']


class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class PostListSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'date', 'author']
        depth = 1


class PostDetailSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = models.Post
        fields = '__all__'
        # fields = ['id', 'title', 'body', 'banner_img', 'date', 'author', 'category', 'region']
        depth = 1


class RegionListSerializer(ModelSerializer):
    class Meta:
        model = models.Region
        fields = ['name']


class RegionDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'
