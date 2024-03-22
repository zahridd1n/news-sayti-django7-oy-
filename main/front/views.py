from django.shortcuts import render
from .. import models


def index(request):
    category = models.Category.objects.all()
    region = models.Region.objects.all()
    blog = models.Post.objects.all()
    last = blog.last()
    last2 = blog[len(blog) - 2]
    head_blog =[last,last2]
    # for blog in models.Post.objects.all():
    #     if len(head_blog) < 3 :
    context = {
        'category': category,
        'region': region,
        'head_blog': head_blog,
    }
    #         head_blog.append(blog)
    return render(request, 'front/index.html', context)


# def single_post(request):
#     return render(request, 'front/single-post.html')
#

def contact(request):
    return render(request, 'front/contact.html')


def category(request, id):
    category = models.Category.objects.all()
    region = models.Region.objects.all()
    categor = models.Category.objects.get(id=id)
    posts = models.Post.objects.filter(category=categor)
    context = {
        'category': category,
        'posts': posts,
        'region': region
    }
    return render(request, 'front/catagory.html', context)


def region(request, id):
    region_item = models.Region.objects.get(id=id)
    category = models.Category.objects.all()
    region = models.Region.objects.all()
    posts = models.Post.objects.filter(region=region_item)
    context = {
        'region_item':region_item,
        'posts': posts,
        'region': region,
        'category': category
    }

    return render(request, 'front/region.html', context)


def post_detail(request, id):
    post_item = models.Post.objects.get(id=id)
    post_img = models.PostImg.objects.filter(post=id)
    # post_video = models.PostVideo.objects.get(id=id)
    category = models.Category.objects.all()
    region = models.Region.objects.all()
    context = {
        'post_item': post_item,
        'category': category,
        'region': region,
        'post_img': post_img,
        # 'post_video': post_video
    }
    return render(request, 'front/single-post.html', context)
