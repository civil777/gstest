from django.urls import path
from rooms import  views as room_views
from homes import views as home_views
from gsfarm import views as gsfarm_views

app_name = "core"

urlpatterns = [
    path("list/", room_views.HomeView.as_view(), name="roomlist"),
    path("", home_views.HometestView.as_view(), name="home"),
    path("gsfarm/", gsfarm_views.HometestView.as_view(), name="gsfarm"),

]
