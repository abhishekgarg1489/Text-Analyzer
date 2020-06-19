from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("HOME")

def analyze(request):
    djtext = request.GET.get('text', 'default')

    removepunc = request.GET.get('removepunc', 'off')
    uppercase = request.GET.get('uppercase', 'off')
    newlinerem = request.GET.get('newlinerem', 'off')
    Extraspacerem = request.GET.get('spacerem', 'off')
    charcount = request.GET.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuation','analyzed_text':analyzed}
        return render(request, 'analyze.html',params)

    elif(uppercase == "on"):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif(newlinerem == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n":
                analyzed += char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (Extraspacerem == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        params = {'purpose': 'Spaces Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (charcount == "on"):
        analyzed = len(djtext)
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse(djtext)

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
</html>
"""

"""
index.html
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
    <input type='checkbox' name='uppercase'>Upper Case<br>
    <input type='checkbox' name='newlinerem'>New Line Remover<br>
    <input type='checkbox' name='spacerem'>Extra Space Remover<br>
    <input type='checkbox' name='charcount'>Character Count<br>

    <button type='submit'>Analyze Text</button>
</form>

</body>
</html>
"""

"""
urls.py

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('analyze/', views.analyze,name='analyze'),


]

"""