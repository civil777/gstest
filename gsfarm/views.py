from django.shortcuts import render
from django.views import generic
from . models import Gsfarmmodel


class HometestView(generic.ListView):
    model = Gsfarmmodel
    template_name = 'gsfarm/index.html'

