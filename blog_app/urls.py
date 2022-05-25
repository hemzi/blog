from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
  #index
  path('', views.home, name='home'),
  path('posts/edit/', views.post_edit, name='post_edit'),
]