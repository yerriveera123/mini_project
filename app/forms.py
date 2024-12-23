from django import forms
from django.forms import ModelForm
from app.models import *
class Taskform(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control',
               'placeholder':'Add new task'})
    )
    class Meta:
        model=Task
        fields='__all__'
        widgets={
            'other_field':forms.TextInput(attrs={'class':'form-control'}),

        }