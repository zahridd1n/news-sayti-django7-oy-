from django.shortcuts import render, redirect
from .. import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login


@login_required(login_url='dashboard:register')
def index(request):
    """admin panelning asosiy sahifasi"""
    category = models.Category.objects.all()
    context = {
        'category': category
    }

    return render(request, 'dashboard/index.html', context)


@login_required(login_url='dashboard:register')
def create_category(request):
    """categorya yaratish"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            models.Category.objects.create(
                name=name,
            )
            messages.success(request, 'Category created successfully')
        except:
            messages.error(request, 'Category creation failed')

    return render(request, 'dashboard/categorya/create.html')


@login_required(login_url='dashboard:register')
def list_category(request):
    category = models.Category.objects.all()

    context = {
        'category': category,
    }

    return render(request, 'dashboard/categorya/list.html', context)


@login_required(login_url='dashboard:register')
def detail_category(request, id):
    category = models.Category.objects.get(id=id)

    context = {
        'category': category,
    }

    return render(request, 'dashboard/categorya/detail.html', context)


def edit_category(request, id):
    """categoryani tahririrlash"""
    category = models.Category.objects.get(id=id)
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            models.Category.objects.filter(id=id).update(
                name=name,
            )
            messages.success(request, 'Category updated successfully')
            return redirect('dashboard:detail_category', category.id)
        except:
            messages.error(request, 'Category update failed')

    return render(request, 'dashboard/categorya/edit.html', context={'category': category})


def delete_category(request, id):
    """categoryani o'cirish"""
    try:
        models.Category.objects.filter(id=id).delete()
        messages.success(request, 'Category deleted successfully')
        return redirect('dashboard:list_category')
    except:
        messages.error(request, 'Category deletion failed')
        return redirect('dashboard:list_category')


# --------region------------#
def create_region(request):
    """regiona yaratish"""
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            models.Region.objects.create(
                name=name,
            )
            messages.success(request, 'Region created successfully')
        except:
            messages.error(request, 'Region creation failed')

    return render(request, 'dashboard/region/create.html')


def list_region(request):
    """regionlar ro'yxati"""
    regions = models.Region.objects.all()
    context = {
        'regions': regions,
    }
    return render(request, 'dashboard/region/list.html', context)


def detail_region(request, id):
    region = models.Region.objects.get(id=id)
    context = {
        'region': region,
    }
    return render(request, 'dashboard/region/detail.html', context)


def edit_region(request, id):
    """regionani tahririrlash"""
    region = models.Region.objects.get(id=id)
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            models.Region.objects.filter(id=id).update(
                name=name,
            )
            messages.success(request, 'Region updated successfully')
            return redirect('dashboard:detail_region', region.id)
        except:
            messages.error(request, 'Region update failed')

    return render(request, 'dashboard/region/edit.html', context={'region': region})


def delete_region(request, id):
    try:
        models.Region.objects.get(id=id).delete()
        messages.success(request, 'Region deletion successful')
        return redirect('dashboard:list_region')
    except:
        messages.error(request, 'Region deletion failed')
        return redirect('dashboard:list_region')


def register(request):
    """ro'yxatdan o'tish va kirish uchun"""
    # -------registratsiya qismi, register templatimda sign in va sign up bitada bolganligi uchun bita funksiyaga yozdim ikklasanini

    if request.POST.get('password-confirm'):
        if request.method == 'POST':
            username = request.POST.get('username-up')
            password = request.POST.get('password-up')
            password_confirm = request.POST.get('password-confirm')
            if password_confirm == password:
                User.objects.create_user(
                    username=username,
                    password=password
                )
                messages.success(request, 'User yaratildi')

                user = authenticate(
                    username=username,
                    password=password
                )

                if user:
                    login(request, user)
                    return redirect('dashboard:index')
            else:

                messages.error(request, 'User yaratishda xatoli yuzaga keldi')


    # login qismi, register templatimda sign in va sign up bitada bolganligi uchun bita funksiyaga yozdim ikklasanini
    elif request.POST.get('username-in'):
        if request.method == 'POST':
            username = request.POST.get('username-in')
            password = request.POST.get('password-in')

            user = authenticate(
                username=username,
                password=password,
            )
            if user:
                login(request, user)
                messages.success(request, 'Kirish amalga to`gri amalga oshdi')
                return redirect('dashboard:index')
            else:
                messages.error(request, 'kirishda xatolik, qayta urinib ko\'ring ')

    return render(request, 'auth/index.html')


def log_out(request):
    """chiqish"""
    logout(request)
    return redirect('main:index')


def create_news(request):
    categorys = models.Category.objects.all()
    regions = models.Region.objects.all()
    authors = models.User.objects.all()

    if request.method == 'POST':
        try:
            category_id = request.POST.get('category_id')
            title = request.POST.get('title')
            body = request.POST.get('body')
            banner = request.FILES.get('banner')
            date = request.POST.get('date')
            author_id = request.POST.get('author_id')
            region_id = request.POST.get('region_id')
            news = models.Post.objects.create(
                title=title,
                body=body,
                banner=banner,
                date=date,
                author_id=author_id,
                category_id=category_id,
                region_id=region_id
            )

            images = request.FILES.getlist('img')
            for img in images:
                image = models.PostImg.objects.create(
                    post=news,
                    img=img,
                )

            messages.success(request, 'News created successfully')
        except:
            messages.error(request, 'News creation failed')

    context = {
        'categorys': categorys,
        'authors': authors,
        'regions': regions,
    }

    return render(request, 'dashboard/news/create.html', context)


def list_news(request):
    posts = models.Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'dashboard/news/list.html', context)


def detail_news(request, id):
    post = models.Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'dashboard/news/detail.html', context)


def edit_news(request, id):
    post = models.Post.objects.get(id=id)
    categorys = models.Category.objects.all()
    authors = models.User.objects.all()
    regions = models.Region.objects.all()
    context = {
        'post': post,
        'categorys': categorys,
        'authors': authors,
        'regions': regions,
    }
    if request.method == 'POST':

        title = request.POST.get('title')
        body = request.POST.get('body')
        author_id = request.POST.get('author_id')
        category_id = request.POST.get('category_id')
        region_id = request.POST.get('region_id')
        if request.FILES.get('banner'):
            post.banner = request.FILES.get('banner')
        post.save()
        news = models.Post.objects.filter(id=id).update(
            title=title,
            body=body,
            author_id=author_id,
            category_id=category_id,
            region_id=region_id
        )
        images = request.FILES.getlist('img')
        for img in images:
            image = models.PostImg.objects.create(
                post=models.Post.objects.get(id=id),
                img=img,
            )
        # messages.success(request, 'News updated successfully')
        return redirect('dashboard:detail_news', post.id)

        # messages.error(request, 'News update failed')
    return render(request, 'dashboard/news/edit.html', context)


def delete_news(request, id):
    try:
        models.Post.objects.filter(id=id).delete()
        messages.success(request, 'News deleted successfully')
        return redirect('dashboard:list_news')
    except:
        messages.error(request, 'News deletion failed')
    return render(request, 'dashboard/news/delete.html')
