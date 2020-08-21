from django.shortcuts import render
from django.views.generic import View,ListView
from .models import Todo_Items

# Create your views here.

class HomeView(ListView):
    model =Todo_Items
    template_name = 'home.html'
    
