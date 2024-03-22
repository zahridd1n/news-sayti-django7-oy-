from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail/<int:id>', views.post_detail, name='post_detail'),
    # path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<int:id>/', views.category, name='category'),
    path('region/<int:id>', views.region, name='region_select')
    ]