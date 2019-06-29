from . import views
from django.urls import path

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('map', views.map, name='map'),
]