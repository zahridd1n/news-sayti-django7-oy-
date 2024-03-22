from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    # category
    path('create_category/', views.create_category, name='create_category'),
    path('list_category/', views.list_category, name='list_category'),
    path('detail_category/<int:id>/', views.detail_category, name='detail_category'),
    path('edit_category/<int:id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),

    # region
    path('create_region/', views.create_region, name='create_region'),
    path('list_region/', views.list_region, name='list_region'),
    path('detail_region/<int:id>/', views.detail_region, name='detail_region'),
    path('edit_region/<int:id>/', views.edit_region, name='edit_region'),
    path('delete_region/<int:id>/', views.delete_region, name='delete_region'),

    # register
    path('register/', views.register, name='register'),
    path('log-out/', views.log_out, name='log_out'),

    # news
    path('create_news/', views.create_news, name='create_news'),
    path('list_news/', views.list_news, name='list_news'),
    path('detail_news/<int:id>/', views.detail_news, name='detail_news'),
    path('edit_news/<int:id>/', views.edit_news, name='edit_news'),
    path('delete_news/<int:id>/', views.delete_news, name='delete_news'),
]
