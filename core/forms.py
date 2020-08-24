from django import forms

class Todo_form(forms.Form):
    contents=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mr-sm-2',
        'placeholder':'Add Items',
        'name':'contents'
    }))

class Profile_form(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type':'text',
        'class':"form-control", 
        'name':'name',
        'placeholder':"First name",
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text" ,
        'class':"form-control", 
        'name':'last_name',
        'placeholder':"sur name",
    }))

    email_id = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text" ,
        'class':"form-control",
        'name':'email_id', 
        'placeholder':"Enter your email",
    }))

    profile_pic = forms.ImageField(required=False)

    