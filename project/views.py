from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.urls import reverse

# import forms here
from .forms import RegistrationForm

User = get_user_model()


# Create your views here.
def Test(request):
    return render(request, 'project/test/index.html')


def SignUp(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
    else:
        form = RegistrationForm()

    return render(request, 'project/auth/signup.html', {
        'form': form
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
