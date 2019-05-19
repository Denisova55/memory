import random
from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import auth


def posts_list(request):
    """Страница со списком всех постов"""
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'mysite/posts_list.html', context={'posts': posts, 'page': page})


def post_detail(request, post_id):
    """Страница поста"""
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'mysite/post_detail.html', context={'post': post})


def create_new_post(request):
    """Создание нового поста"""
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.name = request.user
            post.save()
            return redirect('post_detail', post_id=post.id)
        else:
            return render(request, 'mysite/create_new_post.html', context={'post_form': post_form})
    else:
        post_form = PostForm()
        return render(request, 'mysite/create_new_post.html', context={'post_form': post_form})


def persons_list(request):
    """Лист с персональнымии постами"""
    all_posts = Post.objects.filter(star__exact="True")
    paginator = Paginator(all_posts, 1)
    page = request.GET.get('page')
    try:
        all_posts = paginator.page(page)
    except PageNotAnInteger:
        all_posts = paginator.page(1)
    except EmptyPage:
        all_posts = paginator.page(paginator.num_pages)
    return render(request, 'mysite/persons_list.html', context={'all_posts': all_posts, 'page': page})


def random_post(request):
    """Рандомный пост"""
    items = Post.objects.all()
    random_item = random.choice(items)
    return render(request, 'mysite/random_post.html', context={'random_object': random_item})


def registration(request):
    """Регистрация пользователя"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('registration')
    else:
        form = UserCreationForm()
    return render(request, 'mysite/registration.html', {'form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('posts_list')
        else:
            messages.error(request, 'Error wrong username/password')
    return render(request, 'mysite/log_in.html')


def log_out(request):
    """Выход авторизованного пользователя из системы"""
    auth.logout(request)
    return redirect('posts_list')

