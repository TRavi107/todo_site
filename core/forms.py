from django import forms

class Todo_form(forms.Form):
    contents=forms.CharField(max_length=1000)
    