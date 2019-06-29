from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def login(request):
    return render(request, 'dashboard/login.html')


def index(request):
    return render(request, 'dashboard/index.html')


def map(request):
    return render(request, 'dashboard/map.html')


def button(request):

    return render(request,'dashboard/home.html')

def output(request):
    data=requests.get("https://www.google.com/")
    print(data.text)
    data=data.text
    return render(request,'home.html',{'data':data})

