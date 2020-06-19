from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("HOME")

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    if removepunc=="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Removed Punctuation','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
            return HttpResponse("Please Check the Check Box")

"""
Analyze.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Analyzing your text...</title>
</head>
<body>
<h1>Your Analyzed Text - {{purpose}}</h1>
<p>
    {{ analyzed_text }}

</p>

</body>
</html>"""

"""
Index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TextUtils</title>
</head>
<body>
    <h1>The Text Analyzer</h1>
<form action='/analyze' method='get'>
    <textarea  name='text' style='margin: 0px; width: 700px; height: 100px;'> </textarea>
    <br>
    <input type='checkbox' name='removepunc'>Remove Punctuations <br>

    <button type='submit'>Analyze Text</button>
</form>

</body>
</html>
"""

"""
urls.py
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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('analyze/', views.analyze,name='analyze'),


]

"""