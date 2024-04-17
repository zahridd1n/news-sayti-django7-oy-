from . import views
from django.urls import path

urlpatterns = [
    # ---------category----------------
    path('category-list/', views.category_list),
    path('category-detail/<int:id>/', views.category_detail),
    # ---------post----------------
    path('post-list/', views.post_list),
    path('post-detail/<int:id>/', views.post_detail),
    # ---------region----------------
    path('region-list/', views.region_list),
    path('region-detail/<int:id>/', views.region_detail),
]
