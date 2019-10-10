from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST,require_http_methods
from .forms import ArticleModelForm
from IPython import embed
from .models import Article
# CRUD

@require_http_methods(['GET','POST'])
def new(request):
    if request.method == 'POST':
        form = ArticleModelForm(request.POST)
    # 요청이 GET/ POST 중 어떤 것인지 확인한다.
    # 만약 POST 라면
        # ArticleModelForm 을 생성하고 data 를 채운다(binding).
        # binding 된 form 이 유효한지 체크한다.
        if form.is_valid():
            # 유효하다면 form 을 저장한다.
            article = form.save()
            # 저장한 article 로 redirect 한다.
            return redirect(article)   # 이건 redirect('board:detail', article.id)줄인거다.
        # form 이 유효하지 않다면,
    # GET 이라면
    else:
        # 비어있는 form을 만든다.
        form = ArticleModelForm()
        # form 과 html 을 사용자에게 보여준다.
    return render(request, 'board/new.html', {
        'form':form,
    })


def list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles':articles,
    })

@require_http_methods(['GET','POST'])
def edit(request, id):
    if request.method == 'POST':  # 여긴 제출
        form = ArticleModelForm(request.POST)
        if form_is_valid():
            article = form.save()
            return redirect(article)
    else:   # 여긴 종이주세요
        article = get_object_or_404(Article, id=id)
        form = ArticleModelForm(instance=article)
        return render(request, 'board/edit.html', {
            'form':form,
        })

    



def detail(request):
    article = get_object_or_404(Article,id=id)
    return render(request, 'board/detail.html', {
        'article': article,
    })

def delete(request):
    pass
























###  여기서부턴 원래 우리가 했던거  ###
# from .models import Article
# from .forms import ArticleModelForm
# # Create your views here.


# @require_GET
# def index(request):
#     return render(request, 'board/index.html')



# @require_GET
# def list(request):
#     articles = Article.objects.all()   # [<A1>,<A2>,<A3>,....] 이런식으로 들어옴
#     return render(request, 'board/list.html', {
#         'articles':articles,
#     })


# @require_GET
# def detail(request, id):
#     article = get_object_or_404(Article, id=id)
#     return render(request, 'board/detail.html', {
#         'article':article,
#     })


# def new(request):
#     if request.method == 'POST':
#         form = ArticleModelForm(request.POST)
#         if form.is_valid():
#             article = form.save()
#             return redirect(article)
#     else:
#         form = ArticleModelForm()
#         return render(request, 'board/new.html', {
#             'form':form,
#         })




# def edit(request, id):
#     article = get_object_or_404(Article, id=id)
#     if request.method == 'POST':
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.save()
#         return redirect(article)
#     else:
#         return render(request, 'board/edit.html', {
#             'article':article,
#         })
       


# @require_POST
# def delete(request, id):
#     article = get_object_or_404(Article, id=id)
#     article.delete()
#     return redirect('board:list')

