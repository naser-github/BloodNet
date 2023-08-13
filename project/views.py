from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse

# import forms here
from .forms import RegistrationForm
from .forms import LoginForm

# import models here
from .models import BloodGroup

User = get_user_model()


# Create your views here.
def test(request):
    return render(request, 'project/test/index.html')


def signup(request):
    blood_groups = None
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.instance.password = make_password(form.cleaned_data['password'])
            form.save()
            return redirect(reverse('login'))
    else:
        form = format_registration_form
        blood_groups = BloodGroup.objects.all()

    return render(request, 'project/auth/signup.html', {
        'blood_groups': blood_groups, 'form': form
    })


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('donor-list'))
            else:
                messages.error(request, "there was an error")

    form = format_login_form()
    return render(request, 'project/auth/login.html', {
        'form': form,
    })


def logout_user(request):
    logout(request)
    return redirect(reverse('login'))


def profile(request):
    breadcrumb = [{'url': 'profile', 'name': 'Profile'}]

    return render(request, 'project/profile/index.html', {
        'breadcrumb': breadcrumb
    })


def donor_list(request):
    breadcrumb = [{'url': 'donor-list', 'name': 'Donor List'}]

    items_per_page = 10

    donors = User.objects.filter(can_donate=True)

    paginator = Paginator(donors, items_per_page)
    page_number = request.GET.get('page')
    donors = paginator.get_page(page_number)

    return render(request, 'project/donor/index.html', {
        'breadcrumb': breadcrumb, 'donors': donors
    })


def news_feed(request):
    return render(request, 'project/posts/index.html')


# helper functions
def format_registration_form():
    form = RegistrationForm()

    form.fields['first_name'].widget.attrs['class'] = 'form-control'
    form.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
    form.fields['first_name'].required = True

    form.fields['last_name'].widget.attrs['class'] = 'form-control'
    form.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
    form.fields['last_name'].required = True

    form.fields['email'].widget.attrs['class'] = 'form-control'
    form.fields['email'].widget.attrs['placeholder'] = 'Email'
    form.fields['email'].required = True

    form.fields['phone'].widget.attrs['class'] = 'form-control'
    form.fields['phone'].widget.attrs['placeholder'] = 'Phone'
    form.fields['phone'].required = True

    form.fields['password'].widget.attrs['class'] = 'form-control'
    form.fields['password'].widget.attrs['placeholder'] = 'Password'
    form.fields['password'].widget.input_type = 'password'
    form.fields['password'].required = True

    form.fields['address'].widget.attrs['class'] = 'form-control'
    form.fields['address'].widget.attrs['placeholder'] = 'Address'
    form.fields['address'].required = True

    form.fields['lat'].widget.attrs['class'] = 'form-control'
    form.fields['lat'].widget.attrs['placeholder'] = 'Latitude'
    form.fields['lat'].required = True

    form.fields['long'].widget.attrs['class'] = 'form-control'
    form.fields['long'].widget.attrs['placeholder'] = 'Longitude'
    form.fields['long'].required = True

    form.fields['blood_group'].widget.attrs['class'] = 'custom-select'
    form.fields['blood_group'].widget.attrs['placeholder'] = 'Blood Group'
    form.fields['blood_group'].required = True

    return form


def format_login_form():
    form = LoginForm()

    form.fields['email'].widget.attrs['class'] = 'form-control'
    form.fields['email'].widget.attrs['placeholder'] = 'Email'
    form.fields['email'].required = True

    form.fields['password'].widget.attrs['class'] = 'form-control'
    form.fields['password'].widget.attrs['placeholder'] = 'Password'
    form.fields['password'].widget.input_type = 'password'
    form.fields['password'].required = True

    return form
