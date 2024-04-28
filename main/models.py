from django.db import models
from django.contrib.auth.models import User


# class User(AbstractUser):
#     manzil = models.CharField(max_length=255, blank=True, null=True)
#     tel = models.CharField(max_length=255, blank=True, null=True)
#     avatar = models.ImageField(max_length=255, blank=True, null=True, upload_to='avatar/')


class Region(models.Model):
    name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    banner = models.ImageField(upload_to='banner/')
    date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def post_img(self):
        return PostImg.objects.filter(post=self)

    @property
    def post_video(self):
        return PostVideo.objects.filter(post=self)


class PostImg(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post-img/')


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to='post-video/')
    video_url = models.URLField(blank=True, null=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
