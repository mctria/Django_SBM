from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='First name')

    class Meta:
        model = User
        fields = ("username", "first_name", "password1", "password2")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]