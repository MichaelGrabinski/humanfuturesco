from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
 #  path("<str:name>", views.greet1, name="greet"),
    path("Home", views.Home, name="Home"),
    path("AboutUs", views.AboutUs, name="AboutUs"),
    path("GameStudio", views.GameStudio, name="GameStudio")
] 
