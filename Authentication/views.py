from django.shortcuts import render

# Create your views here.

def login(request):
    template = 'accounts/login.html'
    return render(request, template, {})


def signup(request):
    template = 'accounts/signup.html'
    return render(request, template, {})