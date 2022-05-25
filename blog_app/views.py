from django.shortcuts import render
from .models import Post
# for testing
from django.http import HttpResponse

# Create your views here.
def home(request):
  posts = Post.objects.order_by('-created')
  context = {'posts':posts}
  return render(request, 'blog_app/home.html', context)