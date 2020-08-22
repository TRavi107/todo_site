from django.urls import path
from .views import CardDetailView,todo_actions,HomeView

app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<slug>',CardDetailView.as_view(),name='card_detail'),
    path('<id>/<action>',todo_actions,name='action')
]