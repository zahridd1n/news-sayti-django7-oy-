from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page),
    path('posts-in-category/<int:id>/', views.post_in_category),  # categoryaga tegishli postlarni chiqaradi
    path('posts-in-region/<int:id>/', views.post_in_region),  # regionaga tegishli postlarni chiqaradi
    # ---------comment-------------
    path('comment/<int:id>/', views.comment_post),  # comment
    # ---------post----------------
    path('post-list/', views.post_list),
    path('post-detail/<int:id>/', views.post_detail),
    # ---------category----------------
    path('category-list/', views.category_list),
    path('category-detail/<int:id>/', views.category_detail),
    # ---------region----------------
    path('region-list/', views.region_list),
    path('region-detail/<int:id>/', views.region_detail),
]
