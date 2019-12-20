from django.http import HttpResponse
from django.shortcuts import render
def ram(request):
    return render(request,"siv.html",{"jaggu":"9676583753"})
def wel(requst):
    return HttpResponse("<h1>raja<h1/>")
