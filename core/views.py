from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,ListView
from django.contrib import messages

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

    def post(self,*args,**kwargs):
        form = Todo_form(self.request.POST or None)
        if form.is_valid():
            contents = form.cleaned_data.get('contents')
            if self.request.user !=None:
                user = self.request.user

            else:
                user = None
            todo_items = Todo_Items(content=contents,user=user)
            todo_items.save()
            data = {
                'contents':contents,
                'user':todo_items.user.username,
                'id':todo_items.id,
            }
            return JsonResponse(data)

        messages.info(self.request,"Something wrong")
        return redirect('.')
    
