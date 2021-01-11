from django.shortcuts import render
from django.views import generic
from . models import Homesmodel


class HometestView(generic.ListView):
    model = Homesmodel
    template_name = 'homes/home_list.html'

class HomeintestView(generic.ListView):
    model = Homesmodel
    template_name = 'homes/homeint_list.html'

class SuView(generic.ListView):
    model = Homesmodel
    template_name = 'partials/susan.html'
