from django.shortcuts import render, redirect
from django.utils import timezone
from . models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    todo_list_due = Todo.objects.all().order_by('-added_date').filter(completed=False)
    todo_list_completed = Todo.objects.all().order_by('-added_date').filter(completed=True)
    context = {
        'todo_list_due': todo_list_due,
        'todo_list_completed': todo_list_completed
    }
    return render(request, 'home.html', context)


@csrf_exempt
def add_todo(request):
    text_todo = request.POST['text_in']
    current_date = timezone.now()
    Todo.objects.create(text=text_todo, added_date=current_date)
    return redirect('/')

def done_item(request, todo_id):
    item = Todo.objects.filter(id=todo_id)
    for i in item:
        i.completed = True
        Todo.objects.create(text=i.text, completed=True)
        i.delete()
    return redirect('/')

def done_all(request):
    item = Todo.objects.all().filter(completed=False)
    for i in item:
        i.completed = True
        Todo.objects.create(text=i.text, completed=True)
        i.delete()
    return redirect('/')

@csrf_exempt
def delete_item(request, todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')

def delete_all(request):
    Todo.objects.all().delete()
    return redirect('/')

def delete_completed(request):
    Todo.objects.all().filter(completed=True).delete()
    return redirect('/')

def delete_due(request):
    Todo.objects.all().filter(completed=False).delete()
    return redirect('/')

def search(request):
    search_for = request.POST['search']
    items_found_due = Todo.objects.filter(text__icontains=search_for).filter(completed=False)
    items_found_completed = Todo.objects.filter(text__icontains=search_for).filter(completed=True)
    context = {
        'items_found_due': items_found_due,
        'items_found_completed': items_found_completed
    }
    return render(request, 'search_result.html', context)
