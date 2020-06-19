from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newlinerem = request.POST.get('newlinerem', 'off')
    Extraspacerem = request.POST.get('spacerem', 'off')
    charcount = request.POST.get('charcount', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if uppercase == "on":
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlinerem == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed

    if Extraspacerem == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed += char
        params = {'purpose': 'Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}

    if removepunc == "off" and uppercase == "off" and newlinerem == "off" and Extraspacerem == "off" and charcount == "off":
        return HttpResponse("Error")
    else:
        return render(request, 'analyze.html', params)
