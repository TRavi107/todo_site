from django.urls import path
from .views import (
    CardDetailView,
    todo_actions,
    HomeView,
    create_card,
    ProfilePage,
    delete_card
)
app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('detail/<slug>',CardDetailView.as_view(),name='card_detail'),
    path('actions/<id>/<action>',todo_actions,name='action'),
    path('create/',create_card,name='create'),
    path('delete/<slug>',delete_card,name='card_delete'),
    path('profile/<slug>',ProfilePage.as_view(),name='profile'),
]