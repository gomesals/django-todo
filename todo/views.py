from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Todo

from .forms import TodoForm


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'todo/index.html', context)


def detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    context = {'todo': todo}
    return render(request, 'todo/detail.html', context)


def new(request):
    form = TodoForm()
    todo = {
        'id': 0
    }
    context = {'form': form, 'todo': todo}

    return render(request, 'todo/form.html', context)


def form(request, todo_id):
    error_message = None
    is_todo_updated = False
    if not todo_id == 0:
        todo = get_object_or_404(Todo, pk=todo_id)

    if request.method == 'GET':
        if todo_id == 0:
            return new(request)
        form = TodoForm(initial=todo.__dict__)
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            if todo_id == 0:
                todo = Todo(**form.cleaned_data)
                todo.save()
                todo_id = todo.id
            else:
                Todo.objects.filter(pk=todo_id).update(**form.cleaned_data)
                is_todo_updated = True
        else:
            error_message = 'Há campos inválidos no formulário, corrija-os e tente novamente.'
        pass

    context = {'todo': todo, 'form': form, 'error_message': error_message}

    if is_todo_updated:
        return HttpResponseRedirect(reverse('todo:detail', args=(todo.id, )))

    return render(request, 'todo/form.html', context)


def delete(request, todo_id):
    return HttpResponse('hwhw')
