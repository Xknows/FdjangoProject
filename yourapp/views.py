from django.shortcuts import render
from django.http import HttpResponse

def sayHello(request):
    return HttpResponse("hello")

def sayBay(request):
    return render(request, 'hello.html')
