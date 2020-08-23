from django.urls import path
from .views import CardDetailView,todo_actions,HomeView,create_card

app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<slug>',CardDetailView.as_view(),name='card_detail'),
    path('<id>/<action>',todo_actions,name='action'),
    path('create/',create_card,name='create'),
]