from django.urls import path
from .views import homePageView1,homePageView2,HomePageView,AboutPageView


urlpatterns = [
    #path("", homePageView1, name="default"),
    #path("about/", homePageView2, name="about"),
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]