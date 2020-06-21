from django.shortcuts import render, redirect
from django.utils import timezone
from . models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    todo_list = Todo.objects.all().order_by('-added_date')
    for todo in todo_list:
        print(todo.id, todo.text)
    return render(request, 'home.html', {
    'todo_list': todo_list
    })


@csrf_exempt
def add_todo(request):
    text_todo = request.POST['text_in']
    current_date = timezone.now()
    Todo.objects.create(text=text_todo, added_date=current_date)
    return redirect('/')

@csrf_exempt
def delete_item(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')

def delete_all(request):
    Todo.objects.all().delete()
    return redirect('/')

def search(request):
    search_for = request.POST['search']
    items_found = Todo.objects.filter(text__icontains=search_for)
    context = {
        'items_found': items_found
    }
    print(search_for)
    print(items_found)
    return render(request, 'search_result.html', context)
