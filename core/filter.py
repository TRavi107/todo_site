import django_filters
from .models import Todo_card

class Card_Filter(django_filters.FilterSet):
    model = Todo_card
    title = django_filters.CharFilter(
        #Customize the search bar design
        lookup_expr = 'icontains'
    )