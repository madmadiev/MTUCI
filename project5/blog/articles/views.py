from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.http import Http404
from django.contrib import messages
from .forms import ArticleForm, UserRegistrationForm
from django.contrib.auth import authenticate, login

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
    
def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
        
def create_post(request):
    if request.user.is_anonymous:
        raise Http404

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('get_article', article_id=article.id)
        else:
            return render(request, 'create_post.html', {'form': form})
    else:
        form = ArticleForm()
        return render(request, 'create_post.html', {'form': form})
        
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('article_list')
            else:
                messages.error(request, 'Неправильное имя пользователя или пароль.')
        else:
            messages.error(request, 'Пожалуйста, заполните все поля.')
    return render(request, 'registration/login.html')