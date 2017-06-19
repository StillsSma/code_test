from django import forms

class APIForm(forms.Form):
    api_key = forms.IntegerField()

    
