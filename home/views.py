from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#    return HttpResponse("Hello, world. You're at the #SecureITall index.")

#index page "hello world"
def index(request):
    return render(request, "home/index.html",)