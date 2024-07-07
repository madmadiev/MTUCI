from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.http import Http404
from .forms import ArticleForm

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