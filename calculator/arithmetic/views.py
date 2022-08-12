from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
a=int(input("Enter a value: "))
b=int(input("Enter b value: "))
def add(request):
    c=a+b
    return HttpResponse(c)
def sub(request):
    d=a-b
    return HttpResponse(d)
def multi(request):
    e=a*b
    return HttpResponse(e)
def div(request):
    f=a/b
    return HttpResponse(f)