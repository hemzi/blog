from django.shortcuts import render, redirect
from .models import Post
from .forms import PostNewForm, PostEditForm
# for testing
from django.http import HttpResponse

# Create your views here.
def home(request):
  '''return all posts in descending order'''
  posts = Post.objects.order_by('-created')
  context = {'posts':posts}
  return render(request, 'blog_app/home.html', context)

def post_new(request):
  '''create post'''
  if request.method != 'POST':
    # send empty form if GET
    form = PostNewForm()
  else:
    form = PostNewForm(data=request.POST)
    # check form and save to table
    if form.is_valid():
      form.save()
      return redirect('blog_app:home')
  context = {'form':form}
  return render(request, 'blog_app/post_new.html', context)

def post_edit(request, post_id):
  '''edit post'''
  post = Post.objects.get(id=post_id)
  if request.method != 'POST':
    form = PostEditForm(instance=post)
  else:
    form = PostEditForm(instance=post, data=request.POST)
    # check form and save to table
    if form.is_valid():
      form.save()
      return redirect('blog_app:home')
  context = {'form':form, 'post_id':post_id}
  return render(request, 'blog_app/post_edit.html', context)