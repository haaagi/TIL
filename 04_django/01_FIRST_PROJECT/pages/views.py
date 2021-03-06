from django.shortcuts import render, HttpResponse
import json


def index(request):
    return HttpResponse('Hi django! :)')


def about(request):
    me = {
        'name': '유태영',
        'role': 'Teacher',
        'email': 'neo@hphk.kr',
    }
    return HttpResponse(json.dumps(me))


# HTML 을 내보내고 싶다.
def portfolio(request):
    return render(request, 'portfolio.html')


# pages/help/ => help() view 함수 실행 => help.html (내용 무관)
def help(request):
    return render(request, 'help.html')