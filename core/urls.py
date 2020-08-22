from django.urls import path
from .views import HomeView,todo_actions

app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<id>/<action>',todo_actions,name='action')

]