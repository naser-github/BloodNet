from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'address', 'lat', 'long', 'blood_group',
                  'lat', 'long']
