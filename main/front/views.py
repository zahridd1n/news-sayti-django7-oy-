from django.shortcuts import render
from .. import models


def index(request):
    category = models.Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'front/index.html', context)


def single_post(request):
    return render(request, 'front/single-post.html')


def contact(request):
    return render(request, 'front/contact.html')
