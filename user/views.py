from django.shortcuts import render
from .models import data

def user_home(request):
    person = data.objects.all()
    return render(request, 'index_user.html', {'person': person})
