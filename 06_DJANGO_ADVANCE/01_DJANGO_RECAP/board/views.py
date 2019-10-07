from django.shortcuts import render
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


