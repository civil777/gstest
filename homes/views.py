from django.shortcuts import render
from django.views import generic
from . models import Homesmodel


class HometestView(generic.ListView):
    model = Homesmodel
    template_name = 'homes/home_list.html'

