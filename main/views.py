from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def m1(request):
    return render(request, 'index_m1.html')

def m2(request):
    return render(request, 'index_m2.html')

def m3(request):
    return render(request, 'index_m3.html')

def m4(request):
    return render(request, 'index_m4.html')

def m5(request):
    return render(request, 'index_m5.html')

def rewiew(request):
    return render(request, 'index_rewiew.html')
