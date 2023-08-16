from django.contrib.auth import get_user_model
from django import forms

from .models import Post

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'address', 'lat', 'long', 'blood_group',
                  'lat', 'long']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'contact_no', 'location']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'}),
            'location': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
