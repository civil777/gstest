from django.shortcuts import render
from django.views import generic
from . models import Mainshopmodel


class MainshopView(generic.ListView):
    model = Mainshopmodel
    template_name = 'mainshop/mainshop.html'


class MainshopdetailView(generic.ListView):
    model = Mainshopmodel
    template_name = 'mainshop/mainshopdetail.html'

