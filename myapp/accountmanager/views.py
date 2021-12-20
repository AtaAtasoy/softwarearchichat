from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, request
from django.urls import reverse

from accountmanager.forms import RegisterForm

# Create your views here.
User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()
    return render(request, 'accountmanager/register.html', {'form': form})


def loginView(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account Not Active")
        else:
            context = {'notfound': True}
            print(
                f"INVALID CREDENTIALS (USERNAME: {username} - PASSWORD: {password})")
            print(context)
            return render(request, 'accountmanager/login.html', context)
    else:
        return render(request, 'accountmanager/login.html')

def logoutView(request):
    logout(request)
    return render(request, 'accountmanager/login.html')
