from django import forms
from django.forms import ModelForm
#from .models import tweet

class SearchForm(forms.Form):
    keyword = forms.CharField(label='', max_length=100, required=False)
    keyword.widget.attrs['class'] = 'form-control mr-sm-2 my-2'
    keyword.widget.attrs['placeholder'] = 'Search for tweets.'

