from django.urls import path
from .views import homePageView1,homePageView2

urlpatterns = [
    path("", homePageView1, name="home"),
    path("about/", homePageView2, name="about"),
]