from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<h1>안녕, 장고야~! views.index다.</h2>")

