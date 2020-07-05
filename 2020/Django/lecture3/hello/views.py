from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def leo(request):
    return HttpResponse("Hello, Leo!")

def greet(request, name):
    return render(request, "Hello/greet.html", {
        "name": name.capitalize()
    })