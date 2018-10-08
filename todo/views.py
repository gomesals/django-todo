from django.http import HttpResponse
from django.shortcuts import render

from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/index.html', context)


def detail(request, todo_id):
    return HttpResponse('hwhw')


def form(request, todo_id):
    return HttpResponse('hwhw')


def delete(request, todo_id):
    return HttpResponse('hwhw')
