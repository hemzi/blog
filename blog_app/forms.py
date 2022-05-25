from django import forms
from .models import Post


class post_edit(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        labels = {'text': '', 'body': ''}
