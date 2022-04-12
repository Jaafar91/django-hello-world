from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
def homePageView1(request):
    return HttpResponse("Hello, World!")

def homePageView2(request):
    return HttpResponse("Hello, Earth!")

class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"