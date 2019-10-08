from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from .models import Student


def list(request):
    students = Student.objects.all()
    return render(request, 'classroom/list.html', {
        'students':students,
    })


def new(request):
    return render(request, 'classroom/new.html')


def detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'classroom/detail.html',{
        'student':student,
    })


def create(request):
    student = Student()
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.save()
    return redirect('classroom:detail', student.id)


def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'classroom/edit.html', {
        'student': student,
    })


def update(request, id):
    student = Student.objects.get(id=id)
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.save()
    return redirect('classroom:detail', student.id)


def delete(reqeust, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('classroom:list')
