from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=200)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateField(auto_now=True)
  # tags = 
  def __str__(self):
    return self.title[:10]