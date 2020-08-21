from django.shortcuts import render
from django.views.generic import View,ListView
from .models import Todo_Items
from .forms import Todo_form

# Create your views here.

class HomeView(ListView):
    model =Todo_Items
    template_name = 'home.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = Todo_form
        context['form'] = form

        return context
    
