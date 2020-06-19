#I have created this file
from django.http import HttpResponse

def index(request):
    s='''
    <h1>HOME</h1>
    <button value='Go Back' onclick="window.history.front()">Back</button>
    '''
    return HttpResponse(s)

def removepunc(request):
    s = '''
        <h1>remove punc</h1>
        <button value='Go Back' onclick="window.history.back()">Back</button>
        '''
    return HttpResponse(s)

def capfirst(request):
    s = '''
            <h1>Capitalise First</h1>
            <input type=button value="Go Back" onclick="window.history.back()"></button>
            '''
    return HttpResponse(s)


def newlinerem(request):
    s = '''
            <h1>New Line Remove</h1>
            <button value="Go Back" onclick="window.history.back()">Back</button>
        '''
    return HttpResponse(s)

"""
"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('removepunc/', views.removepunc, name='rempunc'),
    path('Capitalizefirst/', views.capfirst, name='capfirst'),
    path('newlineremove/', views.newlinerem, name='newlinerem'),

]

"""