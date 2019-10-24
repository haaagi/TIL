from django.shortcuts import render, redirect, get_object_or_404
# accounts 에서 import 할 모든 것들은 django.contrib 이다 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# accounts 에서 import 할 Model(User) 과 Form(UserCreationForm, AF)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# user 모델을 가져오는 함수
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from django.views.decorators.http import require_http_methods


# @require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:  # is_authenticated 는 함수가 아니다
        return redirect('articles:article_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/form.html', {
        'form':form,
    })
        


def login(request):
    if request.user.is_authenticated:  # is_authenticated 는 함수가 아니다
        return redirect('articles:article_list')
    if request.method == 'POST':
        # AuthForm 은 인자가 2(request, request.POST)개 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인 성공 => 성공한 user 를 꺼낸다. 
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:article_list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/form.html', {
        'form':form,
    })


def logout(request):
    auth_logout(request)
    return redirect('articles:article_list')


