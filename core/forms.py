from django import forms

class Todo_form(forms.Form):
    contents=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mr-sm-2',
        'placeholder':'Add Items',
        'name':'contents'
    }))
    