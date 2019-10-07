from django.shortcuts import render, HttpResponse

# Create your views here.


def guess(request):
    return render(request, 'home/guess.html')


def index(request):
    return render(request, 'home/index.html')


def answer(request):
    count = 0
    if request.POST.get('q1') == '0115':
        count += 1
    if request.POST.get('q2') == '275':
        count += 1
    if request.POST.get('q3') == 'B':
        count += 1
    return render(request, 'home/answer.html', {'count':count})
