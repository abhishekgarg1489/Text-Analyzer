#I have created this file
from django.http import HttpResponse
"""def index(request):
    return HttpResponse("<a href='https://www.youtube.com/'>YOUTUBE</a>")
"""
def navigation(request):
    s='''<h2>Navigation Bar</h2>
        <a href="https://www.youtube.com/">YOUTUBE</a><br>
        <a href="https://www.facebook.com/">FACEBOOK</a><br>
        <a href="https://www.flipkart.com/">FLIPKART</a><br>
        <a href="https://www.hindustantimes.com/">NEWS</a><br>
        <a href="https://www.google.com/">GOOGLE</a><br>
    '''
    return HttpResponse(s)

def about(request):
    return HttpResponse("About Abhishek")


"""
# urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.navigation,name='navigation'),
    path('about/', views.about, name='about'),
]"""