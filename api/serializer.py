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
        fields = ['id', 'name']


class CategoryDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class PostImageSerializer(ModelSerializer):
    class Meta:
        model = models.PostImg
        fields = ['post', 'img']


class PostVideoSerializer(ModelSerializer):
    class Meta:
        model = models.PostVideo
        fields = ['post', 'video', 'video_url']


class PostListSerializer(ModelSerializer):
    author = UserSerializer()
    post_img = PostImageSerializer(many=True)
    post_video = PostVideoSerializer(many=True)

    class Meta:
        model = models.Post
        fields = ['id', 'title', 'date', 'author', 'banner', 'post_img', 'post_video']
        depth = 1


class PostDetailSerializer(ModelSerializer):
    author = UserSerializer()
    post_img = PostImageSerializer(many=True)
    post_video = PostVideoSerializer(many=True)

    class Meta:
        model = models.Post
        fields = '__all__'
        # fields = ['id', 'title', 'body', 'banner_img', 'date', 'author', 'category', 'region']
        depth = 1


class RegionListSerializer(ModelSerializer):
    class Meta:
        model = models.Region
        fields = ['id', 'name']


class RegionDetailSerializer(ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'
