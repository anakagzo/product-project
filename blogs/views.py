from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Blog
from accounts.views import create_acc
from accounts.models import Acc


# Create your views here.
def home(request):
    bloginfo = Blog.objects
    productinfo = Acc.objects
    return render(request, 'home.html', {'blogs': bloginfo, 'products': productinfo})


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            try:
                existing_user = User.objects.get(email=request.POST['email'])
                return render(request, 'signup.html', {'error': 'email already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error': 'password does not match'})
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'error': 'email or password incorrect'})
        else:
            auth.login(request, user)
            return redirect('home')

    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


@login_required(login_url='/signup')
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog})




# detailblog=get_object_or_404(Blog, pk=blog_id)
