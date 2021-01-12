from django.urls import path
from rooms import  views as room_views
from homes import views as home_views
from gsfarm import views as gsfarm_views
from mainshop import views as mainshop_views

app_name = "core"

urlpatterns = [
    path("list/", room_views.HomeView.as_view(), name="roomlist"),
    path("", home_views.HometestView.as_view(), name="home"),
    path("in/", home_views.HomeintestView.as_view(), name="homein"),
    path("su/", home_views.SuView.as_view(), name="su"),
    path("a1/", home_views.A1View.as_view(), name="a1"),
    path("b1/", home_views.B1View.as_view(), name="b1"),
    path("b1/b11/", home_views.B11View.as_view(), name="b11"),
    path("b1/b12/", home_views.B12View.as_view(), name="b12"),
    path("b1/b13/", home_views.B13View.as_view(), name="b13"),
    path("b1/b14/", home_views.B14View.as_view(), name="b14"),
    path("a1/a11/", home_views.A11View.as_view(), name="a11"),
    path("a1/a12/", home_views.A12View.as_view(), name="a12"),
    path("a1/a13/", home_views.A13View.as_view(), name="a13"),
    path("gsfarm/", gsfarm_views.GsfarmView.as_view(), name="gsfarm"),
    path("mainshop/", mainshop_views.MainshopView.as_view(), name="mainshop"),
    path("mainshop/detail/", mainshop_views.MainshopdetailView.as_view(), name="maindetail"),

]
