from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('single_post', views.single_post, name='single_post'),
    # path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    ]