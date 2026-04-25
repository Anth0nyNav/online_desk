from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'my_app/index.html')


def messanger(request):
    return HttpResponse('<h1>Здесь скоро будет мессенджер</h1>')

def calendar(request):
    return HttpResponse('<h1>Здесь скоро будет календарь</h1>')

def desks(request):
    return HttpResponse('<h1>Здесь скоро будут доски</h1>')

def aihelper(request):
    return HttpResponse('<h1>Здесь скоро будет AI помощник</h1>')

def lc(request):
    return HttpResponse('<h1>А это личный кабинет</h1>')

