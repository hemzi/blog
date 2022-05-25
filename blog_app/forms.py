from django import forms
from .models import Post


class PostNewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        labels = {'title': '', 'body': ''}
