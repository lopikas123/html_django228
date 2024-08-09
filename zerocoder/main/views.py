from django.shortcuts import render
from django.http import HttpResponse

def data(request):
    return render(request, 'main/data.html')

def index(request):
    return render(request, 'main/index.html')

def bur(request):
    return render(request, 'main/bur.html')

def fom(request):
    return render(request, 'main/fom.html')

def tou(request):
    return render(request, 'main/tou.html')
