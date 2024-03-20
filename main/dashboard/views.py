from django.shortcuts import render, redirect
from .. import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login


def index(request):
    """admin panelning asosiy sahifasi"""
    category = models.Category.objects.all()
    user = User.objects.last()

    context = {
        'category': category,
        'user': user,
    }

    return render(request, 'dashboard/index.html', context)


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


def list_category(request):
    category = models.Category.objects.all()

    context = {
        'category': category,
    }

    return render(request, 'dashboard/categorya/list.html', context)


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

    return render(request, 'dashboard/categorya/delete.html')



def register(request):
    """ro'yxatdan o'tish va kirish uchun"""

    # registratsiya qismi, register templatimda sign in va sign up bitada bolganligi uchun bita funksiyaga yozdim ikklasanini
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


    #login qismi, register templatimda sign in va sign up bitada bolganligi uchun bita funksiyaga yozdim ikklasanini
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


