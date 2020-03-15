from django.shortcuts import render
from .forms import UserLoginForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect

def login_view(request):
    next = request.GET.get('next', reverse('login'))
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            next = request.POST.get('next', reverse('login'))
            return HttpResponseRedirect(next)
    context = {
        'form': form,
        'next': next,
    }
    return render(request, 'initial/login.html', context=context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def home_view(request):
    return render(request, 'initial/home.html')