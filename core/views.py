from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,ListView,DetailView
from django.contrib import messages
from django.shortcuts import  get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import Todo_Items,Todo_card
from .forms import Todo_form


# Create your views here.

class HomeView(ListView):
    model =Todo_card
    template_name = 'home.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        todo_items =Todo_Items.objects.all()
        context['todo_items']=todo_items
        return context

class CardDetailView(DetailView):
    model =Todo_Items
    template_name = 'detailview.html'

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
            todo_items = Todo_Items(content=contents,user=user,checked=False)
            todo_items.save()
            data = {
                'contents':contents,
                'user':todo_items.user.username,
                'id':todo_items.id,
            }
            return JsonResponse(data)

        messages.info(self.request,"Something wrong")
        return redirect('.')
    

def todo_actions(request,id,action):
    try:
        item = get_object_or_404(Todo_Items,id=id)
        if action=='check':
            if item.checked :
                item.checked = False

            else :
                item.checked = True
            item.save()
            data ={
                'id':item.id,
                'action':'check',
                'content':item.content,
                'checked':item.checked
            }

        if action=='edit':
            data ={
                'id':item.id,
                'action':'edit',
                'content':item.content,
                'checked':item.checked
            }
        if action=='delete':
            data={
                'action':'delete'
            }
            item.delete()
        return JsonResponse(data)

    except ObjectDoesNotExist:
        pass
    
    print(item.checked)
    return JsonResponse()


