from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    username = forms.CharField(label="",max_length="100",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':' Username'}))
    date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type':'date', 'class':'flow-control', 'placeholer':'DateOfBirth'}))

    class Meta:
        model= User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2')
