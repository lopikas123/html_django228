from django.urls import path
from . import views

urlpatterns = [
    path('', views.data),
    path('index', views.index),
    path('bur', views.bur),
    path('fom', views.fom),
    path('tou', views.tou),
]
