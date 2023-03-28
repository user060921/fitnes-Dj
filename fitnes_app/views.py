from django.core import serializers
from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.files.storage import default_storage


def home_page(request): 
    context = {'home': 'active'}
    return render(request, 'home.html', context)


def register_page(request):
    context = {'register': 'active'}
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            context['message'] = 'Bunday Email mavjud'
            return render(request, 'register.html', context)

        user = User.objects.create(
            username=email,
            email=email, first_name=first_name,
            last_name=last_name)
        user.set_password(password)
        user.save()
        return redirect('home')

    return render(request, 'register.html')


def login_page(request):
    context = {'login': 'active'}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            context['message'] = 'Email yoki Parol xato!!!'
            context['email'] = email
            context['password'] = password
    return render(request, 'login.html', context)


@login_required
def logout_page(request):
    logout(request)
    return redirect('home')


def programms_page(request):
    programms = FitnessProgramm.objects.all()
    context = {
        'programms': programms,
        'prog': 'active'
    }
    return render(request, 'programms.html', context)


def programm_detail_page(request, slug):
    programm = FitnessProgramm.objects.get(slug=slug)
    context = {
        'programm': programm,
        'prog': 'active',
    }
    if request.user.is_authenticated:
        is_liked = Favorite.objects.filter(favorite_slug=slug, user=request.user).exists()
        is_liked = 'solid' if is_liked else 'regular'
    else:
        is_liked = None

    context['is_liked'] = is_liked

    return render(request, 'programm_detail.html', context)


def articles_page(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
        'article': 'active'
    }
    return render(request, 'articles.html', context)


def article_detail_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {
        'article_item': article,
        'article': 'active',
    }

    if request.user.is_authenticated:
        is_liked = Favorite.objects.filter(favorite_slug=slug, user=request.user).exists()
        is_liked = 'solid' if is_liked else 'regular'
    else:
        is_liked = None

    context['is_liked'] = is_liked
    return render(request, 'article_detail.html', context)


@login_required
def profile_page(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.user.email)
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('fname')
        user.last_name = request.POST.get('lname')
        avatar = request.FILES.get('avatar')
        is_delete = request.POST.get('avater_delete')

        if avatar:
            filename = f'avatar/{avatar}'
            with default_storage.open(filename, 'wb+') as f:
                for chunk in avatar.chunks():
                    f.write(chunk)
            user.avatar = filename
        elif is_delete:
            user.avatar.delete()

        user.save()
        return redirect('profile')
        
    return render(request, 'profile.html')


def reset_password_page(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        user = User.objects.filter(email=email)
        if user.exists():
            if password == password1:
                user = user.first()
                user.set_password(password)
                user.save()
            else:
                context['error'] = 'Parol birxil emas!'
        else:
            context['error'] = 'B unday emailmavjud emas!'

    return render(request, 'reset_password.html', context)


def check_like(request):
    if request.method == 'GET':
        slug = request.GET.get('slug')
        like = request.GET.get('like')
        title = request.GET.get('title')
        if like == 'true':
            tip = request.GET.get('tip')
            Favorite.objects.create(
                user=request.user, favorite_title=title,
                favorite_slug=slug, favorite_type=tip
            )
        else:
            Favorite.objects.get(favorite_slug=slug).delete()
        return HttpResponse(status=200)


def favorite_page(request):
    favorites = Favorite.objects.filter(user=request.user)
    context = {
        'favorites': favorites,
        'favorite': 'active',
    }
    return render(request, 'favorite.html', context)


def search_programm(request):
    data = request.GET
    new_data = []
    for i in data:
        new_data.append(str(data[i]))
    programms = FitnessProgramm.objects.filter(intensity=new_data[0]).filter(type=new_data[1]).filter(gender=new_data[2]).filter(part_of_body=new_data[3])

    data = serializers.serialize('json', programms)
    return HttpResponse(data, content_type="application/json")
