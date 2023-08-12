from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.urls import reverse

# import models here
from .models import BloodGroup
# import forms here
from .forms import RegistrationForm

User = get_user_model()


# Create your views here.
def Test(request):
    return render(request, 'project/test/index.html')


def SignUp(request):
    blood_groups = None
    if request.method == 'POST':
        print(request.POST)
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
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




        blood_groups = BloodGroup.objects.all()
        print(blood_groups)
    return render(request, 'project/auth/signup.html', {
        'blood_groups': blood_groups, 'form': form
    })


def Login(request):
    if request.method == 'POST':
        print(request.POST)
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('donor-list'))
        else:
            messages.error(request, "there was an error")
        return redirect(reverse('login'))
    else:
        return render(request, 'project/auth/login.html')


def Logout(request):
    logout(request)
    return redirect(reverse('login'))


def DonorList(request):
    breadcrumb = [{'url': 'donor-list', 'name': 'Donor List'}]

    items_per_page = 10

    donors = User.objects.filter(can_donate=True)

    paginator = Paginator(donors, items_per_page)
    page_number = request.GET.get('page')
    donors = paginator.get_page(page_number)

    return render(request, 'project/donor/index.html', {
        'breadcrumb': breadcrumb, 'donors': donors
    })
