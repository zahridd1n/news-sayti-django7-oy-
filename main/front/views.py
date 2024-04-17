from django.shortcuts import render
from .. import models


def index(request):
    categorys = models.Category.objects.all()
    regions = models.Region.objects.all()
    blog = models.Post.objects.all()
    head_blog = blog.filter().order_by('-id')[:2]
    context = {
        'category': categorys,
        'region': regions,
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
    categorys = models.Category.objects.all()
    regions = models.Region.objects.all()
    categor = models.Category.objects.get(id=id)
    posts = models.Post.objects.filter(category=categor)
    context = {
        'category': categorys,
        'posts': posts,
        'region': regions
    }
    return render(request, 'front/catagory.html', context)


def region(request, id):
    region_item = models.Region.objects.get(id=id)
    category = models.Category.objects.all()
    region = models.Region.objects.all()
    posts = models.Post.objects.filter(region=region_item)
    context = {
        'region_item': region_item,
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
