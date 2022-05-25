from django.shortcuts import render
# for testing
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'blog_app/base.html')