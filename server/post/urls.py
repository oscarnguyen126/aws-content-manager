from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post'),
    path('posts/<slug:id>', views.PostDetail.as_view(), name='post_detail'),
]
