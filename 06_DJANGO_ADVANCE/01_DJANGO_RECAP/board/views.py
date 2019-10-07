from django.shortcuts import render, redirect
from .models import Article
# Create your views here.


def index(request):
    return render(request, 'board/index.html')


def list(request):
    articles = Article.objects.all()   # [<A1>,<A2>,<A3>,....] 이런식으로 들어옴
    return render(request, 'board/list.html', {
        'articles':articles,
    })


def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'board/detail.html', {
        'article':article,
    })


def new(request):
    return render(request, 'board/new.html')


def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    print(article.id, article.title, article.content)
    return redirect('board:detail',article.id)

