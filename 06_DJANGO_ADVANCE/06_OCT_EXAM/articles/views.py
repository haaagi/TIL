from django.shortcuts import render, redirect, get_object_or_404
# accounts 에서 import 할 모든 것들은 django.contrib 이다 
# accounts 에서 import 할 Model(User) 과 Form(UserCreationForm, AF)
# user 모델을 가져오는 함수
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Article
from .forms import ArticleForm



@login_required
def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    # if article.like_users.filter(id=user.id).exists():   이게 제대로된 코드
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return redirect('articles:article_list')


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles':articles,
    })

@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {
        'article':article,
    })


@login_required
@require_http_methods(['GET','POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  # 혹은 article.user_id = request.user.id
            # = article.user_id = request.user.id
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/form.html', {
        'form':form,
    })


@login_required
@require_http_methods(['GET','POST'])
def article_update(request, article_id):
    # update 추가사항
    # 0. article 하나 찾기
    article = get_object_or_404(Article, id=article_id)
    # 1. user 비교하기 
    if article.user != request.user:
        return redirect('articles:article_list')
    # 2. instance 주기
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        # 4.  또 instance 주기 
        form = ArticleForm(instance=article)
    return render(request, 'articles/form.html', {
        'form':form,
    })


@login_required
@require_POST
def article_delete(request, article_id):
    # article = get_object_or_404(Article, id=article_id)
    # if request.user != 
    pass