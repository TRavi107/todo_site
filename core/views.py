from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.generic import View,ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import  get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from .models import Todo_Items,Todo_card,Profile
from .forms import Todo_form,Profile_form
from .filter import Card_Filter


# Create your views here.

class ProfilePage(LoginRequiredMixin,DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_context_data(self,*args,**kwargs):
        context = context = super().get_context_data(*args,**kwargs)
        profile = self.get_object()
        form = Profile_form(initial={
            'name':profile.user.first_name,
            'last_name':profile.user.last_name,
            'email_id':profile.user.email,
            }
        )

        context['form']=form
        return context

    def post(self,*args,**kwargs):
        form = Profile_form(self.request.POST or None)
        profile = self.get_object()
        if form.is_valid():
            f_name = form.cleaned_data.get('name')
            s_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email_id')
            profile.user.first_name =f_name
            profile.user.last_name = s_name
            profile.user.email = email
            profile.user.save()
            profile.save() 
            return redirect('core:profile',slug=profile.slug)

        messages.info(self.request,form.errors)
        return redirect('core:profile',slug=profile.slug)


class HomeView(ListView):
    model =Todo_card
    template_name = 'home.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        todo_items =Todo_Items.objects.all()
        context['todo_items']=todo_items
        return context

    def post(self,*args,**kwargs):
        if 'title' in self.request.POST:
            title = self.request.POST.get("title")
            id = self.request.POST.get("id")
            obj = get_object_or_404(Todo_card,id=id)
            try:
                obj.title = title
                obj.slug = title+str(id)
                obj.save()
            except ObjectDoesNotExist:
                messages.info(self.request,"Obejct not found")
            

        return redirect('.')

class CardDetailView(DetailView,LoginRequiredMixin):
    model =Todo_card
    template_name = 'detailview.html'

    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['todo_items']=Todo_Items.objects.all().filter(card=self.get_object())
        form = Todo_form
        context['form'] = form
        return context

    def post(self,*args,**kwargs):
        obj = self.get_object()
        if 'item-edit' in self.request.POST :
            id = self.request.POST.get('id')
            text = self.request.POST.get('item-edit')
            item = get_object_or_404(Todo_Items,id=id)
            item.content = text
            item.save()
            return redirect('core:card_detail',slug = obj.slug)
        form = Todo_form(self.request.POST or None)
        if form.is_valid():
            contents = form.cleaned_data.get('contents')
            todo_items = Todo_Items(content=contents,checked=False,card=self.get_object())
            todo_items.save()
            data = {
                'contents':contents,
                'id':todo_items.id,
            }
            return JsonResponse(data)

        messages.info(self.request,"Could not edit")
        return redirect('core:card_detail',slug = obj.slug)

@login_required
def create_card(request):
    card = Todo_card(user=request.user)
    card.save()
    card.slug = card.title + str(card.created_time)
    card.save()
    return redirect('/')

@login_required
def delete_card(request,slug):
    card = get_object_or_404(Todo_card,slug = slug)
    try:
        card.delete()
        return JsonResponse({})
    except ObjectDoesNotExist :
        messages.info(request,"Object doesnot exits")
        return JsonResponse({})

@login_required
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
    
    return JsonResponse()


