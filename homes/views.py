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

class A1View(generic.ListView):
    model = Homesmodel
    template_name = 'partials/a1.html'

class A11View(generic.ListView):
    model = Homesmodel
    template_name = 'partials/a11.html'
class A12View(generic.ListView):
    model = Homesmodel
    template_name = 'partials/a12.html'
class A13View(generic.ListView):
    model = Homesmodel
    template_name = 'partials/a13.html'

class B1View(generic.ListView):
    model = Homesmodel
    template_name = 'partials/b1.html'