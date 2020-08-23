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
        'placeholder':"First name",
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text" ,
        'class':"form-control", 
        'placeholder':"sur name",
    }))

    phone_number = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'type':"text" ,
        'class':"form-control", 
        'placeholder':"enter phone number",
    }))

    address = forms.CharField(required=False,widget=forms.TextInput(attrs={
        'type':"text" ,
        'class':"form-control", 
        'placeholder':"Enter your address",
    }))

    email_id = forms.CharField(widget=forms.TextInput(attrs={
        'type':"text" ,
        'class':"form-control", 
        'placeholder':"Enter your email",
    }))

    profile_pic = forms.ImageField()

    