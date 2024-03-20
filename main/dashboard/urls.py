from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    #category
    path('create_category/', views.create_category, name='create_category'),
    path('list_category/', views.list_category, name='list_category'),
    path('detail_category/<int:id>/', views.detail_category, name='detail_category'),
    path('edit_category/<int:id>/', views.edit_category, name = 'edit_category'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),

    #register
    path('register/', views.register, name='register'),
    path('log-out/', views.log_out, name='log_out'),

    ]