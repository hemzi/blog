from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
  #index
  path('', views.home, name='home')
]