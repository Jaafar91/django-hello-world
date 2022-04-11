from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView1(request):
    return HttpResponse("Hello, World!")

def homePageView2(request):
    return HttpResponse("Hello, Earth!")