from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'home.html')

def todos(request):
    items = TodoItem.objects.all()
    return render(request, 'todos.html', {"todos": items})

def detalles(request, id):
    todo = TodoItem.objects.get(id=id)
    template = loader.get_template('detalles.html')
    context = {
        'todo' : todo,
    }
    return HttpResponse(template.render(context, request))

def testeo(request):
    template = loader.get_template('testeo.html')
    context = {
        'frutas': ['Manzana', 'Pera', 'Naranja']
    }
    return HttpResponse(template.render(context, request))