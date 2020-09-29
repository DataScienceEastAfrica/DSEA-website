from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from mdeditor.fields import MDTextFormField
from .models import Comment


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class CreatePostForm(forms.Form):
    cover_Image = forms.FileField()
    Title = forms.CharField(
        max_length=200, widget=forms.TextInput(attrs={"placeholder": "Enter the Title"})
    )
    content = MDTextFormField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")
        body = MDTextFormField
