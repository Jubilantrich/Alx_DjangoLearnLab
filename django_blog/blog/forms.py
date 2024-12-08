from .models import Post
from django import forms

class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

