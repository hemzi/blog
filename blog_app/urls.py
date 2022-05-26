from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
  #index
  path('', views.home, name='home'),
  path('posts/new/', views.post_new, name='post_new'),
  path('posts/edit/<int:post_id>', views.post_edit, name='post_edit'),
]