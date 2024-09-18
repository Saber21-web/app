from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница магазина - Home',
        'list' : ['one', 'two', 'three'],
        'dict' : {'one': 1, 'two': 2, 'three': 3},
        'is_authenticated': False
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("Hello, world. You're at the main about.")