from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('path/1', views.m1),
    path('path/2', views.m2),
    path('path/3', views.m3),
    path('path/4', views.m4),
    path('path/5', views.m5),
]